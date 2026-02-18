"""AbstractVariationRestriction AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 104)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 88)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ModelRestrictionTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ModelRestrictionTypes import (
    FullBindingTimeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from abc import ABC, abstractmethod


class AbstractVariationRestriction(ARObject, ABC):
    """AUTOSAR AbstractVariationRestriction."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    valid_bindings: list[FullBindingTimeEnum]
    variation: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize AbstractVariationRestriction."""
        super().__init__()
        self.valid_bindings: list[FullBindingTimeEnum] = []
        self.variation: Optional[Boolean] = None


class AbstractVariationRestrictionBuilder:
    """Builder for AbstractVariationRestriction."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractVariationRestriction = AbstractVariationRestriction()

    def build(self) -> AbstractVariationRestriction:
        """Build and return AbstractVariationRestriction object.

        Returns:
            AbstractVariationRestriction instance
        """
        # TODO: Add validation
        return self._obj
