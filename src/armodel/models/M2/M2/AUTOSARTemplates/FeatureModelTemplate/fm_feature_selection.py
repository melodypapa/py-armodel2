"""FMFeatureSelection AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 40)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_attribute_value import (
    FMAttributeValue,
)


class FMFeatureSelection(Identifiable):
    """AUTOSAR FMFeatureSelection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "attribute_values": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=FMAttributeValue,
        ),  # attributeValues
    }

    def __init__(self) -> None:
        """Initialize FMFeatureSelection."""
        super().__init__()
        self.attribute_values: list[FMAttributeValue] = []


class FMFeatureSelectionBuilder:
    """Builder for FMFeatureSelection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureSelection = FMFeatureSelection()

    def build(self) -> FMFeatureSelection:
        """Build and return FMFeatureSelection object.

        Returns:
            FMFeatureSelection instance
        """
        # TODO: Add validation
        return self._obj
