"""SecureCommunicationAuthenticationProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 371)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SecureCommunicationAuthenticationProps(Identifiable):
    """AUTOSAR SecureCommunicationAuthenticationProps."""

    auth_info_tx: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SecureCommunicationAuthenticationProps."""
        super().__init__()
        self.auth_info_tx: Optional[PositiveInteger] = None


class SecureCommunicationAuthenticationPropsBuilder:
    """Builder for SecureCommunicationAuthenticationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecureCommunicationAuthenticationProps = SecureCommunicationAuthenticationProps()

    def build(self) -> SecureCommunicationAuthenticationProps:
        """Build and return SecureCommunicationAuthenticationProps object.

        Returns:
            SecureCommunicationAuthenticationProps instance
        """
        # TODO: Add validation
        return self._obj
