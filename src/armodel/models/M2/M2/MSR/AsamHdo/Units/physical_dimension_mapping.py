"""PhysicalDimensionMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 399)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_Units.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.Units.physical_dimension import (
    PhysicalDimension,
)


class PhysicalDimensionMapping(ARObject):
    """AUTOSAR PhysicalDimensionMapping."""

    def __init__(self) -> None:
        """Initialize PhysicalDimensionMapping."""
        super().__init__()
        self.first_physical: Optional[PhysicalDimension] = None
        self.second_physical: Optional[PhysicalDimension] = None


class PhysicalDimensionMappingBuilder:
    """Builder for PhysicalDimensionMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PhysicalDimensionMapping = PhysicalDimensionMapping()

    def build(self) -> PhysicalDimensionMapping:
        """Build and return PhysicalDimensionMapping object.

        Returns:
            PhysicalDimensionMapping instance
        """
        # TODO: Add validation
        return self._obj
