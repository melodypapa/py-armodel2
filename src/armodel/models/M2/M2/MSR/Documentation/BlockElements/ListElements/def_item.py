"""DefItem AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)


class DefItem(Paginateable):
    """AUTOSAR DefItem."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "def_": XMLMember(
            xml_tag='DEF',
            is_attribute=False,
            multiplicity="1",
            element_class=DocumentationBlock,
            xml_name_override='DEF',
        ),  # def
        "help_entry": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # helpEntry
    }

    def __init__(self) -> None:
        """Initialize DefItem."""
        super().__init__()
        self.def_: DocumentationBlock = None
        self.help_entry: Optional[String] = None


class DefItemBuilder:
    """Builder for DefItem."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DefItem = DefItem()

    def build(self) -> DefItem:
        """Build and return DefItem object.

        Returns:
            DefItem instance
        """
        # TODO: Add validation
        return self._obj
