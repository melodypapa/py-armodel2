"""ReceiverAnnotation AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.sender_receiver_annotation import (
    SenderReceiverAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class ReceiverAnnotation(SenderReceiverAnnotation):
    """AUTOSAR ReceiverAnnotation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "signal_age": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultidimensionalTime,
        ),  # signalAge
    }

    def __init__(self) -> None:
        """Initialize ReceiverAnnotation."""
        super().__init__()
        self.signal_age: Optional[MultidimensionalTime] = None


class ReceiverAnnotationBuilder:
    """Builder for ReceiverAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ReceiverAnnotation = ReceiverAnnotation()

    def build(self) -> ReceiverAnnotation:
        """Build and return ReceiverAnnotation object.

        Returns:
            ReceiverAnnotation instance
        """
        # TODO: Add validation
        return self._obj
