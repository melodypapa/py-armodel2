"""DdsDurability AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 530)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds import (
    DdsDurabilityKindEnum,
)


class DdsDurability(ARObject):
    """AUTOSAR DdsDurability."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    durability_kind: Optional[DdsDurabilityKindEnum]
    def __init__(self) -> None:
        """Initialize DdsDurability."""
        super().__init__()
        self.durability_kind: Optional[DdsDurabilityKindEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsDurability":
        """Deserialize XML element to DdsDurability object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsDurability object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse durability_kind
        child = ARObject._find_child_element(element, "DURABILITY-KIND")
        if child is not None:
            durability_kind_value = child.text
            obj.durability_kind = durability_kind_value

        return obj



class DdsDurabilityBuilder:
    """Builder for DdsDurability."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsDurability = DdsDurability()

    def build(self) -> DdsDurability:
        """Build and return DdsDurability object.

        Returns:
            DdsDurability instance
        """
        # TODO: Add validation
        return self._obj
