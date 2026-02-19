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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcuResourceEstimation":
        """Deserialize XML element to EcuResourceEstimation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcuResourceEstimation object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse bsw_resource
        child = ARObject._find_child_element(element, "BSW-RESOURCE")
        if child is not None:
            bsw_resource_value = ARObject._deserialize_by_tag(child, "ResourceConsumption")
            obj.bsw_resource = bsw_resource_value

        # Parse ecu_instance
        child = ARObject._find_child_element(element, "ECU-INSTANCE")
        if child is not None:
            ecu_instance_value = ARObject._deserialize_by_tag(child, "EcuInstance")
            obj.ecu_instance = ecu_instance_value

        # Parse introduction
        child = ARObject._find_child_element(element, "INTRODUCTION")
        if child is not None:
            introduction_value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.introduction = introduction_value

        # Parse rte_resource
        child = ARObject._find_child_element(element, "RTE-RESOURCE")
        if child is not None:
            rte_resource_value = ARObject._deserialize_by_tag(child, "ResourceConsumption")
            obj.rte_resource = rte_resource_value

        # Parse sw_comp_to_ecu_refs (list from container "SW-COMP-TO-ECUS")
        obj.sw_comp_to_ecu_refs = []
        container = ARObject._find_child_element(element, "SW-COMP-TO-ECUS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_comp_to_ecu_refs.append(child_value)

        return obj



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
