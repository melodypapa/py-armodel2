"""SdgCaption AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 91)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_SpecialData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.multilanguage_referrable import (
    MultilanguageReferrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)


class SdgCaption(MultilanguageReferrable):
    """AUTOSAR SdgCaption."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    desc: Optional[MultiLanguageOverviewParagraph]
    def __init__(self) -> None:
        """Initialize SdgCaption."""
        super().__init__()
        self.desc: Optional[MultiLanguageOverviewParagraph] = None

    def serialize(self) -> ET.Element:
        """Serialize SdgCaption to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SdgCaption, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize desc
        if self.desc is not None:
            serialized = ARObject._serialize_item(self.desc, "MultiLanguageOverviewParagraph")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DESC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgCaption":
        """Deserialize XML element to SdgCaption object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SdgCaption object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SdgCaption, cls).deserialize(element)

        # Parse desc
        child = ARObject._find_child_element(element, "DESC")
        if child is not None:
            desc_value = ARObject._deserialize_with_type(child, "MultiLanguageOverviewParagraph")
            obj.desc = desc_value

        return obj



class SdgCaptionBuilder:
    """Builder for SdgCaption."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgCaption = SdgCaption()

    def build(self) -> SdgCaption:
        """Build and return SdgCaption object.

        Returns:
            SdgCaption instance
        """
        # TODO: Add validation
        return self._obj
