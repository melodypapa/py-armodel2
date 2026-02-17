"""AbstractMultiplicityRestriction AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 422)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 88)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ModelRestrictionTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class AbstractMultiplicityRestriction(ARObject):
    """AUTOSAR AbstractMultiplicityRestriction."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize AbstractMultiplicityRestriction."""
        super().__init__()
        self.lower_multiplicity: Optional[PositiveInteger] = None
        self.upper_multiplicity: Optional[Boolean] = None


class AbstractMultiplicityRestrictionBuilder:
    """Builder for AbstractMultiplicityRestriction."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractMultiplicityRestriction = AbstractMultiplicityRestriction()

    def build(self) -> AbstractMultiplicityRestriction:
        """Build and return AbstractMultiplicityRestriction object.

        Returns:
            AbstractMultiplicityRestriction instance
        """
        # TODO: Add validation
        return self._obj
