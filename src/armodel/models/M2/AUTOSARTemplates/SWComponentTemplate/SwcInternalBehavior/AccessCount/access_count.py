"""AccessCount AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 57)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_AccessCount.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)


class AccessCount(ARObject):
    """AUTOSAR AccessCount."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    access_point: Optional[AbstractAccessPoint]
    value: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize AccessCount."""
        super().__init__()
        self.access_point: Optional[AbstractAccessPoint] = None
        self.value: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AccessCount":
        """Deserialize XML element to AccessCount object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AccessCount object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse access_point
        child = ARObject._find_child_element(element, "ACCESS-POINT")
        if child is not None:
            access_point_value = ARObject._deserialize_by_tag(child, "AbstractAccessPoint")
            obj.access_point = access_point_value

        # Parse value
        child = ARObject._find_child_element(element, "VALUE")
        if child is not None:
            value_value = child.text
            obj.value = value_value

        return obj



class AccessCountBuilder:
    """Builder for AccessCount."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AccessCount = AccessCount()

    def build(self) -> AccessCount:
        """Build and return AccessCount object.

        Returns:
            AccessCount instance
        """
        # TODO: Add validation
        return self._obj
