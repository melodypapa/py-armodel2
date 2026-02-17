"""AutosarOperationArgumentInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 85)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class AutosarOperationArgumentInstance(Identifiable):
    """AUTOSAR AutosarOperationArgumentInstance."""

    operation: Optional[DataPrototype]
    def __init__(self) -> None:
        """Initialize AutosarOperationArgumentInstance."""
        super().__init__()
        self.operation: Optional[DataPrototype] = None


class AutosarOperationArgumentInstanceBuilder:
    """Builder for AutosarOperationArgumentInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AutosarOperationArgumentInstance = AutosarOperationArgumentInstance()

    def build(self) -> AutosarOperationArgumentInstance:
        """Build and return AutosarOperationArgumentInstance object.

        Returns:
            AutosarOperationArgumentInstance instance
        """
        # TODO: Add validation
        return self._obj
