"""TriggerIPduSendCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 399)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class TriggerIPduSendCondition(ARObject):
    """AUTOSAR TriggerIPduSendCondition."""

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
