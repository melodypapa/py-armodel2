"""EngineeringObject AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    RevisionLabelString,
)


class EngineeringObject(ARObject):
    """AUTOSAR EngineeringObject."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("category", None, True, False, None),  # category
        ("domain", None, True, False, None),  # domain
        ("revision_label_strings", None, False, True, None),  # revisionLabelStrings
        ("short_label", None, True, False, None),  # shortLabel
    ]

    def __init__(self) -> None:
        """Initialize EngineeringObject."""
        super().__init__()
        self.category: NameToken = None
        self.domain: Optional[NameToken] = None
        self.revision_label_strings: list[RevisionLabelString] = []
        self.short_label: NameToken = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EngineeringObject to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EngineeringObject":
        """Create EngineeringObject from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EngineeringObject instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EngineeringObject since parent returns ARObject
        return cast("EngineeringObject", obj)


class EngineeringObjectBuilder:
    """Builder for EngineeringObject."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EngineeringObject = EngineeringObject()

    def build(self) -> EngineeringObject:
        """Build and return EngineeringObject object.

        Returns:
            EngineeringObject instance
        """
        # TODO: Add validation
        return self._obj
