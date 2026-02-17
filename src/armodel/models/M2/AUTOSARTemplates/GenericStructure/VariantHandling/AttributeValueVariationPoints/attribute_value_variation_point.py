"""AttributeValueVariationPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 617)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 209)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 41)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling_AttributeValueVariationPoints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    BindingTimeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PrimitiveIdentifier,
    String,
)


class AttributeValueVariationPoint(ARObject):
    """AUTOSAR AttributeValueVariationPoint."""

    def __init__(self) -> None:
        """Initialize AttributeValueVariationPoint."""
        super().__init__()
        self.binding_time_enum: Optional[BindingTimeEnum] = None
        self.blueprint_value: Optional[String] = None
        self.sd: Optional[String] = None
        self.short_label: Optional[PrimitiveIdentifier] = None


class AttributeValueVariationPointBuilder:
    """Builder for AttributeValueVariationPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AttributeValueVariationPoint = AttributeValueVariationPoint()

    def build(self) -> AttributeValueVariationPoint:
        """Build and return AttributeValueVariationPoint object.

        Returns:
            AttributeValueVariationPoint instance
        """
        # TODO: Add validation
        return self._obj
