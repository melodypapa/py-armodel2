"""FMFeatureMapCondition AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 55)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class FMFeatureMapCondition(Identifiable):
    """AUTOSAR FMFeatureMapCondition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "fm_cond_and_attributes": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # fmCondAndAttributes
    }

    def __init__(self) -> None:
        """Initialize FMFeatureMapCondition."""
        super().__init__()
        self.fm_cond_and_attributes: Optional[Any] = None


class FMFeatureMapConditionBuilder:
    """Builder for FMFeatureMapCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureMapCondition = FMFeatureMapCondition()

    def build(self) -> FMFeatureMapCondition:
        """Build and return FMFeatureMapCondition object.

        Returns:
            FMFeatureMapCondition instance
        """
        # TODO: Add validation
        return self._obj
