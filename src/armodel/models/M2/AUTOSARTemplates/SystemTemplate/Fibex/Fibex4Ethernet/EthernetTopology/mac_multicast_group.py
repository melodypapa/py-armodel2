"""MacMulticastGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 103)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MacAddressString,
)


class MacMulticastGroup(Identifiable):
    """AUTOSAR MacMulticastGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mac_multicast: Optional[MacAddressString]
    def __init__(self) -> None:
        """Initialize MacMulticastGroup."""
        super().__init__()
        self.mac_multicast: Optional[MacAddressString] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "MacMulticastGroup":
        """Deserialize XML element to MacMulticastGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MacMulticastGroup object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse mac_multicast
        child = ARObject._find_child_element(element, "MAC-MULTICAST")
        if child is not None:
            mac_multicast_value = child.text
            obj.mac_multicast = mac_multicast_value

        return obj



class MacMulticastGroupBuilder:
    """Builder for MacMulticastGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MacMulticastGroup = MacMulticastGroup()

    def build(self) -> MacMulticastGroup:
        """Build and return MacMulticastGroup object.

        Returns:
            MacMulticastGroup instance
        """
        # TODO: Add validation
        return self._obj
