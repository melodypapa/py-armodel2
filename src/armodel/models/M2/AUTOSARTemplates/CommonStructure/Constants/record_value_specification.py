"""RecordValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 328)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 435)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.composite_value_specification import (
    CompositeValueSpecification,
)


class RecordValueSpecification(CompositeValueSpecification):
    """AUTOSAR RecordValueSpecification."""

    def __init__(self) -> None:
        """Initialize RecordValueSpecification."""
        super().__init__()


class RecordValueSpecificationBuilder:
    """Builder for RecordValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RecordValueSpecification = RecordValueSpecification()

    def build(self) -> RecordValueSpecification:
        """Build and return RecordValueSpecification object.

        Returns:
            RecordValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
