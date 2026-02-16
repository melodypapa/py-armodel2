"""PostBuildVariantCriterionValueSet AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)


class PostBuildVariantCriterionValueSet(ARElement):
    """AUTOSAR PostBuildVariantCriterionValueSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "post_build_variants": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (PostBuildVariant),
        ),  # postBuildVariants
    }

    def __init__(self) -> None:
        """Initialize PostBuildVariantCriterionValueSet."""
        super().__init__()
        self.post_build_variants: list[Any] = []


class PostBuildVariantCriterionValueSetBuilder:
    """Builder for PostBuildVariantCriterionValueSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PostBuildVariantCriterionValueSet = PostBuildVariantCriterionValueSet()

    def build(self) -> PostBuildVariantCriterionValueSet:
        """Build and return PostBuildVariantCriterionValueSet object.

        Returns:
            PostBuildVariantCriterionValueSet instance
        """
        # TODO: Add validation
        return self._obj
