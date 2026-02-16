"""VariableAndParameterInterfaceMapping AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import (
    PortInterfaceMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_prototype_mapping import (
    DataPrototypeMapping,
)


class VariableAndParameterInterfaceMapping(PortInterfaceMapping):
    """AUTOSAR VariableAndParameterInterfaceMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "data_mappings": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DataPrototypeMapping,
        ),  # dataMappings
    }

    def __init__(self) -> None:
        """Initialize VariableAndParameterInterfaceMapping."""
        super().__init__()
        self.data_mappings: list[DataPrototypeMapping] = []


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
