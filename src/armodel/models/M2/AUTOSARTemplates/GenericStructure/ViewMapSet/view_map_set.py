"""ViewMapSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2079)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 401)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_ViewMapSet.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.ViewMapSet.view_map import (
    ViewMap,
)


class ViewMapSet(ARElement):
    """AUTOSAR ViewMapSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    view_maps: list[ViewMap]
    def __init__(self) -> None:
        """Initialize ViewMapSet."""
        super().__init__()
        self.view_maps: list[ViewMap] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ViewMapSet":
        """Deserialize XML element to ViewMapSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ViewMapSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse view_maps (list)
        obj.view_maps = []
        for child in ARObject._find_all_child_elements(element, "VIEW-MAPS"):
            view_maps_value = ARObject._deserialize_by_tag(child, "ViewMap")
            obj.view_maps.append(view_maps_value)

        return obj



class ViewMapSetBuilder:
    """Builder for ViewMapSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ViewMapSet = ViewMapSet()

    def build(self) -> ViewMapSet:
        """Build and return ViewMapSet object.

        Returns:
            ViewMapSet instance
        """
        # TODO: Add validation
        return self._obj
