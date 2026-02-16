"""IEEE1722TpAcfConnection AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_connection import (
    IEEE1722TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus import (
    IEEE1722TpAcfBus,
)


class IEEE1722TpAcfConnection(IEEE1722TpConnection):
    """AUTOSAR IEEE1722TpAcfConnection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "acf_transporteds": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=IEEE1722TpAcfBus,
        ),  # acfTransporteds
        "collection": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # collection
        "mixed_bus_type": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # mixedBusType
    }

    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfConnection."""
        super().__init__()
        self.acf_transporteds: list[IEEE1722TpAcfBus] = []
        self.collection: Optional[TimeValue] = None
        self.mixed_bus_type: Optional[Boolean] = None


class IEEE1722TpAcfConnectionBuilder:
    """Builder for IEEE1722TpAcfConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpAcfConnection = IEEE1722TpAcfConnection()

    def build(self) -> IEEE1722TpAcfConnection:
        """Build and return IEEE1722TpAcfConnection object.

        Returns:
            IEEE1722TpAcfConnection instance
        """
        # TODO: Add validation
        return self._obj
