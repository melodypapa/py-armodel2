"""CouplingPortFifo AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_structural_element import (
    CouplingPortStructuralElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CouplingPortFifo(CouplingPortStructuralElement):
    """AUTOSAR CouplingPortFifo."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("assigned_traffic", None, True, False, None),  # assignedTraffic
        ("minimum_fifo", None, True, False, None),  # minimumFifo
        ("shaper", None, False, False, any (CouplingPortAbstract)),  # shaper
    ]

    def __init__(self) -> None:
        """Initialize CouplingPortFifo."""
        super().__init__()
        self.assigned_traffic: PositiveInteger = None
        self.minimum_fifo: Optional[PositiveInteger] = None
        self.shaper: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CouplingPortFifo to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPortFifo":
        """Create CouplingPortFifo from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CouplingPortFifo instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CouplingPortFifo since parent returns ARObject
        return cast("CouplingPortFifo", obj)


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
