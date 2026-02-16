"""CycleCounter AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cycle import (
    CommunicationCycle,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class CycleCounter(CommunicationCycle):
    """AUTOSAR CycleCounter."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("cycle_counter", None, True, False, None),  # CycleCounter
    ]

    def __init__(self) -> None:
        """Initialize CycleCounter."""
        super().__init__()
        self.cycle_counter: Optional[Integer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CycleCounter to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CycleCounter":
        """Create CycleCounter from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CycleCounter instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CycleCounter since parent returns ARObject
        return cast("CycleCounter", obj)


class CycleCounterBuilder:
    """Builder for CycleCounter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CycleCounter = CycleCounter()

    def build(self) -> CycleCounter:
        """Build and return CycleCounter object.

        Returns:
            CycleCounter instance
        """
        # TODO: Add validation
        return self._obj
