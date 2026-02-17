"""ConditionalChangeNad AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class ConditionalChangeNad(LinConfigurationEntry):
    """AUTOSAR ConditionalChangeNad."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize ConditionalChangeNad."""
        super().__init__()


class ConditionalChangeNadBuilder:
    """Builder for ConditionalChangeNad."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConditionalChangeNad = ConditionalChangeNad()

    def build(self) -> ConditionalChangeNad:
        """Build and return ConditionalChangeNad object.

        Returns:
            ConditionalChangeNad instance
        """
        # TODO: Add validation
        return self._obj
