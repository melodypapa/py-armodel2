"""DcmIPdu AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)


class DcmIPdu(IPdu):
    """AUTOSAR DcmIPdu."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "diag_pdu_type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagPduType,
        ),  # diagPduType
    }

    def __init__(self) -> None:
        """Initialize DcmIPdu."""
        super().__init__()
        self.diag_pdu_type: Optional[DiagPduType] = None


class DcmIPduBuilder:
    """Builder for DcmIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DcmIPdu = DcmIPdu()

    def build(self) -> DcmIPdu:
        """Build and return DcmIPdu object.

        Returns:
            DcmIPdu instance
        """
        # TODO: Add validation
        return self._obj
