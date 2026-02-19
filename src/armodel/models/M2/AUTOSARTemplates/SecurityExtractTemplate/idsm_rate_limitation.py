"""IdsmRateLimitation AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 28)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
    PositiveInteger,
)


class IdsmRateLimitation(Identifiable):
    """AUTOSAR IdsmRateLimitation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    max_events_in: PositiveInteger
    time_interval: Float
    def __init__(self) -> None:
        """Initialize IdsmRateLimitation."""
        super().__init__()
        self.max_events_in: PositiveInteger = None
        self.time_interval: Float = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "IdsmRateLimitation":
        """Deserialize XML element to IdsmRateLimitation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IdsmRateLimitation object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse max_events_in
        child = ARObject._find_child_element(element, "MAX-EVENTS-IN")
        if child is not None:
            max_events_in_value = child.text
            obj.max_events_in = max_events_in_value

        # Parse time_interval
        child = ARObject._find_child_element(element, "TIME-INTERVAL")
        if child is not None:
            time_interval_value = child.text
            obj.time_interval = time_interval_value

        return obj



class IdsmRateLimitationBuilder:
    """Builder for IdsmRateLimitation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsmRateLimitation = IdsmRateLimitation()

    def build(self) -> IdsmRateLimitation:
        """Build and return IdsmRateLimitation object.

        Returns:
            IdsmRateLimitation instance
        """
        # TODO: Add validation
        return self._obj
