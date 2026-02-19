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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Graphic":
        """Deserialize XML element to Graphic object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Graphic object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Graphic, cls).deserialize(element)

        # Parse editfit
        child = ARObject._find_child_element(element, "EDITFIT")
        if child is not None:
            editfit_value = GraphicFitEnum.deserialize(child)
            obj.editfit = editfit_value

        # Parse edit_height
        child = ARObject._find_child_element(element, "EDIT-HEIGHT")
        if child is not None:
            edit_height_value = child.text
            obj.edit_height = edit_height_value

        # Parse editscale
        child = ARObject._find_child_element(element, "EDITSCALE")
        if child is not None:
            editscale_value = child.text
            obj.editscale = editscale_value

        # Parse edit_width
        child = ARObject._find_child_element(element, "EDIT-WIDTH")
        if child is not None:
            edit_width_value = child.text
            obj.edit_width = edit_width_value

        # Parse filename
        child = ARObject._find_child_element(element, "FILENAME")
        if child is not None:
            filename_value = child.text
            obj.filename = filename_value

        # Parse fit
        child = ARObject._find_child_element(element, "FIT")
        if child is not None:
            fit_value = GraphicFitEnum.deserialize(child)
            obj.fit = fit_value

        # Parse generator
        child = ARObject._find_child_element(element, "GENERATOR")
        if child is not None:
            generator_value = child.text
            obj.generator = generator_value

        # Parse height
        child = ARObject._find_child_element(element, "HEIGHT")
        if child is not None:
            height_value = child.text
            obj.height = height_value

        # Parse html_fit
        child = ARObject._find_child_element(element, "HTML-FIT")
        if child is not None:
            html_fit_value = GraphicFitEnum.deserialize(child)
            obj.html_fit = html_fit_value

        # Parse html_height
        child = ARObject._find_child_element(element, "HTML-HEIGHT")
        if child is not None:
            html_height_value = child.text
            obj.html_height = html_height_value

        # Parse html_scale
        child = ARObject._find_child_element(element, "HTML-SCALE")
        if child is not None:
            html_scale_value = child.text
            obj.html_scale = html_scale_value

        # Parse html_width
        child = ARObject._find_child_element(element, "HTML-WIDTH")
        if child is not None:
            html_width_value = child.text
            obj.html_width = html_width_value

        # Parse notation
        child = ARObject._find_child_element(element, "NOTATION")
        if child is not None:
            notation_value = GraphicNotationEnum.deserialize(child)
            obj.notation = notation_value

        # Parse scale
        child = ARObject._find_child_element(element, "SCALE")
        if child is not None:
            scale_value = child.text
            obj.scale = scale_value

        # Parse width
        child = ARObject._find_child_element(element, "WIDTH")
        if child is not None:
            width_value = child.text
            obj.width = width_value

        return obj



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
