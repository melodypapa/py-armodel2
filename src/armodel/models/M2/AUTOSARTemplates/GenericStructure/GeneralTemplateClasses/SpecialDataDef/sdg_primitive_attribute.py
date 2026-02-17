"""SdgPrimitiveAttribute AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 100)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_abstract_primitive_attribute import (
    SdgAbstractPrimitiveAttribute,
)


class SdgPrimitiveAttribute(SdgAbstractPrimitiveAttribute):
    """AUTOSAR SdgPrimitiveAttribute."""

    def __init__(self) -> None:
        """Initialize SdgPrimitiveAttribute."""
        super().__init__()


class SdgPrimitiveAttributeBuilder:
    """Builder for SdgPrimitiveAttribute."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgPrimitiveAttribute = SdgPrimitiveAttribute()

    def build(self) -> SdgPrimitiveAttribute:
        """Build and return SdgPrimitiveAttribute object.

        Returns:
            SdgPrimitiveAttribute instance
        """
        # TODO: Add validation
        return self._obj
