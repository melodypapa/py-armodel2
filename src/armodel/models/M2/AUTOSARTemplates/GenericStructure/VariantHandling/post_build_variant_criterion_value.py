"""PostBuildVariantCriterionValue AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.MSR.Documentation.Annotation.annotation import (
    Annotation,
)


class PostBuildVariantCriterionValue(ARObject):
    """AUTOSAR PostBuildVariantCriterionValue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "annotations": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Annotation,
        ),  # annotations
        "value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # value
        "variant_criterion": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=any (PostBuildVariant),
        ),  # variantCriterion
    }

    def __init__(self) -> None:
        """Initialize PostBuildVariantCriterionValue."""
        super().__init__()
        self.annotations: list[Annotation] = []
        self.value: Integer = None
        self.variant_criterion: Any = None


class PostBuildVariantCriterionValueBuilder:
    """Builder for PostBuildVariantCriterionValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PostBuildVariantCriterionValue = PostBuildVariantCriterionValue()

    def build(self) -> PostBuildVariantCriterionValue:
        """Build and return PostBuildVariantCriterionValue object.

        Returns:
            PostBuildVariantCriterionValue instance
        """
        # TODO: Add validation
        return self._obj
