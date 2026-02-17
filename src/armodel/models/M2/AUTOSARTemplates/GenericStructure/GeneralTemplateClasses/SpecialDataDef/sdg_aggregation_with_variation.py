"""SdgAggregationWithVariation AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 101)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_element_with_gid import (
    SdgElementWithGid,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_class import (
    SdgClass,
)


class SdgAggregationWithVariation(SdgElementWithGid):
    """AUTOSAR SdgAggregationWithVariation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "sub_sdg": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SdgClass,
        ),  # subSdg
    }

    def __init__(self) -> None:
        """Initialize SdgAggregationWithVariation."""
        super().__init__()
        self.sub_sdg: Optional[SdgClass] = None


class SdgAggregationWithVariationBuilder:
    """Builder for SdgAggregationWithVariation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgAggregationWithVariation = SdgAggregationWithVariation()

    def build(self) -> SdgAggregationWithVariation:
        """Build and return SdgAggregationWithVariation object.

        Returns:
            SdgAggregationWithVariation instance
        """
        # TODO: Add validation
        return self._obj
