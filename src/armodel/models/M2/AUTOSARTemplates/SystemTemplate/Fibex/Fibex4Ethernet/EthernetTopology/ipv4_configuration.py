"""Ipv4Configuration AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class Ipv4Configuration(NetworkEndpointAddress):
    """AUTOSAR Ipv4Configuration."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize Ipv4Configuration."""
        super().__init__()


class Ipv4ConfigurationBuilder:
    """Builder for Ipv4Configuration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ipv4Configuration = Ipv4Configuration()

    def build(self) -> Ipv4Configuration:
        """Build and return Ipv4Configuration object.

        Returns:
            Ipv4Configuration instance
        """
        # TODO: Add validation
        return self._obj
