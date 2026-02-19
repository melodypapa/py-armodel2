"""LGraphic AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 307)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_Figure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.language_specific import (
    LanguageSpecific,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.Figure.graphic import (
    Graphic,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Figure.map import (
    Map,
)


class LGraphic(LanguageSpecific):
    """AUTOSAR LGraphic."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    graphic: Graphic
    map: Optional[Map]
    def __init__(self) -> None:
        """Initialize LGraphic."""
        super().__init__()
        self.graphic: Graphic = None
        self.map: Optional[Map] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "LGraphic":
        """Deserialize XML element to LGraphic object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LGraphic object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse graphic
        child = ARObject._find_child_element(element, "GRAPHIC")
        if child is not None:
            graphic_value = ARObject._deserialize_by_tag(child, "Graphic")
            obj.graphic = graphic_value

        # Parse map
        child = ARObject._find_child_element(element, "MAP")
        if child is not None:
            map_value = ARObject._deserialize_by_tag(child, "Map")
            obj.map = map_value

        return obj



class LGraphicBuilder:
    """Builder for LGraphic."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LGraphic = LGraphic()

    def build(self) -> LGraphic:
        """Build and return LGraphic object.

        Returns:
            LGraphic instance
        """
        # TODO: Add validation
        return self._obj
