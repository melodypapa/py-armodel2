"""IEEE1722TpAcfLin AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus import (
    IEEE1722TpAcfBus,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class IEEE1722TpAcfLin(IEEE1722TpAcfBus):
    """AUTOSAR IEEE1722TpAcfLin."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base_frequency", None, True, False, None),  # baseFrequency
        ("frame_sync_enabled", None, True, False, None),  # frameSyncEnabled
        ("timestamp", None, True, False, None),  # timestamp
    ]

    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfLin."""
        super().__init__()
        self.base_frequency: Optional[PositiveInteger] = None
        self.frame_sync_enabled: Optional[Boolean] = None
        self.timestamp: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IEEE1722TpAcfLin to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAcfLin":
        """Create IEEE1722TpAcfLin from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IEEE1722TpAcfLin instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IEEE1722TpAcfLin since parent returns ARObject
        return cast("IEEE1722TpAcfLin", obj)


class IEEE1722TpAcfLinBuilder:
    """Builder for IEEE1722TpAcfLin."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpAcfLin = IEEE1722TpAcfLin()

    def build(self) -> IEEE1722TpAcfLin:
        """Build and return IEEE1722TpAcfLin object.

        Returns:
            IEEE1722TpAcfLin instance
        """
        # TODO: Add validation
        return self._obj
