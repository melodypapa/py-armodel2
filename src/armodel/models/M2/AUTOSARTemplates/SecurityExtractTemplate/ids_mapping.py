"""IdsMapping AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 62)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import (
    IdsCommonElement,
)


class IdsMapping(IdsCommonElement):
    """AUTOSAR IdsMapping."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize IdsMapping."""
        super().__init__()


class IdsMappingBuilder:
    """Builder for IdsMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsMapping = IdsMapping()

    def build(self) -> IdsMapping:
        """Build and return IdsMapping object.

        Returns:
            IdsMapping instance
        """
        # TODO: Add validation
        return self._obj
