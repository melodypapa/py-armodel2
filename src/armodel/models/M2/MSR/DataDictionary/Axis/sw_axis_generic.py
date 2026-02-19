"""SwAxisGeneric AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 355)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_Axis.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.DataDictionary.Axis.sw_axis_type import (
    SwAxisType,
)
from armodel.models.M2.MSR.DataDictionary.Axis.sw_generic_axis_param import (
    SwGenericAxisParam,
)


class SwAxisGeneric(ARObject):
    """AUTOSAR SwAxisGeneric."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sw_axis_type: Optional[SwAxisType]
    sw_generic_axis_params: list[SwGenericAxisParam]
    def __init__(self) -> None:
        """Initialize SwAxisGeneric."""
        super().__init__()
        self.sw_axis_type: Optional[SwAxisType] = None
        self.sw_generic_axis_params: list[SwGenericAxisParam] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwAxisGeneric":
        """Deserialize XML element to SwAxisGeneric object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwAxisGeneric object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse sw_axis_type
        child = ARObject._find_child_element(element, "SW-AXIS-TYPE")
        if child is not None:
            sw_axis_type_value = ARObject._deserialize_by_tag(child, "SwAxisType")
            obj.sw_axis_type = sw_axis_type_value

        # Parse sw_generic_axis_params (list from container "SW-GENERIC-AXIS-PARAMS")
        obj.sw_generic_axis_params = []
        container = ARObject._find_child_element(element, "SW-GENERIC-AXIS-PARAMS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_generic_axis_params.append(child_value)

        return obj



class SwAxisGenericBuilder:
    """Builder for SwAxisGeneric."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwAxisGeneric = SwAxisGeneric()

    def build(self) -> SwAxisGeneric:
        """Build and return SwAxisGeneric object.

        Returns:
            SwAxisGeneric instance
        """
        # TODO: Add validation
        return self._obj
