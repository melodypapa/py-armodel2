"""MsrQueryChapter AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 343)

JSON Source: docs/json/packages/M2_MSR_Documentation_MsrQuery.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_props import (
    MsrQueryProps,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_result_chapter import (
        MsrQueryResultChapter,
    )



class MsrQueryChapter(Paginateable):
    """AUTOSAR MsrQueryChapter."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    msr_query_props: MsrQueryProps
    msr_query_result_chapter: Optional[MsrQueryResultChapter]
    def __init__(self) -> None:
        """Initialize MsrQueryChapter."""
        super().__init__()
        self.msr_query_props: MsrQueryProps = None
        self.msr_query_result_chapter: Optional[MsrQueryResultChapter] = None

    def serialize(self) -> ET.Element:
        """Serialize MsrQueryChapter to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MsrQueryChapter, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize msr_query_props
        if self.msr_query_props is not None:
            serialized = ARObject._serialize_item(self.msr_query_props, "MsrQueryProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MSR-QUERY-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize msr_query_result_chapter
        if self.msr_query_result_chapter is not None:
            serialized = ARObject._serialize_item(self.msr_query_result_chapter, "MsrQueryResultChapter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MSR-QUERY-RESULT-CHAPTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MsrQueryChapter":
        """Deserialize XML element to MsrQueryChapter object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MsrQueryChapter object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MsrQueryChapter, cls).deserialize(element)

        # Parse msr_query_props
        child = ARObject._find_child_element(element, "MSR-QUERY-PROPS")
        if child is not None:
            msr_query_props_value = ARObject._deserialize_by_tag(child, "MsrQueryProps")
            obj.msr_query_props = msr_query_props_value

        # Parse msr_query_result_chapter
        child = ARObject._find_child_element(element, "MSR-QUERY-RESULT-CHAPTER")
        if child is not None:
            msr_query_result_chapter_value = ARObject._deserialize_by_tag(child, "MsrQueryResultChapter")
            obj.msr_query_result_chapter = msr_query_result_chapter_value

        return obj



class MsrQueryChapterBuilder:
    """Builder for MsrQueryChapter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MsrQueryChapter = MsrQueryChapter()

    def build(self) -> MsrQueryChapter:
        """Build and return MsrQueryChapter object.

        Returns:
            MsrQueryChapter instance
        """
        # TODO: Add validation
        return self._obj
