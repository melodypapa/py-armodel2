"""CanCommunicationConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 74)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.abstract_can_communication_connector import (
    AbstractCanCommunicationConnector,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    PositiveUnlimitedInteger,
)


class CanCommunicationConnector(AbstractCanCommunicationConnector):
    """AUTOSAR CanCommunicationConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    pnc_wakeup_can: Optional[PositiveInteger]
    pnc_wakeup: Optional[PositiveUnlimitedInteger]
    pnc_wakeup_dlc: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize CanCommunicationConnector."""
        super().__init__()
        self.pnc_wakeup_can: Optional[PositiveInteger] = None
        self.pnc_wakeup: Optional[PositiveUnlimitedInteger] = None
        self.pnc_wakeup_dlc: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanCommunicationConnector":
        """Deserialize XML element to CanCommunicationConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanCommunicationConnector object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CanCommunicationConnector, cls).deserialize(element)

        # Parse pnc_wakeup_can
        child = ARObject._find_child_element(element, "PNC-WAKEUP-CAN")
        if child is not None:
            pnc_wakeup_can_value = child.text
            obj.pnc_wakeup_can = pnc_wakeup_can_value

        # Parse pnc_wakeup
        child = ARObject._find_child_element(element, "PNC-WAKEUP")
        if child is not None:
            pnc_wakeup_value = child.text
            obj.pnc_wakeup = pnc_wakeup_value

        # Parse pnc_wakeup_dlc
        child = ARObject._find_child_element(element, "PNC-WAKEUP-DLC")
        if child is not None:
            pnc_wakeup_dlc_value = child.text
            obj.pnc_wakeup_dlc = pnc_wakeup_dlc_value

        return obj



class CanCommunicationConnectorBuilder:
    """Builder for CanCommunicationConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanCommunicationConnector = CanCommunicationConnector()

    def build(self) -> CanCommunicationConnector:
        """Build and return CanCommunicationConnector object.

        Returns:
            CanCommunicationConnector instance
        """
        # TODO: Add validation
        return self._obj
