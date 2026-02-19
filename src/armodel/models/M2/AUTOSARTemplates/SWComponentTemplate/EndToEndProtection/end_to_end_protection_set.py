"""EndToEndProtectionSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 214)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 383)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_EndToEndProtection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection.end_to_end_protection import (
    EndToEndProtection,
)


class EndToEndProtectionSet(ARElement):
    """AUTOSAR EndToEndProtectionSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    end_to_ends: list[EndToEndProtection]
    def __init__(self) -> None:
        """Initialize EndToEndProtectionSet."""
        super().__init__()
        self.end_to_ends: list[EndToEndProtection] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EndToEndProtectionSet":
        """Deserialize XML element to EndToEndProtectionSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EndToEndProtectionSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EndToEndProtectionSet, cls).deserialize(element)

        # Parse end_to_ends (list from container "END-TO-ENDS")
        obj.end_to_ends = []
        container = ARObject._find_child_element(element, "END-TO-ENDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.end_to_ends.append(child_value)

        return obj



class EndToEndProtectionSetBuilder:
    """Builder for EndToEndProtectionSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EndToEndProtectionSet = EndToEndProtectionSet()

    def build(self) -> EndToEndProtectionSet:
        """Build and return EndToEndProtectionSet object.

        Returns:
            EndToEndProtectionSet instance
        """
        # TODO: Add validation
        return self._obj
