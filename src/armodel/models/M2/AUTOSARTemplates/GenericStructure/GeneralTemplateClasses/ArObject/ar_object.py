"""ARObject AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 191)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ArObject.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Union, get_type_hints, get_args, get_origin
import xml.etree.ElementTree as ET
from armodel.serialization.name_converter import NameConverter
from armodel.serialization.model_factory import ModelFactory

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    String,
)


class ARObject:
    """AUTOSAR ARObject."""
    """Abstract base class - do not instantiate directly."""

    checksum: Optional[String]
    timestamp: Optional[DateTime]
    def __init__(self) -> None:
        """Initialize ARObject."""
        self.checksum: Optional[String] = None
        self.timestamp: Optional[DateTime] = None

    def serialize(self) -> ET.Element:
        """Serialize object to XML element using reflection.

        Automatically discovers all non-private attributes via vars(self),
        converts names to XML tags, and serializes them as child elements.

        Note: This is a base class for all AUTOSAR elements. Namespace handling
        is applied only when the current object type is AUTOSAR (the root element).

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Add AUTOSAR namespace attributes if this is an AUTOSAR instance (root element only)
        if self.__class__.__name__ == 'AUTOSAR':
            elem.set("xmlns", "http://autosar.org/schema/r4.0")
            elem.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
            elem.set("xsi:schemaLocation", "http://autosar.org/schema/r4.0 AUTOSAR_4-0-3.xsd")

        # Get all instance attributes
        for name, value in vars(self).items():
            # Skip private attributes
            if name.startswith('_'):
                continue

            # Convert Python name to XML tag
            xml_tag = NameConverter.to_xml_tag(name)

            # Skip None values
            if value is None:
                continue

            # Check if this should be an XML attribute (via decorator)
            if self._is_xml_attribute(name):
                elem.set(xml_tag, str(value))
            elif hasattr(value, 'serialize'):
                # Recursively serialize child objects
                child = value.serialize()
                elem.append(child)
            elif isinstance(value, list):
                # Serialize list items - create wrapper element
                wrapper = ET.Element(xml_tag)
                for item in value:
                    if hasattr(item, 'serialize'):
                        wrapper.append(item.serialize())
                    else:
                        child = ET.Element(xml_tag)
                        child.text = str(item)
                        wrapper.append(child)
                elem.append(wrapper)
            else:
                # Primitive value - create element with text content
                child = ET.Element(xml_tag)
                child.text = str(value)
                elem.append(child)

        return elem

    def _get_xml_tag(self) -> str:
        """Get XML tag name for this class.

        Checks for @xml_tag decorator override, otherwise auto-generates from class name.

        Returns:
            XML tag name
        """
        # Check for decorator override
        if hasattr(self.__class__, '_xml_tag'):
            return self.__class__._xml_tag

        # Auto-generate from class name
        return NameConverter.to_xml_tag(self.__class__.__name__)

    def _is_xml_attribute(self, attr_name: str) -> bool:
        """Check if an attribute should be serialized as XML attribute.

        Checks for @xml_attribute decorator on the property.

        Args:
            attr_name: Name of the attribute to check

        Returns:
            True if should be XML attribute, False if element
        """
        # Get the property if it exists
        prop = getattr(self.__class__, attr_name, None)
        if prop and hasattr(prop, 'fget'):
            # Check if the property getter has the decorator marker
            return hasattr(prop.fget, '_is_xml_attribute') and prop.fget._is_xml_attribute

        # Check if the attribute itself has the marker
        attr = getattr(self.__class__, attr_name, None)
        if attr and hasattr(attr, '_is_xml_attribute'):
            return attr._is_xml_attribute

        return False

    @classmethod
    def deserialize(cls, element: ET.Element) -> ARObject:
        """Deserialize XML element to Python object.

        Creates a new instance and populates attributes by matching
        XML tags to Python attribute names.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Python object
        """
        # Create instance without calling __init__
        obj = cls.__new__(cls)

        # Call __init__ to set default values
        obj.__init__()

        # Get type hints to know what attributes to expect
        try:
            type_hints = get_type_hints(cls)
        except Exception:
            # Fallback: Use __annotations__ directly if get_type_hints fails
            # This can happen due to circular imports or missing types
            # Note: Annotations will be strings due to 'from __future__ import annotations'
            type_hints = {}
            # Collect annotations from entire MRO
            for base_cls in cls.__mro__:
                if hasattr(base_cls, '__annotations__'):
                    for attr_name, attr_type_str in base_cls.__annotations__.items():
                        if attr_name not in type_hints:
                            # Keep as string - _extract_value will handle it
                            type_hints[attr_name] = attr_type_str

        # Helper function to strip namespace from tag
        def strip_namespace(tag: str) -> str:
            """Strip namespace from XML tag.

            Args:
                tag: XML tag with optional namespace

            Returns:
                Tag without namespace
            """
            if '}' in tag:
                return tag.split('}')[1]
            return tag

        # Process each attribute from type hints
        for attr_name, attr_type in type_hints.items():
            # Convert Python name to XML tag
            xml_tag = NameConverter.to_xml_tag(attr_name)

            # Check if this should be an XML attribute
            if ARObject._is_xml_attribute_static(cls, attr_name):
                value = element.get(xml_tag)
            else:
                # Find child element - try both with and without namespace
                child = element.find(xml_tag)
                if child is None:
                    # Try to find by matching stripped tag names
                    for elem in element:
                        if strip_namespace(elem.tag) == xml_tag:
                            child = elem
                            break

                if child is not None:
                    # Get value based on type
                    value = ARObject._extract_value(child, attr_type)
                else:
                    value = None

            # Set attribute
            setattr(obj, attr_name, value)

        return obj

    @staticmethod
    def _is_xml_attribute_static(cls, attr_name: str) -> bool:
        """Static version to check if attribute should be XML attribute.

        Args:
            cls: The class to check
            attr_name: Name of the attribute

        Returns:
            True if should be XML attribute
        """
        prop = getattr(cls, attr_name, None)
        if prop and hasattr(prop, 'fget'):
            return hasattr(prop.fget, '_is_xml_attribute') and prop.fget._is_xml_attribute

        attr = getattr(cls, attr_name, None)
        if attr and hasattr(attr, '_is_xml_attribute'):
            return attr._is_xml_attribute

        return False

    @staticmethod
    def _import_class_by_name(class_name: str):
        """Import a class by name from armodel.models.M2.

        Args:
            class_name: Name of the class to import (e.g., "ARPackage")

        Returns:
            The imported class, or None if not found
        """
        import sys
        import importlib

        # Check if already in sys.modules
        for module_name, module in sys.modules.items():
            if module_name.startswith('armodel.models.M2'):
                if hasattr(module, class_name):
                    cls = getattr(module, class_name)
                    if isinstance(cls, type):
                        return cls

        # Try to import from known locations
        # Convert class name to snake_case for filename
        class_filename = class_name.replace('<', '_').replace('>', '_')

        # Common package paths to search
        search_paths = [
            f'armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.{class_name}.{class_filename}',
            f'armodel.models.M2.AUTOSARTemplates.{class_name}.{class_filename}',
            f'armodel.models.M2.MSR.{class_name}.{class_filename}',
        ]

        for module_path in search_paths:
            try:
                module = importlib.import_module(module_path)
                if hasattr(module, class_name):
                    return getattr(module, class_name)
            except (ImportError, ModuleError):
                continue

        # Fallback: try searching through all M2 modules
        try:
            from armodel.models.M2 import AUTOSARTemplates, MSR

            # Search in AUTOSARTemplates
            if hasattr(AUTOSARTemplates, '__path__'):
                from pkgutil import walk_packages
                for importer, modname, ispkg in walk_packages(AUTOSARTemplates.__path__, AUTOSARTemplates.__name__ + '.'):
                    try:
                        module = importlib.import_module(modname)
                        if hasattr(module, class_name):
                            cls = getattr(module, class_name)
                            if isinstance(cls, type):
                                return cls
                    except (ImportError, ModuleError):
                        continue
        except Exception:
            pass

        return None

    @staticmethod
    def _strip_namespace(tag: str) -> str:
        """Strip namespace from XML tag.

        Args:
            tag: XML tag with optional namespace

        Returns:
            Tag without namespace
        """
        if '}' in tag:
            return tag.split('}')[1]
        return tag

    @staticmethod
    def _extract_text(element: ET.Element) -> Optional[str]:
        """Extract text content from XML element, returning None if missing or empty.

        Protected static helper method for deserialization. Accessible to all subclasses.

        Args:
            element: XML element to extract text from

        Returns:
            Text content or None if element is missing or empty
        """
        if element is None or element.text is None:
            return None
        text = element.text.strip()
        return text if text else None

    @staticmethod
    def _extract_value(element: ET.Element, attr_type):
        """Extract value from XML element based on type.

        Args:
            element: XML element
            attr_type: Expected type (from type hints) - can be type object or string

        Returns:
            Extracted value
        """
        if element is None:
            return None

        # Get factory instance
        factory = ModelFactory()
        if not factory.is_initialized():
            factory.load_mappings()
        """Extract value from XML element based on type.

        Args:
            element: XML element
            attr_type: Expected type (from type hints) - can be type object or string

        Returns:
            Extracted value
        """
        if element is None:
            return None

        # Handle string type annotations (from __annotations__ with future import)
        if isinstance(attr_type, str):
            # Parse string type annotations like "list[ARPackage]" or "Optional[SomeType]"
            import re

            # Extract list type
            list_match = re.match(r'list\[(.+?)\]', attr_type)
            if list_match:
                inner_type_str = list_match.group(1)
                # Find all direct child elements
                children = list(element)

                # Try to import the base class to check for polymorphic types
                base_class = ARObject._import_class_by_name(inner_type_str)

                # Deserialize each child element
                result = []
                for child in children:
                    # Get the child's XML tag name (strip namespace if present)
                    child_tag = ARObject._strip_namespace(child.tag)

                    # Check if base class is an ARObject subclass (polymorphic case)
                    if base_class and isinstance(base_class, type) and issubclass(base_class, ARObject):
                        # Get the expected XML tag for the base class
                        expected_tag = NameConverter.to_xml_tag(base_class.__name__)

                        # If child tag differs from base class tag, try to use concrete class
                        if child_tag != expected_tag:
                            # Get concrete class from factory
                            concrete_class = factory.get_class(child_tag)

                            # Check if concrete class is a subclass of base_class
                            if concrete_class and issubclass(concrete_class, base_class):
                                # Use concrete class for deserialization
                                item = concrete_class.deserialize(child)
                                result.append(item)
                                continue

                        # Fallback to base class deserialization
                        if hasattr(base_class, 'deserialize'):
                            item = base_class.deserialize(child)
                            result.append(item)
                        else:
                            result.append(child.text if child.text else None)
                    else:
                        # For non-polymorphic types, try to deserialize using the class name directly
                        item_class = ARObject._import_class_by_name(inner_type_str)
                        if item_class and hasattr(item_class, 'deserialize'):
                            item = item_class.deserialize(child)
                            result.append(item)
                        else:
                            # Fallback to text content
                            result.append(child.text if child.text else None)

                return result

            # Handle optional types
            optional_match = re.match(r'Optional\[(.+?)\]', attr_type)
            if optional_match:
                inner_type_str = optional_match.group(1)
                # Try to import and deserialize
                item_class = ARObject._import_class_by_name(inner_type_str)
                if item_class and hasattr(item_class, 'deserialize'):
                    return item_class.deserialize(element)

                # Fallback to text content
                return element.text if element.text else None

            # For simple class names, try to import and deserialize
            item_class = ARObject._import_class_by_name(attr_type)
            if item_class and hasattr(item_class, 'deserialize'):
                return item_class.deserialize(element)

            # For simple string types, just return text
            return element.text if element.text else None

        # Check if it's a list type
        if get_origin(attr_type) is list:
            # Get the element type
            type_args = get_args(attr_type)
            if type_args:
                item_type = type_args[0]

                # Find all direct child elements (not grandchildren)
                children = list(element)

                # Deserialize each child element
                result = []
                for child in children:
                    # Get the child's XML tag name (strip namespace if present)
                    child_tag = ARObject._strip_namespace(child.tag)

                    # Check if this is an ARObject subclass (polymorphic case)
                    if isinstance(item_type, type) and issubclass(item_type, ARObject):
                        # Get the expected XML tag for the base class
                        expected_tag = NameConverter.to_xml_tag(item_type.__name__)

                        # If child tag differs from base class tag, try to use concrete class
                        if child_tag != expected_tag:
                            # Get concrete class from factory
                            concrete_class = factory.get_class(child_tag)

                            # Check if concrete class is a subclass of item_type
                            if concrete_class and issubclass(concrete_class, item_type):
                                # Use concrete class for deserialization
                                item = concrete_class.deserialize(child)
                                result.append(item)
                                continue

                        # Fallback to base class deserialization
                        if hasattr(item_type, 'deserialize'):
                            item = item_type.deserialize(child)
                            result.append(item)
                        else:
                            result.append(child.text if child.text else None)
                    elif hasattr(item_type, 'deserialize'):
                        # For non-ARObject types with deserialize method
                        item = item_type.deserialize(child)
                        result.append(item)
                    else:
                        # For primitives, get text content
                        result.append(child.text if child.text else None)

                return result

        # Check if it's an Optional type
        if get_origin(attr_type) is Union:
            type_args = get_args(attr_type)
            # Get the first non-None type
            for arg in type_args:
                if arg is not type(None):
                    attr_type = arg
                    break

        # For object types with deserialize method, recursively deserialize
        # Check if attr_type is a class (not a primitive type like str, int, etc.)
        if isinstance(attr_type, type) and hasattr(attr_type, 'deserialize'):
            return attr_type.deserialize(element)

        # For primitive types, return text content
        text = element.text
        if text is None:
            return None

        # Simple type conversions for primitives
        if attr_type is str:
            return text
        elif attr_type is int:
            try:
                return int(text)
            except ValueError:
                return text
        elif attr_type is float:
            try:
                return float(text)
            except ValueError:
                return text
        elif attr_type is bool:
            return text.lower() in ('true', '1', 'yes')
        else:
            # Default to string
            return text


class ARObjectBuilder:
    """Builder for ARObject."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ARObject = ARObject

    def build(self) -> ARObject:
        """Build and return ARObject object.

        Returns:
            ARObject instance
        """
        # TODO: Add validation
        return self._obj