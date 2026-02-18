"""SymbolProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 288)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2074)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 66)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation_props import (
    ImplementationProps,
)


class SymbolProps(ImplementationProps):
    """AUTOSAR SymbolProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize SymbolProps."""
        super().__init__()


class SymbolPropsBuilder:
    """Builder for SymbolProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SymbolProps = SymbolProps()

    def build(self) -> SymbolProps:
        """Build and return SymbolProps object.

        Returns:
            SymbolProps instance
        """
        # TODO: Add validation
        return self._obj
