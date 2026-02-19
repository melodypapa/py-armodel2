"""IPduTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 348)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class IPduTiming(Describable):
    """AUTOSAR IPduTiming."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    minimum_delay: Optional[TimeValue]
    transmission: Optional[Any]
    def __init__(self) -> None:
        """Initialize IPduTiming."""
        super().__init__()
        self.minimum_delay: Optional[TimeValue] = None
        self.transmission: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "IPduTiming":
        """Deserialize XML element to IPduTiming object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IPduTiming object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse minimum_delay
        child = ARObject._find_child_element(element, "MINIMUM-DELAY")
        if child is not None:
            minimum_delay_value = child.text
            obj.minimum_delay = minimum_delay_value

        # Parse transmission
        child = ARObject._find_child_element(element, "TRANSMISSION")
        if child is not None:
            transmission_value = child.text
            obj.transmission = transmission_value

        return obj



class IPduTimingBuilder:
    """Builder for IPduTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IPduTiming = IPduTiming()

    def build(self) -> IPduTiming:
        """Build and return IPduTiming object.

        Returns:
            IPduTiming instance
        """
        # TODO: Add validation
        return self._obj
