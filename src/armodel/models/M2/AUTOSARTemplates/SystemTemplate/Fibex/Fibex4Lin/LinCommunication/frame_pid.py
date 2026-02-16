"""FramePid AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    PositiveInteger,
)


class FramePid(ARObject):
    """AUTOSAR FramePid."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("index", None, True, False, None),  # index
        ("pid", None, True, False, None),  # pid
    ]

    def __init__(self) -> None:
        """Initialize FramePid."""
        super().__init__()
        self.index: Optional[Integer] = None
        self.pid: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FramePid to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FramePid":
        """Create FramePid from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FramePid instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FramePid since parent returns ARObject
        return cast("FramePid", obj)


class FramePidBuilder:
    """Builder for FramePid."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FramePid = FramePid()

    def build(self) -> FramePid:
        """Build and return FramePid object.

        Returns:
            FramePid instance
        """
        # TODO: Add validation
        return self._obj
