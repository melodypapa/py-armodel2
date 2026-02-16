"""FMFeatureMapElement AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_map import (
    FMFeatureMap,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.sw_systemconstant_value_set import (
    SwSystemconstantValueSet,
)


class FMFeatureMapElement(Identifiable):
    """AUTOSAR FMFeatureMapElement."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "assertions": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=FMFeatureMap,
        ),  # assertions
        "conditions": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=FMFeatureMap,
        ),  # conditions
        "post_build_variants": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (PostBuildVariant),
        ),  # postBuildVariants
        "sw_value_sets": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SwSystemconstantValueSet,
        ),  # swValueSets
    }

    def __init__(self) -> None:
        """Initialize FMFeatureMapElement."""
        super().__init__()
        self.assertions: list[FMFeatureMap] = []
        self.conditions: list[FMFeatureMap] = []
        self.post_build_variants: list[Any] = []
        self.sw_value_sets: list[SwSystemconstantValueSet] = []


class FMFeatureMapElementBuilder:
    """Builder for FMFeatureMapElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureMapElement = FMFeatureMapElement()

    def build(self) -> FMFeatureMapElement:
        """Build and return FMFeatureMapElement object.

        Returns:
            FMFeatureMapElement instance
        """
        # TODO: Add validation
        return self._obj
