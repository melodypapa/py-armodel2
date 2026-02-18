"""TDEventVfbPort AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 52)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 221)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb import (
    TDEventVfb,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.Port.port_prototype_blueprint import (
    PortPrototypeBlueprint,
)
from abc import ABC, abstractmethod


class TDEventVfbPort(TDEventVfb, ABC):
    """AUTOSAR TDEventVfbPort."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    is_external: Optional[Boolean]
    port_ref: Optional[ARRef]
    port_prototype_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize TDEventVfbPort."""
        super().__init__()
        self.is_external: Optional[Boolean] = None
        self.port_ref: Optional[ARRef] = None
        self.port_prototype_ref: Optional[ARRef] = None


class TDEventVfbPortBuilder:
    """Builder for TDEventVfbPort."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventVfbPort = TDEventVfbPort()

    def build(self) -> TDEventVfbPort:
        """Build and return TDEventVfbPort object.

        Returns:
            TDEventVfbPort instance
        """
        # TODO: Add validation
        return self._obj
