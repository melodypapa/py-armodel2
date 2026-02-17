"""Sdf AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 92)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_SpecialData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    Numerical,
)


class Sdf(ARObject):
    """AUTOSAR Sdf."""

    gid: NameToken
    value: Optional[Numerical]
    def __init__(self) -> None:
        """Initialize Sdf."""
        super().__init__()
        self.gid: NameToken = None
        self.value: Optional[Numerical] = None


class SdfBuilder:
    """Builder for Sdf."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Sdf = Sdf()

    def build(self) -> Sdf:
        """Build and return Sdf object.

        Returns:
            Sdf instance
        """
        # TODO: Add validation
        return self._obj
