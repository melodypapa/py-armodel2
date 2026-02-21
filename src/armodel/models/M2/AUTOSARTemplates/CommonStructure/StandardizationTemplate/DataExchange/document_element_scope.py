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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef


class DocumentElementScope(SpecElementReference):
    """AUTOSAR DocumentElementScope."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    custom_document_ref: Optional[Any]
    tailoring_refs: list[Any]
    def __init__(self) -> None:
        """Initialize DocumentElementScope."""
        super().__init__()
        self.custom_document_ref: Optional[Any] = None
        self.tailoring_refs: list[Any] = []

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

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize custom_document_ref
        if self.custom_document_ref is not None:
            serialized = ARObject._serialize_item(self.custom_document_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CUSTOM-DOCUMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tailoring_refs (list to container "TAILORING-REFS")
        if self.tailoring_refs:
            wrapper = ET.Element("TAILORING-REFS")
            for item in self.tailoring_refs:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("TAILORING-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
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

        # Parse custom_document_ref
        child = ARObject._find_child_element(element, "CUSTOM-DOCUMENT-REF")
        if child is not None:
            custom_document_ref_value = ARRef.deserialize(child)
            obj.custom_document_ref = custom_document_ref_value

        # Parse tailoring_refs (list from container "TAILORING-REFS")
        obj.tailoring_refs = []
        container = ARObject._find_child_element(element, "TAILORING-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tailoring_refs.append(child_value)

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
