"""BswModeSwitchEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 94)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import (
    BswScheduleEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import (
    ModeActivationKind,
)


class BswModeSwitchEvent(BswScheduleEvent):
    """AUTOSAR BswModeSwitchEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    activation: Optional[ModeActivationKind]
    def __init__(self) -> None:
        """Initialize BswModeSwitchEvent."""
        super().__init__()
        self.activation: Optional[ModeActivationKind] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModeSwitchEvent":
        """Deserialize XML element to BswModeSwitchEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswModeSwitchEvent object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse activation
        child = ARObject._find_child_element(element, "ACTIVATION")
        if child is not None:
            activation_value = child.text
            obj.activation = activation_value

        return obj



class BswModeSwitchEventBuilder:
    """Builder for BswModeSwitchEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModeSwitchEvent = BswModeSwitchEvent()

    def build(self) -> BswModeSwitchEvent:
        """Build and return BswModeSwitchEvent object.

        Returns:
            BswModeSwitchEvent instance
        """
        # TODO: Add validation
        return self._obj
