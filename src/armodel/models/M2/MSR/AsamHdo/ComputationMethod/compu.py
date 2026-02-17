"""Compu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 386)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_const import (
    CompuConst,
)
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_content import (
    CompuContent,
)


class Compu(ARObject):
    """AUTOSAR Compu."""

    compu_content: Optional[CompuContent]
    compu_default: Optional[CompuConst]
    def __init__(self) -> None:
        """Initialize Compu."""
        super().__init__()
        self.compu_content: Optional[CompuContent] = None
        self.compu_default: Optional[CompuConst] = None


class CompuBuilder:
    """Builder for Compu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Compu = Compu()

    def build(self) -> Compu:
        """Build and return Compu object.

        Returns:
            Compu instance
        """
        # TODO: Add validation
        return self._obj
