"""PostBuildVariantCriterion AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 304)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 614)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 76)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 232)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_method import (
    CompuMethod,
)


class PostBuildVariantCriterion(ARElement):
    """AUTOSAR PostBuildVariantCriterion."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "compu_method": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=CompuMethod,
        ),  # compuMethod
    }

    def __init__(self) -> None:
        """Initialize PostBuildVariantCriterion."""
        super().__init__()
        self.compu_method: CompuMethod = None


class PostBuildVariantCriterionBuilder:
    """Builder for PostBuildVariantCriterion."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PostBuildVariantCriterion = PostBuildVariantCriterion()

    def build(self) -> PostBuildVariantCriterion:
        """Build and return PostBuildVariantCriterion object.

        Returns:
            PostBuildVariantCriterion instance
        """
        # TODO: Add validation
        return self._obj
