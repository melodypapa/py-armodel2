"""IPdu AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu import (
    Pdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.contained_i_pdu_props import (
    ContainedIPduProps,
)


class IPdu(Pdu):
    """AUTOSAR IPdu."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("contained_i_pdu_props", None, False, False, ContainedIPduProps),  # containedIPduProps
    ]

    def __init__(self) -> None:
        """Initialize IPdu."""
        super().__init__()
        self.contained_i_pdu_props: Optional[ContainedIPduProps] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IPdu to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IPdu":
        """Create IPdu from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IPdu instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IPdu since parent returns ARObject
        return cast("IPdu", obj)


class IPduBuilder:
    """Builder for IPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IPdu = IPdu()

    def build(self) -> IPdu:
        """Build and return IPdu object.

        Returns:
            IPdu instance
        """
        # TODO: Add validation
        return self._obj
