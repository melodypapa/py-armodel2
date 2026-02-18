"""VariableDataPrototypeInCompositionInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 959)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ImplicitCommunicationBehavior_InstanceRef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class VariableDataPrototypeInCompositionInstanceRef(ARObject):
    """AUTOSAR VariableDataPrototypeInCompositionInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base: Optional[CompositionSwComponentType]
    context_port: Optional[PortPrototype]
    context_sws: list[Any]
    target_variable: Optional[VariableDataPrototype]
    def __init__(self) -> None:
        """Initialize VariableDataPrototypeInCompositionInstanceRef."""
        super().__init__()
        self.base: Optional[CompositionSwComponentType] = None
        self.context_port: Optional[PortPrototype] = None
        self.context_sws: list[Any] = []
        self.target_variable: Optional[VariableDataPrototype] = None


class VariableDataPrototypeInCompositionInstanceRefBuilder:
    """Builder for VariableDataPrototypeInCompositionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VariableDataPrototypeInCompositionInstanceRef = VariableDataPrototypeInCompositionInstanceRef()

    def build(self) -> VariableDataPrototypeInCompositionInstanceRef:
        """Build and return VariableDataPrototypeInCompositionInstanceRef object.

        Returns:
            VariableDataPrototypeInCompositionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
