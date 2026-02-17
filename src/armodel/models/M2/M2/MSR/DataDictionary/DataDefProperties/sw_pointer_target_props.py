"""SwPointerTargetProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 39)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 311)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 286)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 471)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_DataDefProperties.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
        BswModuleEntry,
    )
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



class SwPointerTargetProps(ARObject):
    """AUTOSAR SwPointerTargetProps."""

    def __init__(self) -> None:
        """Initialize SwPointerTargetProps."""
        super().__init__()
        self.function_pointer: Optional[BswModuleEntry] = None
        self.sw_data_def: Optional[SwDataDefProps] = None
        self.target_category: Optional[Identifier] = None


class SwPointerTargetPropsBuilder:
    """Builder for SwPointerTargetProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwPointerTargetProps = SwPointerTargetProps()

    def build(self) -> SwPointerTargetProps:
        """Build and return SwPointerTargetProps object.

        Returns:
            SwPointerTargetProps instance
        """
        # TODO: Add validation
        return self._obj
