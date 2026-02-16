"""CouplingPortCreditBasedShaper AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CouplingPortCreditBasedShaper(Identifiable):
    """AUTOSAR CouplingPortCreditBasedShaper."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("idle_slope", None, True, False, None),  # idleSlope
        ("lower_boundary", None, True, False, None),  # lowerBoundary
        ("upper_boundary", None, True, False, None),  # upperBoundary
    ]

    def __init__(self) -> None:
        """Initialize CouplingPortCreditBasedShaper."""
        super().__init__()
        self.idle_slope: Optional[PositiveInteger] = None
        self.lower_boundary: Optional[PositiveInteger] = None
        self.upper_boundary: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CouplingPortCreditBasedShaper to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPortCreditBasedShaper":
        """Create CouplingPortCreditBasedShaper from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CouplingPortCreditBasedShaper instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CouplingPortCreditBasedShaper since parent returns ARObject
        return cast("CouplingPortCreditBasedShaper", obj)


class CouplingPortCreditBasedShaperBuilder:
    """Builder for CouplingPortCreditBasedShaper."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPortCreditBasedShaper = CouplingPortCreditBasedShaper()

    def build(self) -> CouplingPortCreditBasedShaper:
        """Build and return CouplingPortCreditBasedShaper object.

        Returns:
            CouplingPortCreditBasedShaper instance
        """
        # TODO: Add validation
        return self._obj
