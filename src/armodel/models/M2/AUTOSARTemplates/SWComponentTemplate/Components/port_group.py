"""PortGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_group import (
    PortGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)


class PortGroup(Identifiable):
    """AUTOSAR PortGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("inner_groups", None, False, True, PortGroup),  # innerGroups
        ("outer_ports", None, False, True, PortPrototype),  # outerPorts
    ]

    def __init__(self) -> None:
        """Initialize PortGroup."""
        super().__init__()
        self.inner_groups: list[PortGroup] = []
        self.outer_ports: list[PortPrototype] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PortGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortGroup":
        """Create PortGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PortGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PortGroup since parent returns ARObject
        return cast("PortGroup", obj)


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
