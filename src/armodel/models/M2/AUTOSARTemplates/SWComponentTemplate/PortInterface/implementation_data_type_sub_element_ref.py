"""ImplementationDataTypeSubElementRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 138)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.sub_element_ref import (
    SubElementRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.ar_parameter_in_implementation_data_instance_ref import (
    ArParameterInImplementationDataInstanceRef,
)


class ImplementationDataTypeSubElementRef(SubElementRef):
    """AUTOSAR ImplementationDataTypeSubElementRef."""

    def __init__(self) -> None:
        """Initialize ImplementationDataTypeSubElementRef."""
        super().__init__()
        self.implementation: Optional[Any] = None
        self.parameter: Optional[ArParameterInImplementationDataInstanceRef] = None


class ImplementationDataTypeSubElementRefBuilder:
    """Builder for ImplementationDataTypeSubElementRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ImplementationDataTypeSubElementRef = ImplementationDataTypeSubElementRef()

    def build(self) -> ImplementationDataTypeSubElementRef:
        """Build and return ImplementationDataTypeSubElementRef object.

        Returns:
            ImplementationDataTypeSubElementRef instance
        """
        # TODO: Add validation
        return self._obj
