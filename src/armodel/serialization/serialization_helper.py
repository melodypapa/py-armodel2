"""Serialization helper utilities for ARObject.

This module provides static utility methods for XML serialization and deserialization
of AUTOSAR model objects. These methods were extracted from ARObject to improve
code organization and maintainability.
"""

# mypy: disable-error-code="no-any-return,assignment,union-attr,type-arg,no-untyped-def,unused-ignore"

from __future__ import annotations

import re
import warnings
import xml.etree.ElementTree as ET
from typing import TYPE_CHECKING, Any, Optional, Union, get_args, get_origin

from armodel.core.global_settings import GlobalSettingsManager
from armodel.serialization.name_converter import NameConverter

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import (
        ARObject,
    )


class SerializationHelper:
    """Static utility methods for XML serialization and deserialization."""

    @staticmethod
    def get_atp_variant_wrapper_path(class_name: str) -> str:
        """Derive wrapper path for atpVariation classes from class name.

        AUTOSAR atpVariation pattern wraps all attributes in nested elements.
        The pattern is: <CLASS-TAG>-VARIANTS/<CLASS-TAG>-CONDITIONAL

        Examples:
            SwDataDefProps → "SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL"
            DiagnosticCommonProps → "DIAGNOSTIC-COMMON-PROPS-VARIANTS/DIAGNOSTIC-COMMON-PROPS-CONDITIONAL"

        Args:
            class_name: Python class name (e.g., "SwDataDefProps")

        Returns:
            Wrapper path (e.g., "SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL")
        """
        class_tag = NameConverter.to_xml_tag(class_name)
        return f"{class_tag}-VARIANTS/{class_tag}-CONDITIONAL"

    @staticmethod
    def get_xml_tag(cls: type) -> str:
        """Get XML tag name for a class.

        Auto-generates from class name using NameConverter.

        Args:
            cls: The class to get the tag for

        Returns:
            XML tag name
        """
        return NameConverter.to_xml_tag(cls.__name__)

    @staticmethod
    def is_xml_attribute(obj: Any, attr_name: str) -> bool:  # type: ignore[no-any-return]
        """Check if an attribute should be serialized as XML attribute.

        Checks for @xml_attribute decorator on the property.

        Args:
            obj: The object instance
            attr_name: Name of the attribute to check

        Returns:
            True if should be XML attribute, False if element
        """
        # Get the property if it exists
        prop = getattr(type(obj), attr_name, None)
        if prop and hasattr(prop, 'fget'):
            # Check if the property getter has the decorator marker
            return hasattr(prop.fget, '_is_xml_attribute') and prop.fget._is_xml_attribute  # type: ignore[no-any-return]

        # Check if the attribute itself has the marker
        attr = getattr(type(obj), attr_name, None)
        if attr and hasattr(attr, '_is_xml_attribute'):
            return attr._is_xml_attribute  # type: ignore[no-any-return]

        return False

    @staticmethod
    def is_xml_attribute_static(cls: type, attr_name: str) -> bool:  # type: ignore[no-any-return]
        """Static version to check if attribute should be XML attribute.

        Args:
            cls: The class to check
            attr_name: Name of the attribute

        Returns:
            True if should be XML attribute
        """
        prop = getattr(cls, attr_name, None)
        if prop and hasattr(prop, 'fget'):
            return hasattr(prop.fget, '_is_xml_attribute') and prop.fget._is_xml_attribute  # type: ignore[no-any-return]

        attr = getattr(cls, attr_name, None)
        if attr and hasattr(attr, '_is_xml_attribute'):
            return attr._is_xml_attribute  # type: ignore[no-any-return]

        return False

    @staticmethod
    def get_element_tag(attr_name: str) -> str:
        """Get XML tag name for a class attribute/element.

        Auto-generates from Python attribute name using NameConverter.

        Args:
            attr_name: Name of the Python attribute

        Returns:
            XML tag name to use for this element
        """
        return NameConverter.to_xml_tag(attr_name)

    @staticmethod
    def get_element_tag_path(attr_name: str) -> Union[str, list[str]]:
        """Get full XML tag path for a class attribute/element.

        Auto-generates from Python attribute name using NameConverter.

        Args:
            attr_name: Name of the Python attribute

        Returns:
            XML tag as a string (single-level path only)
        """
        # Auto-generate from Python name
        return NameConverter.to_xml_tag(attr_name)

    @staticmethod
    def get_element_tag_path_static(cls: type, attr_name: str) -> Union[str, list[str]]:
        """Get full XML tag path for a class attribute/element (static version).

        Args:
            cls: The class to check
            attr_name: Name of the attribute to check

        Returns:
            XML tag path as a list for multi-level paths, or a string for single-level paths
        """
        # Auto-generate from Python name
        return NameConverter.to_xml_tag(attr_name)

    @staticmethod
    def has_l_prefix(cls: type, attr_name: str) -> bool:
        """Check if an attribute has @l_prefix decorator.

        Args:
            cls: The class to check
            attr_name: Name of the attribute to check

        Returns:
            True if attribute has @l_prefix decorator
        """
        # Check if it's a property
        prop = getattr(cls, attr_name, None)
        if prop and isinstance(prop, property) and hasattr(prop.fget, '_l_prefix'):
            return True

        # Check if the attribute itself has the marker
        attr = getattr(cls, attr_name, None)
        if attr and hasattr(attr, '_l_prefix'):
            return True

        return False

    @staticmethod
    def get_l_prefix_tag(cls: type, attr_name: str) -> Optional[str]:  # type: ignore[no-any-return]
        """Get the XML tag name for an l_prefix attribute.

        Args:
            cls: The class to check
            attr_name: Name of the attribute to check

        Returns:
            XML tag name if attribute has @l_prefix decorator, None otherwise
        """
        # Check if it's a property
        prop = getattr(cls, attr_name, None)
        if prop and isinstance(prop, property) and hasattr(prop.fget, '_l_prefix_tag'):
            return prop.fget._l_prefix_tag  # type: ignore[no-any-return]

        # Check if the attribute itself has the marker
        attr = getattr(cls, attr_name, None)
        if attr and hasattr(attr, '_l_prefix_tag'):
            return attr._l_prefix_tag  # type: ignore[union-attr,no-any-return]

        return None

    @staticmethod
    def serialize_l_prefix(child_elem: ET.Element, l_prefix_tag: str) -> ET.Element:
        """Wrap a child element in the l_prefix tag.

        This method takes a serialized child element (e.g., LPlainText)
        and wraps it in a language-specific tag (e.g., L-10), copying
        all attributes and text content from the child element.

        Args:
            child_elem: The child element to wrap (already serialized)
            l_prefix_tag: The language-specific tag to use (e.g., "L-10")

        Returns:
            New element wrapping the child content
        """
        wrapped = ET.Element(l_prefix_tag)
        # Copy attributes from child to wrapper
        if hasattr(child_elem, 'attrib'):
            wrapped.attrib.update(child_elem.attrib)
        # Copy text from child to wrapper
        if child_elem.text:
            wrapped.text = child_elem.text
        # Copy all children from child to wrapper
        for child in child_elem:
            wrapped.append(child)
        return wrapped

    @staticmethod
    def validate_deserialization(cls: type, element: ET.Element, type_hints: dict[str, Any]) -> None:  # type: ignore[type-arg]
        """Validate deserialization by checking for unrecognized XML elements.

        This method checks if any XML elements in the input were not
        matched to Python attributes, based on global settings.

        Args:
            cls: The class being deserialized
            element: XML element that was deserialized
            type_hints: Type hints dictionary used for deserialization

        Raises:
            ValueError: If strict_validation is enabled and unrecognized elements found
        """
        settings = GlobalSettingsManager()

        # Skip validation if both settings are disabled
        if not (settings.warn_on_unrecognized or settings.strict_validation):
            return

        # Build set of expected XML tags from type hints
        expected_tags = {NameConverter.to_xml_tag(name) for name in type_hints.keys()}

        # For atp_variant classes, add wrapper tags to expected tags
        # These are not attributes but structural elements
        if hasattr(cls, '_atp_variant'):
            wrapper_path = SerializationHelper.get_atp_variant_wrapper_path(cls.__name__)
            for wrapper_tag in wrapper_path.split('/'):
                expected_tags.add(wrapper_tag)

        # For l_prefix attributes, add their l_prefix tags to expected tags
        # These are language-specific wrapper elements (e.g., L-10, L-4, L-2)
        for attr_name in type_hints.keys():
            # Check both private (e.g., "_l10") and public (e.g., "l10") attribute names
            # Type hints contain private attribute names, but properties are public
            if SerializationHelper.has_l_prefix(cls, attr_name):
                l_prefix_tag = SerializationHelper.get_l_prefix_tag(cls, attr_name)
                if l_prefix_tag:
                    expected_tags.add(l_prefix_tag)
            # Also check the public version (remove leading underscore)
            if attr_name.startswith('_'):
                public_name = attr_name[1:]
                if SerializationHelper.has_l_prefix(cls, public_name):
                    l_prefix_tag = SerializationHelper.get_l_prefix_tag(cls, public_name)
                    if l_prefix_tag:
                        expected_tags.add(l_prefix_tag)

        # Check each child element
        for child in element:
            child_tag = SerializationHelper.strip_namespace(child.tag)
            if child_tag not in expected_tags:
                msg = f"Unrecognized XML element <{child_tag}> in {cls.__name__}. " \
                      f"Element will be ignored during deserialization."
                if settings.strict_validation:
                    raise ValueError(msg)
                else:
                    warnings.warn(msg, UserWarning, stacklevel=3)

    @staticmethod
    def import_class_by_name(class_name: str):  # type: ignore[no-untyped-def]
        """Import a class by name from armodel.models.M2.

        Args:
            class_name: Name of the class to import (e.g., "ARPackage")

        Returns:
            The imported class, or None if not found
        """
        import sys
        import importlib
        from armodel.serialization.model_factory import ModelFactory

        # Check if already in sys.modules
        for module_name, module in sys.modules.items():
            if module_name.startswith('armodel.models.M2'):
                if hasattr(module, class_name):
                    cls = getattr(module, class_name)
                    if isinstance(cls, type):
                        return cls

        # Common package paths to search
        # Convert class name to snake_case for filename
        class_filename = class_name.replace('<', '_').replace('>', '_')

        # Compute snake_case filename for ComputationMethod package
        compu_method_filename = NameConverter.to_python_name(NameConverter.to_xml_tag(class_name))

        search_paths = [
            f'armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.{class_name}.{class_filename}',
            f'armodel.models.M2.AUTOSARTemplates.{class_name}.{class_filename}',
            f'armodel.models.M2.MSR.{class_name}.{class_filename}',
            f'armodel.models.M2.MSR.AsamHdo.ComputationMethod.{compu_method_filename}',
        ]

        for module_path in search_paths:
            try:
                module = importlib.import_module(module_path)
                if hasattr(module, class_name):
                    return getattr(module, class_name)
            except (ImportError, ModuleNotFoundError):
                continue

        # Fallback: try searching through all M2 modules
        try:
            from armodel.models.M2 import AUTOSARTemplates
            from pkgutil import walk_packages

            # Search in AUTOSARTemplates
            if hasattr(AUTOSARTemplates, '__path__'):
                for importer, modname, ispkg in walk_packages(AUTOSARTemplates.__path__, AUTOSARTemplates.__name__ + '.'):
                    try:
                        module = importlib.import_module(modname)
                        if hasattr(module, class_name):
                            cls = getattr(module, class_name)
                            if isinstance(cls, type):
                                return cls
                    except (ImportError, ModuleNotFoundError):
                        continue
        except Exception:
            pass

        # Last resort: Use ModelFactory if available
        try:
            factory = ModelFactory()
            if factory.is_initialized():
                # Try to get the XML tag from class name and look up in factory
                xml_tag = NameConverter.to_xml_tag(class_name)
                cls = factory.get_class(xml_tag)
                if cls:
                    return cls
        except Exception:
            pass

        return None

    @staticmethod
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

    @staticmethod
    def add_text_element(parent: ET.Element, tag: str, value: Any) -> None:
        """Add a child element with text content to parent if value is not None.

        Args:
            parent: Parent XML element to add child to
            tag: XML tag name for the child element
            value: Value to serialize. If None, no element is added.
        """
        if value is not None:
            child = ET.Element(tag)
            child.text = str(value)
            parent.append(child)

    @staticmethod
    def extract_text(element: ET.Element, tag: Optional[str] = None) -> Optional[str]:
        """Extract text content from XML element, returning None if missing or empty.

        If tag is provided, first finds the child element by tag name with namespace handling.

        Args:
            element: XML element to extract text from (or parent element if tag is provided)
            tag: Optional tag name to find child element. Handles namespace prefixes.

        Returns:
            Text content or None if element is missing or empty
        """
        # If tag is provided, find the child element first
        if tag is not None:
            # Try direct match first
            child = element.find(tag)
            if child is None:
                # Try matching by stripped tag name (handles namespace)
                for elem in element:
                    if SerializationHelper.strip_namespace(elem.tag) == tag:
                        child = elem
                        break
            element = child

        if element is None or element.text is None:
            return None
        text = element.text.strip()
        return text if text else None

    @staticmethod
    def unwrap_primitive(result: Any) -> Any:
        """Unwrap ARPrimitive instances to their underlying Python types.

        ARPrimitive wrappers are transparently unwrapped to maintain
        backward compatibility with code expecting plain primitive values.
        Primitives with additional attributes (e.g., Limit with interval_type)
        are kept as-is to preserve metadata.

        Args:
            result: The deserialized value to potentially unwrap

        Returns:
            Unwrapped primitive value, or original result if not unwrapable
        """
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import (
            ARPrimitive,
        )

        if not isinstance(result, ARPrimitive):
            return result

        # Check if primitive has additional non-None attributes besides 'value'
        has_metadata = any(
            not name.startswith('_') and name != 'value' and value is not None
            for name, value in vars(result).items()
        )

        # Only unwrap simple primitives without metadata
        return result if has_metadata else result.value

    @staticmethod
    def extract_value(element: ET.Element, attr_type: Any) -> Any:
        """Extract value from XML element based on type.

        Args:
            element: XML element
            attr_type: Expected type (from type hints) - can be type object or string

        Returns:
            Extracted value
        """
        if element is None:
            return None

        from armodel.serialization.model_factory import ModelFactory

        # Get factory instance
        factory = ModelFactory()
        if not factory.is_initialized():
            factory.load_mappings()

        # Handle string type annotations (from __annotations__ with future import)
        if isinstance(attr_type, str):
            # Parse string type annotations like "list[ARPackage]" or "Optional[SomeType]"

            # Extract list type
            list_match = re.match(r'list\[(.+?)\]', attr_type)
            if list_match:
                inner_type_str = list_match.group(1)
                # Find all direct child elements
                children = list(element)

                # Try to import the base class to check for polymorphic types
                base_class = SerializationHelper.import_class_by_name(inner_type_str)

                # Deserialize each child element
                result = []
                for child in children:
                    # Get the child's XML tag name (strip namespace if present)
                    child_tag = SerializationHelper.strip_namespace(child.tag)

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
                                item = SerializationHelper.unwrap_primitive(concrete_class.deserialize(child))
                                result.append(item)
                                continue

                        # Fallback to base class deserialization
                        if hasattr(base_class, 'deserialize'):
                            item = SerializationHelper.unwrap_primitive(base_class.deserialize(child))
                            result.append(item)
                        else:
                            result.append(child.text if child.text else None)
                    else:
                        # For non-polymorphic types, try to deserialize using the class name directly
                        item_class = SerializationHelper.import_class_by_name(inner_type_str)
                        if item_class and hasattr(item_class, 'deserialize'):
                            item = SerializationHelper.unwrap_primitive(item_class.deserialize(child))
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
                item_class = SerializationHelper.import_class_by_name(inner_type_str)
                if item_class and hasattr(item_class, 'deserialize'):
                    return SerializationHelper.unwrap_primitive(item_class.deserialize(element))

                # Fallback to text content
                return element.text if element.text else None

            # For simple class names, try to import and deserialize
            item_class = SerializationHelper.import_class_by_name(attr_type)
            if item_class and hasattr(item_class, 'deserialize'):
                return SerializationHelper.unwrap_primitive(item_class.deserialize(element))

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
                    child_tag = SerializationHelper.strip_namespace(child.tag)

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
                                item = SerializationHelper.unwrap_primitive(concrete_class.deserialize(child))
                                result.append(item)
                                continue

                        # Fallback to base class deserialization
                        if hasattr(item_type, 'deserialize'):
                            item = SerializationHelper.unwrap_primitive(item_type.deserialize(child))
                            result.append(item)
                        else:
                            result.append(child.text if child.text else None)
                    elif hasattr(item_type, 'deserialize'):
                        # For non-ARObject types with deserialize method
                        item = SerializationHelper.unwrap_primitive(item_type.deserialize(child))
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
            return SerializationHelper.unwrap_primitive(attr_type.deserialize(element))

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

    @staticmethod
    def find_child_element(parent: ET.Element, tag: str) -> Optional[ET.Element]:
        """Find child element by tag name (with namespace handling).

        Args:
            parent: Parent XML element
            tag: Tag name to search for

        Returns:
            Child element if found, None otherwise
        """
        # Direct find without namespace
        child = parent.find(tag)
        if child is not None:
            return child  # type: ignore[assignment]

        # Try with namespace handling
        for elem in parent:
            if elem.tag.endswith(tag):
                return elem  # type: ignore[assignment]
        return None

    @staticmethod
    def find_all_child_elements(parent: ET.Element, tag: str) -> list[ET.Element]:
        """Find all child elements by tag name (with namespace handling).

        Args:
            parent: Parent XML element
            tag: Tag name to search for

        Returns:
            List of child elements
        """
        # Direct findall without namespace
        children = parent.findall(tag)
        if children:
            return children

        # Try with namespace handling
        return [elem for elem in parent if elem.tag.endswith(tag)]

    @staticmethod
    def deserialize_by_tag(element: ET.Element, class_name: Optional[str] = None) -> Optional["ARObject"]:  # type: ignore[no-any-return]
        """Deserialize XML element using class name (for TYPE_CHECKING compatibility).

        This method is used when a class type is only available in TYPE_CHECKING blocks
        but needs to be used at runtime in deserialize() methods. It uses the
        ModelFactory to get the class from the tag name without importing it.

        Args:
            element: XML element to deserialize
            class_name: Name of the class to deserialize to. If None, the class is
                       determined from the element's XML tag name.

        Returns:
            Deserialized object, or None if the element cannot be deserialized
        """
        from armodel.serialization.model_factory import ModelFactory

        factory = ModelFactory()
        if not factory.is_initialized():
            factory.load_mappings()

        # Determine the XML tag to use
        if class_name is None:
            # Use the element's tag directly
            xml_tag = SerializationHelper.strip_namespace(element.tag)
        else:
            # Convert class name to XML tag
            xml_tag = NameConverter.to_xml_tag(class_name)

        # Get the class from the factory
        cls = factory.get_class(xml_tag)
        if cls is None:
            # If class_name was provided, raise an error
            if class_name is not None:
                raise ValueError(f"Unknown class: {class_name}")
            # Otherwise, just return None (skip this element)
            return None

        # Call the deserialize method on the class
        return cls.deserialize(element)

    @staticmethod
    def deserialize_with_type(element: ET.Element, attr_type: str) -> Any:
        """Deserialize an XML element as a specific type.

        This method is used when the XML element's tag is a wrapper (like L-10 for l_prefix)
        and not a class name. It deserializes the element using the provided type instead of
        inferring the type from the XML tag.

        Args:
            element: XML element to deserialize
            attr_type: The type string to deserialize as (e.g., "LPlainText")

        Returns:
            Deserialized object, or None if the type cannot be found or deserialized
        """
        # Handle Optional types
        if attr_type.startswith("Optional["):
            match = re.match(r"Optional\[(.+?)\]", attr_type)
            if match:
                inner_type = match.group(1)
                return SerializationHelper.deserialize_with_type(element, inner_type)
            return None

        # Handle list types
        elif attr_type.startswith("list["):
            match = re.match(r"list\[(.+?)\]", attr_type)
            if match:
                inner_type = match.group(1)
                result = []
                for child in element:
                    value = SerializationHelper.deserialize_with_type(child, inner_type)
                    if value is not None:
                        result.append(value)
                return result
            return []

        # Import the type and deserialize
        try:
            # Convert type string to class
            type_class = SerializationHelper.import_class_by_name(attr_type)
            if type_class and hasattr(type_class, 'deserialize'):
                return type_class.deserialize(element)
        except Exception:
            pass

        # Fallback: try to use deserialize_by_tag
        return SerializationHelper.deserialize_by_tag(element, None)

    @staticmethod
    def serialize_item(value: Any, expected_type: str) -> Optional[ET.Element]:  # type: ignore[no-any-return]
        """Serialize a single item for use in generated serialize() methods.

        This helper method is used by generated serialize() methods to serialize
        individual items (from lists or single attributes) without needing to
        import the actual types. It handles ARPrimitive, AREnum, ARRef, and
        ARObject types efficiently.

        Args:
            value: The value to serialize
            expected_type: The expected type name (for context, can be "Any" for polymorphic)

        Returns:
            Serialized XML element, or None if value is None
        """
        if value is None:
            return None

        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import (
            ARPrimitive,
        )
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import (
            AREnum,
        )
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import (
            ARRef,
        )

        # Handle ARPrimitive types
        if isinstance(value, ARPrimitive):
            return value.serialize()

        # Handle AREnum types
        elif isinstance(value, AREnum):
            elem = ET.Element("VALUE")
            elem.text = str(value.value).upper()
            return elem

        # Handle ARRef types
        elif isinstance(value, ARRef):
            return value.serialize()

        # Handle ARObject types
        elif hasattr(value, 'serialize'):
            return value.serialize()

        # Handle primitive Python types (str, int, float, bool)
        else:
            elem = ET.Element("VALUE")
            elem.text = str(value)
            return elem

    @staticmethod
    def serialize_with_correct_tag(value: Any, xml_tag: str) -> ET.Element:  # type: ignore[no-any-return]
        """Serialize a value with the correct XML tag from parent context.

        For ARPrimitive, AREnum, and ARRef types, uses the parent attribute's tag
        instead of the class name to ensure correct XML element names (e.g., LIMIT
        instead of the class name that might differ).

        Args:
            value: The value to serialize
            xml_tag: The XML tag name from the parent attribute context

        Returns:
            Serialized XML element
        """
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import (
            ARPrimitive,
        )
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import (
            AREnum,
        )
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import (
            ARRef,
        )

        if isinstance(value, ARPrimitive):
            # Serialize the primitive but wrap it with the correct tag
            serialized = value.serialize()
            wrapper = ET.Element(xml_tag)
            # Copy all attributes, text, and children
            wrapper.attrib.update(serialized.attrib)
            wrapper.text = serialized.text
            for child in list(serialized):
                wrapper.append(child)
            return wrapper
        elif isinstance(value, AREnum):
            # For AREnum types, use the parent attribute's tag instead of class name
            # This ensures elements like <SW-CALIBRATION-ACCESS> instead of <SW-CALIBRATION-ACCESS-ENUM>
            child = ET.Element(xml_tag)
            child.text = str(value.value).upper()
            return child
        elif isinstance(value, ARRef):
            # For ARRef types, serialize and wrap with the correct tag
            # ARRef.serialize() returns an element with DEST attribute and text content
            serialized = value.serialize()
            wrapper = ET.Element(xml_tag)
            # Copy all attributes (especially DEST) and text content
            wrapper.attrib.update(serialized.attrib)
            wrapper.text = serialized.text
            return wrapper
        else:
            # For complex objects, serialize directly
            return value.serialize()