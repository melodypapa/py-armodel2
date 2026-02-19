"""TDEventBswInternalBehavior AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 73)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import (
    BswModuleEntity,
)


class TDEventBswInternalBehavior(TimingDescriptionEvent):
    """AUTOSAR TDEventBswInternalBehavior."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bsw_module_entity_entity: Optional[BswModuleEntity]
    td_event_bsw_behavior_type: Optional[Any]
    def __init__(self) -> None:
        """Initialize TDEventBswInternalBehavior."""
        super().__init__()
        self.bsw_module_entity_entity: Optional[BswModuleEntity] = None
        self.td_event_bsw_behavior_type: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventBswInternalBehavior":
        """Deserialize XML element to TDEventBswInternalBehavior object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventBswInternalBehavior object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse bsw_module_entity_entity
        child = ARObject._find_child_element(element, "BSW-MODULE-ENTITY-ENTITY")
        if child is not None:
            bsw_module_entity_entity_value = ARObject._deserialize_by_tag(child, "BswModuleEntity")
            obj.bsw_module_entity_entity = bsw_module_entity_entity_value

        # Parse td_event_bsw_behavior_type
        child = ARObject._find_child_element(element, "TD-EVENT-BSW-BEHAVIOR-TYPE")
        if child is not None:
            td_event_bsw_behavior_type_value = child.text
            obj.td_event_bsw_behavior_type = td_event_bsw_behavior_type_value

        return obj



class TDEventBswInternalBehaviorBuilder:
    """Builder for TDEventBswInternalBehavior."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventBswInternalBehavior = TDEventBswInternalBehavior()

    def build(self) -> TDEventBswInternalBehavior:
        """Build and return TDEventBswInternalBehavior object.

        Returns:
            TDEventBswInternalBehavior instance
        """
        # TODO: Add validation
        return self._obj
