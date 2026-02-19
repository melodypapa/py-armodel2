"""LinCommunicationConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 98)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_configurable_frame import (
    LinConfigurableFrame,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_ordered_configurable_frame import (
    LinOrderedConfigurableFrame,
)


class LinCommunicationConnector(CommunicationConnector):
    """AUTOSAR LinCommunicationConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    initial_nad: Optional[Integer]
    lin_configurable_frames: list[LinConfigurableFrame]
    lin_ordereds: list[LinOrderedConfigurableFrame]
    schedule: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize LinCommunicationConnector."""
        super().__init__()
        self.initial_nad: Optional[Integer] = None
        self.lin_configurable_frames: list[LinConfigurableFrame] = []
        self.lin_ordereds: list[LinOrderedConfigurableFrame] = []
        self.schedule: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinCommunicationConnector":
        """Deserialize XML element to LinCommunicationConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinCommunicationConnector object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse initial_nad
        child = ARObject._find_child_element(element, "INITIAL-NAD")
        if child is not None:
            initial_nad_value = child.text
            obj.initial_nad = initial_nad_value

        # Parse lin_configurable_frames (list)
        obj.lin_configurable_frames = []
        for child in ARObject._find_all_child_elements(element, "LIN-CONFIGURABLE-FRAMES"):
            lin_configurable_frames_value = ARObject._deserialize_by_tag(child, "LinConfigurableFrame")
            obj.lin_configurable_frames.append(lin_configurable_frames_value)

        # Parse lin_ordereds (list)
        obj.lin_ordereds = []
        for child in ARObject._find_all_child_elements(element, "LIN-ORDEREDS"):
            lin_ordereds_value = ARObject._deserialize_by_tag(child, "LinOrderedConfigurableFrame")
            obj.lin_ordereds.append(lin_ordereds_value)

        # Parse schedule
        child = ARObject._find_child_element(element, "SCHEDULE")
        if child is not None:
            schedule_value = child.text
            obj.schedule = schedule_value

        return obj



class LinCommunicationConnectorBuilder:
    """Builder for LinCommunicationConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinCommunicationConnector = LinCommunicationConnector()

    def build(self) -> LinCommunicationConnector:
        """Build and return LinCommunicationConnector object.

        Returns:
            LinCommunicationConnector instance
        """
        # TODO: Add validation
        return self._obj
