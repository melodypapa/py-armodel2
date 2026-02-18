"""CompuConst AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 390)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_const_content import (
    CompuConstContent,
)


class CompuConst(ARObject):
    """AUTOSAR CompuConst."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    compu_const_content: Optional[CompuConstContent]
    def __init__(self) -> None:
        """Initialize CompuConst."""
        super().__init__()
        self.compu_const_content: Optional[CompuConstContent] = None


class CompuConstBuilder:
    """Builder for CompuConst."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuConst = CompuConst()

    def build(self) -> CompuConst:
        """Build and return CompuConst object.

        Returns:
            CompuConst instance
        """
        # TODO: Add validation
        return self._obj
