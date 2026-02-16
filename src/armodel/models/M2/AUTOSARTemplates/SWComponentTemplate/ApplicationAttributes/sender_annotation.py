"""SenderAnnotation AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.sender_receiver_annotation import (
    SenderReceiverAnnotation,
)


class SenderAnnotation(SenderReceiverAnnotation):
    """AUTOSAR SenderAnnotation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize SenderAnnotation."""
        super().__init__()


class SenderAnnotationBuilder:
    """Builder for SenderAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderAnnotation = SenderAnnotation()

    def build(self) -> SenderAnnotation:
        """Build and return SenderAnnotation object.

        Returns:
            SenderAnnotation instance
        """
        # TODO: Add validation
        return self._obj
