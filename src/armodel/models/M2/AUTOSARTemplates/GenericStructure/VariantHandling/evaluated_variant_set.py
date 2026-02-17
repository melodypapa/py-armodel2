"""EvaluatedVariantSet AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 257)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.predefined_variant import (
    PredefinedVariant,
)


class EvaluatedVariantSet(ARElement):
    """AUTOSAR EvaluatedVariantSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "approval_status": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # approvalStatus
        "evaluateds": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=PredefinedVariant,
        ),  # evaluateds
    }

    def __init__(self) -> None:
        """Initialize EvaluatedVariantSet."""
        super().__init__()
        self.approval_status: NameToken = None
        self.evaluateds: list[PredefinedVariant] = []


class EvaluatedVariantSetBuilder:
    """Builder for EvaluatedVariantSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EvaluatedVariantSet = EvaluatedVariantSet()

    def build(self) -> EvaluatedVariantSet:
        """Build and return EvaluatedVariantSet object.

        Returns:
            EvaluatedVariantSet instance
        """
        # TODO: Add validation
        return self._obj
