"""TlvDataIdDefinition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 830)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.argument_data_prototype import (
    ArgumentDataPrototype,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import (
        AbstractImplementationDataType,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class TlvDataIdDefinition(ARObject):
    """AUTOSAR TlvDataIdDefinition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TLV-DATA-ID-DEFINITION"


    id: Optional[PositiveInteger]
    tlv_argument_ref: Optional[ARRef]
    tlv_ref: Optional[ARRef]
    tlv_record_ref: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "ID": lambda obj, elem: setattr(obj, "id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "TLV-ARGUMENT-REF": lambda obj, elem: setattr(obj, "tlv_argument_ref", ARRef.deserialize(elem)),
        "TLV-REF": ("_POLYMORPHIC", "tlv_ref", ["ImplementationDataType"]),
        "TLV-RECORD-REF": lambda obj, elem: setattr(obj, "tlv_record_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize TlvDataIdDefinition."""
        super().__init__()
        self.id: Optional[PositiveInteger] = None
        self.tlv_argument_ref: Optional[ARRef] = None
        self.tlv_ref: Optional[ARRef] = None
        self.tlv_record_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize TlvDataIdDefinition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TlvDataIdDefinition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize id
        if self.id is not None:
            serialized = SerializationHelper.serialize_item(self.id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tlv_argument_ref
        if self.tlv_argument_ref is not None:
            serialized = SerializationHelper.serialize_item(self.tlv_argument_ref, "ArgumentDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TLV-ARGUMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tlv_ref
        if self.tlv_ref is not None:
            serialized = SerializationHelper.serialize_item(self.tlv_ref, "AbstractImplementationDataType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TLV-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tlv_record_ref
        if self.tlv_record_ref is not None:
            serialized = SerializationHelper.serialize_item(self.tlv_record_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TLV-RECORD-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TlvDataIdDefinition":
        """Deserialize XML element to TlvDataIdDefinition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TlvDataIdDefinition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TlvDataIdDefinition, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ID":
                setattr(obj, "id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "TLV-ARGUMENT-REF":
                setattr(obj, "tlv_argument_ref", ARRef.deserialize(child))
            elif tag == "TLV-REF":
                setattr(obj, "tlv_ref", ARRef.deserialize(child))
            elif tag == "TLV-RECORD-REF":
                setattr(obj, "tlv_record_ref", ARRef.deserialize(child))

        return obj



class TlvDataIdDefinitionBuilder(BuilderBase):
    """Builder for TlvDataIdDefinition with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TlvDataIdDefinition = TlvDataIdDefinition()


    def with_id(self, value: Optional[PositiveInteger]) -> "TlvDataIdDefinitionBuilder":
        """Set id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.id = value
        return self

    def with_tlv_argument(self, value: Optional[ArgumentDataPrototype]) -> "TlvDataIdDefinitionBuilder":
        """Set tlv_argument attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tlv_argument = value
        return self

    def with_tlv(self, value: Optional[AbstractImplementationDataType]) -> "TlvDataIdDefinitionBuilder":
        """Set tlv attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tlv = value
        return self

    def with_tlv_record(self, value: Optional[any (ApplicationRecord)]) -> "TlvDataIdDefinitionBuilder":
        """Set tlv_record attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tlv_record = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "id",
        "tlv",
        "tlvArgument",
        "tlvRecord",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TlvDataIdDefinition:
        """Build and return the TlvDataIdDefinition instance with validation."""
        self._validate_instance()
        return self._obj