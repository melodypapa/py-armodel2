"""ConstantReference AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 440)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.constant_specification import (
    ConstantSpecification,
)


class ConstantReference(ValueSpecification):
    """AUTOSAR ConstantReference."""

    def __init__(self) -> None:
        """Initialize ConstantReference."""
        super().__init__()
        self.constant: Optional[ConstantSpecification] = None


class ConstantReferenceBuilder:
    """Builder for ConstantReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConstantReference = ConstantReference()

    def build(self) -> ConstantReference:
        """Build and return ConstantReference object.

        Returns:
            ConstantReference instance
        """
        # TODO: Add validation
        return self._obj
