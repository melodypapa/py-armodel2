"""VariableDataPrototypeInSystemInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1003)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.root_sw_composition_prototype import (
    RootSwCompositionPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class VariableDataPrototypeInSystemInstanceRef(ARObject):
    """AUTOSAR VariableDataPrototypeInSystemInstanceRef."""

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
    target_data: Optional[VariableDataPrototype]
    def __init__(self) -> None:
        """Initialize VariableDataPrototypeInSystemInstanceRef."""
        super().__init__()
        self.base: Optional[System] = None
        self.context: Optional[RootSwCompositionPrototype] = None
        self.context_port: PortPrototype = None
        self.target_data: Optional[VariableDataPrototype] = None


class VariableDataPrototypeInSystemInstanceRefBuilder:
    """Builder for VariableDataPrototypeInSystemInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VariableDataPrototypeInSystemInstanceRef = VariableDataPrototypeInSystemInstanceRef()

    def build(self) -> VariableDataPrototypeInSystemInstanceRef:
        """Build and return VariableDataPrototypeInSystemInstanceRef object.

        Returns:
            VariableDataPrototypeInSystemInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
