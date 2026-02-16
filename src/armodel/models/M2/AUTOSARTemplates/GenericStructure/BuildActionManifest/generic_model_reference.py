"""GenericModelReference AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    Ref,
)


class GenericModelReference(ARObject):
    """AUTOSAR GenericModelReference."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base", None, True, False, None),  # base
        ("dest", None, True, False, None),  # dest
        ("ref", None, True, False, None),  # ref
    ]

    def __init__(self) -> None:
        """Initialize GenericModelReference."""
        super().__init__()
        self.base: NameToken = None
        self.dest: NameToken = None
        self.ref: Ref = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert GenericModelReference to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GenericModelReference":
        """Create GenericModelReference from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            GenericModelReference instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to GenericModelReference since parent returns ARObject
        return cast("GenericModelReference", obj)


class GenericModelReferenceBuilder:
    """Builder for GenericModelReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GenericModelReference = GenericModelReference()

    def build(self) -> GenericModelReference:
        """Build and return GenericModelReference object.

        Returns:
            GenericModelReference instance
        """
        # TODO: Add validation
        return self._obj
