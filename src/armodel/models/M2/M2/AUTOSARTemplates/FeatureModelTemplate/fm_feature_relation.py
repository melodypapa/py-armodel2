"""FMFeatureRelation AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature import (
    FMFeature,
)


class FMFeatureRelation(Identifiable):
    """AUTOSAR FMFeatureRelation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "features": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=FMFeature,
        ),  # features
        "restriction": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (FMConditionByFeatures),
        ),  # restriction
    }

    def __init__(self) -> None:
        """Initialize FMFeatureRelation."""
        super().__init__()
        self.features: list[FMFeature] = []
        self.restriction: Optional[Any] = None


class FMFeatureRelationBuilder:
    """Builder for FMFeatureRelation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureRelation = FMFeatureRelation()

    def build(self) -> FMFeatureRelation:
        """Build and return FMFeatureRelation object.

        Returns:
            FMFeatureRelation instance
        """
        # TODO: Add validation
        return self._obj
