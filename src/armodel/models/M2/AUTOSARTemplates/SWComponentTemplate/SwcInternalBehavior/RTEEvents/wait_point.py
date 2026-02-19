"""WaitPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 550)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
        RTEEvent,
    )



class WaitPoint(Identifiable):
    """AUTOSAR WaitPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    timeout: Optional[TimeValue]
    trigger: Optional[RTEEvent]
    def __init__(self) -> None:
        """Initialize WaitPoint."""
        super().__init__()
        self.timeout: Optional[TimeValue] = None
        self.trigger: Optional[RTEEvent] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "WaitPoint":
        """Deserialize XML element to WaitPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized WaitPoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(WaitPoint, cls).deserialize(element)

        # Parse timeout
        child = ARObject._find_child_element(element, "TIMEOUT")
        if child is not None:
            timeout_value = child.text
            obj.timeout = timeout_value

        # Parse trigger
        child = ARObject._find_child_element(element, "TRIGGER")
        if child is not None:
            trigger_value = ARObject._deserialize_by_tag(child, "RTEEvent")
            obj.trigger = trigger_value

        return obj



class WaitPointBuilder:
    """Builder for WaitPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: WaitPoint = WaitPoint()

    def build(self) -> WaitPoint:
        """Build and return WaitPoint object.

        Returns:
            WaitPoint instance
        """
        # TODO: Add validation
        return self._obj
