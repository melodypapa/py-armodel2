"""FlexrayTpEcu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 596)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)


class FlexrayTpEcu(ARObject):
    """AUTOSAR FlexrayTpEcu."""

    def __init__(self) -> None:
        """Initialize FlexrayTpEcu."""
        super().__init__()
        self.cancellation: Optional[Boolean] = None
        self.cycle_time_main: Optional[TimeValue] = None
        self.ecu_instance: Optional[EcuInstance] = None
        self.full_duplex: Optional[Boolean] = None


class FlexrayTpEcuBuilder:
    """Builder for FlexrayTpEcu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayTpEcu = FlexrayTpEcu()

    def build(self) -> FlexrayTpEcu:
        """Build and return FlexrayTpEcu object.

        Returns:
            FlexrayTpEcu instance
        """
        # TODO: Add validation
        return self._obj
