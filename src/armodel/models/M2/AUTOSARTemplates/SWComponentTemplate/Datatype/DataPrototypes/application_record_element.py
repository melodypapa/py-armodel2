"""ApplicationRecordElement AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.application_composite_element_data_prototype import (
    ApplicationCompositeElementDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class ApplicationRecordElement(ApplicationCompositeElementDataPrototype):
    """AUTOSAR ApplicationRecordElement."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("is_optional", None, True, False, None),  # isOptional
    ]

    def __init__(self) -> None:
        """Initialize ApplicationRecordElement."""
        super().__init__()
        self.is_optional: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ApplicationRecordElement to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationRecordElement":
        """Create ApplicationRecordElement from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ApplicationRecordElement instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ApplicationRecordElement since parent returns ARObject
        return cast("ApplicationRecordElement", obj)


class ApplicationRecordElementBuilder:
    """Builder for ApplicationRecordElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationRecordElement = ApplicationRecordElement()

    def build(self) -> ApplicationRecordElement:
        """Build and return ApplicationRecordElement object.

        Returns:
            ApplicationRecordElement instance
        """
        # TODO: Add validation
        return self._obj
