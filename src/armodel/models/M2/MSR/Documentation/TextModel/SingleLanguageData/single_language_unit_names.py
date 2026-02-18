"""SingleLanguageUnitNames AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 400)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_SingleLanguageData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class SingleLanguageUnitNames(ARObject):
    """AUTOSAR SingleLanguageUnitNames."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize SingleLanguageUnitNames."""
        super().__init__()


class SingleLanguageUnitNamesBuilder:
    """Builder for SingleLanguageUnitNames."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SingleLanguageUnitNames = SingleLanguageUnitNames()

    def build(self) -> SingleLanguageUnitNames:
        """Build and return SingleLanguageUnitNames object.

        Returns:
            SingleLanguageUnitNames instance
        """
        # TODO: Add validation
        return self._obj
