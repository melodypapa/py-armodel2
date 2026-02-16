"""LogAndTraceMessageCollectionSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_message import (
    DltMessage,
)


class LogAndTraceMessageCollectionSet(ARElement):
    """AUTOSAR LogAndTraceMessageCollectionSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("dlt_messages", None, False, True, DltMessage),  # dltMessages
    ]

    def __init__(self) -> None:
        """Initialize LogAndTraceMessageCollectionSet."""
        super().__init__()
        self.dlt_messages: list[DltMessage] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert LogAndTraceMessageCollectionSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LogAndTraceMessageCollectionSet":
        """Create LogAndTraceMessageCollectionSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            LogAndTraceMessageCollectionSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to LogAndTraceMessageCollectionSet since parent returns ARObject
        return cast("LogAndTraceMessageCollectionSet", obj)


class LogAndTraceMessageCollectionSetBuilder:
    """Builder for LogAndTraceMessageCollectionSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LogAndTraceMessageCollectionSet = LogAndTraceMessageCollectionSet()

    def build(self) -> LogAndTraceMessageCollectionSet:
        """Build and return LogAndTraceMessageCollectionSet object.

        Returns:
            LogAndTraceMessageCollectionSet instance
        """
        # TODO: Add validation
        return self._obj
