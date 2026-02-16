"""IndentSample AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_overview_paragraph import (
    LOverviewParagraph,
)


class IndentSample(ARObject):
    """AUTOSAR IndentSample."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("item_label_pos_enum", None, False, False, ItemLabelPosEnum),  # itemLabelPosEnum
        ("l2", None, False, False, LOverviewParagraph),  # l2
    ]

    def __init__(self) -> None:
        """Initialize IndentSample."""
        super().__init__()
        self.item_label_pos_enum: Optional[ItemLabelPosEnum] = None
        self.l2: LOverviewParagraph = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IndentSample to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IndentSample":
        """Create IndentSample from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IndentSample instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IndentSample since parent returns ARObject
        return cast("IndentSample", obj)


class IndentSampleBuilder:
    """Builder for IndentSample."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IndentSample = IndentSample()

    def build(self) -> IndentSample:
        """Build and return IndentSample object.

        Returns:
            IndentSample instance
        """
        # TODO: Add validation
        return self._obj
