"""AutosarVariableInstance AUTOSAR element.

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


class AutosarVariableInstance(Identifiable):
    """AUTOSAR AutosarVariableInstance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    variable_instance_instance_ref: Optional[DataPrototype]
    def __init__(self) -> None:
        """Initialize AutosarVariableInstance."""
        super().__init__()
        self.variable_instance_instance_ref: Optional[DataPrototype] = None


class AutosarVariableInstanceBuilder:
    """Builder for AutosarVariableInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AutosarVariableInstance = AutosarVariableInstance()

    def build(self) -> AutosarVariableInstance:
        """Build and return AutosarVariableInstance object.

        Returns:
            AutosarVariableInstance instance
        """
        # TODO: Add validation
        return self._obj
