"""SwSystemconstValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2068)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 80)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 235)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)
from armodel.models.M2.MSR.Documentation.Annotation.annotation import (
    Annotation,
)
from armodel.models.M2.MSR.DataDictionary.SystemConstant.sw_systemconst import (
    SwSystemconst,
)


class SwSystemconstValue(ARObject):
    """AUTOSAR SwSystemconstValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    annotations: list[Annotation]
    sw_systemconst: SwSystemconst
    value: Numerical
    def __init__(self) -> None:
        """Initialize SwSystemconstValue."""
        super().__init__()
        self.annotations: list[Annotation] = []
        self.sw_systemconst: SwSystemconst = None
        self.value: Numerical = None


class SwSystemconstValueBuilder:
    """Builder for SwSystemconstValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwSystemconstValue = SwSystemconstValue()

    def build(self) -> SwSystemconstValue:
        """Build and return SwSystemconstValue object.

        Returns:
            SwSystemconstValue instance
        """
        # TODO: Add validation
        return self._obj
