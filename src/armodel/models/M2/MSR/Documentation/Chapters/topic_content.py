"""TopicContent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable.table import (
    Table,
)


class TopicContent(ARObject):
    """AUTOSAR TopicContent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("block_level", None, False, False, DocumentationBlock),  # blockLevel
        ("table", None, False, False, Table),  # table
        ("traceable_table", None, False, False, any (TraceableTable)),  # traceableTable
    ]

    def __init__(self) -> None:
        """Initialize TopicContent."""
        super().__init__()
        self.block_level: DocumentationBlock = None
        self.table: Optional[Table] = None
        self.traceable_table: Any = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TopicContent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TopicContent":
        """Create TopicContent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TopicContent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TopicContent since parent returns ARObject
        return cast("TopicContent", obj)


class TopicContentBuilder:
    """Builder for TopicContent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TopicContent = TopicContent()

    def build(self) -> TopicContent:
        """Build and return TopicContent object.

        Returns:
            TopicContent instance
        """
        # TODO: Add validation
        return self._obj
