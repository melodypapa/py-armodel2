"""Prms AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 338)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_GerneralParameters.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)


class Prms(Paginateable):
    """AUTOSAR Prms."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "label": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultilanguageLongName,
        ),  # label
        "prm": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=any (GeneralParameter),
        ),  # prm
    }

    def __init__(self) -> None:
        """Initialize Prms."""
        super().__init__()
        self.label: Optional[MultilanguageLongName] = None
        self.prm: Any = None


class PrmsBuilder:
    """Builder for Prms."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Prms = Prms()

    def build(self) -> Prms:
        """Build and return Prms object.

        Returns:
            Prms instance
        """
        # TODO: Add validation
        return self._obj
