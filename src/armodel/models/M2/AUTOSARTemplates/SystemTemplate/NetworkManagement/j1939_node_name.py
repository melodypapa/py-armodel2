"""J1939NodeName AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class J1939NodeName(ARObject):
    """AUTOSAR J1939NodeName."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize J1939NodeName."""
        super().__init__()


class J1939NodeNameBuilder:
    """Builder for J1939NodeName."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939NodeName = J1939NodeName()

    def build(self) -> J1939NodeName:
        """Build and return J1939NodeName object.

        Returns:
            J1939NodeName instance
        """
        # TODO: Add validation
        return self._obj
