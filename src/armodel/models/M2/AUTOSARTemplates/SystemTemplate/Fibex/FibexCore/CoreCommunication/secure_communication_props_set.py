"""SecureCommunicationPropsSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 370)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)


class SecureCommunicationPropsSet(FibexElement):
    """AUTOSAR SecureCommunicationPropsSet."""

    authentications: list[Any]
    freshness_propses: list[Any]
    def __init__(self) -> None:
        """Initialize SecureCommunicationPropsSet."""
        super().__init__()
        self.authentications: list[Any] = []
        self.freshness_propses: list[Any] = []


class SecureCommunicationPropsSetBuilder:
    """Builder for SecureCommunicationPropsSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecureCommunicationPropsSet = SecureCommunicationPropsSet()

    def build(self) -> SecureCommunicationPropsSet:
        """Build and return SecureCommunicationPropsSet object.

        Returns:
            SecureCommunicationPropsSet instance
        """
        # TODO: Add validation
        return self._obj
