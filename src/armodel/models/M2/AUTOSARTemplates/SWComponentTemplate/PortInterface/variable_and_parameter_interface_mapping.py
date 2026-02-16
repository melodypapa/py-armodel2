"""VariableAndParameterInterfaceMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import (
    PortInterfaceMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_prototype_mapping import (
    DataPrototypeMapping,
)


class VariableAndParameterInterfaceMapping(PortInterfaceMapping):
    """AUTOSAR VariableAndParameterInterfaceMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_mappings", None, False, True, DataPrototypeMapping),  # dataMappings
    ]

    def __init__(self) -> None:
        """Initialize VariableAndParameterInterfaceMapping."""
        super().__init__()
        self.data_mappings: list[DataPrototypeMapping] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert VariableAndParameterInterfaceMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "VariableAndParameterInterfaceMapping":
        """Create VariableAndParameterInterfaceMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            VariableAndParameterInterfaceMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to VariableAndParameterInterfaceMapping since parent returns ARObject
        return cast("VariableAndParameterInterfaceMapping", obj)


class VariableAndParameterInterfaceMappingBuilder:
    """Builder for VariableAndParameterInterfaceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VariableAndParameterInterfaceMapping = VariableAndParameterInterfaceMapping()

    def build(self) -> VariableAndParameterInterfaceMapping:
        """Build and return VariableAndParameterInterfaceMapping object.

        Returns:
            VariableAndParameterInterfaceMapping instance
        """
        # TODO: Add validation
        return self._obj
