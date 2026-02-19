"""MultiLanguageVerbatim AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 291)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_MultilanguageData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    FloatEnum,
    PgwideEnum,
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    allow_break: Optional[NameToken]
    float: Optional[FloatEnum]
    help_entry: Optional[String]
    l5: LVerbatim
    pgwide: Optional[PgwideEnum]
    def __init__(self) -> None:
        """Initialize MultiLanguageVerbatim."""
        super().__init__()
        self.allow_break: Optional[NameToken] = None
        self.float: Optional[FloatEnum] = None
        self.help_entry: Optional[String] = None
        self.l5: LVerbatim = None
        self.pgwide: Optional[PgwideEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultiLanguageVerbatim":
        """Deserialize XML element to MultiLanguageVerbatim object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MultiLanguageVerbatim object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MultiLanguageVerbatim, cls).deserialize(element)

        # Parse allow_break
        child = ARObject._find_child_element(element, "ALLOW-BREAK")
        if child is not None:
            allow_break_value = child.text
            obj.allow_break = allow_break_value

        # Parse float
        child = ARObject._find_child_element(element, "FLOAT")
        if child is not None:
            float_value = FloatEnum.deserialize(child)
            obj.float = float_value

        # Parse help_entry
        child = ARObject._find_child_element(element, "HELP-ENTRY")
        if child is not None:
            help_entry_value = child.text
            obj.help_entry = help_entry_value

        # Parse l5
        child = ARObject._find_child_element(element, "L5")
        if child is not None:
            l5_value = ARObject._deserialize_by_tag(child, "LVerbatim")
            obj.l5 = l5_value

        # Parse pgwide
        child = ARObject._find_child_element(element, "PGWIDE")
        if child is not None:
            pgwide_value = PgwideEnum.deserialize(child)
            obj.pgwide = pgwide_value

        return obj



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
