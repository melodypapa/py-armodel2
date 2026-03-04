"""SenderReceiverToSignalGroupMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 234)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.data_mapping import (
    DataMapping,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.data_mapping import DataMappingBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_composite_type_mapping import (
    SenderRecCompositeTypeMapping,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal_group import (
    SystemSignalGroup,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SenderReceiverToSignalGroupMapping(DataMapping):
    """AUTOSAR SenderReceiverToSignalGroupMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING"


    data_element_ref: Optional[ARRef]
    signal_group_ref: Optional[ARRef]
    type_mapping: Optional[SenderRecCompositeTypeMapping]
    _DESERIALIZE_DISPATCH = {
        "DATA-ELEMENT-REF": lambda obj, elem: setattr(obj, "data_element_ref", ARRef.deserialize(elem)),
        "SIGNAL-GROUP-REF": lambda obj, elem: setattr(obj, "signal_group_ref", ARRef.deserialize(elem)),
        "TYPE-MAPPING": ("_POLYMORPHIC", "type_mapping", ["SenderRecArrayTypeMapping", "SenderRecRecordTypeMapping"]),
    }


    def __init__(self) -> None:
        """Initialize SenderReceiverToSignalGroupMapping."""
        super().__init__()
        self.data_element_ref: Optional[ARRef] = None
        self.signal_group_ref: Optional[ARRef] = None
        self.type_mapping: Optional[SenderRecCompositeTypeMapping] = None

    def serialize(self) -> ET.Element:
        """Serialize SenderReceiverToSignalGroupMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SenderReceiverToSignalGroupMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_element_ref
        if self.data_element_ref is not None:
            serialized = SerializationHelper.serialize_item(self.data_element_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-ELEMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize signal_group_ref
        if self.signal_group_ref is not None:
            serialized = SerializationHelper.serialize_item(self.signal_group_ref, "SystemSignalGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SIGNAL-GROUP-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize type_mapping
        if self.type_mapping is not None:
            serialized = SerializationHelper.serialize_item(self.type_mapping, "SenderRecCompositeTypeMapping")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TYPE-MAPPING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderReceiverToSignalGroupMapping":
        """Deserialize XML element to SenderReceiverToSignalGroupMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderReceiverToSignalGroupMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SenderReceiverToSignalGroupMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATA-ELEMENT-REF":
                setattr(obj, "data_element_ref", ARRef.deserialize(child))
            elif tag == "SIGNAL-GROUP-REF":
                setattr(obj, "signal_group_ref", ARRef.deserialize(child))
            elif tag == "TYPE-MAPPING":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "SENDER-REC-ARRAY-TYPE-MAPPING":
                        setattr(obj, "type_mapping", SerializationHelper.deserialize_by_tag(child[0], "SenderRecArrayTypeMapping"))
                    elif concrete_tag == "SENDER-REC-RECORD-TYPE-MAPPING":
                        setattr(obj, "type_mapping", SerializationHelper.deserialize_by_tag(child[0], "SenderRecRecordTypeMapping"))

        return obj



class SenderReceiverToSignalGroupMappingBuilder(DataMappingBuilder):
    """Builder for SenderReceiverToSignalGroupMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SenderReceiverToSignalGroupMapping = SenderReceiverToSignalGroupMapping()


    def with_data_element(self, value: Optional[VariableDataPrototype]) -> "SenderReceiverToSignalGroupMappingBuilder":
        """Set data_element attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_element = value
        return self

    def with_signal_group(self, value: Optional[SystemSignalGroup]) -> "SenderReceiverToSignalGroupMappingBuilder":
        """Set signal_group attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.signal_group = value
        return self

    def with_type_mapping(self, value: Optional[SenderRecCompositeTypeMapping]) -> "SenderReceiverToSignalGroupMappingBuilder":
        """Set type_mapping attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.type_mapping = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dataElement",
        "signalGroup",
        "typeMapping",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SenderReceiverToSignalGroupMapping:
        """Build and return the SenderReceiverToSignalGroupMapping instance with validation."""
        self._validate_instance()
        return self._obj