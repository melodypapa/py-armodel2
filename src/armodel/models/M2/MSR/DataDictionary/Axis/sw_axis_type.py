"""SwAxisType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 355)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_Axis.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.MSR.DataDictionary.Axis.sw_generic_axis_param import (
    SwGenericAxisParam,
)


class SwAxisType(ARElement):
    """AUTOSAR SwAxisType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sw_generic_axis: Optional[DocumentationBlock]
    sw_generic_axis_params: list[SwGenericAxisParam]
    def __init__(self) -> None:
        """Initialize SwAxisType."""
        super().__init__()
        self.sw_generic_axis: Optional[DocumentationBlock] = None
        self.sw_generic_axis_params: list[SwGenericAxisParam] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwAxisType":
        """Deserialize XML element to SwAxisType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwAxisType object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse sw_generic_axis
        child = ARObject._find_child_element(element, "SW-GENERIC-AXIS")
        if child is not None:
            sw_generic_axis_value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.sw_generic_axis = sw_generic_axis_value

        # Parse sw_generic_axis_params (list)
        obj.sw_generic_axis_params = []
        for child in ARObject._find_all_child_elements(element, "SW-GENERIC-AXIS-PARAMS"):
            sw_generic_axis_params_value = ARObject._deserialize_by_tag(child, "SwGenericAxisParam")
            obj.sw_generic_axis_params.append(sw_generic_axis_params_value)

        return obj



class SwAxisTypeBuilder:
    """Builder for SwAxisType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwAxisType = SwAxisType()

    def build(self) -> SwAxisType:
        """Build and return SwAxisType object.

        Returns:
            SwAxisType instance
        """
        # TODO: Add validation
        return self._obj
