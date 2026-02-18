"""ApplicationValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 299)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 455)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.MSR.CalibrationData.CalibrationValue.sw_axis_cont import (
    SwAxisCont,
)
from armodel.models.M2.MSR.CalibrationData.CalibrationValue.sw_value_cont import (
    SwValueCont,
)


class ApplicationValueSpecification(ValueSpecification):
    """AUTOSAR ApplicationValueSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    category: Optional[Identifier]
    sw_axis_conts: list[SwAxisCont]
    sw_value_cont: Optional[SwValueCont]
    def __init__(self) -> None:
        """Initialize ApplicationValueSpecification."""
        super().__init__()
        self.category: Optional[Identifier] = None
        self.sw_axis_conts: list[SwAxisCont] = []
        self.sw_value_cont: Optional[SwValueCont] = None


class ApplicationValueSpecificationBuilder:
    """Builder for ApplicationValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationValueSpecification = ApplicationValueSpecification()

    def build(self) -> ApplicationValueSpecification:
        """Build and return ApplicationValueSpecification object.

        Returns:
            ApplicationValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
