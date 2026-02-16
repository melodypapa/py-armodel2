"""CycleRepetition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cycle import (
    CommunicationCycle,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class CycleRepetition(CommunicationCycle):
    """AUTOSAR CycleRepetition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base_cycle", None, True, False, None),  # BaseCycle
        ("cycle_repetition", None, False, False, CycleRepetitionType),  # CycleRepetition
    ]

    def __init__(self) -> None:
        """Initialize CycleRepetition."""
        super().__init__()
        self.base_cycle: Optional[Integer] = None
        self.cycle_repetition: Optional[CycleRepetitionType] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CycleRepetition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CycleRepetition":
        """Create CycleRepetition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CycleRepetition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CycleRepetition since parent returns ARObject
        return cast("CycleRepetition", obj)


class CycleRepetitionBuilder:
    """Builder for CycleRepetition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CycleRepetition = CycleRepetition()

    def build(self) -> CycleRepetition:
        """Build and return CycleRepetition object.

        Returns:
            CycleRepetition instance
        """
        # TODO: Add validation
        return self._obj
