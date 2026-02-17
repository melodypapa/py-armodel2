"""AutosarVariableRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 307)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 315)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_DataElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class AutosarVariableRef(ARObject):
    """AUTOSAR AutosarVariableRef."""

    def __init__(self) -> None:
        """Initialize AutosarVariableRef."""
        super().__init__()
        self.autosar_variable: Optional[Any] = None
        self.local_variable: Optional[VariableDataPrototype] = None


class AutosarVariableRefBuilder:
    """Builder for AutosarVariableRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AutosarVariableRef = AutosarVariableRef()

    def build(self) -> AutosarVariableRef:
        """Build and return AutosarVariableRef object.

        Returns:
            AutosarVariableRef instance
        """
        # TODO: Add validation
        return self._obj
