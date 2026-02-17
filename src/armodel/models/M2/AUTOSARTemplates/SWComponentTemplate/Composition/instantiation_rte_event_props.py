"""InstantiationRTEEventProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 85)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)


class InstantiationRTEEventProps(ARObject):
    """AUTOSAR InstantiationRTEEventProps."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize InstantiationRTEEventProps."""
        super().__init__()
        self.refined_event: Optional[RTEEvent] = None
        self.short_label: Optional[Identifier] = None


class InstantiationRTEEventPropsBuilder:
    """Builder for InstantiationRTEEventProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InstantiationRTEEventProps = InstantiationRTEEventProps()

    def build(self) -> InstantiationRTEEventProps:
        """Build and return InstantiationRTEEventProps object.

        Returns:
            InstantiationRTEEventProps instance
        """
        # TODO: Add validation
        return self._obj
