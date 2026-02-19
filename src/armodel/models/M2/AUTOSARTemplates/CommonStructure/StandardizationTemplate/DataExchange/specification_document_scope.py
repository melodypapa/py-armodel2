"""SpecificationDocumentScope AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 97)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchange.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.spec_element_reference import (
    SpecElementReference,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchange.document_element_scope import (
    DocumentElementScope,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1.documentation import (
    Documentation,
)


class SpecificationDocumentScope(SpecElementReference):
    """AUTOSAR SpecificationDocumentScope."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    custom_documentation: Optional[Documentation]
    documents: list[DocumentElementScope]
    def __init__(self) -> None:
        """Initialize SpecificationDocumentScope."""
        super().__init__()
        self.custom_documentation: Optional[Documentation] = None
        self.documents: list[DocumentElementScope] = []

    def serialize(self) -> ET.Element:
        """Serialize SpecificationDocumentScope to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SpecificationDocumentScope, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize custom_documentation
        if self.custom_documentation is not None:
            serialized = ARObject._serialize_item(self.custom_documentation, "Documentation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CUSTOM-DOCUMENTATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize documents (list to container "DOCUMENTS")
        if self.documents:
            wrapper = ET.Element("DOCUMENTS")
            for item in self.documents:
                serialized = ARObject._serialize_item(item, "DocumentElementScope")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SpecificationDocumentScope":
        """Deserialize XML element to SpecificationDocumentScope object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SpecificationDocumentScope object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SpecificationDocumentScope, cls).deserialize(element)

        # Parse custom_documentation
        child = ARObject._find_child_element(element, "CUSTOM-DOCUMENTATION")
        if child is not None:
            custom_documentation_value = ARObject._deserialize_by_tag(child, "Documentation")
            obj.custom_documentation = custom_documentation_value

        # Parse documents (list from container "DOCUMENTS")
        obj.documents = []
        container = ARObject._find_child_element(element, "DOCUMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.documents.append(child_value)

        return obj



class SpecificationDocumentScopeBuilder:
    """Builder for SpecificationDocumentScope."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SpecificationDocumentScope = SpecificationDocumentScope()

    def build(self) -> SpecificationDocumentScope:
        """Build and return SpecificationDocumentScope object.

        Returns:
            SpecificationDocumentScope instance
        """
        # TODO: Add validation
        return self._obj
