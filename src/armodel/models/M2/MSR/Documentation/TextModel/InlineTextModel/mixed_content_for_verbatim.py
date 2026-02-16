"""MixedContentForVerbatim AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.br import (
    Br,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.emphasis_text import (
    EmphasisText,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.tt import (
    Tt,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.xref import (
    Xref,
)


class MixedContentForVerbatim(ARObject):
    """AUTOSAR MixedContentForVerbatim."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("br", None, False, False, Br),  # br
        ("e", None, False, False, EmphasisText),  # e
        ("tt", None, False, False, Tt),  # tt
        ("xref", None, False, False, Xref),  # xref
    ]

    def __init__(self) -> None:
        """Initialize MixedContentForVerbatim."""
        super().__init__()
        self.br: Br = None
        self.e: EmphasisText = None
        self.tt: Tt = None
        self.xref: Xref = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MixedContentForVerbatim to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MixedContentForVerbatim":
        """Create MixedContentForVerbatim from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MixedContentForVerbatim instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MixedContentForVerbatim since parent returns ARObject
        return cast("MixedContentForVerbatim", obj)


class MixedContentForVerbatimBuilder:
    """Builder for MixedContentForVerbatim."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MixedContentForVerbatim = MixedContentForVerbatim()

    def build(self) -> MixedContentForVerbatim:
        """Build and return MixedContentForVerbatim object.

        Returns:
            MixedContentForVerbatim instance
        """
        # TODO: Add validation
        return self._obj
