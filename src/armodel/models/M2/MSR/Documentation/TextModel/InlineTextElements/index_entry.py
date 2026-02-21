"""IndexEntry AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 317)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import (
    Superscript,
)


class IndexEntry(ARObject):
    """AUTOSAR IndexEntry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sub: Superscript
    sup: Superscript
    def __init__(self) -> None:
        """Initialize IndexEntry."""
        super().__init__()
        self.sub: Superscript = None
        self.sup: Superscript = None

    def serialize(self) -> ET.Element:
        """Serialize IndexEntry to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IndexEntry, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sub
        if self.sub is not None:
            serialized = SerializationHelper.serialize_item(self.sub, "Superscript")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUB")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sup
        if self.sup is not None:
            serialized = SerializationHelper.serialize_item(self.sup, "Superscript")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IndexEntry":
        """Deserialize XML element to IndexEntry object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IndexEntry object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IndexEntry, cls).deserialize(element)

        # Parse sub
        child = SerializationHelper.find_child_element(element, "SUB")
        if child is not None:
            sub_value = child.text
            obj.sub = sub_value

        # Parse sup
        child = SerializationHelper.find_child_element(element, "SUP")
        if child is not None:
            sup_value = child.text
            obj.sup = sup_value

        return obj



class IndexEntryBuilder:
    """Builder for IndexEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IndexEntry = IndexEntry()

    def build(self) -> IndexEntry:
        """Build and return IndexEntry object.

        Returns:
            IndexEntry instance
        """
        # TODO: Add validation
        return self._obj
