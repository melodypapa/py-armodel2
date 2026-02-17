"""FMFeatureRestriction AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 32)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class FMFeatureRestriction(Identifiable):
    """AUTOSAR FMFeatureRestriction."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "restriction_and_attributes": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (FMConditionByFeatures),
        ),  # restrictionAndAttributes
    }

    def __init__(self) -> None:
        """Initialize FMFeatureRestriction."""
        super().__init__()
        self.restriction_and_attributes: Optional[Any] = None


class FMFeatureRestrictionBuilder:
    """Builder for FMFeatureRestriction."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureRestriction = FMFeatureRestriction()

    def build(self) -> FMFeatureRestriction:
        """Build and return FMFeatureRestriction object.

        Returns:
            FMFeatureRestriction instance
        """
        # TODO: Add validation
        return self._obj
