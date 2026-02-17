"""McFunction AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 186)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.mc_function_data_ref_set import (
    McFunctionDataRefSet,
)


class McFunction(ARElement):
    """AUTOSAR McFunction."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "def_calprm_set": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=McFunctionDataRefSet,
        ),  # defCalprmSet
        "in_measurement": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=McFunctionDataRefSet,
        ),  # inMeasurement
        "loc": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=McFunctionDataRefSet,
        ),  # loc
        "out": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=McFunctionDataRefSet,
        ),  # out
        "ref_calprm_set": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=McFunctionDataRefSet,
        ),  # refCalprmSet
        "sub_functions": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class="McFunction",
        ),  # subFunctions
    }

    def __init__(self) -> None:
        """Initialize McFunction."""
        super().__init__()
        self.def_calprm_set: Optional[McFunctionDataRefSet] = None
        self.in_measurement: Optional[McFunctionDataRefSet] = None
        self.loc: Optional[McFunctionDataRefSet] = None
        self.out: Optional[McFunctionDataRefSet] = None
        self.ref_calprm_set: Optional[McFunctionDataRefSet] = None
        self.sub_functions: list[McFunction] = []


class McFunctionBuilder:
    """Builder for McFunction."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: McFunction = McFunction()

    def build(self) -> McFunction:
        """Build and return McFunction object.

        Returns:
            McFunction instance
        """
        # TODO: Add validation
        return self._obj
