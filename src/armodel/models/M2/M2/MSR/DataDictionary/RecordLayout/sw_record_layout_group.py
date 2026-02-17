"""SwRecordLayoutGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 422)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2066)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_RecordLayout.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.MSR.DataDictionary.RecordLayout import (
    AsamRecordLayoutSemantics,
    RecordLayoutIteratorPoint,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)
from armodel.models.M2.MSR.DataDictionary.Axis.sw_generic_axis_param import (
    SwGenericAxisParam,
)


class SwRecordLayoutGroup(ARObject):
    """AUTOSAR SwRecordLayoutGroup."""

    def __init__(self) -> None:
        """Initialize SwRecordLayoutGroup."""
        super().__init__()
        self.category: Optional[AsamRecordLayoutSemantics] = None
        self.desc: Optional[MultiLanguageOverviewParagraph] = None
        self.short_label: Optional[Identifier] = None
        self.sw_generic_axis_param: Optional[SwGenericAxisParam] = None
        self.sw_record: Optional[RecordLayoutIteratorPoint] = None


class SwRecordLayoutGroupBuilder:
    """Builder for SwRecordLayoutGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwRecordLayoutGroup = SwRecordLayoutGroup()

    def build(self) -> SwRecordLayoutGroup:
        """Build and return SwRecordLayoutGroup object.

        Returns:
            SwRecordLayoutGroup instance
        """
        # TODO: Add validation
        return self._obj
