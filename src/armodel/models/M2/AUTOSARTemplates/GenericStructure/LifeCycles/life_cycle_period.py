"""LifeCyclePeriod AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 392)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_LifeCycles.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    RevisionLabelString,
)


class LifeCyclePeriod(ARObject):
    """AUTOSAR LifeCyclePeriod."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ar_release: Optional[RevisionLabelString]
    date: Optional[DateTime]
    product_release: Optional[RevisionLabelString]
    def __init__(self) -> None:
        """Initialize LifeCyclePeriod."""
        super().__init__()
        self.ar_release: Optional[RevisionLabelString] = None
        self.date: Optional[DateTime] = None
        self.product_release: Optional[RevisionLabelString] = None


class LifeCyclePeriodBuilder:
    """Builder for LifeCyclePeriod."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LifeCyclePeriod = LifeCyclePeriod()

    def build(self) -> LifeCyclePeriod:
        """Build and return LifeCyclePeriod object.

        Returns:
            LifeCyclePeriod instance
        """
        # TODO: Add validation
        return self._obj
