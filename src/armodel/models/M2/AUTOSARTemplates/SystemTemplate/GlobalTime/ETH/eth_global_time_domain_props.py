"""EthGlobalTimeDomainProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 867)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_ETH.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.abstract_global_time_domain_props import (
    AbstractGlobalTimeDomainProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.ETH import (
    EthGlobalTimeMessageFormatEnum,
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    crc_flags: Optional[EthTSynCrcFlags]
    destination: Optional[MacAddressString]
    fup_data_id_list: PositiveInteger
    manageds: list[Any]
    message: Optional[EthGlobalTimeMessageFormatEnum]
    vlan_priority: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize EthGlobalTimeDomainProps."""
        super().__init__()
        self.crc_flags: Optional[EthTSynCrcFlags] = None
        self.destination: Optional[MacAddressString] = None
        self.fup_data_id_list: PositiveInteger = None
        self.manageds: list[Any] = []
        self.message: Optional[EthGlobalTimeMessageFormatEnum] = None
        self.vlan_priority: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthGlobalTimeDomainProps":
        """Deserialize XML element to EthGlobalTimeDomainProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthGlobalTimeDomainProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EthGlobalTimeDomainProps, cls).deserialize(element)

        # Parse crc_flags
        child = ARObject._find_child_element(element, "CRC-FLAGS")
        if child is not None:
            crc_flags_value = ARObject._deserialize_by_tag(child, "EthTSynCrcFlags")
            obj.crc_flags = crc_flags_value

        # Parse destination
        child = ARObject._find_child_element(element, "DESTINATION")
        if child is not None:
            destination_value = child.text
            obj.destination = destination_value

        # Parse fup_data_id_list
        child = ARObject._find_child_element(element, "FUP-DATA-ID-LIST")
        if child is not None:
            fup_data_id_list_value = child.text
            obj.fup_data_id_list = fup_data_id_list_value

        # Parse manageds (list from container "MANAGEDS")
        obj.manageds = []
        container = ARObject._find_child_element(element, "MANAGEDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.manageds.append(child_value)

        # Parse message
        child = ARObject._find_child_element(element, "MESSAGE")
        if child is not None:
            message_value = EthGlobalTimeMessageFormatEnum.deserialize(child)
            obj.message = message_value

        # Parse vlan_priority
        child = ARObject._find_child_element(element, "VLAN-PRIORITY")
        if child is not None:
            vlan_priority_value = child.text
            obj.vlan_priority = vlan_priority_value

        return obj



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
