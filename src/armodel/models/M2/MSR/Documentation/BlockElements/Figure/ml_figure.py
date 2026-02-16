"""MlFigure AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.BlockElements.caption import (
    Caption,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Figure.l_graphic import (
    LGraphic,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_verbatim import (
    MultiLanguageVerbatim,
)


class MlFigure(Paginateable):
    """AUTOSAR MlFigure."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("figure_caption", None, False, False, Caption),  # figureCaption
        ("frame", None, False, False, FrameEnum),  # frame
        ("help_entry", None, True, False, None),  # helpEntry
        ("l_graphics", None, False, True, LGraphic),  # lGraphics
        ("pgwide", None, False, False, PgwideEnum),  # pgwide
        ("verbatim", None, False, False, MultiLanguageVerbatim),  # verbatim
    ]

    def __init__(self) -> None:
        """Initialize MlFigure."""
        super().__init__()
        self.figure_caption: Optional[Caption] = None
        self.frame: Optional[FrameEnum] = None
        self.help_entry: Optional[String] = None
        self.l_graphics: list[LGraphic] = []
        self.pgwide: Optional[PgwideEnum] = None
        self.verbatim: Optional[MultiLanguageVerbatim] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MlFigure to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MlFigure":
        """Create MlFigure from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MlFigure instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MlFigure since parent returns ARObject
        return cast("MlFigure", obj)


class MlFigureBuilder:
    """Builder for MlFigure."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MlFigure = MlFigure()

    def build(self) -> MlFigure:
        """Build and return MlFigure object.

        Returns:
            MlFigure instance
        """
        # TODO: Add validation
        return self._obj
