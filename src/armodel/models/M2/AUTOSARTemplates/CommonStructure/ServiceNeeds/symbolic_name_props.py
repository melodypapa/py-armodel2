"""SymbolicNameProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 610)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation_props import (
    ImplementationProps,
)


class SymbolicNameProps(ImplementationProps):
    """AUTOSAR SymbolicNameProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize SymbolicNameProps."""
        super().__init__()


class SymbolicNamePropsBuilder:
    """Builder for SymbolicNameProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SymbolicNameProps = SymbolicNameProps()

    def build(self) -> SymbolicNameProps:
        """Build and return SymbolicNameProps object.

        Returns:
            SymbolicNameProps instance
        """
        # TODO: Add validation
        return self._obj
