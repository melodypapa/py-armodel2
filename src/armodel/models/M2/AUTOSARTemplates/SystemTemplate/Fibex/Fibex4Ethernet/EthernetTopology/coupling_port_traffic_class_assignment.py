"""CouplingPortTrafficClassAssignment AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CouplingPortTrafficClassAssignment(Referrable):
    """AUTOSAR CouplingPortTrafficClassAssignment."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("priority", None, True, False, None),  # priority
        ("traffic_class", None, True, False, None),  # trafficClass
    ]

    def __init__(self) -> None:
        """Initialize CouplingPortTrafficClassAssignment."""
        super().__init__()
        self.priority: PositiveInteger = None
        self.traffic_class: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CouplingPortTrafficClassAssignment to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPortTrafficClassAssignment":
        """Create CouplingPortTrafficClassAssignment from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CouplingPortTrafficClassAssignment instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CouplingPortTrafficClassAssignment since parent returns ARObject
        return cast("CouplingPortTrafficClassAssignment", obj)


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
