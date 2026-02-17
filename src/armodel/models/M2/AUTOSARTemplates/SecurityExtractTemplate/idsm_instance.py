"""IdsmInstance AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 44)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import (
    IdsCommonElement,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "block_states": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BlockState,
        ),  # blockStates
        "ecu_instance": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EcuInstance,
        ),  # ecuInstance
        "idsm_instance_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # idsmInstanceId
        "idsm_module": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=IdsmModuleInstantiation,
        ),  # idsmModule
        "rate_limitation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=IdsmRateLimitation,
        ),  # rateLimitation
        "signature": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (IdsmSignatureSupport),
        ),  # signature
        "timestamp": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timestamp
        "traffic_limitation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=IdsmTrafficLimitation,
        ),  # trafficLimitation
    }

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
