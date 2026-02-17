"""SenderRecCompositeTypeMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 235)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class SenderRecCompositeTypeMapping(ARObject):
    """AUTOSAR SenderRecCompositeTypeMapping."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize SenderRecCompositeTypeMapping."""
        super().__init__()


class SenderRecCompositeTypeMappingBuilder:
    """Builder for SenderRecCompositeTypeMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderRecCompositeTypeMapping = SenderRecCompositeTypeMapping()

    def build(self) -> SenderRecCompositeTypeMapping:
        """Build and return SenderRecCompositeTypeMapping object.

        Returns:
            SenderRecCompositeTypeMapping instance
        """
        # TODO: Add validation
        return self._obj
