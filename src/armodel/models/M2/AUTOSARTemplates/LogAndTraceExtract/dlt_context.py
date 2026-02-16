"""DltContext AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_message import (
    DltMessage,
)


class DltContext(ARElement):
    """AUTOSAR DltContext."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("context", None, True, False, None),  # context
        ("context_id", None, True, False, None),  # contextId
        ("dlt_messages", None, False, True, DltMessage),  # dltMessages
    ]

    def __init__(self) -> None:
        """Initialize DltContext."""
        super().__init__()
        self.context: Optional[String] = None
        self.context_id: Optional[String] = None
        self.dlt_messages: list[DltMessage] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DltContext to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DltContext":
        """Create DltContext from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DltContext instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DltContext since parent returns ARObject
        return cast("DltContext", obj)


class DltContextBuilder:
    """Builder for DltContext."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DltContext = DltContext()

    def build(self) -> DltContext:
        """Build and return DltContext object.

        Returns:
            DltContext instance
        """
        # TODO: Add validation
        return self._obj
