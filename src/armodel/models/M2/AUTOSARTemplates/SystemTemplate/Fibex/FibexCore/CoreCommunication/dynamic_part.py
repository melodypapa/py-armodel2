"""DynamicPart AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 410)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.multiplexed_part import (
    MultiplexedPart,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.dynamic_part_alternative import (
    DynamicPartAlternative,
)


class DynamicPart(MultiplexedPart):
    """AUTOSAR DynamicPart."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dynamic_parts: list[DynamicPartAlternative]
    def __init__(self) -> None:
        """Initialize DynamicPart."""
        super().__init__()
        self.dynamic_parts: list[DynamicPartAlternative] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DynamicPart":
        """Deserialize XML element to DynamicPart object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DynamicPart object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DynamicPart, cls).deserialize(element)

        # Parse dynamic_parts (list from container "DYNAMIC-PARTS")
        obj.dynamic_parts = []
        container = ARObject._find_child_element(element, "DYNAMIC-PARTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dynamic_parts.append(child_value)

        return obj



class DynamicPartBuilder:
    """Builder for DynamicPart."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DynamicPart = DynamicPart()

    def build(self) -> DynamicPart:
        """Build and return DynamicPart object.

        Returns:
            DynamicPart instance
        """
        # TODO: Add validation
        return self._obj
