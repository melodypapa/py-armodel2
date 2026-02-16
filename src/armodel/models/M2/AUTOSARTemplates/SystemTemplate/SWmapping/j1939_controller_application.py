"""J1939ControllerApplication AUTOSAR element."""

from typing import Optional, cast
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("function_id", None, True, False, None),  # functionId
        ("sw_component_prototype", None, False, False, SwComponentPrototype),  # swComponentPrototype
    ]

    def __init__(self) -> None:
        """Initialize J1939ControllerApplication."""
        super().__init__()
        self.function_id: Optional[PositiveInteger] = None
        self.sw_component_prototype: Optional[SwComponentPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert J1939ControllerApplication to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939ControllerApplication":
        """Create J1939ControllerApplication from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            J1939ControllerApplication instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to J1939ControllerApplication since parent returns ARObject
        return cast("J1939ControllerApplication", obj)


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
