"""LOverviewParagraph AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 348)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_LanguageDataModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class LOverviewParagraph(ARObject):
    """AUTOSAR LOverviewParagraph."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    blueprint_value: Optional[String]
    def __init__(self) -> None:
        """Initialize LOverviewParagraph."""
        super().__init__()
        self.blueprint_value: Optional[String] = None
    def serialize(self) -> ET.Element:
        """Serialize LOverviewParagraph to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize blueprint_value
        if self.blueprint_value is not None:
            serialized = ARObject._serialize_item(self.blueprint_value, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BLUEPRINT-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LOverviewParagraph":
        """Deserialize XML element to LOverviewParagraph object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LOverviewParagraph object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse blueprint_value
        child = ARObject._find_child_element(element, "BLUEPRINT-VALUE")
        if child is not None:
            blueprint_value_value = child.text
            obj.blueprint_value = blueprint_value_value

        return obj



class LOverviewParagraphBuilder:
    """Builder for LOverviewParagraph."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LOverviewParagraph = LOverviewParagraph()

    def build(self) -> LOverviewParagraph:
        """Build and return LOverviewParagraph object.

        Returns:
            LOverviewParagraph instance
        """
        # TODO: Add validation
        return self._obj
