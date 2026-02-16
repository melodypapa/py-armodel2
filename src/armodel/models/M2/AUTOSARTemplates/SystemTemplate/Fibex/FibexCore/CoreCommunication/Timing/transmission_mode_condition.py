"""TransmissionModeCondition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter.data_filter import (
    DataFilter,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_to_i_pdu_mapping import (
    ISignalToIPduMapping,
)


class TransmissionModeCondition(ARObject):
    """AUTOSAR TransmissionModeCondition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_filter", None, False, False, DataFilter),  # dataFilter
        ("i_signal_in_i_pdu", None, False, False, ISignalToIPduMapping),  # iSignalInIPdu
    ]

    def __init__(self) -> None:
        """Initialize TransmissionModeCondition."""
        super().__init__()
        self.data_filter: Optional[DataFilter] = None
        self.i_signal_in_i_pdu: Optional[ISignalToIPduMapping] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TransmissionModeCondition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransmissionModeCondition":
        """Create TransmissionModeCondition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TransmissionModeCondition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TransmissionModeCondition since parent returns ARObject
        return cast("TransmissionModeCondition", obj)


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
