"""CryptoServiceNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 235)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 733)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)


class CryptoServiceNeeds(ServiceNeeds):
    """AUTOSAR CryptoServiceNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    algorithm_family: Optional[String]
    algorithm_mode: Optional[String]
    crypto_key: Optional[String]
    maximum_key: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize CryptoServiceNeeds."""
        super().__init__()
        self.algorithm_family: Optional[String] = None
        self.algorithm_mode: Optional[String] = None
        self.crypto_key: Optional[String] = None
        self.maximum_key: Optional[PositiveInteger] = None


class CryptoServiceNeedsBuilder:
    """Builder for CryptoServiceNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CryptoServiceNeeds = CryptoServiceNeeds()

    def build(self) -> CryptoServiceNeeds:
        """Build and return CryptoServiceNeeds object.

        Returns:
            CryptoServiceNeeds instance
        """
        # TODO: Add validation
        return self._obj
