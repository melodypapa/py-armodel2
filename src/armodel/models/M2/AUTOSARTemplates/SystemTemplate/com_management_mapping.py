"""ComManagementMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_group import (
    PortGroup,
)


class ComManagementMapping(Identifiable):
    """AUTOSAR ComManagementMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("coms", None, False, True, PortGroup),  # coms
        ("physical_channels", None, False, True, PhysicalChannel),  # physicalChannels
    ]

    def __init__(self) -> None:
        """Initialize ComManagementMapping."""
        super().__init__()
        self.coms: list[PortGroup] = []
        self.physical_channels: list[PhysicalChannel] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ComManagementMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ComManagementMapping":
        """Create ComManagementMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ComManagementMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ComManagementMapping since parent returns ARObject
        return cast("ComManagementMapping", obj)


class ComManagementMappingBuilder:
    """Builder for ComManagementMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ComManagementMapping = ComManagementMapping()

    def build(self) -> ComManagementMapping:
        """Build and return ComManagementMapping object.

        Returns:
            ComManagementMapping instance
        """
        # TODO: Add validation
        return self._obj
