"""MultiLanguageVerbatim AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable.float_enum import (
    FloatEnum,
)
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable.pgwide_enum import (
    PgwideEnum,
)


class MultiLanguageVerbatim(Paginateable):
    """AUTOSAR MultiLanguageVerbatim."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("allow_break", None, True, False, None),  # allowBreak
        ("float", None, False, False, FloatEnum),  # float
        ("help_entry", None, True, False, None),  # helpEntry
        ("l5", None, False, False, LVerbatim),  # l5
        ("pgwide", None, False, False, PgwideEnum),  # pgwide
    ]

    def __init__(self) -> None:
        """Initialize MultiLanguageVerbatim."""
        super().__init__()
        self.allow_break: Optional[NameToken] = None
        self.float: Optional[FloatEnum] = None
        self.help_entry: Optional[String] = None
        self.l5: LVerbatim = None
        self.pgwide: Optional[PgwideEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MultiLanguageVerbatim to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultiLanguageVerbatim":
        """Create MultiLanguageVerbatim from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MultiLanguageVerbatim instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MultiLanguageVerbatim since parent returns ARObject
        return cast("MultiLanguageVerbatim", obj)


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
