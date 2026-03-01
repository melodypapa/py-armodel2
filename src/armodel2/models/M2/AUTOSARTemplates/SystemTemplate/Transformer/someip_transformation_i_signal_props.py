"""SOMEIPTransformationISignalProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 778)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import atp_variant

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    SOMEIPMessageTypeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.tlv_data_id_definition_set import (
    TlvDataIdDefinitionSet,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


@atp_variant()

class SOMEIPTransformationISignalProps(ARObject):
    """AUTOSAR SOMEIPTransformationISignalProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "S-O-M-E-I-P-TRANSFORMATION-I-SIGNAL-PROPS"


    implements: Optional[Boolean]
    interface_version: Optional[PositiveInteger]
    is_dynamic: Optional[Boolean]
    message_type: Optional[SOMEIPMessageTypeEnum]
    size_of_array: Optional[PositiveInteger]
    size_of_string: Optional[PositiveInteger]
    size_of_struct: Optional[PositiveInteger]
    size_of_union: Optional[PositiveInteger]
    tlv_data_id_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "IMPLEMENTS": lambda obj, elem: setattr(obj, "implements", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "INTERFACE-VERSION": lambda obj, elem: setattr(obj, "interface_version", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "IS-DYNAMIC": lambda obj, elem: setattr(obj, "is_dynamic", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "MESSAGE-TYPE": lambda obj, elem: setattr(obj, "message_type", SOMEIPMessageTypeEnum.deserialize(elem)),
        "SIZE-OF-ARRAY": lambda obj, elem: setattr(obj, "size_of_array", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SIZE-OF-STRING": lambda obj, elem: setattr(obj, "size_of_string", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SIZE-OF-STRUCT": lambda obj, elem: setattr(obj, "size_of_struct", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SIZE-OF-UNION": lambda obj, elem: setattr(obj, "size_of_union", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "TLV-DATA-ID-REFS": lambda obj, elem: obj.tlv_data_id_refs.append(ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize SOMEIPTransformationISignalProps."""
        super().__init__()
        self.implements: Optional[Boolean] = None
        self.interface_version: Optional[PositiveInteger] = None
        self.is_dynamic: Optional[Boolean] = None
        self.message_type: Optional[SOMEIPMessageTypeEnum] = None
        self.size_of_array: Optional[PositiveInteger] = None
        self.size_of_string: Optional[PositiveInteger] = None
        self.size_of_struct: Optional[PositiveInteger] = None
        self.size_of_union: Optional[PositiveInteger] = None
        self.tlv_data_id_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize SOMEIPTransformationISignalProps to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SOMEIPTransformationISignalProps, self).serialize()

        # Copy all attributes from parent element to outer element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element to outer element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Copy parent's children: metadata to outer element, others to inner element
        metadata_tags = {'SHORT-NAME', 'LONG-NAME', 'DESC', 'ADMIN-DATA'}
        for child in parent_elem:
            tag = SerializationHelper.strip_namespace(child.tag)
            if tag in metadata_tags:
                # Metadata elements stay outside the atp_variant wrapper
                elem.append(child)
            else:
                # Other elements go inside the atp_variant wrapper
                inner_elem.append(child)

        # Serialize implements
        if self.implements is not None:
            serialized = SerializationHelper.serialize_item(self.implements, "Boolean")
            if serialized is not None:
                wrapped = ET.Element("IMPLEMENTS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize interface_version
        if self.interface_version is not None:
            serialized = SerializationHelper.serialize_item(self.interface_version, "PositiveInteger")
            if serialized is not None:
                wrapped = ET.Element("INTERFACE-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize is_dynamic
        if self.is_dynamic is not None:
            serialized = SerializationHelper.serialize_item(self.is_dynamic, "Boolean")
            if serialized is not None:
                wrapped = ET.Element("IS-DYNAMIC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize message_type
        if self.message_type is not None:
            serialized = SerializationHelper.serialize_item(self.message_type, "SOMEIPMessageTypeEnum")
            if serialized is not None:
                wrapped = ET.Element("MESSAGE-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize size_of_array
        if self.size_of_array is not None:
            serialized = SerializationHelper.serialize_item(self.size_of_array, "PositiveInteger")
            if serialized is not None:
                wrapped = ET.Element("SIZE-OF-ARRAY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize size_of_string
        if self.size_of_string is not None:
            serialized = SerializationHelper.serialize_item(self.size_of_string, "PositiveInteger")
            if serialized is not None:
                wrapped = ET.Element("SIZE-OF-STRING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize size_of_struct
        if self.size_of_struct is not None:
            serialized = SerializationHelper.serialize_item(self.size_of_struct, "PositiveInteger")
            if serialized is not None:
                wrapped = ET.Element("SIZE-OF-STRUCT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize size_of_union
        if self.size_of_union is not None:
            serialized = SerializationHelper.serialize_item(self.size_of_union, "PositiveInteger")
            if serialized is not None:
                wrapped = ET.Element("SIZE-OF-UNION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize tlv_data_id_refs (list)
        for item in self.tlv_data_id_refs:
            serialized = SerializationHelper.serialize_item(item, "TlvDataIdDefinitionSet")
            if serialized is not None:
                wrapped = ET.Element("TLV-DATA-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "SOMEIPTransformationISignalProps")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SOMEIPTransformationISignalProps":
        """Deserialize XML element to SOMEIPTransformationISignalProps object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SOMEIPTransformationISignalProps object
        """
        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "SOMEIPTransformationISignalProps")
        if inner_elem is None:
            # No wrapper structure found, create instance with default values
            obj = cls.__new__(cls)
            obj.__init__()
            return obj

        # Temporarily copy children from inner element to outer element
        # so parent's deserialize can find inherited attributes
        for child in list(inner_elem):
            element.append(child)

        # Call parent's deserialize with outer element (now contains parent's children)
        obj = super(SOMEIPTransformationISignalProps, cls).deserialize(element)

        # Clean up: remove the temporarily copied children from outer element
        # (they are now in obj, so we don't need them in element anymore)
        for child in list(inner_elem):
            element.remove(child)

        # Parse implements
        child = SerializationHelper.find_child_element(inner_elem, "IMPLEMENTS")
        if child is not None:
            implements_value = child.text
            obj.implements = implements_value

        # Parse interface_version
        child = SerializationHelper.find_child_element(inner_elem, "INTERFACE-VERSION")
        if child is not None:
            interface_version_value = child.text
            obj.interface_version = interface_version_value

        # Parse is_dynamic
        child = SerializationHelper.find_child_element(inner_elem, "IS-DYNAMIC")
        if child is not None:
            is_dynamic_value = child.text
            obj.is_dynamic = is_dynamic_value

        # Parse message_type
        child = SerializationHelper.find_child_element(inner_elem, "MESSAGE-TYPE")
        if child is not None:
            message_type_value = SOMEIPMessageTypeEnum.deserialize(child)
            obj.message_type = message_type_value

        # Parse size_of_array
        child = SerializationHelper.find_child_element(inner_elem, "SIZE-OF-ARRAY")
        if child is not None:
            size_of_array_value = child.text
            obj.size_of_array = size_of_array_value

        # Parse size_of_string
        child = SerializationHelper.find_child_element(inner_elem, "SIZE-OF-STRING")
        if child is not None:
            size_of_string_value = child.text
            obj.size_of_string = size_of_string_value

        # Parse size_of_struct
        child = SerializationHelper.find_child_element(inner_elem, "SIZE-OF-STRUCT")
        if child is not None:
            size_of_struct_value = child.text
            obj.size_of_struct = size_of_struct_value

        # Parse size_of_union
        child = SerializationHelper.find_child_element(inner_elem, "SIZE-OF-UNION")
        if child is not None:
            size_of_union_value = child.text
            obj.size_of_union = size_of_union_value

        # Parse tlv_data_id_refs (list)
        obj.tlv_data_id_refs = []
        for child in SerializationHelper.find_all_child_elements(inner_elem, "TLV-DATA-ID"):
            tlv_data_id_refs_value = ARRef.deserialize(child)
            obj.tlv_data_id_refs.append(tlv_data_id_refs_value)

        return obj



class SOMEIPTransformationISignalPropsBuilder(BuilderBase):
    """Builder for SOMEIPTransformationISignalProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SOMEIPTransformationISignalProps = SOMEIPTransformationISignalProps()


    def with_implements(self, value: Optional[Boolean]) -> "SOMEIPTransformationISignalPropsBuilder":
        """Set implements attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.implements = value
        return self

    def with_interface_version(self, value: Optional[PositiveInteger]) -> "SOMEIPTransformationISignalPropsBuilder":
        """Set interface_version attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.interface_version = value
        return self

    def with_is_dynamic(self, value: Optional[Boolean]) -> "SOMEIPTransformationISignalPropsBuilder":
        """Set is_dynamic attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.is_dynamic = value
        return self

    def with_message_type(self, value: Optional[SOMEIPMessageTypeEnum]) -> "SOMEIPTransformationISignalPropsBuilder":
        """Set message_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.message_type = value
        return self

    def with_size_of_array(self, value: Optional[PositiveInteger]) -> "SOMEIPTransformationISignalPropsBuilder":
        """Set size_of_array attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.size_of_array = value
        return self

    def with_size_of_string(self, value: Optional[PositiveInteger]) -> "SOMEIPTransformationISignalPropsBuilder":
        """Set size_of_string attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.size_of_string = value
        return self

    def with_size_of_struct(self, value: Optional[PositiveInteger]) -> "SOMEIPTransformationISignalPropsBuilder":
        """Set size_of_struct attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.size_of_struct = value
        return self

    def with_size_of_union(self, value: Optional[PositiveInteger]) -> "SOMEIPTransformationISignalPropsBuilder":
        """Set size_of_union attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.size_of_union = value
        return self

    def with_tlv_data_ids(self, items: list[TlvDataIdDefinitionSet]) -> "SOMEIPTransformationISignalPropsBuilder":
        """Set tlv_data_ids list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.tlv_data_ids = list(items) if items else []
        return self


    def add_tlv_data_id(self, item: TlvDataIdDefinitionSet) -> "SOMEIPTransformationISignalPropsBuilder":
        """Add a single item to tlv_data_ids list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.tlv_data_ids.append(item)
        return self

    def clear_tlv_data_ids(self) -> "SOMEIPTransformationISignalPropsBuilder":
        """Clear all items from tlv_data_ids list.

        Returns:
            self for method chaining
        """
        self._obj.tlv_data_ids = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> SOMEIPTransformationISignalProps:
        """Build and return the SOMEIPTransformationISignalProps instance with validation."""
        self._validate_instance()
        pass
        return self._obj