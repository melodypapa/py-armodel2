"""PortGroup AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)


class PortGroup(Identifiable):
    """AUTOSAR PortGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "inner_groups": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=PortGroup,
        ),  # innerGroups
        "outer_ports": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=PortPrototype,
        ),  # outerPorts
    }

    def __init__(self) -> None:
        """Initialize PortGroup."""
        super().__init__()
        self.inner_groups: list[PortGroup] = []
        self.outer_ports: list[PortPrototype] = []


class PortGroupBuilder:
    """Builder for PortGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortGroup = PortGroup()

    def build(self) -> PortGroup:
        """Build and return PortGroup object.

        Returns:
            PortGroup instance
        """
        # TODO: Add validation
        return self._obj
