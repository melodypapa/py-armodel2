"""UnitGroup AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)


class UnitGroup(ARElement):
    """AUTOSAR UnitGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "units": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Unit,
        ),  # units
    }

    def __init__(self) -> None:
        """Initialize UnitGroup."""
        super().__init__()
        self.units: list[Unit] = []


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
