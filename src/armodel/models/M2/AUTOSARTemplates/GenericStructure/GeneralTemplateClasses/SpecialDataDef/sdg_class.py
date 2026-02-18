"""SdgClass AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 99)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 207)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_element_with_gid import (
    SdgElementWithGid,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    MetaClassName,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_attribute import (
    SdgAttribute,
)
from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable_text import (
    TraceableText,
)


class SdgClass(SdgElementWithGid):
    """AUTOSAR SdgClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    attributes: list[SdgAttribute]
    caption: Optional[Boolean]
    extends_meta: Optional[MetaClassName]
    sdg_constraints: list[TraceableText]
    def __init__(self) -> None:
        """Initialize SdgClass."""
        super().__init__()
        self.attributes: list[SdgAttribute] = []
        self.caption: Optional[Boolean] = None
        self.extends_meta: Optional[MetaClassName] = None
        self.sdg_constraints: list[TraceableText] = []


class SdgClassBuilder:
    """Builder for SdgClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgClass = SdgClass()

    def build(self) -> SdgClass:
        """Build and return SdgClass object.

        Returns:
            SdgClass instance
        """
        # TODO: Add validation
        return self._obj
