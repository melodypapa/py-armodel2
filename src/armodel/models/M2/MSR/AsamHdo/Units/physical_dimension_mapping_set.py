"""PhysicalDimensionMappingSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 399)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_Units.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.Units.physical_dimension import (
    PhysicalDimension,
)


class PhysicalDimensionMappingSet(ARElement):
    """AUTOSAR PhysicalDimensionMappingSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    physicals: list[PhysicalDimension]
    def __init__(self) -> None:
        """Initialize PhysicalDimensionMappingSet."""
        super().__init__()
        self.physicals: list[PhysicalDimension] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "PhysicalDimensionMappingSet":
        """Deserialize XML element to PhysicalDimensionMappingSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PhysicalDimensionMappingSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PhysicalDimensionMappingSet, cls).deserialize(element)

        # Parse physicals (list from container "PHYSICALS")
        obj.physicals = []
        container = ARObject._find_child_element(element, "PHYSICALS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.physicals.append(child_value)

        return obj



class PhysicalDimensionMappingSetBuilder:
    """Builder for PhysicalDimensionMappingSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PhysicalDimensionMappingSet = PhysicalDimensionMappingSet()

    def build(self) -> PhysicalDimensionMappingSet:
        """Build and return PhysicalDimensionMappingSet object.

        Returns:
            PhysicalDimensionMappingSet instance
        """
        # TODO: Add validation
        return self._obj
