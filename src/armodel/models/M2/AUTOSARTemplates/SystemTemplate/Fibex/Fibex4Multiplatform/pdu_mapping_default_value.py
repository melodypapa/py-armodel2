"""PduMappingDefaultValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 841)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Multiplatform.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.default_value_element import (
    DefaultValueElement,
)


class PduMappingDefaultValue(ARObject):
    """AUTOSAR PduMappingDefaultValue."""

    default_values: list[DefaultValueElement]
    def __init__(self) -> None:
        """Initialize PduMappingDefaultValue."""
        super().__init__()
        self.default_values: list[DefaultValueElement] = []


class PduMappingDefaultValueBuilder:
    """Builder for PduMappingDefaultValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PduMappingDefaultValue = PduMappingDefaultValue()

    def build(self) -> PduMappingDefaultValue:
        """Build and return PduMappingDefaultValue object.

        Returns:
            PduMappingDefaultValue instance
        """
        # TODO: Add validation
        return self._obj
