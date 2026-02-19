"""LabeledList AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 296)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_ListElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.indent_sample import (
    IndentSample,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.labeled_item import (
        LabeledItem,
    )



class LabeledList(Paginateable):
    """AUTOSAR LabeledList."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    indent_sample: Optional[IndentSample]
    labeled_item_label: LabeledItem
    def __init__(self) -> None:
        """Initialize LabeledList."""
        super().__init__()
        self.indent_sample: Optional[IndentSample] = None
        self.labeled_item_label: LabeledItem = None
    def serialize(self) -> ET.Element:
        """Serialize LabeledList to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LabeledList, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize indent_sample
        if self.indent_sample is not None:
            serialized = ARObject._serialize_item(self.indent_sample, "IndentSample")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INDENT-SAMPLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize labeled_item_label
        if self.labeled_item_label is not None:
            serialized = ARObject._serialize_item(self.labeled_item_label, "LabeledItem")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LABELED-ITEM-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LabeledList":
        """Deserialize XML element to LabeledList object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LabeledList object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LabeledList, cls).deserialize(element)

        # Parse indent_sample
        child = ARObject._find_child_element(element, "INDENT-SAMPLE")
        if child is not None:
            indent_sample_value = ARObject._deserialize_by_tag(child, "IndentSample")
            obj.indent_sample = indent_sample_value

        # Parse labeled_item_label
        child = ARObject._find_child_element(element, "LABELED-ITEM-LABEL")
        if child is not None:
            labeled_item_label_value = ARObject._deserialize_by_tag(child, "LabeledItem")
            obj.labeled_item_label = labeled_item_label_value

        return obj



class LabeledListBuilder:
    """Builder for LabeledList."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LabeledList = LabeledList()

    def build(self) -> LabeledList:
        """Build and return LabeledList object.

        Returns:
            LabeledList instance
        """
        # TODO: Add validation
        return self._obj
