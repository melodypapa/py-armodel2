"""CouplingPortShaper AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 123)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_structural_element import (
    CouplingPortStructuralElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_fifo import (
    CouplingPortFifo,
)


class CouplingPortShaper(CouplingPortStructuralElement):
    """AUTOSAR CouplingPortShaper."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    idle_slope: Optional[PositiveInteger]
    predecessor_fifo: CouplingPortFifo
    def __init__(self) -> None:
        """Initialize CouplingPortShaper."""
        super().__init__()
        self.idle_slope: Optional[PositiveInteger] = None
        self.predecessor_fifo: CouplingPortFifo = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPortShaper":
        """Deserialize XML element to CouplingPortShaper object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CouplingPortShaper object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse idle_slope
        child = ARObject._find_child_element(element, "IDLE-SLOPE")
        if child is not None:
            idle_slope_value = child.text
            obj.idle_slope = idle_slope_value

        # Parse predecessor_fifo
        child = ARObject._find_child_element(element, "PREDECESSOR-FIFO")
        if child is not None:
            predecessor_fifo_value = ARObject._deserialize_by_tag(child, "CouplingPortFifo")
            obj.predecessor_fifo = predecessor_fifo_value

        return obj



class CouplingPortShaperBuilder:
    """Builder for CouplingPortShaper."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPortShaper = CouplingPortShaper()

    def build(self) -> CouplingPortShaper:
        """Build and return CouplingPortShaper object.

        Returns:
            CouplingPortShaper instance
        """
        # TODO: Add validation
        return self._obj
