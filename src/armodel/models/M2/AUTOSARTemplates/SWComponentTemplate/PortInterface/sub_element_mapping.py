"""SubElementMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.sub_element_ref import (
    SubElementRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_mapping import (
    TextTableMapping,
)


class SubElementMapping(ARObject):
    """AUTOSAR SubElementMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("first_element", None, False, False, SubElementRef),  # firstElement
        ("second_element", None, False, False, SubElementRef),  # secondElement
        ("text_table", None, False, False, TextTableMapping),  # textTable
    ]

    def __init__(self) -> None:
        """Initialize SubElementMapping."""
        super().__init__()
        self.first_element: Optional[SubElementRef] = None
        self.second_element: Optional[SubElementRef] = None
        self.text_table: TextTableMapping = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SubElementMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SubElementMapping":
        """Create SubElementMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SubElementMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SubElementMapping since parent returns ARObject
        return cast("SubElementMapping", obj)


class SubElementMappingBuilder:
    """Builder for SubElementMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SubElementMapping = SubElementMapping()

    def build(self) -> SubElementMapping:
        """Build and return SubElementMapping object.

        Returns:
            SubElementMapping instance
        """
        # TODO: Add validation
        return self._obj
