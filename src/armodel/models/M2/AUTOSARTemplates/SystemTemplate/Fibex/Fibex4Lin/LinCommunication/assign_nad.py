"""AssignNad AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 438)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import (
    LinConfigurationEntry,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class AssignNad(LinConfigurationEntry):
    """AUTOSAR AssignNad."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    new_nad: Optional[Integer]
    def __init__(self) -> None:
        """Initialize AssignNad."""
        super().__init__()
        self.new_nad: Optional[Integer] = None


class AssignNadBuilder:
    """Builder for AssignNad."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AssignNad = AssignNad()

    def build(self) -> AssignNad:
        """Build and return AssignNad object.

        Returns:
            AssignNad instance
        """
        # TODO: Add validation
        return self._obj
