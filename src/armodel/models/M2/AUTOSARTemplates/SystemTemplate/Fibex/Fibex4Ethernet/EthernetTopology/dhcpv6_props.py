"""Dhcpv6Props AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class Dhcpv6Props(ARObject):
    """AUTOSAR Dhcpv6Props."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize Dhcpv6Props."""
        super().__init__()


class Dhcpv6PropsBuilder:
    """Builder for Dhcpv6Props."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Dhcpv6Props = Dhcpv6Props()

    def build(self) -> Dhcpv6Props:
        """Build and return Dhcpv6Props object.

        Returns:
            Dhcpv6Props instance
        """
        # TODO: Add validation
        return self._obj
