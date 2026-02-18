"""ArVariableInImplementationDataInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 322)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_DataElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class ArVariableInImplementationDataInstanceRef(ARObject):
    """AUTOSAR ArVariableInImplementationDataInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context_datas: list[Any]
    port_prototype_ref: Optional[ARRef]
    root_variable_ref: Optional[ARRef]
    target_data: Optional[Any]
    def __init__(self) -> None:
        """Initialize ArVariableInImplementationDataInstanceRef."""
        super().__init__()
        self.context_datas: list[Any] = []
        self.port_prototype_ref: Optional[ARRef] = None
        self.root_variable_ref: Optional[ARRef] = None
        self.target_data: Optional[Any] = None


class ArVariableInImplementationDataInstanceRefBuilder:
    """Builder for ArVariableInImplementationDataInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ArVariableInImplementationDataInstanceRef = ArVariableInImplementationDataInstanceRef()

    def build(self) -> ArVariableInImplementationDataInstanceRef:
        """Build and return ArVariableInImplementationDataInstanceRef object.

        Returns:
            ArVariableInImplementationDataInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
