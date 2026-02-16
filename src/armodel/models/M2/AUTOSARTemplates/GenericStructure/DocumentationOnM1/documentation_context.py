"""DocumentationContext AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.multilanguage_referrable import (
    MultilanguageReferrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class DocumentationContext(MultilanguageReferrable):
    """AUTOSAR DocumentationContext."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("feature", None, False, False, AtpFeature),  # feature
        ("identifiable", None, False, False, Identifiable),  # identifiable
    ]

    def __init__(self) -> None:
        """Initialize DocumentationContext."""
        super().__init__()
        self.feature: Optional[AtpFeature] = None
        self.identifiable: Optional[Identifiable] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DocumentationContext to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DocumentationContext":
        """Create DocumentationContext from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DocumentationContext instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DocumentationContext since parent returns ARObject
        return cast("DocumentationContext", obj)


class DocumentationContextBuilder:
    """Builder for DocumentationContext."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DocumentationContext = DocumentationContext()

    def build(self) -> DocumentationContext:
        """Build and return DocumentationContext object.

        Returns:
            DocumentationContext instance
        """
        # TODO: Add validation
        return self._obj
