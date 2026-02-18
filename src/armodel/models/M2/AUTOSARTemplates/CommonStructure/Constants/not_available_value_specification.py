"""NotAvailableValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 440)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class NotAvailableValueSpecification(ValueSpecification):
    """AUTOSAR NotAvailableValueSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    default_pattern: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize NotAvailableValueSpecification."""
        super().__init__()
        self.default_pattern: Optional[PositiveInteger] = None


class NotAvailableValueSpecificationBuilder:
    """Builder for NotAvailableValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NotAvailableValueSpecification = NotAvailableValueSpecification()

    def build(self) -> NotAvailableValueSpecification:
        """Build and return NotAvailableValueSpecification object.

        Returns:
            NotAvailableValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
