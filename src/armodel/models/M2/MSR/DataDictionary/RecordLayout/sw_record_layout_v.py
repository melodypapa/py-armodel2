"""SwRecordLayoutV AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 421)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_RecordLayout.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    NameToken,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)
from armodel.models.M2.MSR.AsamHdo.BaseTypes.sw_base_type import (
    SwBaseType,
)
from armodel.models.M2.MSR.DataDictionary.Axis.sw_generic_axis_param import (
    SwGenericAxisParam,
)


class SwRecordLayoutV(ARObject):
    """AUTOSAR SwRecordLayoutV."""

    def __init__(self) -> None:
        """Initialize SwRecordLayoutV."""
        super().__init__()
        self.base_type: Optional[SwBaseType] = None
        self.desc: Optional[MultiLanguageOverviewParagraph] = None
        self.short_label: Optional[Identifier] = None
        self.sw_generic_axis_param: Optional[SwGenericAxisParam] = None
        self.sw_record: Optional[NameToken] = None


class SwRecordLayoutVBuilder:
    """Builder for SwRecordLayoutV."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwRecordLayoutV = SwRecordLayoutV()

    def build(self) -> SwRecordLayoutV:
        """Build and return SwRecordLayoutV object.

        Returns:
            SwRecordLayoutV instance
        """
        # TODO: Add validation
        return self._obj
