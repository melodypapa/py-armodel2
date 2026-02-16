"""Unit AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "display_name": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SingleLanguageUnitNames,
        ),  # displayName
        "factor_si_to_unit": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # factorSiToUnit
        "offset_si_to_unit": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # offsetSiToUnit
        "physical": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PhysicalDimension,
        ),  # physical
    }

    def __init__(self) -> None:
        """Initialize Unit."""
        super().__init__()
        self.display_name: Optional[SingleLanguageUnitNames] = None
        self.factor_si_to_unit: Optional[Float] = None
        self.offset_si_to_unit: Optional[Float] = None
        self.physical: Optional[PhysicalDimension] = None


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
