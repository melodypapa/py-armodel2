"""DiagnosticStorageConditionGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 200)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticConditionGroup.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticConditionGroup.diagnostic_condition_group import (
    DiagnosticConditionGroup,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticStorageConditionGroup(DiagnosticConditionGroup):
    """AUTOSAR DiagnosticStorageConditionGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    storages: list[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticStorageConditionGroup."""
        super().__init__()
        self.storages: list[Any] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticStorageConditionGroup":
        """Deserialize XML element to DiagnosticStorageConditionGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticStorageConditionGroup object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse storages (list)
        obj.storages = []
        for child in ARObject._find_all_child_elements(element, "STORAGES"):
            storages_value = child.text
            obj.storages.append(storages_value)

        return obj



class DiagnosticStorageConditionGroupBuilder:
    """Builder for DiagnosticStorageConditionGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticStorageConditionGroup = DiagnosticStorageConditionGroup()

    def build(self) -> DiagnosticStorageConditionGroup:
        """Build and return DiagnosticStorageConditionGroup object.

        Returns:
            DiagnosticStorageConditionGroup instance
        """
        # TODO: Add validation
        return self._obj
