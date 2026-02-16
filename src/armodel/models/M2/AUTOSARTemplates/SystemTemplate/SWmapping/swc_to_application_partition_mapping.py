"""SwcToApplicationPartitionMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.application_partition import (
    ApplicationPartition,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_component_prototype import (
    SwComponentPrototype,
)


class SwcToApplicationPartitionMapping(Identifiable):
    """AUTOSAR SwcToApplicationPartitionMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("application", None, False, False, ApplicationPartition),  # application
        ("sw_component_prototype", None, False, False, SwComponentPrototype),  # swComponentPrototype
    ]

    def __init__(self) -> None:
        """Initialize SwcToApplicationPartitionMapping."""
        super().__init__()
        self.application: Optional[ApplicationPartition] = None
        self.sw_component_prototype: Optional[SwComponentPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwcToApplicationPartitionMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcToApplicationPartitionMapping":
        """Create SwcToApplicationPartitionMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwcToApplicationPartitionMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwcToApplicationPartitionMapping since parent returns ARObject
        return cast("SwcToApplicationPartitionMapping", obj)


class SwcToApplicationPartitionMappingBuilder:
    """Builder for SwcToApplicationPartitionMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcToApplicationPartitionMapping = SwcToApplicationPartitionMapping()

    def build(self) -> SwcToApplicationPartitionMapping:
        """Build and return SwcToApplicationPartitionMapping object.

        Returns:
            SwcToApplicationPartitionMapping instance
        """
        # TODO: Add validation
        return self._obj
