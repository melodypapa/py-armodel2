"""MlFormula AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "formula_caption": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Caption,
        ),  # formulaCaption
        "generic_math": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultiLanguagePlainText,
        ),  # genericMath
        "l_graphics": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=LGraphic,
        ),  # lGraphics
        "tex_math": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultiLanguagePlainText,
        ),  # texMath
        "verbatim": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultiLanguageVerbatim,
        ),  # verbatim
    }

    def __init__(self) -> None:
        """Initialize MlFormula."""
        super().__init__()
        self.formula_caption: Optional[Caption] = None
        self.generic_math: Optional[MultiLanguagePlainText] = None
        self.l_graphics: list[LGraphic] = []
        self.tex_math: Optional[MultiLanguagePlainText] = None
        self.verbatim: Optional[MultiLanguageVerbatim] = None


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
