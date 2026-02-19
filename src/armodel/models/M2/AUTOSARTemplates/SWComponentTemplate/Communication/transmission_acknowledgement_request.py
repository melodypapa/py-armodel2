"""TransmissionAcknowledgementRequest AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 180)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class TransmissionAcknowledgementRequest(ARObject):
    """AUTOSAR TransmissionAcknowledgementRequest."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    timeout: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize TransmissionAcknowledgementRequest."""
        super().__init__()
        self.timeout: Optional[TimeValue] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransmissionAcknowledgementRequest":
        """Deserialize XML element to TransmissionAcknowledgementRequest object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TransmissionAcknowledgementRequest object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse timeout
        child = ARObject._find_child_element(element, "TIMEOUT")
        if child is not None:
            timeout_value = child.text
            obj.timeout = timeout_value

        return obj



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
