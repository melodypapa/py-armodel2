"""SwRecordLayout AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 421)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2066)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_RecordLayout.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.MSR.DataDictionary.RecordLayout.sw_record_layout_group import (
    SwRecordLayoutGroup,
)


class SwRecordLayout(ARElement):
    """AUTOSAR SwRecordLayout."""

    sw_record: Optional[SwRecordLayoutGroup]
    def __init__(self) -> None:
        """Initialize SwRecordLayout."""
        super().__init__()
        self.sw_record: Optional[SwRecordLayoutGroup] = None


class SwRecordLayoutBuilder:
    """Builder for SwRecordLayout."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwRecordLayout = SwRecordLayout()

    def build(self) -> SwRecordLayout:
        """Build and return SwRecordLayout object.

        Returns:
            SwRecordLayout instance
        """
        # TODO: Add validation
        return self._obj
