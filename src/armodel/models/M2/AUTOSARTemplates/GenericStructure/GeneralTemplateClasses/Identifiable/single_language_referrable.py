"""SingleLanguageReferrable AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 64)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_Identifiable.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData.single_language_long_name import (
    SingleLanguageLongName,
)
from abc import ABC, abstractmethod


class SingleLanguageReferrable(Referrable, ABC):
    """AUTOSAR SingleLanguageReferrable."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    long_name1: Optional[SingleLanguageLongName]
    def __init__(self) -> None:
        """Initialize SingleLanguageReferrable."""
        super().__init__()
        self.long_name1: Optional[SingleLanguageLongName] = None


class SingleLanguageReferrableBuilder:
    """Builder for SingleLanguageReferrable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SingleLanguageReferrable = SingleLanguageReferrable()

    def build(self) -> SingleLanguageReferrable:
        """Build and return SingleLanguageReferrable object.

        Returns:
            SingleLanguageReferrable instance
        """
        # TODO: Add validation
        return self._obj
