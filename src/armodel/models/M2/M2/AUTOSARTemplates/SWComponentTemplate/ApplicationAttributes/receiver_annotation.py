"""ReceiverAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 153)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.sender_receiver_annotation import (
    SenderReceiverAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class ReceiverAnnotation(SenderReceiverAnnotation):
    """AUTOSAR ReceiverAnnotation."""

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
