"""IPduTiming AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class IPduTiming(Describable):
    """AUTOSAR IPduTiming."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("minimum_delay", None, True, False, None),  # minimumDelay
        ("transmission", None, False, False, any (TransmissionMode)),  # transmission
    ]

    def __init__(self) -> None:
        """Initialize IPduTiming."""
        super().__init__()
        self.minimum_delay: Optional[TimeValue] = None
        self.transmission: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IPduTiming to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IPduTiming":
        """Create IPduTiming from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IPduTiming instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IPduTiming since parent returns ARObject
        return cast("IPduTiming", obj)


class IPduTimingBuilder:
    """Builder for IPduTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IPduTiming = IPduTiming()

    def build(self) -> IPduTiming:
        """Build and return IPduTiming object.

        Returns:
            IPduTiming instance
        """
        # TODO: Add validation
        return self._obj
