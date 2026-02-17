"""AclOperation AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 384)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 159)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_RolesAndRights.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)


class AclOperation(ARElement):
    """AUTOSAR AclOperation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "implieds": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=AclOperation,
        ),  # implieds
    }

    def __init__(self) -> None:
        """Initialize AclOperation."""
        super().__init__()
        self.implieds: list[AclOperation] = []


class AclOperationBuilder:
    """Builder for AclOperation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AclOperation = AclOperation()

    def build(self) -> AclOperation:
        """Build and return AclOperation object.

        Returns:
            AclOperation instance
        """
        # TODO: Add validation
        return self._obj
