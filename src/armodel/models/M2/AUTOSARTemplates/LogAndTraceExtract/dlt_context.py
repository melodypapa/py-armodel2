"""DltContext AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2017)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 9)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_LogAndTraceExtract.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_message import (
    DltMessage,
)


class DltContext(ARElement):
    """AUTOSAR DltContext."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context: Optional[String]
    context_id: Optional[String]
    dlt_messages: list[DltMessage]
    def __init__(self) -> None:
        """Initialize DltContext."""
        super().__init__()
        self.context: Optional[String] = None
        self.context_id: Optional[String] = None
        self.dlt_messages: list[DltMessage] = []
    def serialize(self) -> ET.Element:
        """Serialize DltContext to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DltContext, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize context
        if self.context is not None:
            serialized = ARObject._serialize_item(self.context, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_id
        if self.context_id is not None:
            serialized = ARObject._serialize_item(self.context_id, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dlt_messages (list to container "DLT-MESSAGES")
        if self.dlt_messages:
            wrapper = ET.Element("DLT-MESSAGES")
            for item in self.dlt_messages:
                serialized = ARObject._serialize_item(item, "DltMessage")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DltContext":
        """Deserialize XML element to DltContext object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DltContext object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DltContext, cls).deserialize(element)

        # Parse context
        child = ARObject._find_child_element(element, "CONTEXT")
        if child is not None:
            context_value = child.text
            obj.context = context_value

        # Parse context_id
        child = ARObject._find_child_element(element, "CONTEXT-ID")
        if child is not None:
            context_id_value = child.text
            obj.context_id = context_id_value

        # Parse dlt_messages (list from container "DLT-MESSAGES")
        obj.dlt_messages = []
        container = ARObject._find_child_element(element, "DLT-MESSAGES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dlt_messages.append(child_value)

        return obj



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
