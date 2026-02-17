"""SdgReference AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 101)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_attribute import (
    SdgAttribute,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_class import (
    SdgClass,
)


class SdgReference(SdgAttribute):
    """AUTOSAR SdgReference."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "dest_sdg": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SdgClass,
        ),  # destSdg
    }

    def __init__(self) -> None:
        """Initialize SdgReference."""
        super().__init__()
        self.dest_sdg: Optional[SdgClass] = None


class SdgReferenceBuilder:
    """Builder for SdgReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgReference = SdgReference()

    def build(self) -> SdgReference:
        """Build and return SdgReference object.

        Returns:
            SdgReference instance
        """
        # TODO: Add validation
        return self._obj
