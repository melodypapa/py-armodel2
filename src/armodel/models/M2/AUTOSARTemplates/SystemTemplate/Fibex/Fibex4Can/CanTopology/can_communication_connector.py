"""CanCommunicationConnector AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.abstract_can_communication_connector import (
    AbstractCanCommunicationConnector,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    PositiveUnlimitedInteger,
)


class CanCommunicationConnector(AbstractCanCommunicationConnector):
    """AUTOSAR CanCommunicationConnector."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("pnc_wakeup_can", None, True, False, None),  # pncWakeupCan
        ("pnc_wakeup", None, True, False, None),  # pncWakeup
        ("pnc_wakeup_dlc", None, True, False, None),  # pncWakeupDlc
    ]

    def __init__(self) -> None:
        """Initialize CanCommunicationConnector."""
        super().__init__()
        self.pnc_wakeup_can: Optional[PositiveInteger] = None
        self.pnc_wakeup: Optional[PositiveUnlimitedInteger] = None
        self.pnc_wakeup_dlc: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CanCommunicationConnector to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanCommunicationConnector":
        """Create CanCommunicationConnector from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CanCommunicationConnector instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CanCommunicationConnector since parent returns ARObject
        return cast("CanCommunicationConnector", obj)


class CanCommunicationConnectorBuilder:
    """Builder for CanCommunicationConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanCommunicationConnector = CanCommunicationConnector()

    def build(self) -> CanCommunicationConnector:
        """Build and return CanCommunicationConnector object.

        Returns:
            CanCommunicationConnector instance
        """
        # TODO: Add validation
        return self._obj
