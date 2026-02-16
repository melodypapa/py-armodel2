"""RunnableEntityGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.runnable_entity import (
    RunnableEntity,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.runnable_entity_group import (
    RunnableEntityGroup,
)


class RunnableEntityGroup(Identifiable):
    """AUTOSAR RunnableEntityGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("runnable_entities", None, False, True, RunnableEntity),  # runnableEntities
        ("runnable_entity_group_group_in_composition_instance_refs", None, False, True, RunnableEntityGroup),  # runnableEntityGroupGroupInCompositionInstanceRefs
    ]

    def __init__(self) -> None:
        """Initialize RunnableEntityGroup."""
        super().__init__()
        self.runnable_entities: list[RunnableEntity] = []
        self.runnable_entity_group_group_in_composition_instance_refs: list[RunnableEntityGroup] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RunnableEntityGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RunnableEntityGroup":
        """Create RunnableEntityGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RunnableEntityGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RunnableEntityGroup since parent returns ARObject
        return cast("RunnableEntityGroup", obj)


class RunnableEntityGroupBuilder:
    """Builder for RunnableEntityGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RunnableEntityGroup = RunnableEntityGroup()

    def build(self) -> RunnableEntityGroup:
        """Build and return RunnableEntityGroup object.

        Returns:
            RunnableEntityGroup instance
        """
        # TODO: Add validation
        return self._obj
