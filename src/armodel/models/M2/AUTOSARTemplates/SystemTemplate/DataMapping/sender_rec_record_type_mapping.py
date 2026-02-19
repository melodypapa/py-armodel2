"""SenderRecRecordTypeMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 235)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_composite_type_mapping import (
    SenderRecCompositeTypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class SenderRecRecordTypeMapping(SenderRecCompositeTypeMapping):
    """AUTOSAR SenderRecRecordTypeMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    record_elements: list[Any]
    def __init__(self) -> None:
        """Initialize SenderRecRecordTypeMapping."""
        super().__init__()
        self.record_elements: list[Any] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderRecRecordTypeMapping":
        """Deserialize XML element to SenderRecRecordTypeMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderRecRecordTypeMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse record_elements (list)
        obj.record_elements = []
        for child in ARObject._find_all_child_elements(element, "RECORD-ELEMENTS"):
            record_elements_value = child.text
            obj.record_elements.append(record_elements_value)

        return obj



class SenderRecRecordTypeMappingBuilder:
    """Builder for SenderRecRecordTypeMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderRecRecordTypeMapping = SenderRecRecordTypeMapping()

    def build(self) -> SenderRecRecordTypeMapping:
        """Build and return SenderRecRecordTypeMapping object.

        Returns:
            SenderRecRecordTypeMapping instance
        """
        # TODO: Add validation
        return self._obj
