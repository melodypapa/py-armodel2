"""BswEvent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.abstract_event import (
    AbstractEvent,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_distinguished_partition import (
    BswDistinguishedPartition,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import (
    BswModuleEntity,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class BswEvent(AbstractEvent):
    """AUTOSAR BswEvent."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("contexts", None, False, True, BswDistinguishedPartition),  # contexts
        ("disabled_in_mode_description_instance_refs", None, False, True, ModeDeclaration),  # disabledInModeDescriptionInstanceRefs
        ("starts_on_event", None, False, False, BswModuleEntity),  # startsOnEvent
    ]

    def __init__(self) -> None:
        """Initialize BswEvent."""
        super().__init__()
        self.contexts: list[BswDistinguishedPartition] = []
        self.disabled_in_mode_description_instance_refs: list[ModeDeclaration] = []
        self.starts_on_event: Optional[BswModuleEntity] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswEvent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswEvent":
        """Create BswEvent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswEvent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswEvent since parent returns ARObject
        return cast("BswEvent", obj)


class BswEventBuilder:
    """Builder for BswEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswEvent = BswEvent()

    def build(self) -> BswEvent:
        """Build and return BswEvent object.

        Returns:
            BswEvent instance
        """
        # TODO: Add validation
        return self._obj
