"""ModeInterfaceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 130)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import (
    PortInterfaceMapping,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeInterfaceMapping(PortInterfaceMapping):
    """AUTOSAR ModeInterfaceMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "mode_mapping": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ModeDeclarationGroup,
        ),  # modeMapping
    }

    def __init__(self) -> None:
        """Initialize ModeInterfaceMapping."""
        super().__init__()
        self.mode_mapping: Optional[ModeDeclarationGroup] = None


class ModeInterfaceMappingBuilder:
    """Builder for ModeInterfaceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeInterfaceMapping = ModeInterfaceMapping()

    def build(self) -> ModeInterfaceMapping:
        """Build and return ModeInterfaceMapping object.

        Returns:
            ModeInterfaceMapping instance
        """
        # TODO: Add validation
        return self._obj
