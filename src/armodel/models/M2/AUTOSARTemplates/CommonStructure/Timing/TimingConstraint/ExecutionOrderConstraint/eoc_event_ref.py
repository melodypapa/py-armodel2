"""EOCEventRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 120)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_ExecutionOrderConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint.eoc_executable_entity_ref_abstract import (
    EOCExecutableEntityRefAbstract,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.abstract_event import (
    AbstractEvent,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation.bsw_implementation import (
    BswImplementation,
)


class EOCEventRef(EOCExecutableEntityRefAbstract):
    """AUTOSAR EOCEventRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bsw_module: Optional[BswImplementation]
    component: Optional[Any]
    event: Optional[AbstractEvent]
    successors: list[Any]
    def __init__(self) -> None:
        """Initialize EOCEventRef."""
        super().__init__()
        self.bsw_module: Optional[BswImplementation] = None
        self.component: Optional[Any] = None
        self.event: Optional[AbstractEvent] = None
        self.successors: list[Any] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EOCEventRef":
        """Deserialize XML element to EOCEventRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EOCEventRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EOCEventRef, cls).deserialize(element)

        # Parse bsw_module
        child = ARObject._find_child_element(element, "BSW-MODULE")
        if child is not None:
            bsw_module_value = ARObject._deserialize_by_tag(child, "BswImplementation")
            obj.bsw_module = bsw_module_value

        # Parse component
        child = ARObject._find_child_element(element, "COMPONENT")
        if child is not None:
            component_value = child.text
            obj.component = component_value

        # Parse event
        child = ARObject._find_child_element(element, "EVENT")
        if child is not None:
            event_value = ARObject._deserialize_by_tag(child, "AbstractEvent")
            obj.event = event_value

        # Parse successors (list from container "SUCCESSORS")
        obj.successors = []
        container = ARObject._find_child_element(element, "SUCCESSORS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.successors.append(child_value)

        return obj



class EOCEventRefBuilder:
    """Builder for EOCEventRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EOCEventRef = EOCEventRef()

    def build(self) -> EOCEventRef:
        """Build and return EOCEventRef object.

        Returns:
            EOCEventRef instance
        """
        # TODO: Add validation
        return self._obj
