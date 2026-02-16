"""MsrQueryArg AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    String,
)


class MsrQueryArg(ARObject):
    """AUTOSAR MsrQueryArg."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("arg", None, True, False, None),  # arg
        ("si", None, True, False, None),  # si
    ]

    def __init__(self) -> None:
        """Initialize MsrQueryArg."""
        super().__init__()
        self.arg: String = None
        self.si: NameToken = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MsrQueryArg to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MsrQueryArg":
        """Create MsrQueryArg from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MsrQueryArg instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MsrQueryArg since parent returns ARObject
        return cast("MsrQueryArg", obj)


class MsrQueryArgBuilder:
    """Builder for MsrQueryArg."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MsrQueryArg = MsrQueryArg()

    def build(self) -> MsrQueryArg:
        """Build and return MsrQueryArg object.

        Returns:
            MsrQueryArg instance
        """
        # TODO: Add validation
        return self._obj
