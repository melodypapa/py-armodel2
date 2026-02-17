"""TlvDataIdDefinitionSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 830)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.tlv_data_id_definition import (
    TlvDataIdDefinition,
)


class TlvDataIdDefinitionSet(ARElement):
    """AUTOSAR TlvDataIdDefinitionSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "tlv_data_ids": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=TlvDataIdDefinition,
        ),  # tlvDataIds
    }

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
