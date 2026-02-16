"""ApplicationArrayElement AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.application_composite_element_data_prototype import (
    ApplicationCompositeElementDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_primitive_data_type import (
    ApplicationPrimitiveDataType,
)


class ApplicationArrayElement(ApplicationCompositeElementDataPrototype):
    """AUTOSAR ApplicationArrayElement."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("array_size_handling", None, False, False, ArraySizeHandlingEnum),  # arraySizeHandling
        ("array_size", None, False, False, ArraySizeSemanticsEnum),  # arraySize
        ("index_data_type", None, False, False, ApplicationPrimitiveDataType),  # indexDataType
        ("max_number_of", None, True, False, None),  # maxNumberOf
    ]

    def __init__(self) -> None:
        """Initialize ApplicationArrayElement."""
        super().__init__()
        self.array_size_handling: Optional[ArraySizeHandlingEnum] = None
        self.array_size: Optional[ArraySizeSemanticsEnum] = None
        self.index_data_type: Optional[ApplicationPrimitiveDataType] = None
        self.max_number_of: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ApplicationArrayElement to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationArrayElement":
        """Create ApplicationArrayElement from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ApplicationArrayElement instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ApplicationArrayElement since parent returns ARObject
        return cast("ApplicationArrayElement", obj)


class ApplicationArrayElementBuilder:
    """Builder for ApplicationArrayElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationArrayElement = ApplicationArrayElement()

    def build(self) -> ApplicationArrayElement:
        """Build and return ApplicationArrayElement object.

        Returns:
            ApplicationArrayElement instance
        """
        # TODO: Add validation
        return self._obj
