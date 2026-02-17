"""EndToEndProtection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 214)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 384)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_EndToEndProtection.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class EndToEndProtection(Identifiable):
    """AUTOSAR EndToEndProtection."""

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
        """Initialize EndToEndProtection."""
        super().__init__()
        self.end_to_ends: list[EndToEndProtection] = []


class EndToEndProtectionBuilder:
    """Builder for EndToEndProtection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EndToEndProtection = EndToEndProtection()

    def build(self) -> EndToEndProtection:
        """Build and return EndToEndProtection object.

        Returns:
            EndToEndProtection instance
        """
        # TODO: Add validation
        return self._obj
