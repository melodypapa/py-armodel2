"""SpecificationScope AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 96)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchange.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchange.specification_document_scope import (
    SpecificationDocumentScope,
)


class SpecificationScope(ARObject):
    """AUTOSAR SpecificationScope."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    specification_documents: list[SpecificationDocumentScope]
    def __init__(self) -> None:
        """Initialize SpecificationScope."""
        super().__init__()
        self.specification_documents: list[SpecificationDocumentScope] = []
    def serialize(self) -> ET.Element:
        """Serialize SpecificationScope to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize specification_documents (list to container "SPECIFICATION-DOCUMENTS")
        if self.specification_documents:
            wrapper = ET.Element("SPECIFICATION-DOCUMENTS")
            for item in self.specification_documents:
                serialized = ARObject._serialize_item(item, "SpecificationDocumentScope")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SpecificationScope":
        """Deserialize XML element to SpecificationScope object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SpecificationScope object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse specification_documents (list from container "SPECIFICATION-DOCUMENTS")
        obj.specification_documents = []
        container = ARObject._find_child_element(element, "SPECIFICATION-DOCUMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.specification_documents.append(child_value)

        return obj



class SpecificationScopeBuilder:
    """Builder for SpecificationScope."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SpecificationScope = SpecificationScope()

    def build(self) -> SpecificationScope:
        """Build and return SpecificationScope object.

        Returns:
            SpecificationScope instance
        """
        # TODO: Add validation
        return self._obj
