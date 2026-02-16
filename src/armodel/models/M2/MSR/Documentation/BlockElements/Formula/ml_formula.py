"""MlFormula AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("formula_caption", None, False, False, Caption),  # formulaCaption
        ("generic_math", None, False, False, MultiLanguagePlainText),  # genericMath
        ("l_graphics", None, False, True, LGraphic),  # lGraphics
        ("tex_math", None, False, False, MultiLanguagePlainText),  # texMath
        ("verbatim", None, False, False, MultiLanguageVerbatim),  # verbatim
    ]

    def __init__(self) -> None:
        """Initialize MlFormula."""
        super().__init__()
        self.formula_caption: Optional[Caption] = None
        self.generic_math: Optional[MultiLanguagePlainText] = None
        self.l_graphics: list[LGraphic] = []
        self.tex_math: Optional[MultiLanguagePlainText] = None
        self.verbatim: Optional[MultiLanguageVerbatim] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MlFormula to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MlFormula":
        """Create MlFormula from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MlFormula instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MlFormula since parent returns ARObject
        return cast("MlFormula", obj)


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
