"""CompuNominatorDenominator AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 391)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class CompuNominatorDenominator(ARObject):
    """AUTOSAR CompuNominatorDenominator."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize CompuNominatorDenominator."""
        super().__init__()


class CompuNominatorDenominatorBuilder:
    """Builder for CompuNominatorDenominator."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuNominatorDenominator = CompuNominatorDenominator()

    def build(self) -> CompuNominatorDenominator:
        """Build and return CompuNominatorDenominator object.

        Returns:
            CompuNominatorDenominator instance
        """
        # TODO: Add validation
        return self._obj
