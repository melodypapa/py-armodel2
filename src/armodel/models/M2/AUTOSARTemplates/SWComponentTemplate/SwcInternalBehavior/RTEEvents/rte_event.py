"""RTEEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 327)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 541)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 208)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 238)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.abstract_event import (
    AbstractEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.runnable_entity import (
        RunnableEntity,
    )

from abc import ABC, abstractmethod


class RTEEvent(AbstractEvent, ABC):
    """AUTOSAR RTEEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    disabled_mode_instance_refs: list[ModeDeclaration]
    start_on_event: Optional[RunnableEntity]
    def __init__(self) -> None:
        """Initialize RTEEvent."""
        super().__init__()
        self.disabled_mode_instance_refs: list[ModeDeclaration] = []
        self.start_on_event: Optional[RunnableEntity] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RTEEvent":
        """Deserialize XML element to RTEEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RTEEvent object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse disabled_mode_instance_refs (list)
        obj.disabled_mode_instance_refs = []
        for child in ARObject._find_all_child_elements(element, "DISABLED-MODE-INSTANCE-REFS"):
            disabled_mode_instance_refs_value = ARObject._deserialize_by_tag(child, "ModeDeclaration")
            obj.disabled_mode_instance_refs.append(disabled_mode_instance_refs_value)

        # Parse start_on_event
        child = ARObject._find_child_element(element, "START-ON-EVENT")
        if child is not None:
            start_on_event_value = ARObject._deserialize_by_tag(child, "RunnableEntity")
            obj.start_on_event = start_on_event_value

        return obj



class RTEEventBuilder:
    """Builder for RTEEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RTEEvent = RTEEvent()

    def build(self) -> RTEEvent:
        """Build and return RTEEvent object.

        Returns:
            RTEEvent instance
        """
        # TODO: Add validation
        return self._obj
