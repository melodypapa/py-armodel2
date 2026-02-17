"""EndToEndProtectionSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 214)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 383)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_EndToEndProtection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection.end_to_end_protection import (
    EndToEndProtection,
)


class EndToEndProtectionSet(ARElement):
    """AUTOSAR EndToEndProtectionSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "end_to_ends": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=EndToEndProtection,
        ),  # endToEnds
    }

    def __init__(self) -> None:
        """Initialize EndToEndProtectionSet."""
        super().__init__()
        self.end_to_ends: list[EndToEndProtection] = []


class EndToEndProtectionSetBuilder:
    """Builder for EndToEndProtectionSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EndToEndProtectionSet = EndToEndProtectionSet()

    def build(self) -> EndToEndProtectionSet:
        """Build and return EndToEndProtectionSet object.

        Returns:
            EndToEndProtectionSet instance
        """
        # TODO: Add validation
        return self._obj
