"""BswEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 87)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 206)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.abstract_event import (
    AbstractEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_distinguished_partition import (
    BswDistinguishedPartition,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import (
    BswModuleEntity,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from abc import ABC, abstractmethod


class BswEvent(AbstractEvent, ABC):
    """AUTOSAR BswEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    contexts: list[BswDistinguishedPartition]
    disabled_in_mode_description_instance_refs: list[ModeDeclaration]
    starts_on_event: Optional[BswModuleEntity]
    def __init__(self) -> None:
        """Initialize BswEvent."""
        super().__init__()
        self.contexts: list[BswDistinguishedPartition] = []
        self.disabled_in_mode_description_instance_refs: list[ModeDeclaration] = []
        self.starts_on_event: Optional[BswModuleEntity] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswEvent":
        """Deserialize XML element to BswEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswEvent, cls).deserialize(element)

        # Parse contexts (list from container "CONTEXTS")
        obj.contexts = []
        container = ARObject._find_child_element(element, "CONTEXTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.contexts.append(child_value)

        # Parse disabled_in_mode_description_instance_refs (list from container "DISABLED-IN-MODE-DESCRIPTION-INSTANCE-REFS")
        obj.disabled_in_mode_description_instance_refs = []
        container = ARObject._find_child_element(element, "DISABLED-IN-MODE-DESCRIPTION-INSTANCE-REFS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.disabled_in_mode_description_instance_refs.append(child_value)

        # Parse starts_on_event
        child = ARObject._find_child_element(element, "STARTS-ON-EVENT")
        if child is not None:
            starts_on_event_value = ARObject._deserialize_by_tag(child, "BswModuleEntity")
            obj.starts_on_event = starts_on_event_value

        return obj



class BswEventBuilder:
    """Builder for BswEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswEvent = BswEvent()

    def build(self) -> BswEvent:
        """Build and return BswEvent object.

        Returns:
            BswEvent instance
        """
        # TODO: Add validation
        return self._obj
