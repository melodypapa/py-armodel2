"""Unit AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)
from armodel.models.M2.MSR.AsamHdo.Units.physical_dimension import (
    PhysicalDimension,
)
from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData.single_language_unit_names import (
    SingleLanguageUnitNames,
)


class Unit(ARElement):
    """AUTOSAR Unit."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("display_name", None, False, False, SingleLanguageUnitNames),  # displayName
        ("factor_si_to_unit", None, True, False, None),  # factorSiToUnit
        ("offset_si_to_unit", None, True, False, None),  # offsetSiToUnit
        ("physical", None, False, False, PhysicalDimension),  # physical
    ]

    def __init__(self) -> None:
        """Initialize Unit."""
        super().__init__()
        self.display_name: Optional[SingleLanguageUnitNames] = None
        self.factor_si_to_unit: Optional[Float] = None
        self.offset_si_to_unit: Optional[Float] = None
        self.physical: Optional[PhysicalDimension] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Unit to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Unit":
        """Create Unit from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Unit instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Unit since parent returns ARObject
        return cast("Unit", obj)


class UnitBuilder:
    """Builder for Unit."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Unit = Unit()

    def build(self) -> Unit:
        """Build and return Unit object.

        Returns:
            Unit instance
        """
        # TODO: Add validation
        return self._obj
