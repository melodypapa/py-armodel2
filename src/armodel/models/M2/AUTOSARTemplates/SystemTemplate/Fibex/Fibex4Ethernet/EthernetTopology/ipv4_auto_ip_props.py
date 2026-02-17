"""Ipv4AutoIpProps AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class Ipv4AutoIpProps(ARObject):
    """AUTOSAR Ipv4AutoIpProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize Ipv4AutoIpProps."""
        super().__init__()


class Ipv4AutoIpPropsBuilder:
    """Builder for Ipv4AutoIpProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ipv4AutoIpProps = Ipv4AutoIpProps()

    def build(self) -> Ipv4AutoIpProps:
        """Build and return Ipv4AutoIpProps object.

        Returns:
            Ipv4AutoIpProps instance
        """
        # TODO: Add validation
        return self._obj
