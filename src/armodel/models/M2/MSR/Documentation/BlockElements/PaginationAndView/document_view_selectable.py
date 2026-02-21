"""DocumentViewSelectable AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 340)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_PaginationAndView.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameTokens,
)
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import (
    ViewTokens,
)
from abc import ABC, abstractmethod


class DocumentViewSelectable(ARObject, ABC):
    """AUTOSAR DocumentViewSelectable."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    si: NameTokens
    view: Optional[ViewTokens]
    def __init__(self) -> None:
        """Initialize DocumentViewSelectable."""
        super().__init__()
        self.si: NameTokens = None
        self.view: Optional[ViewTokens] = None

    def serialize(self) -> ET.Element:
        """Serialize DocumentViewSelectable to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DocumentViewSelectable, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize si
        if self.si is not None:
            serialized = SerializationHelper.serialize_item(self.si, "NameTokens")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SI")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize view
        if self.view is not None:
            serialized = SerializationHelper.serialize_item(self.view, "ViewTokens")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VIEW")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DocumentViewSelectable":
        """Deserialize XML element to DocumentViewSelectable object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DocumentViewSelectable object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DocumentViewSelectable, cls).deserialize(element)

        # Parse si
        child = SerializationHelper.find_child_element(element, "SI")
        if child is not None:
            si_value = child.text
            obj.si = si_value

        # Parse view
        child = SerializationHelper.find_child_element(element, "VIEW")
        if child is not None:
            view_value = child.text
            obj.view = view_value

        return obj



class DocumentViewSelectableBuilder:
    """Builder for DocumentViewSelectable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DocumentViewSelectable = DocumentViewSelectable()

    def build(self) -> DocumentViewSelectable:
        """Build and return DocumentViewSelectable object.

        Returns:
            DocumentViewSelectable instance
        """
        # TODO: Add validation
        return self._obj
