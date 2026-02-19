"""TraceableText AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 178)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 313)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 222)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_RequirementsTracing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
        DocumentationBlock,
    )



class TraceableText(Paginateable):
    """AUTOSAR TraceableText."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    text: DocumentationBlock
    def __init__(self) -> None:
        """Initialize TraceableText."""
        super().__init__()
        self.text: DocumentationBlock = None
    def serialize(self) -> ET.Element:
        """Serialize TraceableText to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TraceableText, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize text
        if self.text is not None:
            serialized = ARObject._serialize_item(self.text, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TEXT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TraceableText":
        """Deserialize XML element to TraceableText object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TraceableText object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TraceableText, cls).deserialize(element)

        # Parse text
        child = ARObject._find_child_element(element, "TEXT")
        if child is not None:
            text_value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.text = text_value

        return obj



class TraceableTextBuilder:
    """Builder for TraceableText."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TraceableText = TraceableText()

    def build(self) -> TraceableText:
        """Build and return TraceableText object.

        Returns:
            TraceableText instance
        """
        # TODO: Add validation
        return self._obj
