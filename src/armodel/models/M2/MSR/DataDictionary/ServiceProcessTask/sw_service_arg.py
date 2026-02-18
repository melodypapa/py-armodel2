"""SwServiceArg AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 38)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 312)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1006)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 472)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 215)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_ServiceProcessTask.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ArgumentDirectionEnum,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.value_list import (
    ValueList,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



class SwServiceArg(Identifiable):
    """AUTOSAR SwServiceArg."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    direction: Optional[ArgumentDirectionEnum]
    sw_arraysize_ref: Optional[ARRef]
    sw_data_def: Optional[SwDataDefProps]
    def __init__(self) -> None:
        """Initialize SwServiceArg."""
        super().__init__()
        self.direction: Optional[ArgumentDirectionEnum] = None
        self.sw_arraysize_ref: Optional[ARRef] = None
        self.sw_data_def: Optional[SwDataDefProps] = None


class SwServiceArgBuilder:
    """Builder for SwServiceArg."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwServiceArg = SwServiceArg()

    def build(self) -> SwServiceArg:
        """Build and return SwServiceArg object.

        Returns:
            SwServiceArg instance
        """
        # TODO: Add validation
        return self._obj
