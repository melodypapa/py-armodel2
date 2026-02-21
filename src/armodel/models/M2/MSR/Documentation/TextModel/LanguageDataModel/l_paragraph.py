"""LParagraph AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 348)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_LanguageDataModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.language_specific import (
    LanguageSpecific,
)
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization.decorators import l_prefix


class LParagraph(LanguageSpecific):
    """AUTOSAR LParagraph."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True if this class is abstract, False otherwise
        """
        return False

    def __init__(self) -> None:
        """Initialize LParagraph."""
        super().__init__()
        self._l1: list[LParagraph] = []
        self._l2: list[LParagraph] = []
        self._l3: list[LParagraph] = []

    @property
    @l_prefix("L-1")
    def l1(self) -> list[LParagraph]:
        """Get l1 with language-specific wrapper."""
        return self._l1

    @l1.setter
    def l1(self, value: list[LParagraph]) -> None:
        """Set l1 with language-specific wrapper."""
        self._l1 = value

    @property
    @l_prefix("L-2")
    def l2(self) -> list[LParagraph]:
        """Get l2 with language-specific wrapper."""
        return self._l2

    @l2.setter
    def l2(self, value: list[LParagraph]) -> None:
        """Set l2 with language-specific wrapper."""
        self._l2 = value

    @property
    @l_prefix("L-3")
    def l3(self) -> list[LParagraph]:
        """Get l3 with language-specific wrapper."""
        return self._l3

    @l3.setter
    def l3(self, value: list[LParagraph]) -> None:
        """Set l3 with language-specific wrapper."""
        self._l3 = value

    def serialize(self) -> ET.Element:
        """Serialize LParagraph to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LParagraph, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text is not None:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize l1 (list to container "L-1")
        if self._l1:
            wrapper = ET.Element("L-1")
            for item in self._l1:
                serialized = item.serialize()
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize l2 (list to container "L-2")
        if self._l2:
            wrapper = ET.Element("L-2")
            for item in self._l2:
                serialized = item.serialize()
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize l3 (list to container "L-3")
        if self._l3:
            wrapper = ET.Element("L-3")
            for item in self._l3:
                serialized = item.serialize()
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LParagraph":
        """Deserialize XML element to LParagraph object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LParagraph object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LParagraph, cls).deserialize(element)

        # Deserialize l1 list from L-1 elements
        obj._l1 = []
        for child in element:
            if SerializationHelper.strip_namespace(child.tag) == "L-1":
                l1_value = LParagraph.deserialize(child)
                obj._l1.append(l1_value)

        # Deserialize l2 list from L-2 elements
        obj._l2 = []
        for child in element:
            if SerializationHelper.strip_namespace(child.tag) == "L-2":
                l2_value = LParagraph.deserialize(child)
                obj._l2.append(l2_value)

        # Deserialize l3 list from L-3 elements
        obj._l3 = []
        for child in element:
            if SerializationHelper.strip_namespace(child.tag) == "L-3":
                l3_value = LParagraph.deserialize(child)
                obj._l3.append(l3_value)

        return obj


class LParagraphBuilder:
    """Builder for LParagraph."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LParagraph = LParagraph()

    def build(self) -> LParagraph:
        """Build and return LParagraph object.

        Returns:
            LParagraph instance
        """
        # TODO: Add validation
        return self._obj