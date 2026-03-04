"""TransmissionModeCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 392)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Filter.data_filter import (
    DataFilter,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_to_i_pdu_mapping import (
    ISignalToIPduMapping,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TransmissionModeCondition(ARObject):
    """AUTOSAR TransmissionModeCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TRANSMISSION-MODE-CONDITION"


    data_filter: Optional[DataFilter]
    i_signal_in_i_pdu_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "DATA-FILTER": lambda obj, elem: setattr(obj, "data_filter", SerializationHelper.deserialize_by_tag(elem, "DataFilter")),
        "I-SIGNAL-IN-I-PDU-REF": lambda obj, elem: setattr(obj, "i_signal_in_i_pdu_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize TransmissionModeCondition."""
        super().__init__()
        self.data_filter: Optional[DataFilter] = None
        self.i_signal_in_i_pdu_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize TransmissionModeCondition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TransmissionModeCondition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_filter
        if self.data_filter is not None:
            serialized = SerializationHelper.serialize_item(self.data_filter, "DataFilter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-FILTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize i_signal_in_i_pdu_ref
        if self.i_signal_in_i_pdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.i_signal_in_i_pdu_ref, "ISignalToIPduMapping")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("I-SIGNAL-IN-I-PDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransmissionModeCondition":
        """Deserialize XML element to TransmissionModeCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TransmissionModeCondition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TransmissionModeCondition, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATA-FILTER":
                setattr(obj, "data_filter", SerializationHelper.deserialize_by_tag(child, "DataFilter"))
            elif tag == "I-SIGNAL-IN-I-PDU-REF":
                setattr(obj, "i_signal_in_i_pdu_ref", ARRef.deserialize(child))

        return obj



class TransmissionModeConditionBuilder(BuilderBase):
    """Builder for TransmissionModeCondition with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TransmissionModeCondition = TransmissionModeCondition()


    def with_data_filter(self, value: Optional[DataFilter]) -> "TransmissionModeConditionBuilder":
        """Set data_filter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_filter = value
        return self

    def with_i_signal_in_i_pdu(self, value: Optional[ISignalToIPduMapping]) -> "TransmissionModeConditionBuilder":
        """Set i_signal_in_i_pdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.i_signal_in_i_pdu = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dataFilter",
        "iSignalInIPdu",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TransmissionModeCondition:
        """Build and return the TransmissionModeCondition instance with validation."""
        self._validate_instance()
        return self._obj