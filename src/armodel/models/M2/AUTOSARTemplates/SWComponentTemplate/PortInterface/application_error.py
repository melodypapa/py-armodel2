"""ApplicationError AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class ApplicationError(Identifiable):
    """AUTOSAR ApplicationError."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("error_code", None, True, False, None),  # errorCode
    ]

    def __init__(self) -> None:
        """Initialize ApplicationError."""
        super().__init__()
        self.error_code: Optional[Integer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ApplicationError to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationError":
        """Create ApplicationError from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ApplicationError instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ApplicationError since parent returns ARObject
        return cast("ApplicationError", obj)


class ApplicationErrorBuilder:
    """Builder for ApplicationError."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationError = ApplicationError()

    def build(self) -> ApplicationError:
        """Build and return ApplicationError object.

        Returns:
            ApplicationError instance
        """
        # TODO: Add validation
        return self._obj
