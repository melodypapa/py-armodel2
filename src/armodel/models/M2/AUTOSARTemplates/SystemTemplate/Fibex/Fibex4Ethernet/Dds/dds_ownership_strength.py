"""DdsOwnershipStrength AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 533)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DdsOwnershipStrength(ARObject):
    """AUTOSAR DdsOwnershipStrength."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ownership: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DdsOwnershipStrength."""
        super().__init__()
        self.ownership: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsOwnershipStrength":
        """Deserialize XML element to DdsOwnershipStrength object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsOwnershipStrength object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ownership
        child = ARObject._find_child_element(element, "OWNERSHIP")
        if child is not None:
            ownership_value = child.text
            obj.ownership = ownership_value

        return obj



class DdsOwnershipStrengthBuilder:
    """Builder for DdsOwnershipStrength."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsOwnershipStrength = DdsOwnershipStrength()

    def build(self) -> DdsOwnershipStrength:
        """Build and return DdsOwnershipStrength object.

        Returns:
            DdsOwnershipStrength instance
        """
        # TODO: Add validation
        return self._obj
