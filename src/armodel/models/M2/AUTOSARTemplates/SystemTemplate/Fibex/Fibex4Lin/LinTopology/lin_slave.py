"""LinSlave AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 97)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_error_response import (
    LinErrorResponse,
)


class LinSlave(ARObject):
    """AUTOSAR LinSlave."""

    def __init__(self) -> None:
        """Initialize LinSlave."""
        super().__init__()
        self.assign_nad: Optional[Boolean] = None
        self.configured_nad: Optional[Integer] = None
        self.function_id: Optional[PositiveInteger] = None
        self.initial_nad: Optional[Integer] = None
        self.lin_error_response: Optional[LinErrorResponse] = None
        self.nas_timeout: Optional[TimeValue] = None
        self.supplier_id: Optional[PositiveInteger] = None
        self.variant_id: Optional[PositiveInteger] = None


class LinSlaveBuilder:
    """Builder for LinSlave."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinSlave = LinSlave()

    def build(self) -> LinSlave:
        """Build and return LinSlave object.

        Returns:
            LinSlave instance
        """
        # TODO: Add validation
        return self._obj
