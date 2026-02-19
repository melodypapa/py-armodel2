"""InstantiationTimingEventProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 85)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.instantiation_rte_event_props import (
    InstantiationRTEEventProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class InstantiationTimingEventProps(InstantiationRTEEventProps):
    """AUTOSAR InstantiationTimingEventProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    period: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize InstantiationTimingEventProps."""
        super().__init__()
        self.period: Optional[TimeValue] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "InstantiationTimingEventProps":
        """Deserialize XML element to InstantiationTimingEventProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InstantiationTimingEventProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse period
        child = ARObject._find_child_element(element, "PERIOD")
        if child is not None:
            period_value = child.text
            obj.period = period_value

        return obj



class InstantiationTimingEventPropsBuilder:
    """Builder for InstantiationTimingEventProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InstantiationTimingEventProps = InstantiationTimingEventProps()

    def build(self) -> InstantiationTimingEventProps:
        """Build and return InstantiationTimingEventProps object.

        Returns:
            InstantiationTimingEventProps instance
        """
        # TODO: Add validation
        return self._obj
