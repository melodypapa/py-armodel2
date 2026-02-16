"""QueuedSenderComSpec AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.sender_com_spec import (
    SenderComSpec,
)


class QueuedSenderComSpec(SenderComSpec):
    """AUTOSAR QueuedSenderComSpec."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize QueuedSenderComSpec."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert QueuedSenderComSpec to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "QueuedSenderComSpec":
        """Create QueuedSenderComSpec from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            QueuedSenderComSpec instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to QueuedSenderComSpec since parent returns ARObject
        return cast("QueuedSenderComSpec", obj)


class QueuedSenderComSpecBuilder:
    """Builder for QueuedSenderComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: QueuedSenderComSpec = QueuedSenderComSpec()

    def build(self) -> QueuedSenderComSpec:
        """Build and return QueuedSenderComSpec object.

        Returns:
            QueuedSenderComSpec instance
        """
        # TODO: Add validation
        return self._obj
