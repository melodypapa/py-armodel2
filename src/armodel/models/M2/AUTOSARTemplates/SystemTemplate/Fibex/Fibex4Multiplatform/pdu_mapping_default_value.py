"""PduMappingDefaultValue AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.default_value_element import (
    DefaultValueElement,
)


class PduMappingDefaultValue(ARObject):
    """AUTOSAR PduMappingDefaultValue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("default_values", None, False, True, DefaultValueElement),  # defaultValues
    ]

    def __init__(self) -> None:
        """Initialize PduMappingDefaultValue."""
        super().__init__()
        self.default_values: list[DefaultValueElement] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PduMappingDefaultValue to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PduMappingDefaultValue":
        """Create PduMappingDefaultValue from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PduMappingDefaultValue instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PduMappingDefaultValue since parent returns ARObject
        return cast("PduMappingDefaultValue", obj)


class PduMappingDefaultValueBuilder:
    """Builder for PduMappingDefaultValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PduMappingDefaultValue = PduMappingDefaultValue()

    def build(self) -> PduMappingDefaultValue:
        """Build and return PduMappingDefaultValue object.

        Returns:
            PduMappingDefaultValue instance
        """
        # TODO: Add validation
        return self._obj
