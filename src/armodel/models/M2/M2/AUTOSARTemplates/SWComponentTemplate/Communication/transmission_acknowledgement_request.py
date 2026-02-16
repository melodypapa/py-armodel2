"""TransmissionAcknowledgementRequest AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class TransmissionAcknowledgementRequest(ARObject):
    """AUTOSAR TransmissionAcknowledgementRequest."""

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
        """Initialize TransmissionAcknowledgementRequest."""
        super().__init__()
        self.timeout: Optional[TimeValue] = None


class TransmissionAcknowledgementRequestBuilder:
    """Builder for TransmissionAcknowledgementRequest."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransmissionAcknowledgementRequest = TransmissionAcknowledgementRequest()

    def build(self) -> TransmissionAcknowledgementRequest:
        """Build and return TransmissionAcknowledgementRequest object.

        Returns:
            TransmissionAcknowledgementRequest instance
        """
        # TODO: Add validation
        return self._obj
