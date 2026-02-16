"""QueuedReceiverComSpec AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.receiver_com_spec import (
    ReceiverComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class QueuedReceiverComSpec(ReceiverComSpec):
    """AUTOSAR QueuedReceiverComSpec."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("queue_length", None, True, False, None),  # queueLength
    ]

    def __init__(self) -> None:
        """Initialize QueuedReceiverComSpec."""
        super().__init__()
        self.queue_length: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert QueuedReceiverComSpec to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "QueuedReceiverComSpec":
        """Create QueuedReceiverComSpec from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            QueuedReceiverComSpec instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to QueuedReceiverComSpec since parent returns ARObject
        return cast("QueuedReceiverComSpec", obj)


class QueuedReceiverComSpecBuilder:
    """Builder for QueuedReceiverComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: QueuedReceiverComSpec = QueuedReceiverComSpec()

    def build(self) -> QueuedReceiverComSpec:
        """Build and return QueuedReceiverComSpec object.

        Returns:
            QueuedReceiverComSpec instance
        """
        # TODO: Add validation
        return self._obj
