"""CouplingPortFifo AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 124)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_structural_element import (
    CouplingPortStructuralElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CouplingPortFifo(CouplingPortStructuralElement):
    """AUTOSAR CouplingPortFifo."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    assigned_traffic: PositiveInteger
    minimum_fifo: Optional[PositiveInteger]
    shaper: Optional[Any]
    def __init__(self) -> None:
        """Initialize CouplingPortFifo."""
        super().__init__()
        self.assigned_traffic: PositiveInteger = None
        self.minimum_fifo: Optional[PositiveInteger] = None
        self.shaper: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPortFifo":
        """Deserialize XML element to CouplingPortFifo object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CouplingPortFifo object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse assigned_traffic
        child = ARObject._find_child_element(element, "ASSIGNED-TRAFFIC")
        if child is not None:
            assigned_traffic_value = child.text
            obj.assigned_traffic = assigned_traffic_value

        # Parse minimum_fifo
        child = ARObject._find_child_element(element, "MINIMUM-FIFO")
        if child is not None:
            minimum_fifo_value = child.text
            obj.minimum_fifo = minimum_fifo_value

        # Parse shaper
        child = ARObject._find_child_element(element, "SHAPER")
        if child is not None:
            shaper_value = child.text
            obj.shaper = shaper_value

        return obj



class CouplingPortFifoBuilder:
    """Builder for CouplingPortFifo."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPortFifo = CouplingPortFifo()

    def build(self) -> CouplingPortFifo:
        """Build and return CouplingPortFifo object.

        Returns:
            CouplingPortFifo instance
        """
        # TODO: Add validation
        return self._obj
