"""DocumentElementScope AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 97)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchange.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.spec_element_reference import (
    SpecElementReference,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DocumentElementScope(SpecElementReference):
    """AUTOSAR DocumentElementScope."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    custom_document: Optional[Any]
    tailorings: list[Any]
    def __init__(self) -> None:
        """Initialize DocumentElementScope."""
        super().__init__()
        self.custom_document: Optional[Any] = None
        self.tailorings: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize DocumentElementScope to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DocumentElementScope, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize custom_document
        if self.custom_document is not None:
            serialized = ARObject._serialize_item(self.custom_document, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CUSTOM-DOCUMENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tailorings (list to container "TAILORINGS")
        if self.tailorings:
            wrapper = ET.Element("TAILORINGS")
            for item in self.tailorings:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DocumentElementScope":
        """Deserialize XML element to DocumentElementScope object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DocumentElementScope object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DocumentElementScope, cls).deserialize(element)

        # Parse custom_document
        child = ARObject._find_child_element(element, "CUSTOM-DOCUMENT")
        if child is not None:
            custom_document_value = child.text
            obj.custom_document = custom_document_value

        # Parse tailorings (list from container "TAILORINGS")
        obj.tailorings = []
        container = ARObject._find_child_element(element, "TAILORINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tailorings.append(child_value)

        return obj



class DocumentElementScopeBuilder:
    """Builder for DocumentElementScope."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DocumentElementScope = DocumentElementScope()

    def build(self) -> DocumentElementScope:
        """Build and return DocumentElementScope object.

        Returns:
            DocumentElementScope instance
        """
        # TODO: Add validation
        return self._obj
