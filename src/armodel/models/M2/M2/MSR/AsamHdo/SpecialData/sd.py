"""Sd AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 91)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_SpecialData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    VerbatimStringPlain,
)


class Sd(ARObject):
    """AUTOSAR Sd."""

    def __init__(self) -> None:
        """Initialize Sd."""
        super().__init__()
        self.gid: NameToken = None
        self.value: VerbatimStringPlain = None
        self.xml_space: Optional[Any] = None


class SdBuilder:
    """Builder for Sd."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Sd = Sd()

    def build(self) -> Sd:
        """Build and return Sd object.

        Returns:
            Sd instance
        """
        # TODO: Add validation
        return self._obj
