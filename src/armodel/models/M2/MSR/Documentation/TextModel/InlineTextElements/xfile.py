"""Xfile AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.single_language_referrable import (
    SingleLanguageReferrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class Xfile(SingleLanguageReferrable):
    """AUTOSAR Xfile."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("tool", None, True, False, None),  # tool
        ("tool_version", None, True, False, None),  # toolVersion
        ("url", None, False, False, any (Url)),  # url
    ]

    def __init__(self) -> None:
        """Initialize Xfile."""
        super().__init__()
        self.tool: Optional[String] = None
        self.tool_version: Optional[String] = None
        self.url: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Xfile to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Xfile":
        """Create Xfile from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Xfile instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Xfile since parent returns ARObject
        return cast("Xfile", obj)


class XfileBuilder:
    """Builder for Xfile."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Xfile = Xfile()

    def build(self) -> Xfile:
        """Build and return Xfile object.

        Returns:
            Xfile instance
        """
        # TODO: Add validation
        return self._obj
