"""J1939ControllerApplicationToJ1939NmNodeMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 206)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.j1939_nm_node import (
    J1939NmNode,
)


class J1939ControllerApplicationToJ1939NmNodeMapping(ARObject):
    """AUTOSAR J1939ControllerApplicationToJ1939NmNodeMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    j1939_controller: Optional[Any]
    j1939_nm_node: Optional[J1939NmNode]
    def __init__(self) -> None:
        """Initialize J1939ControllerApplicationToJ1939NmNodeMapping."""
        super().__init__()
        self.j1939_controller: Optional[Any] = None
        self.j1939_nm_node: Optional[J1939NmNode] = None


class J1939ControllerApplicationToJ1939NmNodeMappingBuilder:
    """Builder for J1939ControllerApplicationToJ1939NmNodeMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939ControllerApplicationToJ1939NmNodeMapping = J1939ControllerApplicationToJ1939NmNodeMapping()

    def build(self) -> J1939ControllerApplicationToJ1939NmNodeMapping:
        """Build and return J1939ControllerApplicationToJ1939NmNodeMapping object.

        Returns:
            J1939ControllerApplicationToJ1939NmNodeMapping instance
        """
        # TODO: Add validation
        return self._obj
