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

    def __init__(self) -> None:
        """Initialize LinCommunicationConnector."""
        super().__init__()
        self.initial_nad: Optional[Integer] = None
        self.lin_configurable_frames: list[LinConfigurableFrame] = []
        self.lin_ordereds: list[LinOrderedConfigurableFrame] = []
        self.schedule: Optional[Boolean] = None


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
