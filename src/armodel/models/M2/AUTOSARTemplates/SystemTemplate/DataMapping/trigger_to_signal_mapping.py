"""TriggerToSignalMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.data_mapping import (
    DataMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class TriggerToSignalMapping(DataMapping):
    """AUTOSAR TriggerToSignalMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("system_signal", None, False, False, SystemSignal),  # systemSignal
        ("trigger", None, False, False, Trigger),  # trigger
    ]

    def __init__(self) -> None:
        """Initialize TriggerToSignalMapping."""
        super().__init__()
        self.system_signal: Optional[SystemSignal] = None
        self.trigger: Optional[Trigger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TriggerToSignalMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TriggerToSignalMapping":
        """Create TriggerToSignalMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TriggerToSignalMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TriggerToSignalMapping since parent returns ARObject
        return cast("TriggerToSignalMapping", obj)


class TriggerToSignalMappingBuilder:
    """Builder for TriggerToSignalMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TriggerToSignalMapping = TriggerToSignalMapping()

    def build(self) -> TriggerToSignalMapping:
        """Build and return TriggerToSignalMapping object.

        Returns:
            TriggerToSignalMapping instance
        """
        # TODO: Add validation
        return self._obj
