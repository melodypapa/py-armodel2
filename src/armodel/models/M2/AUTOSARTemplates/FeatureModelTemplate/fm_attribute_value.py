"""FMAttributeValue AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 42)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_attribute_def import (
    FMAttributeDef,
)


class FMAttributeValue(ARObject):
    """AUTOSAR FMAttributeValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    definition: Optional[FMAttributeDef]
    value: Optional[Numerical]
    def __init__(self) -> None:
        """Initialize FMAttributeValue."""
        super().__init__()
        self.definition: Optional[FMAttributeDef] = None
        self.value: Optional[Numerical] = None


class FMAttributeValueBuilder:
    """Builder for FMAttributeValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMAttributeValue = FMAttributeValue()

    def build(self) -> FMAttributeValue:
        """Build and return FMAttributeValue object.

        Returns:
            FMAttributeValue instance
        """
        # TODO: Add validation
        return self._obj
