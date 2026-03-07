"""ModelFactory for creating AUTOSAR model instances from XML tags."""

from __future__ import annotations

from pathlib import Path
from typing import Optional, Dict, List, Type, Any, TYPE_CHECKING
import importlib
import sys

from armodel2.serialization.name_converter import NameConverter

# Use TYPE_CHECKING to avoid circular import
if TYPE_CHECKING:
    pass


class ModelFactory:
    """Factory for creating AUTOSAR model instances.

    Provides efficient class instantiation from XML tags with:
    - Singleton pattern for global access
    - Cached class imports for performance
    - Polymorphic type resolution
    - Automatic XML tag to class name conversion

    Performance: Uses pre-compiled Python mappings instead of YAML parsing
    to eliminate ~0.588s one-time overhead on first deserialization.
    """

    _instance: Optional[ModelFactory] = None
    _initialized: bool = False

    def __new__(cls) -> ModelFactory:
        """Singleton pattern."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """Initialize factory (only once due to singleton)."""
        if not ModelFactory._initialized:
            self._mappings: Dict[str, Any] = {}
            self._class_cache: Dict[str, Type[Any]] = {}
            self._polymorphic_cache: Dict[str, List[str]] = {}
            self._import_path_cache: Dict[str, str] = {}
            self._polymorphic_dispatch: Dict[str, Dict[str, Type[Any]]] = {}  # base_class -> {xml_tag -> class}
            ModelFactory._initialized = True

    def load_mappings(self, yaml_path: Optional[Path] = None) -> None:
        """Load mappings from pre-compiled Python module.

        Uses pre-compiled model_mappings_compiled.py instead of parsing YAML
        to eliminate ~0.588s one-time overhead on first deserialization.

        Args:
            yaml_path: Deprecated, kept for API compatibility. Path to model_mappings.yaml
        """
        # Try to import pre-compiled mappings first
        try:
            from armodel2.cfg import model_mappings_compiled as mappings

            # Load from compiled module (fast, no YAML parsing)
            self._mappings = {
                "xml_tag_mappings": mappings.XML_TAG_MAPPINGS,
                "class_import_paths": mappings.CLASS_IMPORT_PATHS,
                "polymorphic_types": mappings.POLYMORPHIC_TYPES,
            }

            # Build polymorphic cache
            self._polymorphic_cache = mappings.POLYMORPHIC_TYPES

            # Build import path cache
            self._import_path_cache = mappings.CLASS_IMPORT_PATHS

            # Pre-compute polymorphic dispatch tables for O(1) lookup
            self._build_polymorphic_dispatch()

        except ImportError:
            # Fallback to YAML parsing if compiled module doesn't exist
            # This can happen during development before first regeneration
            if yaml_path is None:
                yaml_path = Path(__file__).parent.parent / "cfg" / "model_mappings.yaml"

            import yaml
            with open(yaml_path, "r", encoding="utf-8") as f:
                self._mappings = yaml.safe_load(f)

            # Build polymorphic cache
            if "polymorphic_types" in self._mappings:
                self._polymorphic_cache = self._mappings["polymorphic_types"]

            # Build import path cache
            if "class_import_paths" in self._mappings:
                self._import_path_cache = self._mappings["class_import_paths"]

            # Pre-compute polymorphic dispatch tables
            self._build_polymorphic_dispatch()

    def _build_polymorphic_dispatch(self) -> None:
        """Pre-compute polymorphic dispatch tables for O(1) type resolution.

        Builds a nested dictionary: base_class_name -> {xml_tag -> concrete_class}
        This eliminates the need for get_polymorphic_implementations() and list
        membership checks during deserialization.
        """
        self._polymorphic_dispatch = {}

        for base_class_name, implementation_list in self._polymorphic_cache.items():
            # Skip special entries that are not real class names
            if base_class_name.startswith('–') or base_class_name.startswith('-'):
                continue

            dispatch_table: Dict[str, Type[Any]] = {}
            for impl_class_name in implementation_list:
                # Skip special entries that are not real class names
                if impl_class_name.startswith('–') or impl_class_name.startswith('-'):
                    continue

                # Get import path and import the class
                import_path = self._import_path_cache.get(impl_class_name)
                if import_path:
                    try:
                        module = importlib.import_module(import_path)
                        cls = getattr(module, impl_class_name)
                        if isinstance(cls, type):
                            # Compute XML tag for this class
                            xml_tag = NameConverter.to_xml_tag(impl_class_name)
                            dispatch_table[xml_tag] = cls
                            # Also cache by class name for reverse lookup
                            self._class_cache[xml_tag] = cls
                    except (ImportError, AttributeError):
                        # Skip classes that can't be imported
                        continue

            if dispatch_table:  # Only add non-empty dispatch tables
                self._polymorphic_dispatch[base_class_name] = dispatch_table
    
    def get_class(self, xml_tag: str, raise_on_failure: bool = True) -> Optional[Type[Any]]:
        """Get class by XML tag.

        Args:
            xml_tag: XML tag name (e.g., "SW-BASE-TYPE")
            raise_on_failure: If True, raise ImportError instead of returning None

        Returns:
            Class type or None if not found (when raise_on_failure=False)

        Raises:
            ImportError: If class cannot be imported and raise_on_failure=True
        """
        # Check cache first
        if xml_tag in self._class_cache:
            return self._class_cache[xml_tag]

        # Ensure mappings are loaded
        if not self._mappings:
            self.load_mappings()

        # Look up in direct mappings
        class_name = self._mappings.get("xml_tag_mappings", {}).get(xml_tag)

        if class_name is None:
            # Try to convert tag to class name
            class_name = NameConverter.tag_to_class_name(xml_tag)

        if class_name:
            cls = self._import_class(class_name, raise_on_failure=raise_on_failure)
            if cls:
                self._class_cache[xml_tag] = cls
                return cls

        if raise_on_failure:
            raise ImportError(
                f"No class mapping found for XML tag '{xml_tag}'. "
                f"Check that the tag is defined in model_mappings.yaml."
            )
        return None
    
    def get_polymorphic_implementations(self, base_class_name: str) -> List[str]:
        """Get list of concrete implementations for a polymorphic base class.
        
        Args:
            base_class_name: Name of base class (e.g., "PackageableElement")
            
        Returns:
            List of concrete class names
        """
        # Ensure mappings are loaded
        if not self._mappings:
            self.load_mappings()
        
        return self._polymorphic_cache.get(base_class_name, [])
    
    def resolve_polymorphic_type(self, xml_tag: str, base_class_name: str) -> Optional[Type[Any]]:
        """Resolve polymorphic type based on XML tag.

        Uses pre-computed dispatch table for O(1) lookup instead of
        iterating through polymorphic implementations list.

        Args:
            xml_tag: XML tag of concrete element (e.g., "SW-BASE-TYPE")
            base_class_name: Expected base class (e.g., "PackageableElement")

        Returns:
            Concrete class type or None
        """
        # Ensure mappings are loaded
        if not self._polymorphic_dispatch:
            self.load_mappings()

        # O(1) lookup in pre-computed dispatch table
        dispatch_table = self._polymorphic_dispatch.get(base_class_name)
        if dispatch_table:
            return dispatch_table.get(xml_tag)

        # Fallback: legacy method for backward compatibility
        # Get class from XML tag (don't raise on failure for fallback)
        cls = self.get_class(xml_tag, raise_on_failure=False)
        if cls is None:
            return None

        # Verify it's a valid subclass
        implementations = self.get_polymorphic_implementations(base_class_name)
        if cls.__name__ in implementations:
            return cls

        return None
    
    def _import_class(self, class_name: str, raise_on_failure: bool = False) -> Optional[Type[Any]]:
        """Import class by name with caching.

        Args:
            class_name: Name of class to import (e.g., "SwBaseType")
            raise_on_failure: If True, raise ImportError instead of returning None

        Returns:
            Imported class or None if not found (when raise_on_failure=False)

        Raises:
            ImportError: If class cannot be imported and raise_on_failure=True
        """
        # Check cache
        if class_name in self._class_cache:
            return self._class_cache[class_name]

        # Get import path from cache
        import_path = self._import_path_cache.get(class_name)

        if import_path:
            try:
                module = importlib.import_module(import_path)
                cls = getattr(module, class_name)
                if isinstance(cls, type):
                    self._class_cache[class_name] = cls
                    return cls
            except ImportError as e:
                if raise_on_failure:
                    raise ImportError(
                        f"Failed to import class '{class_name}' from '{import_path}': {e}. "
                        f"This may be due to a circular import. "
                        f"Check that the class is properly configured in skip_classes.yaml "
                        f"or uses TYPE_CHECKING for circular imports."
                    ) from e
            except AttributeError as e:
                if raise_on_failure:
                    raise ImportError(
                        f"Class '{class_name}' not found in module '{import_path}': {e}"
                    ) from e

        # Fallback to search
        cls = self._search_and_import_class(class_name)
        if cls is None and raise_on_failure:
            raise ImportError(
                f"Class '{class_name}' not found. "
                f"Check that it exists in the model mappings and can be imported."
            )
        return cls
    
    def _search_and_import_class(self, class_name: str) -> Optional[Type[Any]]:
        """Search for and import class (fallback method).

        Args:
            class_name: Name of class to import

        Returns:
            Imported class or None
        """
        # Check sys.modules first
        for module_name, module in sys.modules.items():
            if module_name.startswith('armodel2.models.M2'):
                if hasattr(module, class_name):
                    cls = getattr(module, class_name)
                    if isinstance(cls, type):
                        self._class_cache[class_name] = cls
                        return cls

        return None
    
    def is_initialized(self) -> bool:
        """Check if factory is initialized with mappings.
        
        Returns:
            True if mappings loaded
        """
        return bool(self._mappings)
    
    def clear_cache(self) -> None:
        """Clear class import cache and polymorphic dispatch tables."""
        self._class_cache.clear()
        self._polymorphic_dispatch.clear()

    def get_polymorphic_class(self, xml_tag: str, base_class_name: str) -> Optional[Type[Any]]:
        """Get polymorphic class directly from dispatch table.

        This is a convenience method that combines get_class() and resolve_polymorphic_type()
        for cases where the XML tag might directly map to a class.

        Args:
            xml_tag: XML tag name
            base_class_name: Base class name for polymorphic resolution

        Returns:
            Class type or None
        """
        # First try direct polymorphic resolution
        cls = self.resolve_polymorphic_type(xml_tag, base_class_name)
        if cls:
            return cls

        # Fallback to direct class lookup
        return self.get_class(xml_tag, raise_on_failure=False)