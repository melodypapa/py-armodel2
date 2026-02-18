"""J1939DcmDm19Support AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 831)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)


class J1939DcmDm19Support(ServiceNeeds):
    """AUTOSAR J1939DcmDm19Support."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize J1939DcmDm19Support."""
        super().__init__()


class J1939DcmDm19SupportBuilder:
    """Builder for J1939DcmDm19Support."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939DcmDm19Support = J1939DcmDm19Support()

    def build(self) -> J1939DcmDm19Support:
        """Build and return J1939DcmDm19Support object.

        Returns:
            J1939DcmDm19Support instance
        """
        # TODO: Add validation
        return self._obj
