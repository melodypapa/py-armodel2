"""IEEE1722TpCrfConnection AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_av_connection import (
    IEEE1722TpAvConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class IEEE1722TpCrfConnection(IEEE1722TpAvConnection):
    """AUTOSAR IEEE1722TpCrfConnection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base_frequency", None, True, False, None),  # baseFrequency
        ("crf_pull_enum", None, False, False, IEEE1722TpCrfPullEnum),  # crfPullEnum
        ("crf_type_enum", None, False, False, IEEE1722TpCrfTypeEnum),  # crfTypeEnum
        ("frame_sync", None, True, False, None),  # frameSync
        ("timestamp", None, True, False, None),  # timestamp
    ]

    def __init__(self) -> None:
        """Initialize IEEE1722TpCrfConnection."""
        super().__init__()
        self.base_frequency: Optional[PositiveInteger] = None
        self.crf_pull_enum: Optional[IEEE1722TpCrfPullEnum] = None
        self.crf_type_enum: Optional[IEEE1722TpCrfTypeEnum] = None
        self.frame_sync: Optional[Boolean] = None
        self.timestamp: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IEEE1722TpCrfConnection to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpCrfConnection":
        """Create IEEE1722TpCrfConnection from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IEEE1722TpCrfConnection instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IEEE1722TpCrfConnection since parent returns ARObject
        return cast("IEEE1722TpCrfConnection", obj)


class IEEE1722TpCrfConnectionBuilder:
    """Builder for IEEE1722TpCrfConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpCrfConnection = IEEE1722TpCrfConnection()

    def build(self) -> IEEE1722TpCrfConnection:
        """Build and return IEEE1722TpCrfConnection object.

        Returns:
            IEEE1722TpCrfConnection instance
        """
        # TODO: Add validation
        return self._obj
