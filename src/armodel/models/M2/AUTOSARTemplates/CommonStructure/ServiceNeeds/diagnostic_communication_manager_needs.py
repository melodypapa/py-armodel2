"""DiagnosticCommunicationManagerNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 248)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 779)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticCommunicationManagerNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticCommunicationManagerNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    service_request: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticCommunicationManagerNeeds."""
        super().__init__()
        self.service_request: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticCommunicationManagerNeeds":
        """Deserialize XML element to DiagnosticCommunicationManagerNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticCommunicationManagerNeeds object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse service_request
        child = ARObject._find_child_element(element, "SERVICE-REQUEST")
        if child is not None:
            service_request_value = child.text
            obj.service_request = service_request_value

        return obj



class DiagnosticCommunicationManagerNeedsBuilder:
    """Builder for DiagnosticCommunicationManagerNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticCommunicationManagerNeeds = DiagnosticCommunicationManagerNeeds()

    def build(self) -> DiagnosticCommunicationManagerNeeds:
        """Build and return DiagnosticCommunicationManagerNeeds object.

        Returns:
            DiagnosticCommunicationManagerNeeds instance
        """
        # TODO: Add validation
        return self._obj
