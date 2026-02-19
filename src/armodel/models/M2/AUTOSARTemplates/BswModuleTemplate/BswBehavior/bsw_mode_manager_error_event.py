"""BswModeManagerErrorEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 95)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import (
    BswScheduleEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class BswModeManagerErrorEvent(BswScheduleEvent):
    """AUTOSAR BswModeManagerErrorEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mode_group_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize BswModeManagerErrorEvent."""
        super().__init__()
        self.mode_group_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModeManagerErrorEvent":
        """Deserialize XML element to BswModeManagerErrorEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswModeManagerErrorEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswModeManagerErrorEvent, cls).deserialize(element)

        # Parse mode_group_ref
        child = ARObject._find_child_element(element, "MODE-GROUP")
        if child is not None:
            mode_group_ref_value = ARObject._deserialize_by_tag(child, "ModeDeclarationGroup")
            obj.mode_group_ref = mode_group_ref_value

        return obj



class BswModeManagerErrorEventBuilder:
    """Builder for BswModeManagerErrorEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModeManagerErrorEvent = BswModeManagerErrorEvent()

    def build(self) -> BswModeManagerErrorEvent:
        """Build and return BswModeManagerErrorEvent object.

        Returns:
            BswModeManagerErrorEvent instance
        """
        # TODO: Add validation
        return self._obj
