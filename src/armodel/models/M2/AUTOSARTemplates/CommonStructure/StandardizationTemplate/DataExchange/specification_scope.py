"""SpecificationScope AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchange.specification_document_scope import (
    SpecificationDocumentScope,
)


class SpecificationScope(ARObject):
    """AUTOSAR SpecificationScope."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("specification_documents", None, False, True, SpecificationDocumentScope),  # specificationDocuments
    ]

    def __init__(self) -> None:
        """Initialize SpecificationScope."""
        super().__init__()
        self.specification_documents: list[SpecificationDocumentScope] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SpecificationScope to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SpecificationScope":
        """Create SpecificationScope from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SpecificationScope instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SpecificationScope since parent returns ARObject
        return cast("SpecificationScope", obj)


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
