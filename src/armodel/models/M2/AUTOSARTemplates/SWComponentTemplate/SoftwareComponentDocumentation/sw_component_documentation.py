"""SwComponentDocumentation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 337)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 697)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 465)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SoftwareComponentDocumentation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.Chapters.chapter import (
    Chapter,
)


class SwComponentDocumentation(ARObject):
    """AUTOSAR SwComponentDocumentation."""

    chapters: list[Chapter]
    sw_calibration: Optional[Chapter]
    sw_carb_doc: Optional[Chapter]
    sw_diagnostics: Optional[Chapter]
    sw_feature_def: Optional[Chapter]
    sw_feature_desc: Optional[Chapter]
    sw_maintenance: Optional[Chapter]
    sw_test_desc: Optional[Chapter]
    def __init__(self) -> None:
        """Initialize SwComponentDocumentation."""
        super().__init__()
        self.chapters: list[Chapter] = []
        self.sw_calibration: Optional[Chapter] = None
        self.sw_carb_doc: Optional[Chapter] = None
        self.sw_diagnostics: Optional[Chapter] = None
        self.sw_feature_def: Optional[Chapter] = None
        self.sw_feature_desc: Optional[Chapter] = None
        self.sw_maintenance: Optional[Chapter] = None
        self.sw_test_desc: Optional[Chapter] = None


class SwComponentDocumentationBuilder:
    """Builder for SwComponentDocumentation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwComponentDocumentation = SwComponentDocumentation()

    def build(self) -> SwComponentDocumentation:
        """Build and return SwComponentDocumentation object.

        Returns:
            SwComponentDocumentation instance
        """
        # TODO: Add validation
        return self._obj
