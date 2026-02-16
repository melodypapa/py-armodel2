"""TDEventBswInternalBehavior AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import (
    BswModuleEntity,
)


class TDEventBswInternalBehavior(TimingDescriptionEvent):
    """AUTOSAR TDEventBswInternalBehavior."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("bsw_module_entity_entity", None, False, False, BswModuleEntity),  # bswModuleEntityEntity
        ("td_event_bsw_behavior_type", None, False, False, any (TDEventBswInternal)),  # tdEventBswBehaviorType
    ]

    def __init__(self) -> None:
        """Initialize TDEventBswInternalBehavior."""
        super().__init__()
        self.bsw_module_entity_entity: Optional[BswModuleEntity] = None
        self.td_event_bsw_behavior_type: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDEventBswInternalBehavior to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventBswInternalBehavior":
        """Create TDEventBswInternalBehavior from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDEventBswInternalBehavior instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDEventBswInternalBehavior since parent returns ARObject
        return cast("TDEventBswInternalBehavior", obj)


class TDEventBswInternalBehaviorBuilder:
    """Builder for TDEventBswInternalBehavior."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventBswInternalBehavior = TDEventBswInternalBehavior()

    def build(self) -> TDEventBswInternalBehavior:
        """Build and return TDEventBswInternalBehavior object.

        Returns:
            TDEventBswInternalBehavior instance
        """
        # TODO: Add validation
        return self._obj
