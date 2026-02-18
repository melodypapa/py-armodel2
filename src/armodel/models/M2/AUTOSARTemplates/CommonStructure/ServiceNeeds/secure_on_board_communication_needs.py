"""SecureOnBoardCommunicationNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 824)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    VerificationStatusIndicationModeEnum,
)


class SecureOnBoardCommunicationNeeds(ServiceNeeds):
    """AUTOSAR SecureOnBoardCommunicationNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    verification: Optional[VerificationStatusIndicationModeEnum]
    def __init__(self) -> None:
        """Initialize SecureOnBoardCommunicationNeeds."""
        super().__init__()
        self.verification: Optional[VerificationStatusIndicationModeEnum] = None


class SecureOnBoardCommunicationNeedsBuilder:
    """Builder for SecureOnBoardCommunicationNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecureOnBoardCommunicationNeeds = SecureOnBoardCommunicationNeeds()

    def build(self) -> SecureOnBoardCommunicationNeeds:
        """Build and return SecureOnBoardCommunicationNeeds object.

        Returns:
            SecureOnBoardCommunicationNeeds instance
        """
        # TODO: Add validation
        return self._obj
