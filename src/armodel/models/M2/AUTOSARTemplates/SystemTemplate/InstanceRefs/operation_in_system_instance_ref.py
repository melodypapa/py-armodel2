"""OperationInSystemInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1001)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.root_sw_composition_prototype import (
    RootSwCompositionPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)


class OperationInSystemInstanceRef(ARObject):
    """AUTOSAR OperationInSystemInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base: Optional[System]
    context: Optional[RootSwCompositionPrototype]
    context_port: PortPrototype
    target_operation: Optional[ClientServerOperation]
    def __init__(self) -> None:
        """Initialize OperationInSystemInstanceRef."""
        super().__init__()
        self.base: Optional[System] = None
        self.context: Optional[RootSwCompositionPrototype] = None
        self.context_port: PortPrototype = None
        self.target_operation: Optional[ClientServerOperation] = None


class OperationInSystemInstanceRefBuilder:
    """Builder for OperationInSystemInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: OperationInSystemInstanceRef = OperationInSystemInstanceRef()

    def build(self) -> OperationInSystemInstanceRef:
        """Build and return OperationInSystemInstanceRef object.

        Returns:
            OperationInSystemInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
