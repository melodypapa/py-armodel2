"""EcucContainerValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 119)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2021)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 439)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 185)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_parameter_value import (
    EcucParameterValue,
)


class EcucContainerValue(Identifiable):
    """AUTOSAR EcucContainerValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    definition: Optional[EcucContainerDef]
    parameter_values: list[EcucParameterValue]
    reference_values: list[Any]
    sub_containers: list[EcucContainerValue]
    def __init__(self) -> None:
        """Initialize EcucContainerValue."""
        super().__init__()
        self.definition: Optional[EcucContainerDef] = None
        self.parameter_values: list[EcucParameterValue] = []
        self.reference_values: list[Any] = []
        self.sub_containers: list[EcucContainerValue] = []


class EcucContainerValueBuilder:
    """Builder for EcucContainerValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucContainerValue = EcucContainerValue()

    def build(self) -> EcucContainerValue:
        """Build and return EcucContainerValue object.

        Returns:
            EcucContainerValue instance
        """
        # TODO: Add validation
        return self._obj
