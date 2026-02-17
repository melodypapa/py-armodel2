"""Ieee1722TpEthernetFrame AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class Ieee1722TpEthernetFrame(AbstractEthernetFrame):
    """AUTOSAR Ieee1722TpEthernetFrame."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize Ieee1722TpEthernetFrame."""
        super().__init__()


class Ieee1722TpEthernetFrameBuilder:
    """Builder for Ieee1722TpEthernetFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ieee1722TpEthernetFrame = Ieee1722TpEthernetFrame()

    def build(self) -> Ieee1722TpEthernetFrame:
        """Build and return Ieee1722TpEthernetFrame object.

        Returns:
            Ieee1722TpEthernetFrame instance
        """
        # TODO: Add validation
        return self._obj
