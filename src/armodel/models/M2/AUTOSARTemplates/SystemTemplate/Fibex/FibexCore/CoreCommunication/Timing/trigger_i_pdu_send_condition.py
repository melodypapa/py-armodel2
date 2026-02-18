"""TriggerIPduSendCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 399)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class TriggerIPduSendCondition(ARObject):
    """AUTOSAR TriggerIPduSendCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    modes: list[ModeDeclaration]
    def __init__(self) -> None:
        """Initialize TriggerIPduSendCondition."""
        super().__init__()
        self.modes: list[ModeDeclaration] = []


class TriggerIPduSendConditionBuilder:
    """Builder for TriggerIPduSendCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TriggerIPduSendCondition = TriggerIPduSendCondition()

    def build(self) -> TriggerIPduSendCondition:
        """Build and return TriggerIPduSendCondition object.

        Returns:
            TriggerIPduSendCondition instance
        """
        # TODO: Add validation
        return self._obj
