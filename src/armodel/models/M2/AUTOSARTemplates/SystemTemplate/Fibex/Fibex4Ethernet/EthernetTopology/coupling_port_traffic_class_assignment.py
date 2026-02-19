"""CouplingPortTrafficClassAssignment AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 128)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CouplingPortTrafficClassAssignment(Referrable):
    """AUTOSAR CouplingPortTrafficClassAssignment."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    priority: PositiveInteger
    traffic_class: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize CouplingPortTrafficClassAssignment."""
        super().__init__()
        self.priority: PositiveInteger = None
        self.traffic_class: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPortTrafficClassAssignment":
        """Deserialize XML element to CouplingPortTrafficClassAssignment object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CouplingPortTrafficClassAssignment object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse priority
        child = ARObject._find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        # Parse traffic_class
        child = ARObject._find_child_element(element, "TRAFFIC-CLASS")
        if child is not None:
            traffic_class_value = child.text
            obj.traffic_class = traffic_class_value

        return obj



class CouplingPortTrafficClassAssignmentBuilder:
    """Builder for CouplingPortTrafficClassAssignment."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPortTrafficClassAssignment = CouplingPortTrafficClassAssignment()

    def build(self) -> CouplingPortTrafficClassAssignment:
        """Build and return CouplingPortTrafficClassAssignment object.

        Returns:
            CouplingPortTrafficClassAssignment instance
        """
        # TODO: Add validation
        return self._obj
