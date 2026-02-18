"""SecureCommunicationProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 369)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SecureCommunicationProps(ARObject):
    """AUTOSAR SecureCommunicationProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    auth_data: Optional[PositiveInteger]
    authentication: Optional[PositiveInteger]
    data_id: Optional[PositiveInteger]
    freshness_value: Optional[PositiveInteger]
    message_link: Optional[PositiveInteger]
    secondary: Optional[PositiveInteger]
    secured_area: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SecureCommunicationProps."""
        super().__init__()
        self.auth_data: Optional[PositiveInteger] = None
        self.authentication: Optional[PositiveInteger] = None
        self.data_id: Optional[PositiveInteger] = None
        self.freshness_value: Optional[PositiveInteger] = None
        self.message_link: Optional[PositiveInteger] = None
        self.secondary: Optional[PositiveInteger] = None
        self.secured_area: Optional[PositiveInteger] = None


class SecureCommunicationPropsBuilder:
    """Builder for SecureCommunicationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecureCommunicationProps = SecureCommunicationProps()

    def build(self) -> SecureCommunicationProps:
        """Build and return SecureCommunicationProps object.

        Returns:
            SecureCommunicationProps instance
        """
        # TODO: Add validation
        return self._obj
