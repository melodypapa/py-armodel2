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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ViewMap, cls).deserialize(element)

        # Parse first_elements (list from container "FIRST-ELEMENTS")
        obj.first_elements = []
        container = ARObject._find_child_element(element, "FIRST-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.first_elements.append(child_value)

        # Parse role
        child = ARObject._find_child_element(element, "ROLE")
        if child is not None:
            role_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.role = role_value

        # Parse second_elements (list from container "SECOND-ELEMENTS")
        obj.second_elements = []
        container = ARObject._find_child_element(element, "SECOND-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.second_elements.append(child_value)

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
