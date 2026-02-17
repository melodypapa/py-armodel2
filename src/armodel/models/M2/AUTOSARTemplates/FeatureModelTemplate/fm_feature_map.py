"""FMFeatureMap AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 53)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_map_element import (
    FMFeatureMapElement,
)


class FMFeatureMap(ARElement):
    """AUTOSAR FMFeatureMap."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "mappings": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=FMFeatureMapElement,
        ),  # mappings
    }

    def __init__(self) -> None:
        """Initialize FMFeatureMap."""
        super().__init__()
        self.mappings: list[FMFeatureMapElement] = []


class FMFeatureMapBuilder:
    """Builder for FMFeatureMap."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureMap = FMFeatureMap()

    def build(self) -> FMFeatureMap:
        """Build and return FMFeatureMap object.

        Returns:
            FMFeatureMap instance
        """
        # TODO: Add validation
        return self._obj
