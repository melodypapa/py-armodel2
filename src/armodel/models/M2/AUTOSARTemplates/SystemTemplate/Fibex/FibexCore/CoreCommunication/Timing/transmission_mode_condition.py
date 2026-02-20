"""TransmissionModeCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 392)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter.data_filter import (
    DataFilter,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_to_i_pdu_mapping import (
    ISignalToIPduMapping,
)


class TransmissionModeCondition(ARObject):
    """AUTOSAR TransmissionModeCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_filter: Optional[DataFilter]
    i_signal_in_i_pdu_ref: Optional[ARRef]
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
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize data_filter
        if self.data_filter is not None:
            serialized = ARObject._serialize_item(self.data_filter, "DataFilter")
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
            serialized = ARObject._serialize_item(self.i_signal_in_i_pdu_ref, "ISignalToIPduMapping")
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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_filter
        child = ARObject._find_child_element(element, "DATA-FILTER")
        if child is not None:
            data_filter_value = ARObject._deserialize_by_tag(child, "DataFilter")
            obj.data_filter = data_filter_value

        # Parse i_signal_in_i_pdu_ref
        child = ARObject._find_child_element(element, "I-SIGNAL-IN-I-PDU-REF")
        if child is not None:
            i_signal_in_i_pdu_ref_value = ARRef.deserialize(child)
            obj.i_signal_in_i_pdu_ref = i_signal_in_i_pdu_ref_value

        return obj



class TransmissionModeConditionBuilder:
    """Builder for TransmissionModeCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransmissionModeCondition = TransmissionModeCondition()

    def build(self) -> TransmissionModeCondition:
        """Build and return TransmissionModeCondition object.

        Returns:
            TransmissionModeCondition instance
        """
        # TODO: Add validation
        return self._obj
