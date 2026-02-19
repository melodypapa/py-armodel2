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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SingleLanguageReferrable":
        """Deserialize XML element to SingleLanguageReferrable object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SingleLanguageReferrable object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SingleLanguageReferrable, cls).deserialize(element)

        # Parse long_name1
        child = ARObject._find_child_element(element, "LONG-NAME1")
        if child is not None:
            long_name1_value = ARObject._deserialize_by_tag(child, "SingleLanguageLongName")
            obj.long_name1 = long_name1_value

        return obj



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
