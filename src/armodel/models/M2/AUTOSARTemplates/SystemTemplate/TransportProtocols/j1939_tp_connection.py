"""J1939TpConnection AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class J1939TpConnection(TpConnection):
    """AUTOSAR J1939TpConnection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize J1939TpConnection."""
        super().__init__()


class J1939TpConnectionBuilder:
    """Builder for J1939TpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939TpConnection = J1939TpConnection()

    def build(self) -> J1939TpConnection:
        """Build and return J1939TpConnection object.

        Returns:
            J1939TpConnection instance
        """
        # TODO: Add validation
        return self._obj
