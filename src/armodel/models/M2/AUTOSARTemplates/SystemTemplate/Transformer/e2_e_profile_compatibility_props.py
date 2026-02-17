"""E2EProfileCompatibilityProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 202)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 807)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class E2EProfileCompatibilityProps(ARElement):
    """AUTOSAR E2EProfileCompatibilityProps."""

    transit_to_invalid: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize E2EProfileCompatibilityProps."""
        super().__init__()
        self.transit_to_invalid: Optional[Boolean] = None


class E2EProfileCompatibilityPropsBuilder:
    """Builder for E2EProfileCompatibilityProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: E2EProfileCompatibilityProps = E2EProfileCompatibilityProps()

    def build(self) -> E2EProfileCompatibilityProps:
        """Build and return E2EProfileCompatibilityProps object.

        Returns:
            E2EProfileCompatibilityProps instance
        """
        # TODO: Add validation
        return self._obj
