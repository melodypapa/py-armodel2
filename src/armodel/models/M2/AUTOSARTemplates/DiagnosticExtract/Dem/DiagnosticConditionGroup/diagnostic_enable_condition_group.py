"""DiagnosticEnableConditionGroup AUTOSAR element.

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


class DiagnosticEnableConditionGroup(DiagnosticConditionGroup):
    """AUTOSAR DiagnosticEnableConditionGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    enable_conditions: list[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticEnableConditionGroup."""
        super().__init__()
        self.enable_conditions: list[Any] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEnableConditionGroup":
        """Deserialize XML element to DiagnosticEnableConditionGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEnableConditionGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEnableConditionGroup, cls).deserialize(element)

        # Parse enable_conditions (list from container "ENABLE-CONDITIONS")
        obj.enable_conditions = []
        container = ARObject._find_child_element(element, "ENABLE-CONDITIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.enable_conditions.append(child_value)

        return obj



class DiagnosticEnableConditionGroupBuilder:
    """Builder for DiagnosticEnableConditionGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnableConditionGroup = DiagnosticEnableConditionGroup()

    def build(self) -> DiagnosticEnableConditionGroup:
        """Build and return DiagnosticEnableConditionGroup object.

        Returns:
            DiagnosticEnableConditionGroup instance
        """
        # TODO: Add validation
        return self._obj
