"""Sdg AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData.sdg_caption import (
    SdgCaption,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData.sdg_contents import (
    SdgContents,
)


class Sdg(ARObject):
    """AUTOSAR Sdg."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("gid", None, True, False, None),  # gid
        ("sdg_caption", None, False, False, SdgCaption),  # sdgCaption
        ("sdg_contents", None, False, False, SdgContents),  # sdgContents
    ]

    def __init__(self) -> None:
        """Initialize Sdg."""
        super().__init__()
        self.gid: NameToken = None
        self.sdg_caption: Optional[SdgCaption] = None
        self.sdg_contents: Optional[SdgContents] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Sdg to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Sdg":
        """Create Sdg from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Sdg instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Sdg since parent returns ARObject
        return cast("Sdg", obj)


class SdgBuilder:
    """Builder for Sdg."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Sdg = Sdg()

    def build(self) -> Sdg:
        """Build and return Sdg object.

        Returns:
            Sdg instance
        """
        # TODO: Add validation
        return self._obj
