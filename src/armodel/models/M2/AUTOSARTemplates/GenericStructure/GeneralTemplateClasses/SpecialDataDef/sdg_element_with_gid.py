"""SdgElementWithGid AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)


class SdgElementWithGid(ARObject):
    """AUTOSAR SdgElementWithGid."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("gid", None, True, False, None),  # gid
    ]

    def __init__(self) -> None:
        """Initialize SdgElementWithGid."""
        super().__init__()
        self.gid: Optional[NameToken] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SdgElementWithGid to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgElementWithGid":
        """Create SdgElementWithGid from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SdgElementWithGid instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SdgElementWithGid since parent returns ARObject
        return cast("SdgElementWithGid", obj)


class SdgElementWithGidBuilder:
    """Builder for SdgElementWithGid."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgElementWithGid = SdgElementWithGid()

    def build(self) -> SdgElementWithGid:
        """Build and return SdgElementWithGid object.

        Returns:
            SdgElementWithGid instance
        """
        # TODO: Add validation
        return self._obj
