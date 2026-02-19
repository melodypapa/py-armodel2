"""J1939ControllerApplication AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 207)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_component_prototype import (
    SwComponentPrototype,
)


class J1939ControllerApplication(ARElement):
    """AUTOSAR J1939ControllerApplication."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    function_id: Optional[PositiveInteger]
    sw_component_prototype_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize J1939ControllerApplication."""
        super().__init__()
        self.function_id: Optional[PositiveInteger] = None
        self.sw_component_prototype_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939ControllerApplication":
        """Deserialize XML element to J1939ControllerApplication object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939ControllerApplication object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse function_id
        child = ARObject._find_child_element(element, "FUNCTION-ID")
        if child is not None:
            function_id_value = child.text
            obj.function_id = function_id_value

        # Parse sw_component_prototype_ref
        child = ARObject._find_child_element(element, "SW-COMPONENT-PROTOTYPE")
        if child is not None:
            sw_component_prototype_ref_value = ARObject._deserialize_by_tag(child, "SwComponentPrototype")
            obj.sw_component_prototype_ref = sw_component_prototype_ref_value

        return obj



class J1939ControllerApplicationBuilder:
    """Builder for J1939ControllerApplication."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939ControllerApplication = J1939ControllerApplication()

    def build(self) -> J1939ControllerApplication:
        """Build and return J1939ControllerApplication object.

        Returns:
            J1939ControllerApplication instance
        """
        # TODO: Add validation
        return self._obj
