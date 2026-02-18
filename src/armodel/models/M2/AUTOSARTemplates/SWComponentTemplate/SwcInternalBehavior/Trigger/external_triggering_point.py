"""ExternalTriggeringPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 315)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 584)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_Trigger.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class ExternalTriggeringPoint(ARObject):
    """AUTOSAR ExternalTriggeringPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ident_ref: Optional[ARRef]
    trigger_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ExternalTriggeringPoint."""
        super().__init__()
        self.ident_ref: Optional[ARRef] = None
        self.trigger_ref: Optional[ARRef] = None


class ExternalTriggeringPointBuilder:
    """Builder for ExternalTriggeringPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ExternalTriggeringPoint = ExternalTriggeringPoint()

    def build(self) -> ExternalTriggeringPoint:
        """Build and return ExternalTriggeringPoint object.

        Returns:
            ExternalTriggeringPoint instance
        """
        # TODO: Add validation
        return self._obj
