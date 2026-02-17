"""SdgContents AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 90)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_SpecialData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData.sd import (
    Sd,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData.sdf import (
    Sdf,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.AsamHdo.SpecialData.sdg import (
        Sdg,
    )



class SdgContents(ARObject):
    """AUTOSAR SdgContents."""

    sd: Optional[Sd]
    sdf: Optional[Sdf]
    sdg: Optional[Sdg]
    sdx: Optional[Referrable]
    sdxf: Optional[Referrable]
    def __init__(self) -> None:
        """Initialize SdgContents."""
        super().__init__()
        self.sd: Optional[Sd] = None
        self.sdf: Optional[Sdf] = None
        self.sdg: Optional[Sdg] = None
        self.sdx: Optional[Referrable] = None
        self.sdxf: Optional[Referrable] = None


class SdgContentsBuilder:
    """Builder for SdgContents."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgContents = SdgContents()

    def build(self) -> SdgContents:
        """Build and return SdgContents object.

        Returns:
            SdgContents instance
        """
        # TODO: Add validation
        return self._obj
