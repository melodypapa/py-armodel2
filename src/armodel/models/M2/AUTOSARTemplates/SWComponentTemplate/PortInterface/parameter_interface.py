"""ParameterInterface AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_interface import (
    DataInterface,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)


class ParameterInterface(DataInterface):
    """AUTOSAR ParameterInterface."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("parameters", None, False, True, ParameterDataPrototype),  # parameters
    ]

    def __init__(self) -> None:
        """Initialize ParameterInterface."""
        super().__init__()
        self.parameters: list[ParameterDataPrototype] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ParameterInterface to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ParameterInterface":
        """Create ParameterInterface from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ParameterInterface instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ParameterInterface since parent returns ARObject
        return cast("ParameterInterface", obj)


class ParameterInterfaceBuilder:
    """Builder for ParameterInterface."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ParameterInterface = ParameterInterface()

    def build(self) -> ParameterInterface:
        """Build and return ParameterInterface object.

        Returns:
            ParameterInterface instance
        """
        # TODO: Add validation
        return self._obj
