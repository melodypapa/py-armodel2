"""AbstractEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 541)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 204)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_InternalBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)
from abc import ABC, abstractmethod


class AbstractEvent(Identifiable, ABC):
    """AUTOSAR AbstractEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    activation: Optional[ExecutableEntity]
    def __init__(self) -> None:
        """Initialize AbstractEvent."""
        super().__init__()
        self.activation: Optional[ExecutableEntity] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractEvent":
        """Deserialize XML element to AbstractEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AbstractEvent, cls).deserialize(element)

        # Parse activation
        child = ARObject._find_child_element(element, "ACTIVATION")
        if child is not None:
            activation_value = ARObject._deserialize_by_tag(child, "ExecutableEntity")
            obj.activation = activation_value

        return obj



class AbstractEventBuilder:
    """Builder for AbstractEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractEvent = AbstractEvent()

    def build(self) -> AbstractEvent:
        """Build and return AbstractEvent object.

        Returns:
            AbstractEvent instance
        """
        # TODO: Add validation
        return self._obj
