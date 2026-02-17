"""CryptoServiceNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 235)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 733)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)


class CryptoServiceNeeds(ServiceNeeds):
    """AUTOSAR CryptoServiceNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "algorithm_family": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # algorithmFamily
        "algorithm_mode": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # algorithmMode
        "crypto_key": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # cryptoKey
        "maximum_key": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maximumKey
    }

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
