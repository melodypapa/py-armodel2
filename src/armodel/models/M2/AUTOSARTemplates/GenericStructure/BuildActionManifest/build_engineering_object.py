"""BuildEngineeringObject AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.engineering_object import (
    EngineeringObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    RegularExpression,
    UriString,
)


class BuildEngineeringObject(EngineeringObject):
    """AUTOSAR BuildEngineeringObject."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("file_type", None, True, False, None),  # fileType
        ("file_type_pattern", None, True, False, None),  # fileTypePattern
        ("intended", None, True, False, None),  # intended
    ]

    def __init__(self) -> None:
        """Initialize BuildEngineeringObject."""
        super().__init__()
        self.file_type: NameToken = None
        self.file_type_pattern: RegularExpression = None
        self.intended: Optional[UriString] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BuildEngineeringObject to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BuildEngineeringObject":
        """Create BuildEngineeringObject from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BuildEngineeringObject instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BuildEngineeringObject since parent returns ARObject
        return cast("BuildEngineeringObject", obj)


class BuildEngineeringObjectBuilder:
    """Builder for BuildEngineeringObject."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BuildEngineeringObject = BuildEngineeringObject()

    def build(self) -> BuildEngineeringObject:
        """Build and return BuildEngineeringObject object.

        Returns:
            BuildEngineeringObject instance
        """
        # TODO: Add validation
        return self._obj
