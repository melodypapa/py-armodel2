"""Modification AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 86)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_AdminData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)


class Modification(ARObject):
    """AUTOSAR Modification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    change: MultiLanguageOverviewParagraph
    reason: Optional[MultiLanguageOverviewParagraph]
    def __init__(self) -> None:
        """Initialize Modification."""
        super().__init__()
        self.change: MultiLanguageOverviewParagraph = None
        self.reason: Optional[MultiLanguageOverviewParagraph] = None

    def serialize(self) -> ET.Element:
        """Serialize Modification to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize change
        if self.change is not None:
            serialized = ARObject._serialize_item(self.change, "MultiLanguageOverviewParagraph")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CHANGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize reason
        if self.reason is not None:
            serialized = ARObject._serialize_item(self.reason, "MultiLanguageOverviewParagraph")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REASON")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Modification":
        """Deserialize XML element to Modification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Modification object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse change
        child = ARObject._find_child_element(element, "CHANGE")
        if child is not None:
            change_value = ARObject._deserialize_with_type(child, "MultiLanguageOverviewParagraph")
            obj.change = change_value

        # Parse reason
        child = ARObject._find_child_element(element, "REASON")
        if child is not None:
            reason_value = ARObject._deserialize_with_type(child, "MultiLanguageOverviewParagraph")
            obj.reason = reason_value

        return obj



class ModificationBuilder:
    """Builder for Modification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Modification = Modification()

    def build(self) -> Modification:
        """Build and return Modification object.

        Returns:
            Modification instance
        """
        # TODO: Add validation
        return self._obj
