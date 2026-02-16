"""IEEE1722TpIidcConnection AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_av_connection import (
    IEEE1722TpAvConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class IEEE1722TpIidcConnection(IEEE1722TpAvConnection):
    """AUTOSAR IEEE1722TpIidcConnection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("iidc_channel", None, True, False, None),  # iidcChannel
        ("iidc_data_block", None, True, False, None),  # iidcDataBlock
        ("iidc_fraction", None, True, False, None),  # iidcFraction
        ("iidc_source", None, True, False, None),  # iidcSource
        ("iidc_stream", None, True, False, None),  # iidcStream
        ("iidc_sy", None, True, False, None),  # iidcSy
        ("iidc_tag", None, True, False, None),  # iidcTag
        ("iidc_t_code", None, True, False, None),  # iidcTCode
    ]

    def __init__(self) -> None:
        """Initialize IEEE1722TpIidcConnection."""
        super().__init__()
        self.iidc_channel: Optional[PositiveInteger] = None
        self.iidc_data_block: Optional[PositiveInteger] = None
        self.iidc_fraction: Optional[PositiveInteger] = None
        self.iidc_source: Optional[Boolean] = None
        self.iidc_stream: Optional[PositiveInteger] = None
        self.iidc_sy: Optional[PositiveInteger] = None
        self.iidc_tag: Optional[PositiveInteger] = None
        self.iidc_t_code: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IEEE1722TpIidcConnection to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpIidcConnection":
        """Create IEEE1722TpIidcConnection from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IEEE1722TpIidcConnection instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IEEE1722TpIidcConnection since parent returns ARObject
        return cast("IEEE1722TpIidcConnection", obj)


class IEEE1722TpIidcConnectionBuilder:
    """Builder for IEEE1722TpIidcConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpIidcConnection = IEEE1722TpIidcConnection()

    def build(self) -> IEEE1722TpIidcConnection:
        """Build and return IEEE1722TpIidcConnection object.

        Returns:
            IEEE1722TpIidcConnection instance
        """
        # TODO: Add validation
        return self._obj
