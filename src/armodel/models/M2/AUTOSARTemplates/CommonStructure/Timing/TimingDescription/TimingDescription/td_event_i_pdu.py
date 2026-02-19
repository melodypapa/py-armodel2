"""TDEventIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 66)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_com import (
    TDEventCom,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription import (
    TDEventIPduTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)


class TDEventIPdu(TDEventCom):
    """AUTOSAR TDEventIPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    i_pdu: Optional[IPdu]
    physical_channel: Optional[PhysicalChannel]
    td_event_type: Optional[TDEventIPduTypeEnum]
    def __init__(self) -> None:
        """Initialize TDEventIPdu."""
        super().__init__()
        self.i_pdu: Optional[IPdu] = None
        self.physical_channel: Optional[PhysicalChannel] = None
        self.td_event_type: Optional[TDEventIPduTypeEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventIPdu":
        """Deserialize XML element to TDEventIPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventIPdu object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse i_pdu
        child = ARObject._find_child_element(element, "I-PDU")
        if child is not None:
            i_pdu_value = ARObject._deserialize_by_tag(child, "IPdu")
            obj.i_pdu = i_pdu_value

        # Parse physical_channel
        child = ARObject._find_child_element(element, "PHYSICAL-CHANNEL")
        if child is not None:
            physical_channel_value = ARObject._deserialize_by_tag(child, "PhysicalChannel")
            obj.physical_channel = physical_channel_value

        # Parse td_event_type
        child = ARObject._find_child_element(element, "TD-EVENT-TYPE")
        if child is not None:
            td_event_type_value = child.text
            obj.td_event_type = td_event_type_value

        return obj



class TDEventIPduBuilder:
    """Builder for TDEventIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventIPdu = TDEventIPdu()

    def build(self) -> TDEventIPdu:
        """Build and return TDEventIPdu object.

        Returns:
            TDEventIPdu instance
        """
        # TODO: Add validation
        return self._obj
