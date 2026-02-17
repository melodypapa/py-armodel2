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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_component_prototype import (
    SwComponentPrototype,
)


class J1939ControllerApplication(ARElement):
    """AUTOSAR J1939ControllerApplication."""

    function_id: Optional[PositiveInteger]
    sw_component_prototype: Optional[SwComponentPrototype]
    def __init__(self) -> None:
        """Initialize J1939ControllerApplication."""
        super().__init__()
        self.function_id: Optional[PositiveInteger] = None
        self.sw_component_prototype: Optional[SwComponentPrototype] = None


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
