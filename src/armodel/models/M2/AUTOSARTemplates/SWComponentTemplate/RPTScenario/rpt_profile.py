"""RptProfile AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 853)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_RPTScenario.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport import (
    RptEnablerImplTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
    PositiveInteger,
)


class RptProfile(Identifiable):
    """AUTOSAR RptProfile."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    max_service: Optional[PositiveInteger]
    min_service_point: Optional[PositiveInteger]
    service_point: Optional[CIdentifier]
    stim_enabler: Optional[RptEnablerImplTypeEnum]
    def __init__(self) -> None:
        """Initialize RptProfile."""
        super().__init__()
        self.max_service: Optional[PositiveInteger] = None
        self.min_service_point: Optional[PositiveInteger] = None
        self.service_point: Optional[CIdentifier] = None
        self.stim_enabler: Optional[RptEnablerImplTypeEnum] = None


class RptProfileBuilder:
    """Builder for RptProfile."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RptProfile = RptProfile()

    def build(self) -> RptProfile:
        """Build and return RptProfile object.

        Returns:
            RptProfile instance
        """
        # TODO: Add validation
        return self._obj
