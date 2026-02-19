"""EndToEndProtection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 214)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 384)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_EndToEndProtection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class EndToEndProtection(Identifiable):
    """AUTOSAR EndToEndProtection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    end_to_ends: list[EndToEndProtection]
    def __init__(self) -> None:
        """Initialize EndToEndProtection."""
        super().__init__()
        self.end_to_ends: list[EndToEndProtection] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EndToEndProtection":
        """Deserialize XML element to EndToEndProtection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EndToEndProtection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EndToEndProtection, cls).deserialize(element)

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



class EndToEndProtectionBuilder:
    """Builder for EndToEndProtection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EndToEndProtection = EndToEndProtection()

    def build(self) -> EndToEndProtection:
        """Build and return EndToEndProtection object.

        Returns:
            EndToEndProtection instance
        """
        # TODO: Add validation
        return self._obj
