"""CanTpEcu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 610)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)


class CanTpEcu(ARObject):
    """AUTOSAR CanTpEcu."""

    cycle_time_main: Optional[TimeValue]
    ecu_instance: Optional[EcuInstance]
    def __init__(self) -> None:
        """Initialize CanTpEcu."""
        super().__init__()
        self.cycle_time_main: Optional[TimeValue] = None
        self.ecu_instance: Optional[EcuInstance] = None


class CanTpEcuBuilder:
    """Builder for CanTpEcu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanTpEcu = CanTpEcu()

    def build(self) -> CanTpEcu:
        """Build and return CanTpEcu object.

        Returns:
            CanTpEcu instance
        """
        # TODO: Add validation
        return self._obj
