"""BswModeSwitchAckRequest AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class BswModeSwitchAckRequest(ARObject):
    """AUTOSAR BswModeSwitchAckRequest."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "timeout": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timeout
    }

    def __init__(self) -> None:
        """Initialize BswModeSwitchAckRequest."""
        super().__init__()
        self.timeout: Optional[TimeValue] = None


class BswModeSwitchAckRequestBuilder:
    """Builder for BswModeSwitchAckRequest."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModeSwitchAckRequest = BswModeSwitchAckRequest()

    def build(self) -> BswModeSwitchAckRequest:
        """Build and return BswModeSwitchAckRequest object.

        Returns:
            BswModeSwitchAckRequest instance
        """
        # TODO: Add validation
        return self._obj
