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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class ReceiverAnnotation(SenderReceiverAnnotation):
    """AUTOSAR ReceiverAnnotation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    signal_age: Optional[MultidimensionalTime]
    def __init__(self) -> None:
        """Initialize ReceiverAnnotation."""
        super().__init__()
        self.signal_age: Optional[MultidimensionalTime] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ReceiverAnnotation":
        """Deserialize XML element to ReceiverAnnotation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ReceiverAnnotation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ReceiverAnnotation, cls).deserialize(element)

        # Parse signal_age
        child = ARObject._find_child_element(element, "SIGNAL-AGE")
        if child is not None:
            signal_age_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.signal_age = signal_age_value

        return obj



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
