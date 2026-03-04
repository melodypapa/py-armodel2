"""EndToEndProtectionISignalIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 987)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 384)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_EndToEndProtection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_group import (
    ISignalGroup,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_i_pdu import (
    ISignalIPdu,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EndToEndProtectionISignalIPdu(ARObject):
    """AUTOSAR EndToEndProtectionISignalIPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "END-TO-END-PROTECTION-I-SIGNAL-I-PDU"


    data_offset: Optional[Integer]
    i_signal_group_ref: Optional[ARRef]
    i_signal_i_pdu_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "DATA-OFFSET": lambda obj, elem: setattr(obj, "data_offset", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "I-SIGNAL-GROUP-REF": lambda obj, elem: setattr(obj, "i_signal_group_ref", ARRef.deserialize(elem)),
        "I-SIGNAL-I-PDU-REF": lambda obj, elem: setattr(obj, "i_signal_i_pdu_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize EndToEndProtectionISignalIPdu."""
        super().__init__()
        self.data_offset: Optional[Integer] = None
        self.i_signal_group_ref: Optional[ARRef] = None
        self.i_signal_i_pdu_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize EndToEndProtectionISignalIPdu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EndToEndProtectionISignalIPdu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_offset
        if self.data_offset is not None:
            serialized = SerializationHelper.serialize_item(self.data_offset, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize i_signal_group_ref
        if self.i_signal_group_ref is not None:
            serialized = SerializationHelper.serialize_item(self.i_signal_group_ref, "ISignalGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("I-SIGNAL-GROUP-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize i_signal_i_pdu_ref
        if self.i_signal_i_pdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.i_signal_i_pdu_ref, "ISignalIPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("I-SIGNAL-I-PDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EndToEndProtectionISignalIPdu":
        """Deserialize XML element to EndToEndProtectionISignalIPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EndToEndProtectionISignalIPdu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EndToEndProtectionISignalIPdu, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATA-OFFSET":
                setattr(obj, "data_offset", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "I-SIGNAL-GROUP-REF":
                setattr(obj, "i_signal_group_ref", ARRef.deserialize(child))
            elif tag == "I-SIGNAL-I-PDU-REF":
                setattr(obj, "i_signal_i_pdu_ref", ARRef.deserialize(child))

        return obj



class EndToEndProtectionISignalIPduBuilder(BuilderBase):
    """Builder for EndToEndProtectionISignalIPdu with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EndToEndProtectionISignalIPdu = EndToEndProtectionISignalIPdu()


    def with_data_offset(self, value: Optional[Integer]) -> "EndToEndProtectionISignalIPduBuilder":
        """Set data_offset attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_offset = value
        return self

    def with_i_signal_group(self, value: Optional[ISignalGroup]) -> "EndToEndProtectionISignalIPduBuilder":
        """Set i_signal_group attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.i_signal_group = value
        return self

    def with_i_signal_i_pdu(self, value: Optional[ISignalIPdu]) -> "EndToEndProtectionISignalIPduBuilder":
        """Set i_signal_i_pdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.i_signal_i_pdu = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dataOffset",
        "iSignalGroup",
        "iSignalIPdu",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> EndToEndProtectionISignalIPdu:
        """Build and return the EndToEndProtectionISignalIPdu instance with validation."""
        self._validate_instance()
        return self._obj