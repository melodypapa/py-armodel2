"""DdsDurabilityService AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 530)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DdsDurabilityService(ARObject):
    """AUTOSAR DdsDurabilityService."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    durability: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DdsDurabilityService."""
        super().__init__()
        self.durability: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsDurabilityService":
        """Deserialize XML element to DdsDurabilityService object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsDurabilityService object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse durability
        child = ARObject._find_child_element(element, "DURABILITY")
        if child is not None:
            durability_value = child.text
            obj.durability = durability_value

        return obj



class DdsDurabilityServiceBuilder:
    """Builder for DdsDurabilityService."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsDurabilityService = DdsDurabilityService()

    def build(self) -> DdsDurabilityService:
        """Build and return DdsDurabilityService object.

        Returns:
            DdsDurabilityService instance
        """
        # TODO: Add validation
        return self._obj
