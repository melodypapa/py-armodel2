"""MsrQueryP1 AUTOSAR element.

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
from armodel.serialization import SerializationHelper
from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_props import (
    MsrQueryProps,
)
from armodel.models.M2.MSR.Documentation.Chapters.topic_content import (
    TopicContent,
)


class MsrQueryP1(Paginateable):
    """AUTOSAR MsrQueryP1."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    msr_query_props: MsrQueryProps
    msr_query_result: Optional[TopicContent]
    def __init__(self) -> None:
        """Initialize MsrQueryP1."""
        super().__init__()
        self.msr_query_props: MsrQueryProps = None
        self.msr_query_result: Optional[TopicContent] = None

    def serialize(self) -> ET.Element:
        """Serialize MsrQueryP1 to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MsrQueryP1, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize msr_query_props
        if self.msr_query_props is not None:
            serialized = SerializationHelper.serialize_item(self.msr_query_props, "MsrQueryProps")
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

        # Serialize msr_query_result
        if self.msr_query_result is not None:
            serialized = SerializationHelper.serialize_item(self.msr_query_result, "TopicContent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MSR-QUERY-RESULT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MsrQueryP1":
        """Deserialize XML element to MsrQueryP1 object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MsrQueryP1 object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MsrQueryP1, cls).deserialize(element)

        # Parse msr_query_props
        child = SerializationHelper.find_child_element(element, "MSR-QUERY-PROPS")
        if child is not None:
            msr_query_props_value = SerializationHelper.deserialize_by_tag(child, "MsrQueryProps")
            obj.msr_query_props = msr_query_props_value

        # Parse msr_query_result
        child = SerializationHelper.find_child_element(element, "MSR-QUERY-RESULT")
        if child is not None:
            msr_query_result_value = SerializationHelper.deserialize_by_tag(child, "TopicContent")
            obj.msr_query_result = msr_query_result_value

        return obj



class MsrQueryP1Builder:
    """Builder for MsrQueryP1."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MsrQueryP1 = MsrQueryP1()

    def build(self) -> MsrQueryP1:
        """Build and return MsrQueryP1 object.

        Returns:
            MsrQueryP1 instance
        """
        # TODO: Add validation
        return self._obj
