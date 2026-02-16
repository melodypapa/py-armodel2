"""SwCalprmAxisSet AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter.sw_calprm_axis import (
    SwCalprmAxis,
)


class SwCalprmAxisSet(ARObject):
    """AUTOSAR SwCalprmAxisSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "sw_calprm_axises": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SwCalprmAxis,
        ),  # swCalprmAxises
    }

    def __init__(self) -> None:
        """Initialize SwCalprmAxisSet."""
        super().__init__()
        self.sw_calprm_axises: list[SwCalprmAxis] = []


class SwCalprmAxisSetBuilder:
    """Builder for SwCalprmAxisSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwCalprmAxisSet = SwCalprmAxisSet()

    def build(self) -> SwCalprmAxisSet:
        """Build and return SwCalprmAxisSet object.

        Returns:
            SwCalprmAxisSet instance
        """
        # TODO: Add validation
        return self._obj
