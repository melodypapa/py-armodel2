"""SdgDef AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 99)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 207)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_class import (
    SdgClass,
)


class SdgDef(ARElement):
    """AUTOSAR SdgDef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "sdg_classes": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SdgClass,
        ),  # sdgClasses
    }

    def __init__(self) -> None:
        """Initialize SdgDef."""
        super().__init__()
        self.sdg_classes: list[SdgClass] = []


class SdgDefBuilder:
    """Builder for SdgDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgDef = SdgDef()

    def build(self) -> SdgDef:
        """Build and return SdgDef object.

        Returns:
            SdgDef instance
        """
        # TODO: Add validation
        return self._obj
