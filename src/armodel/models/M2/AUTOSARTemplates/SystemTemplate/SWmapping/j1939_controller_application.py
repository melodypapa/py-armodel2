"""J1939ControllerApplication AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "function_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # functionId
        "sw_component_prototype": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwComponentPrototype,
        ),  # swComponentPrototype
    }

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
