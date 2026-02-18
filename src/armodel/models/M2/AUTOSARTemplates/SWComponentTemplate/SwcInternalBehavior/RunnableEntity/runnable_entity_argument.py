"""RunnableEntityArgument AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 536)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RunnableEntity.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
)


class RunnableEntityArgument(ARObject):
    """AUTOSAR RunnableEntityArgument."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    symbol: Optional[CIdentifier]
    def __init__(self) -> None:
        """Initialize RunnableEntityArgument."""
        super().__init__()
        self.symbol: Optional[CIdentifier] = None


class RunnableEntityArgumentBuilder:
    """Builder for RunnableEntityArgument."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RunnableEntityArgument = RunnableEntityArgument()

    def build(self) -> RunnableEntityArgument:
        """Build and return RunnableEntityArgument object.

        Returns:
            RunnableEntityArgument instance
        """
        # TODO: Add validation
        return self._obj
