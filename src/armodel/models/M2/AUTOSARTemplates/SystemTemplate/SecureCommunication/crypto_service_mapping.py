"""CryptoServiceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 375)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from abc import ABC, abstractmethod


class CryptoServiceMapping(Identifiable, ABC):
    """AUTOSAR CryptoServiceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize CryptoServiceMapping."""
        super().__init__()


class CryptoServiceMappingBuilder:
    """Builder for CryptoServiceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CryptoServiceMapping = CryptoServiceMapping()

    def build(self) -> CryptoServiceMapping:
        """Build and return CryptoServiceMapping object.

        Returns:
            CryptoServiceMapping instance
        """
        # TODO: Add validation
        return self._obj
