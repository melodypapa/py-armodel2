"""ModelFactory for creating AUTOSAR model instances from XML tags."""

from __future__ import annotations

from pathlib import Path
from typing import Optional, Dict, List, Type, Any, TYPE_CHECKING
import yaml
import importlib
import sys

from armodel.serialization.name_converter import NameConverter

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
            ModelFactory._initialized = True
    
    def load_mappings(self, yaml_path: Optional[Path] = None) -> None:
        """Load mappings from YAML file.
        
        Args:
            yaml_path: Path to model_mappings.yaml, defaults to package path
        """
        if yaml_path is None:
            yaml_path = Path(__file__).parent.parent / "cfg" / "model_mappings.yaml"
        
        with open(yaml_path, "r") as f:
            self._mappings = yaml.safe_load(f)
        
        # Build polymorphic cache
        if "polymorphic_types" in self._mappings:
            self._polymorphic_cache = self._mappings["polymorphic_types"]
        
        # Build import path cache
        if "class_import_paths" in self._mappings:
            self._import_path_cache = self._mappings["class_import_paths"]
    
    def get_class(self, xml_tag: str) -> Optional[Type[Any]]:
        """Get class by XML tag.

        Args:
            xml_tag: XML tag name (e.g., "SW-BASE-TYPE")

        Returns:
            Class type or None if not found
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
            cls = self._import_class(class_name)
            if cls:
                self._class_cache[xml_tag] = cls
                return cls

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

        Args:
            xml_tag: XML tag of concrete element (e.g., "SW-BASE-TYPE")
            base_class_name: Expected base class (e.g., "PackageableElement")

        Returns:
            Concrete class type or None
        """
        # Get class from XML tag
        cls = self.get_class(xml_tag)

        if cls is None:
            return None

        # Verify it's a valid subclass
        implementations = self.get_polymorphic_implementations(base_class_name)

        if cls.__name__ in implementations:
            return cls

        return None
    
    def _import_class(self, class_name: str) -> Optional[Type[Any]]:
        """Import class by name with caching.

        Args:
            class_name: Name of class to import (e.g., "SwBaseType")

        Returns:
            Imported class or None if not found
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
            except (ImportError, AttributeError):
                pass

        # Fallback to search
        return self._search_and_import_class(class_name)
    
    def _search_and_import_class(self, class_name: str) -> Optional[Type[Any]]:
        """Search for and import class (fallback method).

        Args:
            class_name: Name of class to import

        Returns:
            Imported class or None
        """
        # Check sys.modules first
        for module_name, module in sys.modules.items():
            if module_name.startswith('armodel.models.M2'):
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
        """Clear class import cache."""
        self._class_cache.clear()