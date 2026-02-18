"""ArParameterInImplementationDataInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 324)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_DataElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)


class ArParameterInImplementationDataInstanceRef(ARObject):
    """AUTOSAR ArParameterInImplementationDataInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context_datas: list[Any]
    port_prototype: Optional[PortPrototype]
    root_parameter: Optional[ParameterDataPrototype]
    target_data: Optional[Any]
    def __init__(self) -> None:
        """Initialize ArParameterInImplementationDataInstanceRef."""
        super().__init__()
        self.context_datas: list[Any] = []
        self.port_prototype: Optional[PortPrototype] = None
        self.root_parameter: Optional[ParameterDataPrototype] = None
        self.target_data: Optional[Any] = None


class ArParameterInImplementationDataInstanceRefBuilder:
    """Builder for ArParameterInImplementationDataInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ArParameterInImplementationDataInstanceRef = ArParameterInImplementationDataInstanceRef()

    def build(self) -> ArParameterInImplementationDataInstanceRef:
        """Build and return ArParameterInImplementationDataInstanceRef object.

        Returns:
            ArParameterInImplementationDataInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
