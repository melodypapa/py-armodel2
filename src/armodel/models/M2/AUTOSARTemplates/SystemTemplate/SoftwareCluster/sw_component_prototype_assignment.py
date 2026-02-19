"""SwComponentPrototypeAssignment AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 894)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class SwComponentPrototypeAssignment(ARObject):
    """AUTOSAR SwComponentPrototypeAssignment."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sw_component: Optional[Any]
    def __init__(self) -> None:
        """Initialize SwComponentPrototypeAssignment."""
        super().__init__()
        self.sw_component: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwComponentPrototypeAssignment":
        """Deserialize XML element to SwComponentPrototypeAssignment object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwComponentPrototypeAssignment object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse sw_component
        child = ARObject._find_child_element(element, "SW-COMPONENT")
        if child is not None:
            sw_component_value = child.text
            obj.sw_component = sw_component_value

        return obj



class SwComponentPrototypeAssignmentBuilder:
    """Builder for SwComponentPrototypeAssignment."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwComponentPrototypeAssignment = SwComponentPrototypeAssignment()

    def build(self) -> SwComponentPrototypeAssignment:
        """Build and return SwComponentPrototypeAssignment object.

        Returns:
            SwComponentPrototypeAssignment instance
        """
        # TODO: Add validation
        return self._obj
