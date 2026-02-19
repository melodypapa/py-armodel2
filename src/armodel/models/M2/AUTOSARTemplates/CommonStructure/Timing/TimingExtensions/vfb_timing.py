"""VfbTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 24)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 223)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingExtensions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.timing_extension import (
    TimingExtension,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import (
    SwComponentType,
)


class VfbTiming(TimingExtension):
    """AUTOSAR VfbTiming."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    component: Optional[SwComponentType]
    def __init__(self) -> None:
        """Initialize VfbTiming."""
        super().__init__()
        self.component: Optional[SwComponentType] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "VfbTiming":
        """Deserialize XML element to VfbTiming object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized VfbTiming object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(VfbTiming, cls).deserialize(element)

        # Parse component
        child = ARObject._find_child_element(element, "COMPONENT")
        if child is not None:
            component_value = ARObject._deserialize_by_tag(child, "SwComponentType")
            obj.component = component_value

        return obj



class VfbTimingBuilder:
    """Builder for VfbTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VfbTiming = VfbTiming()

    def build(self) -> VfbTiming:
        """Build and return VfbTiming object.

        Returns:
            VfbTiming instance
        """
        # TODO: Add validation
        return self._obj
