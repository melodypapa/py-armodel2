"""ARObject AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 191)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ArObject.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Union, get_type_hints, get_args, get_origin
import warnings
import xml.etree.ElementTree as ET

from armodel.core.global_settings import GlobalSettingsManager
from armodel.serialization.name_converter import NameConverter
from armodel.serialization.model_factory import ModelFactory
from armodel.serialization.decorators import xml_attribute

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
        DateTime,
        String,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import (
        ARPrimitive,
    )
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import (
        AREnum,
    )


class ARObject:
    """AUTOSAR ARObject."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize ARObject."""
        self._checksum: Optional["String"] = None
        self._timestamp: Optional["DateTime"] = None

    @property
    def checksum(self) -> Optional["String"]:
        """Checksum attribute."""
        return self._checksum

    @checksum.setter
    def checksum(self, value: Optional["String"]) -> None:
        """Set checksum attribute."""
        self._checksum = value

    @property
    @xml_attribute
    def timestamp(self) -> Optional["DateTime"]:
        """Timestamp attribute serialized as XML attribute 'T'."""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: Optional["DateTime"]) -> None:
        """Set timestamp attribute."""
        self._timestamp = value

    @staticmethod
    def _get_atp_variant_wrapper_path(class_name: str) -> str:
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

        # Note: AUTOSAR namespace attributes are now handled in AUTOSAR.serialize()
        # This base class no longer hardcodes schema location

        # Check if this class uses atpVariation pattern
        if hasattr(self.__class__, '_atp_variant'):
            wrapper_path = self._get_atp_variant_wrapper_path(self.__class__.__name__)
            wrapper_elements = wrapper_path.split('/')
            
            # Create nested wrapper elements
            current_elem = elem
            for wrapper_name in wrapper_elements:
                wrapper_elem = ET.Element(wrapper_name)
                current_elem.append(wrapper_elem)
                current_elem = wrapper_elem
            
            # Serialize all attributes into the innermost wrapper
            for name, value in vars(self).items():
                # Skip private attributes
                if name.startswith('_'):
                    continue

                # Check for custom XML element tag via @xml_element_tag decorator
                xml_tag = self._get_element_tag(name)

                # Skip None values
                if value is None:
                    continue

                # Check if this should be an XML attribute (via decorator)
                if self._is_xml_attribute(name):
                    # XML attributes go on the main element, not inside wrapper
                    elem.set(xml_tag, str(value))
                elif ARObject._has_l_prefix(self.__class__, name):
                    # Handle l_prefix pattern - wrap child element in L-<number> tag
                    l_prefix_tag = ARObject._get_l_prefix_tag(self.__class__, name)
                    if l_prefix_tag and value is not None:
                        # Serialize with natural tag, not xml_tag
                        serialized = value.serialize()
                        # Wrap it in the l_prefix tag (copies L attribute and text)
                        wrapped = self._serialize_l_prefix(serialized, l_prefix_tag)
                        current_elem.append(wrapped)
                elif hasattr(value, 'serialize'):
                    # Recursively serialize child objects
                    child = self._serialize_with_correct_tag(value, xml_tag)
                    current_elem.append(child)
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
                    current_elem.append(wrapper)
                else:
                    # Primitive value - create element with text content
                    child = ET.Element(xml_tag)
                    child.text = str(value)
                    current_elem.append(child)
        else:
            # Standard serialization for non-atpVariant classes
            # Get all instance attributes
            for name, value in vars(self).items():
                # Skip private attributes, except for l_prefix backing fields
                # l_prefix attributes use private backing fields (e.g., _l10)
                if name.startswith('_'):
                    # Check if this is a backing field for a l_prefix property
                    public_name = name[1:]  # Remove leading underscore
                    if not ARObject._has_l_prefix(self.__class__, public_name):
                        continue
                    # This is a l_prefix backing field, use the public name for serialization
                    name = public_name

                # Check for custom XML element tag via @xml_element_tag decorator
                xml_tag = self._get_element_tag(name)

                # Skip None values
                if value is None:
                    continue

                # Check if this should be an XML attribute (via decorator)
                if self._is_xml_attribute(name):
                    elem.set(xml_tag, str(value))
                elif isinstance(value, list):
                    # Check if this list has l_prefix decorator
                    if ARObject._has_l_prefix(self.__class__, name):
                        # Handle l_prefix pattern for lists - wrap each item in L-<number> tag
                        l_prefix_tag = ARObject._get_l_prefix_tag(self.__class__, name)
                        if l_prefix_tag:
                            for item in value:
                                if item is not None:
                                    # Serialize with natural tag, not xml_tag
                                    serialized = item.serialize()
                                    # Wrap it in the l_prefix tag (copies L attribute and text)
                                    wrapped = self._serialize_l_prefix(serialized, l_prefix_tag)
                                    elem.append(wrapped)
                    else:
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
                elif ARObject._has_l_prefix(self.__class__, name):
                    # Handle l_prefix pattern - wrap child element in L-<number> tag
                    l_prefix_tag = ARObject._get_l_prefix_tag(self.__class__, name)
                    if l_prefix_tag and value is not None:
                        # Serialize the child element
                        serialized = self._serialize_with_correct_tag(value, xml_tag)
                        # Wrap it in the l_prefix tag
                        wrapped = self._serialize_l_prefix(serialized, l_prefix_tag)
                        elem.append(wrapped)
                elif hasattr(value, 'serialize'):
                    # Recursively serialize child objects
                    child = self._serialize_with_correct_tag(value, xml_tag)
                    elem.append(child)
                else:
                    # Primitive value - create element with text content
                    child = ET.Element(xml_tag)
                    child.text = str(value)
                    elem.append(child)

        # Also serialize properties that have custom XML tags
        for name, obj in self.__class__.__dict__.items():
            if isinstance(obj, property) and hasattr(obj.fget, '_xml_element_tag'):
                # Get the property value
                try:
                    value = getattr(self, name)
                except AttributeError:
                    continue

                # Skip None values
                if value is None:
                    continue

                # Get the custom XML tag path
                xml_tag_path = obj.fget._xml_element_tag

                # Determine target element for serialization
                # For atp_variant classes, serialize into innermost wrapper
                target_elem = current_elem if hasattr(self.__class__, '_atp_variant') else elem

                # Serialize the value
                if hasattr(value, 'serialize'):
                    serialized_value = value.serialize()

                    # Handle multi-level paths
                    if isinstance(xml_tag_path, list) and len(xml_tag_path) > 1:
                        # Create nested wrapper elements
                        current = target_elem
                        for i, tag in enumerate(xml_tag_path):
                            if i == len(xml_tag_path) - 1:
                                # Last level - this is where we put the serialized content
                                wrapper = ET.Element(tag)
                                # Copy all children from the serialized value to the wrapper
                                for child in list(serialized_value):
                                    wrapper.append(child)
                                # Copy all attributes from the serialized value to the wrapper
                                for attr_name, attr_value in serialized_value.attrib.items():
                                    wrapper.set(attr_name, attr_value)
                                current.append(wrapper)
                            else:
                                # Intermediate level - find or create wrapper element
                                existing_wrapper = None
                                for child in current:
                                    if ARObject._strip_namespace(child.tag) == tag:
                                        existing_wrapper = child
                                        break
                                if existing_wrapper is None:
                                    existing_wrapper = ET.Element(tag)
                                    current.append(existing_wrapper)
                                current = existing_wrapper
                    else:
                        # Single-level path - use the tag directly
                        tag = xml_tag_path[-1] if isinstance(xml_tag_path, list) else xml_tag_path
                        wrapper = ET.Element(tag)
                        # Copy all children from the serialized value to the wrapper
                        for child in list(serialized_value):
                            wrapper.append(child)
                        # Copy all attributes from the serialized value to the wrapper
                        for attr_name, attr_value in serialized_value.attrib.items():
                            wrapper.set(attr_name, attr_value)
                        target_elem.append(wrapper)
                else:
                    # Primitive value
                    tag = xml_tag_path[-1] if isinstance(xml_tag_path, list) else xml_tag_path
                    if isinstance(xml_tag_path, list) and len(xml_tag_path) > 1:
                        # Create nested wrapper elements for primitive
                        current = target_elem
                        for i, level_tag in enumerate(xml_tag_path):
                            if i == len(xml_tag_path) - 1:
                                # Last level - create element with text
                                child = ET.Element(level_tag)
                                child.text = str(value)
                                current.append(child)
                            else:
                                # Intermediate level - find or create wrapper element
                                existing_wrapper = None
                                for existing_child in current:
                                    if ARObject._strip_namespace(existing_child.tag) == level_tag:
                                        existing_wrapper = existing_child
                                        break
                                if existing_wrapper is None:
                                    existing_wrapper = ET.Element(level_tag)
                                    current.append(existing_wrapper)
                                current = existing_wrapper
                    else:
                        child = ET.Element(tag)
                        child.text = str(value)
                        target_elem.append(child)

        # Also serialize properties that don't have decorators but have getters
        # This handles properties like 'checksum' that are simple property getters
        for name, obj in self.__class__.__dict__.items():
            if isinstance(obj, property) and not hasattr(obj.fget, '_xml_element_tag'):
                # Skip internal properties that should not be serialized
                if name == 'is_abstract':
                    continue

                # Skip properties that have @l_prefix decorator
                # These are already handled in the main vars() loop via their private backing fields
                if ARObject._has_l_prefix(self.__class__, name):
                    continue

                # Skip properties that have @xml_element_tag (already handled above)
                # Handle properties that have @xml_attribute
                if self._is_xml_attribute(name):
                    try:
                        value = getattr(self, name)
                    except AttributeError:
                        continue
                    
                    # Skip None values
                    if value is None:
                        continue
                    
                    # Convert property name to XML tag
                    xml_tag = NameConverter.to_xml_tag(name)
                    
                    # Serialize as XML attribute (always on main element)
                    elem.set(xml_tag, str(value))
                    continue

                try:
                    value = getattr(self, name)
                except AttributeError:
                    continue

                # Skip None values
                if value is None:
                    continue

                # Convert property name to XML tag
                xml_tag = NameConverter.to_xml_tag(name)

                # Determine target element for serialization
                # For atp_variant classes, serialize into innermost wrapper
                target_elem = current_elem if hasattr(self.__class__, '_atp_variant') else elem

                # Serialize the value
                if hasattr(value, 'serialize'):
                    child = self._serialize_with_correct_tag(value, xml_tag)
                    target_elem.append(child)
                elif isinstance(value, list):
                    wrapper = ET.Element(xml_tag)
                    for item in value:
                        if hasattr(item, 'serialize'):
                            wrapper.append(item.serialize())
                        else:
                            child = ET.Element(xml_tag)
                            child.text = str(item)
                            wrapper.append(child)
                    target_elem.append(wrapper)
                else:
                    child = ET.Element(xml_tag)
                    child.text = str(value)
                    target_elem.append(child)

        return elem

    def _serialize_with_correct_tag(self, value, xml_tag: str) -> ET.Element:
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
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef

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
            child.text = str(value.value)
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

    def _get_xml_tag(self) -> str:
        """Get XML tag name for this class.

        Auto-generates from class name using NameConverter.

        Returns:
            XML tag name
        """
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

    def _get_element_tag(self, attr_name: str) -> str:
        """Get XML tag name for a class attribute/element.

        Auto-generates from Python attribute name using NameConverter.

        Args:
            attr_name: Name of the Python attribute

        Returns:
            XML tag name to use for this element
        """
        return NameConverter.to_xml_tag(attr_name)

    def _get_element_tag_path(self, attr_name: str) -> Union[str, list[str]]:
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
    def _get_element_class(cls, attr_name: str) -> Optional[str]:
        """Get explicit Python class name from decorator.

        Note: This method is kept for compatibility but always returns None
        since @xml_element_tag decorator has been removed.

        Args:
            cls: The class to check
            attr_name: Name of the attribute to check

        Returns:
            None (decorator has been removed)
        """
        return None

    @staticmethod
    def _get_element_tag_path_static(cls, attr_name: str) -> Union[str, list[str]]:
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
    def _has_xml_element_tag(cls, attr_name: str) -> bool:
        """Check if an attribute has @xml_element_tag decorator.

        Note: This method is kept for compatibility but always returns False
        since @xml_element_tag decorator has been removed.

        Args:
            cls: The class to check
            attr_name: Name of the attribute to check

        Returns:
            False (decorator has been removed)
        """
        return False

    @staticmethod
    def _has_l_prefix(cls, attr_name: str) -> bool:
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
    def _get_l_prefix_tag(cls, attr_name: str) -> Optional[str]:
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
            return prop.fget._l_prefix_tag

        # Check if the attribute itself has the marker
        attr = getattr(cls, attr_name, None)
        if attr and hasattr(attr, '_l_prefix_tag'):
            return attr._l_prefix_tag

        return None

    @staticmethod
    def _serialize_l_prefix(child_elem: ET.Element, l_prefix_tag: str) -> ET.Element:
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
    def _extract_value_with_children(element: ET.Element, attr_type, explicit_class_name: Optional[str] = None):
        """Extract value from XML element's children based on type.

        This is used for @xml_element_tag decorated attributes, where the
        element acts as a wrapper and its children should be deserialized
        directly to the target type.

        Args:
            element: XML element containing children to deserialize
            attr_type: Expected type (from type hints)
            explicit_class_name: Optional explicit Python class name to use for deserialization

        Returns:
            Extracted value
        """
        if element is None or len(list(element)) == 0:
            return None

        # Get the first child element
        child = list(element)[0]

        # Get the child's XML tag name (strip namespace if present)
        child_tag = ARObject._strip_namespace(child.tag)

        # Use ModelFactory to resolve polymorphic types
        factory = ModelFactory()
        if not factory.is_initialized():
            factory.load_mappings()

        # Get concrete class from factory based on child tag
        concrete_class = factory.get_class(child_tag)
        
        # If explicit class name is provided, it's the parent/wrapper type
        wrapper_class = None
        if explicit_class_name:
            wrapper_class = ARObject._import_class_by_name(explicit_class_name)

        # Handle string type annotations
        if isinstance(attr_type, str):
            import re
            optional_match = re.match(r'Optional\[(.+?)\]', attr_type)
            if optional_match:
                inner_type_str = optional_match.group(1)
                item_class = ARObject._import_class_by_name(inner_type_str)

                # Check if concrete class is a subclass of the expected type
                if concrete_class and item_class:
                    if isinstance(concrete_class, type) and issubclass(concrete_class, item_class):
                        # Direct subclass match - deserialize directly
                        return ARObject._unwrap_primitive(concrete_class.deserialize(child))
                
                # Check if we need to create a wrapper object
                if wrapper_class and hasattr(wrapper_class, '__annotations__'):
                    for attr_name, attr_type_hint in wrapper_class.__annotations__.items():
                        if attr_name.startswith('_'):
                            continue
                        
                        type_str = str(attr_type_hint)
                        optional_match = re.match(r'Optional\[(.+?)\]', type_str)
                        if optional_match:
                            inner_type_str = optional_match.group(1)
                            content_class = ARObject._import_class_by_name(inner_type_str)
                        else:
                            content_class = ARObject._import_class_by_name(type_str)
                        
                        if content_class and concrete_class:
                            if isinstance(concrete_class, type) and issubclass(concrete_class, content_class):
                                # Create wrapper object and set its content attribute
                                parent_obj = wrapper_class()
                                deserialized_child = ARObject._unwrap_primitive(concrete_class.deserialize(child))
                                setattr(parent_obj, attr_name, deserialized_child)
                                return parent_obj

                # Fallback to base class deserialization
                if item_class and hasattr(item_class, 'deserialize'):
                    return ARObject._unwrap_primitive(item_class.deserialize(child))

                return child.text if child.text else None

            # For simple class names, try to import and deserialize
            item_class = ARObject._import_class_by_name(attr_type)
            if item_class and hasattr(item_class, 'deserialize'):
                return ARObject._unwrap_primitive(item_class.deserialize(child))

            return child.text if child.text else None

        # Check if it's an Optional type
        from typing import get_origin, get_args
        if get_origin(attr_type) is Union:
            type_args = get_args(attr_type)
            for arg in type_args:
                if arg is not type(None):
                    attr_type = arg
                    break

        # For object types with deserialize method, recursively deserialize
        if isinstance(attr_type, type) and hasattr(attr_type, 'deserialize'):
            # Determine the target type for wrapper object creation
            # Use wrapper_class if provided, otherwise use attr_type
            target_type = wrapper_class if wrapper_class else attr_type
            
            # Check if concrete class is a subclass of the expected type
            if concrete_class and isinstance(concrete_class, type) and issubclass(concrete_class, attr_type):
                return ARObject._unwrap_primitive(concrete_class.deserialize(child))
            else:
                # Check if this is a case where we need to create a parent wrapper object
                # For example: COMPU-SCALES should be wrapped in a Compu object
                # Check if the target type has attributes that could hold the concrete class
                if hasattr(target_type, '__annotations__'):
                    # Look for attributes that could hold the concrete class
                    for attr_name, attr_type_hint in target_type.__annotations__.items():
                        # Skip private attributes and the one we're deserializing
                        if attr_name.startswith('_'):
                            continue

                        # Try to resolve the type hint
                        import re
                        type_str = str(attr_type_hint)

                        # Handle Optional[T]
                        optional_match = re.match(r'Optional\[(.+?)\]', type_str)
                        if optional_match:
                            inner_type_str = optional_match.group(1)
                            content_class = ARObject._import_class_by_name(inner_type_str)
                        else:
                            content_class = ARObject._import_class_by_name(type_str)

                        # Check if concrete class can be stored in this attribute
                        if content_class and concrete_class:
                            if isinstance(concrete_class, type) and issubclass(concrete_class, content_class):
                                # Create parent object and set its content attribute
                                parent_obj = target_type()
                                deserialized_child = ARObject._unwrap_primitive(concrete_class.deserialize(child))
                                setattr(parent_obj, attr_name, deserialized_child)
                                return parent_obj

                # Fallback to standard deserialization
                return ARObject._unwrap_primitive(target_type.deserialize(child))

        # For primitive types, return text content
        text = child.text
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
            return text

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
            # Optimized: Bind get_type_hints locally for faster access
            _get_type_hints = get_type_hints
            type_hints = _get_type_hints(cls)
        except Exception:
            # Fallback: Use __annotations__ directly if get_type_hints fails
            # This can happen due to circular imports or missing types
            # Note: Annotations will be strings due to 'from __future__ import annotations'
            type_hints = {}
            # Optimized: Use local variables for faster MRO iteration
            _mro = cls.__mro__
            for base_cls in _mro:
                if hasattr(base_cls, "__annotations__"):
                    _annotations = base_cls.__annotations__
                    for attr_name, attr_type_str in _annotations.items():
                        if attr_name not in type_hints:
                            # Keep as string - _extract_value will handle it
                            type_hints[attr_name] = attr_type_str

        # For atp_variant classes, navigate through wrapper elements
        if hasattr(cls, '_atp_variant'):
            wrapper_path = cls._get_atp_variant_wrapper_path(cls.__name__)
            wrapper_elements = wrapper_path.split('/')
            
            # Navigate through wrapper elements to find the innermost one
            current_elem = element
            for wrapper_name in wrapper_elements:
                found = False
                for child in current_elem:
                    if ARObject._strip_namespace(child.tag) == wrapper_name:
                        current_elem = child
                        found = True
                        break
                if not found:
                    # Wrapper not found, use current element
                    break
        else:
            current_elem = element

        # Process each attribute from type hints
        for attr_name, attr_type in type_hints.items():
            # Convert Python name to XML tag
            xml_tag = NameConverter.to_xml_tag(attr_name)

            # Check if this should be an XML attribute
            if ARObject._is_xml_attribute_static(cls, attr_name):
                # XML attributes are always on the main element, not inside wrapper
                value = element.get(xml_tag)
            elif ARObject._has_l_prefix(cls, attr_name):
                # Handle l_prefix pattern - look for L-<number> element
                l_prefix_tag = ARObject._get_l_prefix_tag(cls, attr_name)
                if l_prefix_tag:
                    # Find the l_prefix element
                    child = None
                    for elem in current_elem:
                        if ARObject._strip_namespace(elem.tag) == l_prefix_tag:
                            child = elem
                            break

                    if child is not None:
                        # Deserialize the child element using the expected type
                        # The l_prefix wrapper element (e.g., L-10) contains the actual content
                        # which should be deserialized as the expected type (e.g., LPlainText)
                        value = ARObject._deserialize_with_type(child, attr_type)
                    else:
                        value = None
                else:
                    value = None
            # Also check if this is a private attribute (e.g., _l10) that corresponds to a l_prefix property (e.g., l10)
            elif attr_name.startswith('_'):
                public_name = attr_name[1:]  # Remove leading underscore
                if ARObject._has_l_prefix(cls, public_name):
                    # Handle l_prefix pattern for private attribute
                    l_prefix_tag = ARObject._get_l_prefix_tag(cls, public_name)
                    if l_prefix_tag:
                        # Check if this is a list type
                        is_list_type = False
                        if isinstance(attr_type, str) and attr_type.startswith("list["):
                            is_list_type = True
                        elif get_origin(attr_type) is list:
                            is_list_type = True

                        if is_list_type:
                            # For list types with l_prefix, find all l_prefix elements
                            # and deserialize each one as a list item
                            result = []
                            for elem in current_elem:
                                if ARObject._strip_namespace(elem.tag) == l_prefix_tag:
                                    # Get the inner type from list[T]
                                    inner_type = None
                                    if isinstance(attr_type, str):
                                        import re
                                        match = re.match(r'list\[(.+?)\]', attr_type)
                                        if match:
                                            inner_type = match.group(1)
                                    else:
                                        type_args = get_args(attr_type)
                                        if type_args:
                                            inner_type = type_args[0]

                                    if inner_type:
                                        # Deserialize the l_prefix element as the inner type
                                        value = ARObject._deserialize_with_type(elem, str(inner_type))
                                        if value is not None:
                                            result.append(value)
                            value = result
                        else:
                            # For single value types with l_prefix, find the single l_prefix element
                            child = None
                            for elem in current_elem:
                                if ARObject._strip_namespace(elem.tag) == l_prefix_tag:
                                    child = elem
                                    break

                            if child is not None:
                                # Deserialize the child element using the expected type
                                value = ARObject._deserialize_with_type(child, attr_type)
                            else:
                                value = None
                    else:
                        value = None
            else:
                # Get the XML tag name for this attribute
                target_tag = ARObject._get_element_tag_path_static(cls, attr_name)

                # Find child element
                child = current_elem.find(target_tag)
                if child is None:
                    # Try to find by matching stripped tag names
                    for elem in current_elem:
                        if ARObject._strip_namespace(elem.tag) == target_tag:
                            child = elem
                            break

                if child is not None:
                    # Get value based on type
                    value = ARObject._extract_value(child, attr_type)
                else:
                    value = None

            # Set attribute
            setattr(obj, attr_name, value)

        # Validate deserialization - check for unrecognized XML elements
        cls._validate_deserialization(element, type_hints)

        return obj

    @classmethod
    def _validate_deserialization(
        cls,
        element: ET.Element,
        type_hints: dict,
    ) -> None:
        """Validate deserialization by checking for unrecognized XML elements.

        This private method checks if any XML elements in the input were not
        matched to Python attributes, based on global settings.

        Note: Validation is skipped for classes that override deserialize(),
        since they may handle additional elements in custom logic.

        Args:
            element: XML element that was deserialized
            type_hints: Type hints dictionary used for deserialization

        Raises:
            ValueError: If strict_validation is enabled and unrecognized elements found
        """
        # Skip validation for classes with custom deserialize (override check)
        # If the class's deserialize method is different from ARObject.deserialize,
        # it has custom logic that may handle additional elements
        if cls.deserialize.__func__ is not ARObject.deserialize.__func__:
            return

        settings = GlobalSettingsManager()

        # Skip validation if both settings are disabled
        if not (settings.warn_on_unrecognized or settings.strict_validation):
            return

        # Build set of expected XML tags from type hints
        expected_tags = {NameConverter.to_xml_tag(name) for name in type_hints.keys()}
        
        # For atp_variant classes, add wrapper tags to expected tags
        # These are not attributes but structural elements
        if hasattr(cls, '_atp_variant'):
            wrapper_path = cls._get_atp_variant_wrapper_path(cls.__name__)
            for wrapper_tag in wrapper_path.split('/'):
                expected_tags.add(wrapper_tag)

        # For l_prefix attributes, add their l_prefix tags to expected tags
        # These are language-specific wrapper elements (e.g., L-10, L-4, L-2)
        for attr_name in type_hints.keys():
            # Check both private (e.g., "_l10") and public (e.g., "l10") attribute names
            # Type hints contain private attribute names, but properties are public
            if cls._has_l_prefix(cls, attr_name):
                l_prefix_tag = cls._get_l_prefix_tag(cls, attr_name)
                if l_prefix_tag:
                    expected_tags.add(l_prefix_tag)
            # Also check the public version (remove leading underscore)
            if attr_name.startswith('_'):
                public_name = attr_name[1:]
                if cls._has_l_prefix(cls, public_name):
                    l_prefix_tag = cls._get_l_prefix_tag(cls, public_name)
                    if l_prefix_tag:
                        expected_tags.add(l_prefix_tag)

        # Check each child element
        for child in element:
            child_tag = cls._strip_namespace(child.tag)
            if child_tag not in expected_tags:
                msg = f"Unrecognized XML element <{child_tag}> in {cls.__name__}. " \
                      f"Element will be ignored during deserialization."
                if settings.strict_validation:
                    raise ValueError(msg)
                else:
                    warnings.warn(msg, UserWarning, stacklevel=3)

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
            except (ImportError, ModuleNotFoundError):
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
                    except (ImportError, ModuleNotFoundError):
                        continue
        except Exception:
            pass

        # Last resort: Use ModelFactory if available
        try:
            from armodel.serialization.model_factory import ModelFactory
            factory = ModelFactory()
            if factory.is_initialized():
                # Try to get the XML tag from class name and look up in factory
                from armodel.serialization.name_converter import NameConverter
                xml_tag = NameConverter.to_xml_tag(class_name)
                cls = factory.get_class(xml_tag)
                if cls:
                    return cls
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
    def _add_text_element(parent: ET.Element, tag: str, value) -> None:
        """Add a child element with text content to parent if value is not None.

        Protected static helper method for serialization. Accessible to all subclasses.

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
    def _extract_text(element: ET.Element, tag: Optional[str] = None) -> Optional[str]:
        """Extract text content from XML element, returning None if missing or empty.

        Protected static helper method for deserialization. Accessible to all subclasses.

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
                    if ARObject._strip_namespace(elem.tag) == tag:
                        child = elem
                        break
            element = child

        if element is None or element.text is None:
            return None
        text = element.text.strip()
        return text if text else None

    @staticmethod
    def _unwrap_primitive(result):
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
                                item = ARObject._unwrap_primitive(concrete_class.deserialize(child))
                                result.append(item)
                                continue

                        # Fallback to base class deserialization
                        if hasattr(base_class, 'deserialize'):
                            item = ARObject._unwrap_primitive(base_class.deserialize(child))
                            result.append(item)
                        else:
                            result.append(child.text if child.text else None)
                    else:
                        # For non-polymorphic types, try to deserialize using the class name directly
                        item_class = ARObject._import_class_by_name(inner_type_str)
                        if item_class and hasattr(item_class, 'deserialize'):
                            item = ARObject._unwrap_primitive(item_class.deserialize(child))
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
                    return ARObject._unwrap_primitive(item_class.deserialize(element))

                # Fallback to text content
                return element.text if element.text else None

            # For simple class names, try to import and deserialize
            item_class = ARObject._import_class_by_name(attr_type)
            if item_class and hasattr(item_class, 'deserialize'):
                return ARObject._unwrap_primitive(item_class.deserialize(element))

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
                                item = ARObject._unwrap_primitive(concrete_class.deserialize(child))
                                result.append(item)
                                continue

                        # Fallback to base class deserialization
                        if hasattr(item_type, 'deserialize'):
                            item = ARObject._unwrap_primitive(item_type.deserialize(child))
                            result.append(item)
                        else:
                            result.append(child.text if child.text else None)
                    elif hasattr(item_type, 'deserialize'):
                        # For non-ARObject types with deserialize method
                        item = ARObject._unwrap_primitive(item_type.deserialize(child))
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
            return ARObject._unwrap_primitive(attr_type.deserialize(element))

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
    def _find_child_element(parent: ET.Element, tag: str) -> Optional[ET.Element]:
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
            return child

        # Try with namespace handling
        for elem in parent:
            if elem.tag.endswith(tag):
                return elem
        return None

    @staticmethod
    def _find_all_child_elements(parent: ET.Element, tag: str) -> list[ET.Element]:
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
    def _deserialize_by_tag(element: ET.Element, class_name: Optional[str] = None) -> Optional["ARObject"]:
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
        # Get the class from ModelFactory
        from armodel.serialization.model_factory import ModelFactory
        from armodel.serialization.name_converter import NameConverter

        factory = ModelFactory()
        if not factory.is_initialized():
            factory.load_mappings()

        # Determine the XML tag to use
        if class_name is None:
            # Use the element's tag directly
            xml_tag = ARObject._strip_namespace(element.tag)
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
    def _deserialize_with_type(element: ET.Element, attr_type: str) -> Any:
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
            import re
            match = re.match(r"Optional\[(.+?)\]", attr_type)
            if match:
                inner_type = match.group(1)
                return ARObject._deserialize_with_type(element, inner_type)
            return None

        # Handle list types
        elif attr_type.startswith("list["):
            import re
            match = re.match(r"list\[(.+?)\]", attr_type)
            if match:
                inner_type = match.group(1)
                result = []
                for child in element:
                    value = ARObject._deserialize_with_type(child, inner_type)
                    if value is not None:
                        result.append(value)
                return result
            return []

        # Import the type and deserialize
        try:
            # Convert type string to class
            type_class = ARObject._import_class_by_name(attr_type)
            if type_class and hasattr(type_class, 'deserialize'):
                return type_class.deserialize(element)
        except Exception:
            pass

        # Fallback: try to use _deserialize_by_tag
        return ARObject._deserialize_by_tag(element, None)

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
    def _serialize_item(value, expected_type: str) -> Optional[ET.Element]:
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