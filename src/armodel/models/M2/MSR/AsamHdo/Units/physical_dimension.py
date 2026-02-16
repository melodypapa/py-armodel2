"""PhysicalDimension AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)


class PhysicalDimension(ARElement):
    """AUTOSAR PhysicalDimension."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("current_exp", None, True, False, None),  # currentExp
        ("length_exp", None, True, False, None),  # lengthExp
        ("luminous", None, True, False, None),  # luminous
        ("mass_exp", None, True, False, None),  # massExp
        ("molar_amount", None, True, False, None),  # molarAmount
        ("temperature_exp", None, True, False, None),  # temperatureExp
        ("time_exp", None, True, False, None),  # timeExp
    ]

    def __init__(self) -> None:
        """Initialize PhysicalDimension."""
        super().__init__()
        self.current_exp: Optional[Numerical] = None
        self.length_exp: Optional[Numerical] = None
        self.luminous: Optional[Numerical] = None
        self.mass_exp: Optional[Numerical] = None
        self.molar_amount: Optional[Numerical] = None
        self.temperature_exp: Optional[Numerical] = None
        self.time_exp: Optional[Numerical] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PhysicalDimension to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PhysicalDimension":
        """Create PhysicalDimension from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PhysicalDimension instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PhysicalDimension since parent returns ARObject
        return cast("PhysicalDimension", obj)


class PhysicalDimensionBuilder:
    """Builder for PhysicalDimension."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PhysicalDimension = PhysicalDimension()

    def build(self) -> PhysicalDimension:
        """Build and return PhysicalDimension object.

        Returns:
            PhysicalDimension instance
        """
        # TODO: Add validation
        return self._obj
