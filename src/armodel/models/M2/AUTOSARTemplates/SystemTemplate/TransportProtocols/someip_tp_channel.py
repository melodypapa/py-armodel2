"""SomeipTpChannel AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class SomeipTpChannel(Identifiable):
    """AUTOSAR SomeipTpChannel."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("burst_size", None, True, False, None),  # burstSize
        ("rx_timeout_time", None, True, False, None),  # rxTimeoutTime
        ("separation_time", None, True, False, None),  # separationTime
    ]

    def __init__(self) -> None:
        """Initialize SomeipTpChannel."""
        super().__init__()
        self.burst_size: Optional[PositiveInteger] = None
        self.rx_timeout_time: Optional[TimeValue] = None
        self.separation_time: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SomeipTpChannel to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SomeipTpChannel":
        """Create SomeipTpChannel from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SomeipTpChannel instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SomeipTpChannel since parent returns ARObject
        return cast("SomeipTpChannel", obj)


class SomeipTpChannelBuilder:
    """Builder for SomeipTpChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SomeipTpChannel = SomeipTpChannel()

    def build(self) -> SomeipTpChannel:
        """Build and return SomeipTpChannel object.

        Returns:
            SomeipTpChannel instance
        """
        # TODO: Add validation
        return self._obj
