"""DiagnosticComControlSubNodeChannel AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class DiagnosticComControlSubNodeChannel(ARObject):
    """AUTOSAR DiagnosticComControlSubNodeChannel."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("sub_node", None, False, False, any (EthernetPhysical)),  # subNode
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticComControlSubNodeChannel."""
        super().__init__()
        self.sub_node: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticComControlSubNodeChannel to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticComControlSubNodeChannel":
        """Create DiagnosticComControlSubNodeChannel from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticComControlSubNodeChannel instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticComControlSubNodeChannel since parent returns ARObject
        return cast("DiagnosticComControlSubNodeChannel", obj)


class DiagnosticComControlSubNodeChannelBuilder:
    """Builder for DiagnosticComControlSubNodeChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticComControlSubNodeChannel = DiagnosticComControlSubNodeChannel()

    def build(self) -> DiagnosticComControlSubNodeChannel:
        """Build and return DiagnosticComControlSubNodeChannel object.

        Returns:
            DiagnosticComControlSubNodeChannel instance
        """
        # TODO: Add validation
        return self._obj
