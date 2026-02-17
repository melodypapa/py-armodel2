"""Sdg AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 328)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1004)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 78)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 90)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_SpecialData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData.sdg_caption import (
    SdgCaption,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.AsamHdo.SpecialData.sdg_contents import (
        SdgContents,
    )



class Sdg(ARObject):
    """AUTOSAR Sdg."""

    def __init__(self) -> None:
        """Initialize Sdg."""
        super().__init__()
        self.gid: NameToken = None
        self.sdg_caption: Optional[SdgCaption] = None
        self.sdg_contents: Optional[SdgContents] = None


class SdgBuilder:
    """Builder for Sdg."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Sdg = Sdg()

    def build(self) -> Sdg:
        """Build and return Sdg object.

        Returns:
            Sdg instance
        """
        # TODO: Add validation
        return self._obj
