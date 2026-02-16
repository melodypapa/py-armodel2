"""CouplingPortScheduler AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_structural_element import (
    CouplingPortStructuralElement,
)


class CouplingPortScheduler(CouplingPortStructuralElement):
    """AUTOSAR CouplingPortScheduler."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("port_scheduler_scheduler_enum", None, False, False, EthernetCouplingPortSchedulerEnum),  # portSchedulerSchedulerEnum
        ("predecessors", None, False, True, CouplingPortStructuralElement),  # predecessors
    ]

    def __init__(self) -> None:
        """Initialize CouplingPortScheduler."""
        super().__init__()
        self.port_scheduler_scheduler_enum: Optional[EthernetCouplingPortSchedulerEnum] = None
        self.predecessors: list[CouplingPortStructuralElement] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CouplingPortScheduler to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPortScheduler":
        """Create CouplingPortScheduler from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CouplingPortScheduler instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CouplingPortScheduler since parent returns ARObject
        return cast("CouplingPortScheduler", obj)


class CouplingPortSchedulerBuilder:
    """Builder for CouplingPortScheduler."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPortScheduler = CouplingPortScheduler()

    def build(self) -> CouplingPortScheduler:
        """Build and return CouplingPortScheduler object.

        Returns:
            CouplingPortScheduler instance
        """
        # TODO: Add validation
        return self._obj
