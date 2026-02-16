"""UnitGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)


class UnitGroup(ARElement):
    """AUTOSAR UnitGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("units", None, False, True, Unit),  # units
    ]

    def __init__(self) -> None:
        """Initialize UnitGroup."""
        super().__init__()
        self.units: list[Unit] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert UnitGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "UnitGroup":
        """Create UnitGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            UnitGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to UnitGroup since parent returns ARObject
        return cast("UnitGroup", obj)


class UnitGroupBuilder:
    """Builder for UnitGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UnitGroup = UnitGroup()

    def build(self) -> UnitGroup:
        """Build and return UnitGroup object.

        Returns:
            UnitGroup instance
        """
        # TODO: Add validation
        return self._obj
