"""ImplementationDataTypeElementInPortInterfaceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 789)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer_InstanceRef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_prototype_reference import (
    DataPrototypeReference,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import (
        AbstractImplementationDataType,
    )



class ImplementationDataTypeElementInPortInterfaceRef(DataPrototypeReference):
    """AUTOSAR ImplementationDataTypeElementInPortInterfaceRef."""

    contexts: list[Any]
    root_data: Optional[AutosarDataPrototype]
    target: Optional[AbstractImplementationDataType]
    def __init__(self) -> None:
        """Initialize ImplementationDataTypeElementInPortInterfaceRef."""
        super().__init__()
        self.contexts: list[Any] = []
        self.root_data: Optional[AutosarDataPrototype] = None
        self.target: Optional[AbstractImplementationDataType] = None


class ImplementationDataTypeElementInPortInterfaceRefBuilder:
    """Builder for ImplementationDataTypeElementInPortInterfaceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ImplementationDataTypeElementInPortInterfaceRef = ImplementationDataTypeElementInPortInterfaceRef()

    def build(self) -> ImplementationDataTypeElementInPortInterfaceRef:
        """Build and return ImplementationDataTypeElementInPortInterfaceRef object.

        Returns:
            ImplementationDataTypeElementInPortInterfaceRef instance
        """
        # TODO: Add validation
        return self._obj
