"""FlexrayCommunicationConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 89)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Flexray_FlexrayTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Float,
)


class FlexrayCommunicationConnector(CommunicationConnector):
    """AUTOSAR FlexrayCommunicationConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    nm_ready_sleep: Optional[Float]
    wake_up: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize FlexrayCommunicationConnector."""
        super().__init__()
        self.nm_ready_sleep: Optional[Float] = None
        self.wake_up: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayCommunicationConnector":
        """Deserialize XML element to FlexrayCommunicationConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayCommunicationConnector object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse nm_ready_sleep
        child = ARObject._find_child_element(element, "NM-READY-SLEEP")
        if child is not None:
            nm_ready_sleep_value = child.text
            obj.nm_ready_sleep = nm_ready_sleep_value

        # Parse wake_up
        child = ARObject._find_child_element(element, "WAKE-UP")
        if child is not None:
            wake_up_value = child.text
            obj.wake_up = wake_up_value

        return obj



class FlexrayCommunicationConnectorBuilder:
    """Builder for FlexrayCommunicationConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayCommunicationConnector = FlexrayCommunicationConnector()

    def build(self) -> FlexrayCommunicationConnector:
        """Build and return FlexrayCommunicationConnector object.

        Returns:
            FlexrayCommunicationConnector instance
        """
        # TODO: Add validation
        return self._obj
