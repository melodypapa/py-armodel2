"""NPdu AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)


class NPdu(IPdu):
    """AUTOSAR NPdu."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize NPdu."""
        super().__init__()


class NPduBuilder:
    """Builder for NPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NPdu = NPdu()

    def build(self) -> NPdu:
        """Build and return NPdu object.

        Returns:
            NPdu instance
        """
        # TODO: Add validation
        return self._obj
