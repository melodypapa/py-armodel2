"""EcuResourceEstimation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 260)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.resource_consumption import (
    ResourceConsumption,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.swc_to_ecu_mapping import (
    SwcToEcuMapping,
)


class EcuResourceEstimation(ARObject):
    """AUTOSAR EcuResourceEstimation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bsw_resource: Optional[ResourceConsumption]
    ecu_instance: Optional[EcuInstance]
    introduction: Optional[DocumentationBlock]
    rte_resource: Optional[ResourceConsumption]
    sw_comp_to_ecu_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize EcuResourceEstimation."""
        super().__init__()
        self.bsw_resource: Optional[ResourceConsumption] = None
        self.ecu_instance: Optional[EcuInstance] = None
        self.introduction: Optional[DocumentationBlock] = None
        self.rte_resource: Optional[ResourceConsumption] = None
        self.sw_comp_to_ecu_refs: list[ARRef] = []


class EcuResourceEstimationBuilder:
    """Builder for EcuResourceEstimation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcuResourceEstimation = EcuResourceEstimation()

    def build(self) -> EcuResourceEstimation:
        """Build and return EcuResourceEstimation object.

        Returns:
            EcuResourceEstimation instance
        """
        # TODO: Add validation
        return self._obj
