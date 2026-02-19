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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.tlv_data_id_definition import (
    TlvDataIdDefinition,
)


class TlvDataIdDefinitionSet(ARElement):
    """AUTOSAR TlvDataIdDefinitionSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tlv_data_ids: list[TlvDataIdDefinition]
    def __init__(self) -> None:
        """Initialize TlvDataIdDefinitionSet."""
        super().__init__()
        self.tlv_data_ids: list[TlvDataIdDefinition] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TlvDataIdDefinitionSet":
        """Deserialize XML element to TlvDataIdDefinitionSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TlvDataIdDefinitionSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse tlv_data_ids (list)
        obj.tlv_data_ids = []
        for child in ARObject._find_all_child_elements(element, "TLV-DATA-IDS"):
            tlv_data_ids_value = ARObject._deserialize_by_tag(child, "TlvDataIdDefinition")
            obj.tlv_data_ids.append(tlv_data_ids_value)

        return obj



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
