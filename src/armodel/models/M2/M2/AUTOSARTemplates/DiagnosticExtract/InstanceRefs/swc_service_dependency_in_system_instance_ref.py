"""SwcServiceDependencyInSystemInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 369)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.root_sw_composition_prototype import (
    RootSwCompositionPrototype,
)


class SwcServiceDependencyInSystemInstanceRef(ARObject):
    """AUTOSAR SwcServiceDependencyInSystemInstanceRef."""

    def __init__(self) -> None:
        """Initialize SwcServiceDependencyInSystemInstanceRef."""
        super().__init__()
        self.context_root_sw: Optional[RootSwCompositionPrototype] = None
        self.context_sw_prototypes: list[Any] = []
        self.target_swc: Optional[Any] = None


class SwcServiceDependencyInSystemInstanceRefBuilder:
    """Builder for SwcServiceDependencyInSystemInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcServiceDependencyInSystemInstanceRef = SwcServiceDependencyInSystemInstanceRef()

    def build(self) -> SwcServiceDependencyInSystemInstanceRef:
        """Build and return SwcServiceDependencyInSystemInstanceRef object.

        Returns:
            SwcServiceDependencyInSystemInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
