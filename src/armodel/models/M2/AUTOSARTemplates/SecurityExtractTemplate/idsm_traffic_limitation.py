"""IdsmTrafficLimitation AUTOSAR element.

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


class IdsmTrafficLimitation(Identifiable):
    """AUTOSAR IdsmTrafficLimitation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    max_bytes_in: Optional[PositiveInteger]
    time_interval: Optional[Float]
    def __init__(self) -> None:
        """Initialize IdsmTrafficLimitation."""
        super().__init__()
        self.max_bytes_in: Optional[PositiveInteger] = None
        self.time_interval: Optional[Float] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "IdsmTrafficLimitation":
        """Deserialize XML element to IdsmTrafficLimitation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IdsmTrafficLimitation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IdsmTrafficLimitation, cls).deserialize(element)

        # Parse max_bytes_in
        child = ARObject._find_child_element(element, "MAX-BYTES-IN")
        if child is not None:
            max_bytes_in_value = child.text
            obj.max_bytes_in = max_bytes_in_value

        # Parse time_interval
        child = ARObject._find_child_element(element, "TIME-INTERVAL")
        if child is not None:
            time_interval_value = child.text
            obj.time_interval = time_interval_value

        return obj



class IdsmTrafficLimitationBuilder:
    """Builder for IdsmTrafficLimitation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsmTrafficLimitation = IdsmTrafficLimitation()

    def build(self) -> IdsmTrafficLimitation:
        """Build and return IdsmTrafficLimitation object.

        Returns:
            IdsmTrafficLimitation instance
        """
        # TODO: Add validation
        return self._obj
