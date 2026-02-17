"""SdgElementWithGid AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 99)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)


class SdgElementWithGid(ARObject):
    """AUTOSAR SdgElementWithGid."""
    """Abstract base class - do not instantiate directly."""

    gid: Optional[NameToken]
    def __init__(self) -> None:
        """Initialize SdgElementWithGid."""
        super().__init__()
        self.gid: Optional[NameToken] = None


class SdgElementWithGidBuilder:
    """Builder for SdgElementWithGid."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgElementWithGid = SdgElementWithGid()

    def build(self) -> SdgElementWithGid:
        """Build and return SdgElementWithGid object.

        Returns:
            SdgElementWithGid instance
        """
        # TODO: Add validation
        return self._obj
