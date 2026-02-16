"""Gateway AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.frame_mapping import (
    FrameMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.i_pdu_mapping import (
    IPduMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.i_signal_mapping import (
    ISignalMapping,
)


class Gateway(FibexElement):
    """AUTOSAR Gateway."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ecu", None, False, False, EcuInstance),  # ecu
        ("frame_mappings", None, False, True, FrameMapping),  # frameMappings
        ("i_pdu_mappings", None, False, True, IPduMapping),  # iPduMappings
        ("signal_mappings", None, False, True, ISignalMapping),  # signalMappings
    ]

    def __init__(self) -> None:
        """Initialize Gateway."""
        super().__init__()
        self.ecu: Optional[EcuInstance] = None
        self.frame_mappings: list[FrameMapping] = []
        self.i_pdu_mappings: list[IPduMapping] = []
        self.signal_mappings: list[ISignalMapping] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Gateway to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Gateway":
        """Create Gateway from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Gateway instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Gateway since parent returns ARObject
        return cast("Gateway", obj)


class GatewayBuilder:
    """Builder for Gateway."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Gateway = Gateway()

    def build(self) -> Gateway:
        """Build and return Gateway object.

        Returns:
            Gateway instance
        """
        # TODO: Add validation
        return self._obj
