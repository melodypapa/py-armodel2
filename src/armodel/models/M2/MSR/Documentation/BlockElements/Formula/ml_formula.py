"""MlFormula AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 301)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 309)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_Formula.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.caption import (
    Caption,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Figure.l_graphic import (
    LGraphic,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_plain_text import (
    MultiLanguagePlainText,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_verbatim import (
    MultiLanguageVerbatim,
)


class MlFormula(Paginateable):
    """AUTOSAR MlFormula."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    formula_caption: Optional[Caption]
    generic_math: Optional[MultiLanguagePlainText]
    l_graphics: list[LGraphic]
    tex_math: Optional[MultiLanguagePlainText]
    verbatim: Optional[MultiLanguageVerbatim]
    def __init__(self) -> None:
        """Initialize MlFormula."""
        super().__init__()
        self.formula_caption: Optional[Caption] = None
        self.generic_math: Optional[MultiLanguagePlainText] = None
        self.l_graphics: list[LGraphic] = []
        self.tex_math: Optional[MultiLanguagePlainText] = None
        self.verbatim: Optional[MultiLanguageVerbatim] = None
    def serialize(self) -> ET.Element:
        """Serialize MlFormula to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MlFormula, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize formula_caption
        if self.formula_caption is not None:
            serialized = ARObject._serialize_item(self.formula_caption, "Caption")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FORMULA-CAPTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize generic_math
        if self.generic_math is not None:
            serialized = ARObject._serialize_item(self.generic_math, "MultiLanguagePlainText")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("GENERIC-MATH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize l_graphics (list to container "L-GRAPHICS")
        if self.l_graphics:
            wrapper = ET.Element("L-GRAPHICS")
            for item in self.l_graphics:
                serialized = ARObject._serialize_item(item, "LGraphic")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tex_math
        if self.tex_math is not None:
            serialized = ARObject._serialize_item(self.tex_math, "MultiLanguagePlainText")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TEX-MATH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize verbatim
        if self.verbatim is not None:
            serialized = ARObject._serialize_item(self.verbatim, "MultiLanguageVerbatim")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VERBATIM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MlFormula":
        """Deserialize XML element to MlFormula object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MlFormula object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MlFormula, cls).deserialize(element)

        # Parse formula_caption
        child = ARObject._find_child_element(element, "FORMULA-CAPTION")
        if child is not None:
            formula_caption_value = ARObject._deserialize_by_tag(child, "Caption")
            obj.formula_caption = formula_caption_value

        # Parse generic_math
        child = ARObject._find_child_element(element, "GENERIC-MATH")
        if child is not None:
            generic_math_value = ARObject._deserialize_by_tag(child, "MultiLanguagePlainText")
            obj.generic_math = generic_math_value

        # Parse l_graphics (list from container "L-GRAPHICS")
        obj.l_graphics = []
        container = ARObject._find_child_element(element, "L-GRAPHICS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.l_graphics.append(child_value)

        # Parse tex_math
        child = ARObject._find_child_element(element, "TEX-MATH")
        if child is not None:
            tex_math_value = ARObject._deserialize_by_tag(child, "MultiLanguagePlainText")
            obj.tex_math = tex_math_value

        # Parse verbatim
        child = ARObject._find_child_element(element, "VERBATIM")
        if child is not None:
            verbatim_value = ARObject._deserialize_by_tag(child, "MultiLanguageVerbatim")
            obj.verbatim = verbatim_value

        return obj



class MlFormulaBuilder:
    """Builder for MlFormula."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MlFormula = MlFormula()

    def build(self) -> MlFormula:
        """Build and return MlFormula object.

        Returns:
            MlFormula instance
        """
        # TODO: Add validation
        return self._obj
