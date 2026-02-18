"""RptServicePoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 206)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport_RptSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
    PositiveInteger,
)


class RptServicePoint(Identifiable):
    """AUTOSAR RptServicePoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    service_id: Optional[PositiveInteger]
    symbol: Optional[CIdentifier]
    def __init__(self) -> None:
        """Initialize RptServicePoint."""
        super().__init__()
        self.service_id: Optional[PositiveInteger] = None
        self.symbol: Optional[CIdentifier] = None


class RptServicePointBuilder:
    """Builder for RptServicePoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RptServicePoint = RptServicePoint()

    def build(self) -> RptServicePoint:
        """Build and return RptServicePoint object.

        Returns:
            RptServicePoint instance
        """
        # TODO: Add validation
        return self._obj
