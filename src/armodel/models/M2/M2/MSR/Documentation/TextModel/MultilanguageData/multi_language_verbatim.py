"""MultiLanguageVerbatim AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    String,
)
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_verbatim import (
    LVerbatim,
)


class MultiLanguageVerbatim(Paginateable):
    """AUTOSAR MultiLanguageVerbatim."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "allow_break": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # allowBreak
        "float": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=FloatEnum,
        ),  # float
        "help_entry": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # helpEntry
        "l5": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=LVerbatim,
        ),  # l5
        "pgwide": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PgwideEnum,
        ),  # pgwide
    }

    def __init__(self) -> None:
        """Initialize MultiLanguageVerbatim."""
        super().__init__()
        self.allow_break: Optional[NameToken] = None
        self.float: Optional[FloatEnum] = None
        self.help_entry: Optional[String] = None
        self.l5: LVerbatim = None
        self.pgwide: Optional[PgwideEnum] = None


class MultiLanguageVerbatimBuilder:
    """Builder for MultiLanguageVerbatim."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MultiLanguageVerbatim = MultiLanguageVerbatim()

    def build(self) -> MultiLanguageVerbatim:
        """Build and return MultiLanguageVerbatim object.

        Returns:
            MultiLanguageVerbatim instance
        """
        # TODO: Add validation
        return self._obj
