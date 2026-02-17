"""InstantiationDataDefProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 588)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_InstantiationDataDefProps.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_parameter_ref import (
    AutosarParameterRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_variable_ref import (
    AutosarVariableRef,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)


class InstantiationDataDefProps(ARObject):
    """AUTOSAR InstantiationDataDefProps."""

    parameter: Optional[AutosarParameterRef]
    sw_data_def: Optional[SwDataDefProps]
    variable_instance: Optional[AutosarVariableRef]
    def __init__(self) -> None:
        """Initialize InstantiationDataDefProps."""
        super().__init__()
        self.parameter: Optional[AutosarParameterRef] = None
        self.sw_data_def: Optional[SwDataDefProps] = None
        self.variable_instance: Optional[AutosarVariableRef] = None


class InstantiationDataDefPropsBuilder:
    """Builder for InstantiationDataDefProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InstantiationDataDefProps = InstantiationDataDefProps()

    def build(self) -> InstantiationDataDefProps:
        """Build and return InstantiationDataDefProps object.

        Returns:
            InstantiationDataDefProps instance
        """
        # TODO: Add validation
        return self._obj
