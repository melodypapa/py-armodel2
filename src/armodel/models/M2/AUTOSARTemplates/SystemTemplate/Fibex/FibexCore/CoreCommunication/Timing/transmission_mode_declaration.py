"""TransmissionModeDeclaration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 392)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.mode_driven_transmission_mode_condition import (
    ModeDrivenTransmissionModeCondition,
)


class TransmissionModeDeclaration(ARObject):
    """AUTOSAR TransmissionModeDeclaration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mode_drivens: list[ModeDrivenTransmissionModeCondition]
    transmission: Optional[Any]
    def __init__(self) -> None:
        """Initialize TransmissionModeDeclaration."""
        super().__init__()
        self.mode_drivens: list[ModeDrivenTransmissionModeCondition] = []
        self.transmission: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransmissionModeDeclaration":
        """Deserialize XML element to TransmissionModeDeclaration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TransmissionModeDeclaration object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse mode_drivens (list)
        obj.mode_drivens = []
        for child in ARObject._find_all_child_elements(element, "MODE-DRIVENS"):
            mode_drivens_value = ARObject._deserialize_by_tag(child, "ModeDrivenTransmissionModeCondition")
            obj.mode_drivens.append(mode_drivens_value)

        # Parse transmission
        child = ARObject._find_child_element(element, "TRANSMISSION")
        if child is not None:
            transmission_value = child.text
            obj.transmission = transmission_value

        return obj



class TransmissionModeDeclarationBuilder:
    """Builder for TransmissionModeDeclaration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransmissionModeDeclaration = TransmissionModeDeclaration()

    def build(self) -> TransmissionModeDeclaration:
        """Build and return TransmissionModeDeclaration object.

        Returns:
            TransmissionModeDeclaration instance
        """
        # TODO: Add validation
        return self._obj
