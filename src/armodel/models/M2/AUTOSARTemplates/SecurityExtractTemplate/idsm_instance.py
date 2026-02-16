"""IdsmInstance AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("block_states", None, False, True, BlockState),  # blockStates
        ("ecu_instance", None, False, False, EcuInstance),  # ecuInstance
        ("idsm_instance_id", None, True, False, None),  # idsmInstanceId
        ("idsm_module", None, False, False, IdsmModuleInstantiation),  # idsmModule
        ("rate_limitation", None, False, False, IdsmRateLimitation),  # rateLimitation
        ("signature", None, False, False, any (IdsmSignatureSupport)),  # signature
        ("timestamp", None, True, False, None),  # timestamp
        ("traffic_limitation", None, False, False, IdsmTrafficLimitation),  # trafficLimitation
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IdsmInstance to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IdsmInstance":
        """Create IdsmInstance from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IdsmInstance instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IdsmInstance since parent returns ARObject
        return cast("IdsmInstance", obj)


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
