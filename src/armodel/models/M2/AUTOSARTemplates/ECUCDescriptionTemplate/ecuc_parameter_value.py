"""EcucParameterValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 124)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 442)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 189)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_indexable_value import (
    EcucIndexableValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.MSR.Documentation.Annotation.annotation import (
    Annotation,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import (
    EcucParameterDef,
)


class EcucParameterValue(EcucIndexableValue):
    """AUTOSAR EcucParameterValue."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize EcucParameterValue."""
        super().__init__()
        self.annotations: list[Annotation] = []
        self.definition: Optional[EcucParameterDef] = None
        self.is_auto_value: Optional[Boolean] = None


class EcucParameterValueBuilder:
    """Builder for EcucParameterValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucParameterValue = EcucParameterValue()

    def build(self) -> EcucParameterValue:
        """Build and return EcucParameterValue object.

        Returns:
            EcucParameterValue instance
        """
        # TODO: Add validation
        return self._obj
