"""FMFormulaByFeaturesAndAttributes AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 61)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_attribute_def import (
    FMAttributeDef,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature import (
    FMFeature,
)


class FMFormulaByFeaturesAndAttributes(ARObject):
    """AUTOSAR FMFormulaByFeaturesAndAttributes."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "attribute": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=FMAttributeDef,
        ),  # attribute
        "feature": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=FMFeature,
        ),  # feature
    }

    def __init__(self) -> None:
        """Initialize FMFormulaByFeaturesAndAttributes."""
        super().__init__()
        self.attribute: Optional[FMAttributeDef] = None
        self.feature: Optional[FMFeature] = None


class FMFormulaByFeaturesAndAttributesBuilder:
    """Builder for FMFormulaByFeaturesAndAttributes."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFormulaByFeaturesAndAttributes = FMFormulaByFeaturesAndAttributes()

    def build(self) -> FMFormulaByFeaturesAndAttributes:
        """Build and return FMFormulaByFeaturesAndAttributes object.

        Returns:
            FMFormulaByFeaturesAndAttributes instance
        """
        # TODO: Add validation
        return self._obj
