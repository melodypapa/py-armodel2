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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEcuInstanceProps":
        """Deserialize XML element to DiagnosticEcuInstanceProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEcuInstanceProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEcuInstanceProps, cls).deserialize(element)

        # Parse ecu_instances (list from container "ECU-INSTANCES")
        obj.ecu_instances = []
        container = ARObject._find_child_element(element, "ECU-INSTANCES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ecu_instances.append(child_value)

        # Parse obd_support
        child = ARObject._find_child_element(element, "OBD-SUPPORT")
        if child is not None:
            obd_support_value = DiagnosticObdSupportEnum.deserialize(child)
            obj.obd_support = obd_support_value

        return obj



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
