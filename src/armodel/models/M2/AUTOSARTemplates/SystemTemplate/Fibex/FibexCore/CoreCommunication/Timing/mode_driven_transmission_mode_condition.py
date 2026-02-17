"""ModeDrivenTransmissionModeCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 393)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class ModeDrivenTransmissionModeCondition(ARObject):
    """AUTOSAR ModeDrivenTransmissionModeCondition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "modes": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ModeDeclaration,
        ),  # modes
    }

    def __init__(self) -> None:
        """Initialize ModeDrivenTransmissionModeCondition."""
        super().__init__()
        self.modes: list[ModeDeclaration] = []


class ModeDrivenTransmissionModeConditionBuilder:
    """Builder for ModeDrivenTransmissionModeCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeDrivenTransmissionModeCondition = ModeDrivenTransmissionModeCondition()

    def build(self) -> ModeDrivenTransmissionModeCondition:
        """Build and return ModeDrivenTransmissionModeCondition object.

        Returns:
            ModeDrivenTransmissionModeCondition instance
        """
        # TODO: Add validation
        return self._obj
