"""ApplicationArrayDataType AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_composite_data_type import (
    ApplicationCompositeDataType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class ApplicationArrayDataType(ApplicationCompositeDataType):
    """AUTOSAR ApplicationArrayDataType."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("dynamic_array", None, True, False, None),  # dynamicArray
        ("element", None, False, False, any (ApplicationArray)),  # element
    ]

    def __init__(self) -> None:
        """Initialize ApplicationArrayDataType."""
        super().__init__()
        self.dynamic_array: Optional[String] = None
        self.element: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ApplicationArrayDataType to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationArrayDataType":
        """Create ApplicationArrayDataType from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ApplicationArrayDataType instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ApplicationArrayDataType since parent returns ARObject
        return cast("ApplicationArrayDataType", obj)


class ApplicationArrayDataTypeBuilder:
    """Builder for ApplicationArrayDataType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationArrayDataType = ApplicationArrayDataType()

    def build(self) -> ApplicationArrayDataType:
        """Build and return ApplicationArrayDataType object.

        Returns:
            ApplicationArrayDataType instance
        """
        # TODO: Add validation
        return self._obj
