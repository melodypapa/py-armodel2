"""ApplicationValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 299)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 455)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.MSR.CalibrationData.CalibrationValue.sw_axis_cont import (
    SwAxisCont,
)
from armodel.models.M2.MSR.CalibrationData.CalibrationValue.sw_value_cont import (
    SwValueCont,
)


class ApplicationValueSpecification(ValueSpecification):
    """AUTOSAR ApplicationValueSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    category: Optional[Identifier]
    sw_axis_conts: list[SwAxisCont]
    sw_value_cont: Optional[SwValueCont]
    def __init__(self) -> None:
        """Initialize ApplicationValueSpecification."""
        super().__init__()
        self.category: Optional[Identifier] = None
        self.sw_axis_conts: list[SwAxisCont] = []
        self.sw_value_cont: Optional[SwValueCont] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationValueSpecification":
        """Deserialize XML element to ApplicationValueSpecification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationValueSpecification object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse category
        child = ARObject._find_child_element(element, "CATEGORY")
        if child is not None:
            category_value = child.text
            obj.category = category_value

        # Parse sw_axis_conts (list)
        obj.sw_axis_conts = []
        for child in ARObject._find_all_child_elements(element, "SW-AXIS-CONTS"):
            sw_axis_conts_value = ARObject._deserialize_by_tag(child, "SwAxisCont")
            obj.sw_axis_conts.append(sw_axis_conts_value)

        # Parse sw_value_cont
        child = ARObject._find_child_element(element, "SW-VALUE-CONT")
        if child is not None:
            sw_value_cont_value = ARObject._deserialize_by_tag(child, "SwValueCont")
            obj.sw_value_cont = sw_value_cont_value

        return obj



class ApplicationValueSpecificationBuilder:
    """Builder for ApplicationValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationValueSpecification = ApplicationValueSpecification()

    def build(self) -> ApplicationValueSpecification:
        """Build and return ApplicationValueSpecification object.

        Returns:
            ApplicationValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
