"""EthGlobalTimeDomainProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.abstract_global_time_domain_props import (
    AbstractGlobalTimeDomainProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MacAddressString,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.ETH.eth_t_syn_crc_flags import (
    EthTSynCrcFlags,
)


class EthGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):
    """AUTOSAR EthGlobalTimeDomainProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("crc_flags", None, False, False, EthTSynCrcFlags),  # crcFlags
        ("destination", None, True, False, None),  # destination
        ("fup_data_id_list", None, True, False, None),  # fupDataIDList
        ("manageds", None, False, True, any (EthGlobalTime)),  # manageds
        ("message", None, False, False, EthGlobalTimeMessageFormatEnum),  # message
        ("vlan_priority", None, True, False, None),  # vlanPriority
    ]

    def __init__(self) -> None:
        """Initialize EthGlobalTimeDomainProps."""
        super().__init__()
        self.crc_flags: Optional[EthTSynCrcFlags] = None
        self.destination: Optional[MacAddressString] = None
        self.fup_data_id_list: PositiveInteger = None
        self.manageds: list[Any] = []
        self.message: Optional[EthGlobalTimeMessageFormatEnum] = None
        self.vlan_priority: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EthGlobalTimeDomainProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthGlobalTimeDomainProps":
        """Create EthGlobalTimeDomainProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EthGlobalTimeDomainProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EthGlobalTimeDomainProps since parent returns ARObject
        return cast("EthGlobalTimeDomainProps", obj)


class EthGlobalTimeDomainPropsBuilder:
    """Builder for EthGlobalTimeDomainProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthGlobalTimeDomainProps = EthGlobalTimeDomainProps()

    def build(self) -> EthGlobalTimeDomainProps:
        """Build and return EthGlobalTimeDomainProps object.

        Returns:
            EthGlobalTimeDomainProps instance
        """
        # TODO: Add validation
        return self._obj
