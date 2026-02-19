"""LinSporadicFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 429)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame import (
    LinFrame,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_unconditional_frame import (
    LinUnconditionalFrame,
)


class LinSporadicFrame(LinFrame):
    """AUTOSAR LinSporadicFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    substituteds: list[LinUnconditionalFrame]
    def __init__(self) -> None:
        """Initialize LinSporadicFrame."""
        super().__init__()
        self.substituteds: list[LinUnconditionalFrame] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinSporadicFrame":
        """Deserialize XML element to LinSporadicFrame object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinSporadicFrame object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse substituteds (list)
        obj.substituteds = []
        for child in ARObject._find_all_child_elements(element, "SUBSTITUTEDS"):
            substituteds_value = ARObject._deserialize_by_tag(child, "LinUnconditionalFrame")
            obj.substituteds.append(substituteds_value)

        return obj



class LinSporadicFrameBuilder:
    """Builder for LinSporadicFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinSporadicFrame = LinSporadicFrame()

    def build(self) -> LinSporadicFrame:
        """Build and return LinSporadicFrame object.

        Returns:
            LinSporadicFrame instance
        """
        # TODO: Add validation
        return self._obj
