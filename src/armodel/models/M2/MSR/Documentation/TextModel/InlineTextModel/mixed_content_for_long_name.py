"""MixedContentForLongName AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Superscript,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.emphasis_text import (
    EmphasisText,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.index_entry import (
    IndexEntry,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.tt import (
    Tt,
)


class MixedContentForLongName(ARObject):
    """AUTOSAR MixedContentForLongName."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("e", None, False, False, EmphasisText),  # e
        ("ie", None, False, False, IndexEntry),  # ie
        ("sub", None, True, False, None),  # sub
        ("sup", None, True, False, None),  # sup
        ("tt", None, False, False, Tt),  # tt
    ]

    def __init__(self) -> None:
        """Initialize MixedContentForLongName."""
        super().__init__()
        self.e: EmphasisText = None
        self.ie: IndexEntry = None
        self.sub: Superscript = None
        self.sup: Superscript = None
        self.tt: Tt = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MixedContentForLongName to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MixedContentForLongName":
        """Create MixedContentForLongName from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MixedContentForLongName instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MixedContentForLongName since parent returns ARObject
        return cast("MixedContentForLongName", obj)


class MixedContentForLongNameBuilder:
    """Builder for MixedContentForLongName."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MixedContentForLongName = MixedContentForLongName()

    def build(self) -> MixedContentForLongName:
        """Build and return MixedContentForLongName object.

        Returns:
            MixedContentForLongName instance
        """
        # TODO: Add validation
        return self._obj
