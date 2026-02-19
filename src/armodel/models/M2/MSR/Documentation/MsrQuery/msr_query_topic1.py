"""MsrQueryTopic1 AUTOSAR element.

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
from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_result_topic1 import (
    MsrQueryResultTopic1,
)


class MsrQueryTopic1(Paginateable):
    """AUTOSAR MsrQueryTopic1."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    msr_query_props: MsrQueryProps
    msr_query_result_topic1: Optional[MsrQueryResultTopic1]
    def __init__(self) -> None:
        """Initialize MsrQueryTopic1."""
        super().__init__()
        self.msr_query_props: MsrQueryProps = None
        self.msr_query_result_topic1: Optional[MsrQueryResultTopic1] = None
    def serialize(self) -> ET.Element:
        """Serialize MsrQueryTopic1 to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MsrQueryTopic1, self).serialize()

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

        # Serialize msr_query_result_topic1
        if self.msr_query_result_topic1 is not None:
            serialized = ARObject._serialize_item(self.msr_query_result_topic1, "MsrQueryResultTopic1")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MSR-QUERY-RESULT-TOPIC1")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MsrQueryTopic1":
        """Deserialize XML element to MsrQueryTopic1 object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MsrQueryTopic1 object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MsrQueryTopic1, cls).deserialize(element)

        # Parse msr_query_props
        child = ARObject._find_child_element(element, "MSR-QUERY-PROPS")
        if child is not None:
            msr_query_props_value = ARObject._deserialize_by_tag(child, "MsrQueryProps")
            obj.msr_query_props = msr_query_props_value

        # Parse msr_query_result_topic1
        child = ARObject._find_child_element(element, "MSR-QUERY-RESULT-TOPIC1")
        if child is not None:
            msr_query_result_topic1_value = ARObject._deserialize_by_tag(child, "MsrQueryResultTopic1")
            obj.msr_query_result_topic1 = msr_query_result_topic1_value

        return obj



class MsrQueryTopic1Builder:
    """Builder for MsrQueryTopic1."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MsrQueryTopic1 = MsrQueryTopic1()

    def build(self) -> MsrQueryTopic1:
        """Build and return MsrQueryTopic1 object.

        Returns:
            MsrQueryTopic1 instance
        """
        # TODO: Add validation
        return self._obj
