"""CouplingPortRatePolicy AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_rate_policy import (
    CouplingPortRatePolicy,
)


class CouplingPortRatePolicy(ARObject):
    """AUTOSAR CouplingPortRatePolicy."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_length", None, True, False, None),  # dataLength
        ("policy_action", None, False, False, CouplingPortRatePolicy),  # policyAction
        ("priority", None, True, False, None),  # priority
        ("time_interval", None, True, False, None),  # timeInterval
        ("v_lans", None, False, True, any (EthernetPhysical)),  # vLans
    ]

    def __init__(self) -> None:
        """Initialize CouplingPortRatePolicy."""
        super().__init__()
        self.data_length: Optional[PositiveInteger] = None
        self.policy_action: Optional[CouplingPortRatePolicy] = None
        self.priority: Optional[PositiveInteger] = None
        self.time_interval: Optional[TimeValue] = None
        self.v_lans: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CouplingPortRatePolicy to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPortRatePolicy":
        """Create CouplingPortRatePolicy from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CouplingPortRatePolicy instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CouplingPortRatePolicy since parent returns ARObject
        return cast("CouplingPortRatePolicy", obj)


class CouplingPortRatePolicyBuilder:
    """Builder for CouplingPortRatePolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPortRatePolicy = CouplingPortRatePolicy()

    def build(self) -> CouplingPortRatePolicy:
        """Build and return CouplingPortRatePolicy object.

        Returns:
            CouplingPortRatePolicy instance
        """
        # TODO: Add validation
        return self._obj
