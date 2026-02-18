"""DiagnosticEcuInstanceProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 207)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticContribution.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution import (
    DiagnosticObdSupportEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)


class DiagnosticEcuInstanceProps(DiagnosticCommonElement):
    """AUTOSAR DiagnosticEcuInstanceProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ecu_instances: list[EcuInstance]
    obd_support: Optional[DiagnosticObdSupportEnum]
    def __init__(self) -> None:
        """Initialize DiagnosticEcuInstanceProps."""
        super().__init__()
        self.ecu_instances: list[EcuInstance] = []
        self.obd_support: Optional[DiagnosticObdSupportEnum] = None


class DiagnosticEcuInstancePropsBuilder:
    """Builder for DiagnosticEcuInstanceProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEcuInstanceProps = DiagnosticEcuInstanceProps()

    def build(self) -> DiagnosticEcuInstanceProps:
        """Build and return DiagnosticEcuInstanceProps object.

        Returns:
            DiagnosticEcuInstanceProps instance
        """
        # TODO: Add validation
        return self._obj
