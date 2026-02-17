"""SwSystemconst AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 343)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 312)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 448)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2068)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 79)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 234)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_SystemConstant.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



class SwSystemconst(ARElement):
    """AUTOSAR SwSystemconst."""

    sw_data_def: Optional[SwDataDefProps]
    def __init__(self) -> None:
        """Initialize SwSystemconst."""
        super().__init__()
        self.sw_data_def: Optional[SwDataDefProps] = None


class SwSystemconstBuilder:
    """Builder for SwSystemconst."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwSystemconst = SwSystemconst()

    def build(self) -> SwSystemconst:
        """Build and return SwSystemconst object.

        Returns:
            SwSystemconst instance
        """
        # TODO: Add validation
        return self._obj
