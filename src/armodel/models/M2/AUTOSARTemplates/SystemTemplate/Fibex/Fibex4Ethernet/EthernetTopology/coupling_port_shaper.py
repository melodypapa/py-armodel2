"""CouplingPortShaper AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_structural_element import (
    CouplingPortStructuralElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_fifo import (
    CouplingPortFifo,
)


class CouplingPortShaper(CouplingPortStructuralElement):
    """AUTOSAR CouplingPortShaper."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("idle_slope", None, True, False, None),  # idleSlope
        ("predecessor_fifo", None, False, False, CouplingPortFifo),  # predecessorFifo
    ]

    def __init__(self) -> None:
        """Initialize CouplingPortShaper."""
        super().__init__()
        self.idle_slope: Optional[PositiveInteger] = None
        self.predecessor_fifo: CouplingPortFifo = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CouplingPortShaper to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPortShaper":
        """Create CouplingPortShaper from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CouplingPortShaper instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CouplingPortShaper since parent returns ARObject
        return cast("CouplingPortShaper", obj)


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
