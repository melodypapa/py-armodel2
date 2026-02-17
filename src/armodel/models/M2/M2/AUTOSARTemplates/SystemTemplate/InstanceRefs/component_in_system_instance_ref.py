"""ComponentInSystemInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 999)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.root_sw_composition_prototype import (
    RootSwCompositionPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)


class ComponentInSystemInstanceRef(ARObject):
    """AUTOSAR ComponentInSystemInstanceRef."""

    def __init__(self) -> None:
        """Initialize ComponentInSystemInstanceRef."""
        super().__init__()
        self.base: Optional[System] = None
        self.context: Optional[RootSwCompositionPrototype] = None
        self.target: Any = None


class ComponentInSystemInstanceRefBuilder:
    """Builder for ComponentInSystemInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ComponentInSystemInstanceRef = ComponentInSystemInstanceRef()

    def build(self) -> ComponentInSystemInstanceRef:
        """Build and return ComponentInSystemInstanceRef object.

        Returns:
            ComponentInSystemInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
