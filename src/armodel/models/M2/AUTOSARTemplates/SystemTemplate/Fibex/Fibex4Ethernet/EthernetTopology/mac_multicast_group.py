"""MacMulticastGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 103)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MacAddressString,
)


class MacMulticastGroup(Identifiable):
    """AUTOSAR MacMulticastGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "mac_multicast": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # macMulticast
    }

    def __init__(self) -> None:
        """Initialize MacMulticastGroup."""
        super().__init__()
        self.mac_multicast: Optional[MacAddressString] = None


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
