"""IEEE1722TpAcfLinPart AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus_part import (
    IEEE1722TpAcfBusPart,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class IEEE1722TpAcfLinPart(IEEE1722TpAcfBusPart):
    """AUTOSAR IEEE1722TpAcfLinPart."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "lin_identifier": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # linIdentifier
        "sdu": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PduTriggering,
        ),  # sdu
    }

    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfLinPart."""
        super().__init__()
        self.lin_identifier: Optional[PositiveInteger] = None
        self.sdu: Optional[PduTriggering] = None


class IEEE1722TpAcfLinPartBuilder:
    """Builder for IEEE1722TpAcfLinPart."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpAcfLinPart = IEEE1722TpAcfLinPart()

    def build(self) -> IEEE1722TpAcfLinPart:
        """Build and return IEEE1722TpAcfLinPart object.

        Returns:
            IEEE1722TpAcfLinPart instance
        """
        # TODO: Add validation
        return self._obj
