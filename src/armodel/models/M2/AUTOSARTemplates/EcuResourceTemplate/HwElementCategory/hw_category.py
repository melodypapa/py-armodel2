"""HwCategory AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 24)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate_HwElementCategory.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_attribute_def import (
    HwAttributeDef,
)


class HwCategory(ARElement):
    """AUTOSAR HwCategory."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    hw_attribute_defs: list[HwAttributeDef]
    def __init__(self) -> None:
        """Initialize HwCategory."""
        super().__init__()
        self.hw_attribute_defs: list[HwAttributeDef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwCategory":
        """Deserialize XML element to HwCategory object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HwCategory object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(HwCategory, cls).deserialize(element)

        # Parse hw_attribute_defs (list from container "HW-ATTRIBUTE-DEFS")
        obj.hw_attribute_defs = []
        container = ARObject._find_child_element(element, "HW-ATTRIBUTE-DEFS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.hw_attribute_defs.append(child_value)

        return obj



class HwCategoryBuilder:
    """Builder for HwCategory."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwCategory = HwCategory()

    def build(self) -> HwCategory:
        """Build and return HwCategory object.

        Returns:
            HwCategory instance
        """
        # TODO: Add validation
        return self._obj
