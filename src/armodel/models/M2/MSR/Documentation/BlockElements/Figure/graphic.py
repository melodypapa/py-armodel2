"""Graphic AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 302)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_Figure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.engineering_object import (
    EngineeringObject,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Figure import (
    GraphicFitEnum,
    GraphicNotationEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    String,
)


class Graphic(EngineeringObject):
    """AUTOSAR Graphic."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    editfit: Optional[GraphicFitEnum]
    edit_height: Optional[String]
    editscale: Optional[String]
    edit_width: Optional[String]
    filename: Optional[String]
    fit: Optional[GraphicFitEnum]
    generator: Optional[NameToken]
    height: Optional[String]
    html_fit: Optional[GraphicFitEnum]
    html_height: Optional[String]
    html_scale: Optional[String]
    html_width: Optional[String]
    notation: Optional[GraphicNotationEnum]
    scale: Optional[String]
    width: Optional[String]
    def __init__(self) -> None:
        """Initialize Graphic."""
        super().__init__()
        self.editfit: Optional[GraphicFitEnum] = None
        self.edit_height: Optional[String] = None
        self.editscale: Optional[String] = None
        self.edit_width: Optional[String] = None
        self.filename: Optional[String] = None
        self.fit: Optional[GraphicFitEnum] = None
        self.generator: Optional[NameToken] = None
        self.height: Optional[String] = None
        self.html_fit: Optional[GraphicFitEnum] = None
        self.html_height: Optional[String] = None
        self.html_scale: Optional[String] = None
        self.html_width: Optional[String] = None
        self.notation: Optional[GraphicNotationEnum] = None
        self.scale: Optional[String] = None
        self.width: Optional[String] = None


class GraphicBuilder:
    """Builder for Graphic."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Graphic = Graphic()

    def build(self) -> Graphic:
        """Build and return Graphic object.

        Returns:
            Graphic instance
        """
        # TODO: Add validation
        return self._obj
