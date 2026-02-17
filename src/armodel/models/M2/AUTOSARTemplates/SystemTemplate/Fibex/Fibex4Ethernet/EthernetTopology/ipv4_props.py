"""Ipv4Props AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class Ipv4Props(ARObject):
    """AUTOSAR Ipv4Props."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize Ipv4Props."""
        super().__init__()


class Ipv4PropsBuilder:
    """Builder for Ipv4Props."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ipv4Props = Ipv4Props()

    def build(self) -> Ipv4Props:
        """Build and return Ipv4Props object.

        Returns:
            Ipv4Props instance
        """
        # TODO: Add validation
        return self._obj
