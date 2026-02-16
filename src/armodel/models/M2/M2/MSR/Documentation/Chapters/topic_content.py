"""TopicContent AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "block_level": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=DocumentationBlock,
        ),  # blockLevel
        "table": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Table,
        ),  # table
        "traceable_table": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=any (TraceableTable),
        ),  # traceableTable
    }

    def __init__(self) -> None:
        """Initialize TopicContent."""
        super().__init__()
        self.block_level: DocumentationBlock = None
        self.table: Optional[Table] = None
        self.traceable_table: Any = None


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
