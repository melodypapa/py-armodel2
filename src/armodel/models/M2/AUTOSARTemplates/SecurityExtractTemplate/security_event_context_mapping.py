"""SecurityEventContextMapping AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 32)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_mapping import (
    IdsMapping,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.idsm_instance import (
    IdsmInstance,
)
from abc import ABC, abstractmethod


class SecurityEventContextMapping(IdsMapping, ABC):
    """AUTOSAR SecurityEventContextMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    filter_chain: Optional[Any]
    idsm_instance: Optional[IdsmInstance]
    mapped_securities: list[Any]
    def __init__(self) -> None:
        """Initialize SecurityEventContextMapping."""
        super().__init__()
        self.filter_chain: Optional[Any] = None
        self.idsm_instance: Optional[IdsmInstance] = None
        self.mapped_securities: list[Any] = []


class SecurityEventContextMappingBuilder:
    """Builder for SecurityEventContextMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventContextMapping = SecurityEventContextMapping()

    def build(self) -> SecurityEventContextMapping:
        """Build and return SecurityEventContextMapping object.

        Returns:
            SecurityEventContextMapping instance
        """
        # TODO: Add validation
        return self._obj
