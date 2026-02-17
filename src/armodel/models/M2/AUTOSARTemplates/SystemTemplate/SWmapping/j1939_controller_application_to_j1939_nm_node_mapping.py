"""J1939ControllerApplicationToJ1939NmNodeMapping AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class J1939ControllerApplicationToJ1939NmNodeMapping(ARObject):
    """AUTOSAR J1939ControllerApplicationToJ1939NmNodeMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize J1939ControllerApplicationToJ1939NmNodeMapping."""
        super().__init__()


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
