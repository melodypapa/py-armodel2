"""AccessCountSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 57)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_AccessCount.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.access_count import (
    AccessCount,
)


class AccessCountSet(ARObject):
    """AUTOSAR AccessCountSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    access_counts: list[AccessCount]
    count_profile: Optional[NameToken]
    def __init__(self) -> None:
        """Initialize AccessCountSet."""
        super().__init__()
        self.access_counts: list[AccessCount] = []
        self.count_profile: Optional[NameToken] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AccessCountSet":
        """Deserialize XML element to AccessCountSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AccessCountSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse access_counts (list from container "ACCESS-COUNTS")
        obj.access_counts = []
        container = ARObject._find_child_element(element, "ACCESS-COUNTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.access_counts.append(child_value)

        # Parse count_profile
        child = ARObject._find_child_element(element, "COUNT-PROFILE")
        if child is not None:
            count_profile_value = child.text
            obj.count_profile = count_profile_value

        return obj



class AccessCountSetBuilder:
    """Builder for AccessCountSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AccessCountSet = AccessCountSet()

    def build(self) -> AccessCountSet:
        """Build and return AccessCountSet object.

        Returns:
            AccessCountSet instance
        """
        # TODO: Add validation
        return self._obj
