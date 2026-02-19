"""IdsmInstance AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 44)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import (
    IdsCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.block_state import (
    BlockState,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.IntrusionDetectionSystem.idsm_module_instantiation import (
    IdsmModuleInstantiation,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.idsm_rate_limitation import (
    IdsmRateLimitation,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.idsm_traffic_limitation import (
    IdsmTrafficLimitation,
)


class IdsmInstance(IdsCommonElement):
    """AUTOSAR IdsmInstance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    block_states: list[BlockState]
    ecu_instance: Optional[EcuInstance]
    idsm_instance_id: Optional[PositiveInteger]
    idsm_module: Optional[IdsmModuleInstantiation]
    rate_limitation: Optional[IdsmRateLimitation]
    signature: Optional[Any]
    timestamp: Optional[String]
    traffic_limitation: Optional[IdsmTrafficLimitation]
    def __init__(self) -> None:
        """Initialize IdsmInstance."""
        super().__init__()
        self.block_states: list[BlockState] = []
        self.ecu_instance: Optional[EcuInstance] = None
        self.idsm_instance_id: Optional[PositiveInteger] = None
        self.idsm_module: Optional[IdsmModuleInstantiation] = None
        self.rate_limitation: Optional[IdsmRateLimitation] = None
        self.signature: Optional[Any] = None
        self.timestamp: Optional[String] = None
        self.traffic_limitation: Optional[IdsmTrafficLimitation] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "IdsmInstance":
        """Deserialize XML element to IdsmInstance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IdsmInstance object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse block_states (list)
        obj.block_states = []
        for child in ARObject._find_all_child_elements(element, "BLOCK-STATES"):
            block_states_value = ARObject._deserialize_by_tag(child, "BlockState")
            obj.block_states.append(block_states_value)

        # Parse ecu_instance
        child = ARObject._find_child_element(element, "ECU-INSTANCE")
        if child is not None:
            ecu_instance_value = ARObject._deserialize_by_tag(child, "EcuInstance")
            obj.ecu_instance = ecu_instance_value

        # Parse idsm_instance_id
        child = ARObject._find_child_element(element, "IDSM-INSTANCE-ID")
        if child is not None:
            idsm_instance_id_value = child.text
            obj.idsm_instance_id = idsm_instance_id_value

        # Parse idsm_module
        child = ARObject._find_child_element(element, "IDSM-MODULE")
        if child is not None:
            idsm_module_value = ARObject._deserialize_by_tag(child, "IdsmModuleInstantiation")
            obj.idsm_module = idsm_module_value

        # Parse rate_limitation
        child = ARObject._find_child_element(element, "RATE-LIMITATION")
        if child is not None:
            rate_limitation_value = ARObject._deserialize_by_tag(child, "IdsmRateLimitation")
            obj.rate_limitation = rate_limitation_value

        # Parse signature
        child = ARObject._find_child_element(element, "SIGNATURE")
        if child is not None:
            signature_value = child.text
            obj.signature = signature_value

        # Parse timestamp
        child = ARObject._find_child_element(element, "TIMESTAMP")
        if child is not None:
            timestamp_value = child.text
            obj.timestamp = timestamp_value

        # Parse traffic_limitation
        child = ARObject._find_child_element(element, "TRAFFIC-LIMITATION")
        if child is not None:
            traffic_limitation_value = ARObject._deserialize_by_tag(child, "IdsmTrafficLimitation")
            obj.traffic_limitation = traffic_limitation_value

        return obj



class IdsmInstanceBuilder:
    """Builder for IdsmInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsmInstance = IdsmInstance()

    def build(self) -> IdsmInstance:
        """Build and return IdsmInstance object.

        Returns:
            IdsmInstance instance
        """
        # TODO: Add validation
        return self._obj
