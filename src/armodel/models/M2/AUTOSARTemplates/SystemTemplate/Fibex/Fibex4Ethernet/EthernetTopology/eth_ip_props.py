"""EthIpProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 146)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv4_props import (
    Ipv4Props,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv6_props import (
    Ipv6Props,
)


class EthIpProps(ARElement):
    """AUTOSAR EthIpProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ipv4_props: Optional[Ipv4Props]
    ipv6_props: Optional[Ipv6Props]
    def __init__(self) -> None:
        """Initialize EthIpProps."""
        super().__init__()
        self.ipv4_props: Optional[Ipv4Props] = None
        self.ipv6_props: Optional[Ipv6Props] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthIpProps":
        """Deserialize XML element to EthIpProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthIpProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EthIpProps, cls).deserialize(element)

        # Parse ipv4_props
        child = ARObject._find_child_element(element, "IPV4-PROPS")
        if child is not None:
            ipv4_props_value = ARObject._deserialize_by_tag(child, "Ipv4Props")
            obj.ipv4_props = ipv4_props_value

        # Parse ipv6_props
        child = ARObject._find_child_element(element, "IPV6-PROPS")
        if child is not None:
            ipv6_props_value = ARObject._deserialize_by_tag(child, "Ipv6Props")
            obj.ipv6_props = ipv6_props_value

        return obj



class EthIpPropsBuilder:
    """Builder for EthIpProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthIpProps = EthIpProps()

    def build(self) -> EthIpProps:
        """Build and return EthIpProps object.

        Returns:
            EthIpProps instance
        """
        # TODO: Add validation
        return self._obj
