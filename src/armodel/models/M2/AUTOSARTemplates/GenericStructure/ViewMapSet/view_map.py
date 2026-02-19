"""ViewMap AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2079)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 401)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_ViewMapSet.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)


class ViewMap(Identifiable):
    """AUTOSAR ViewMap."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    first_elements: list[AtpFeature]
    role: Optional[Identifier]
    second_elements: list[AtpFeature]
    def __init__(self) -> None:
        """Initialize ViewMap."""
        super().__init__()
        self.first_elements: list[AtpFeature] = []
        self.role: Optional[Identifier] = None
        self.second_elements: list[AtpFeature] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ViewMap":
        """Deserialize XML element to ViewMap object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ViewMap object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse first_elements (list)
        obj.first_elements = []
        for child in ARObject._find_all_child_elements(element, "FIRST-ELEMENTS"):
            first_elements_value = ARObject._deserialize_by_tag(child, "AtpFeature")
            obj.first_elements.append(first_elements_value)

        # Parse role
        child = ARObject._find_child_element(element, "ROLE")
        if child is not None:
            role_value = child.text
            obj.role = role_value

        # Parse second_elements (list)
        obj.second_elements = []
        for child in ARObject._find_all_child_elements(element, "SECOND-ELEMENTS"):
            second_elements_value = ARObject._deserialize_by_tag(child, "AtpFeature")
            obj.second_elements.append(second_elements_value)

        return obj



class ViewMapBuilder:
    """Builder for ViewMap."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ViewMap = ViewMap()

    def build(self) -> ViewMap:
        """Build and return ViewMap object.

        Returns:
            ViewMap instance
        """
        # TODO: Add validation
        return self._obj
