"""IEEE1722TpAcfCan AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus import (
    IEEE1722TpAcfBus,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_can import (
    IEEE1722TpAcfCan,
)


class IEEE1722TpAcfCan(IEEE1722TpAcfBus):
    """AUTOSAR IEEE1722TpAcfCan."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "message_type_message_type_enum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=IEEE1722TpAcfCan,
        ),  # messageTypeMessageTypeEnum
    }

    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfCan."""
        super().__init__()
        self.message_type_message_type_enum: Optional[IEEE1722TpAcfCan] = None


class IEEE1722TpAcfCanBuilder:
    """Builder for IEEE1722TpAcfCan."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpAcfCan = IEEE1722TpAcfCan()

    def build(self) -> IEEE1722TpAcfCan:
        """Build and return IEEE1722TpAcfCan object.

        Returns:
            IEEE1722TpAcfCan instance
        """
        # TODO: Add validation
        return self._obj
