"""XrefTarget AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 321)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.single_language_referrable import (
    SingleLanguageReferrable,
)


class XrefTarget(SingleLanguageReferrable):
    """AUTOSAR XrefTarget."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize XrefTarget."""
        super().__init__()


class XrefTargetBuilder:
    """Builder for XrefTarget."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: XrefTarget = XrefTarget()

    def build(self) -> XrefTarget:
        """Build and return XrefTarget object.

        Returns:
            XrefTarget instance
        """
        # TODO: Add validation
        return self._obj
