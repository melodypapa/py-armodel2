"""TlvDataIdDefinitionSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 830)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.tlv_data_id_definition import (
    TlvDataIdDefinition,
)


class TlvDataIdDefinitionSet(ARElement):
    """AUTOSAR TlvDataIdDefinitionSet."""

    tlv_data_ids: list[TlvDataIdDefinition]
    def __init__(self) -> None:
        """Initialize TlvDataIdDefinitionSet."""
        super().__init__()
        self.tlv_data_ids: list[TlvDataIdDefinition] = []


class TlvDataIdDefinitionSetBuilder:
    """Builder for TlvDataIdDefinitionSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TlvDataIdDefinitionSet = TlvDataIdDefinitionSet()

    def build(self) -> TlvDataIdDefinitionSet:
        """Build and return TlvDataIdDefinitionSet object.

        Returns:
            TlvDataIdDefinitionSet instance
        """
        # TODO: Add validation
        return self._obj
