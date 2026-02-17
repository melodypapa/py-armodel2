"""AutosarParameterRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 306)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 317)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_DataElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
        DataPrototype,
    )



class AutosarParameterRef(ARObject):
    """AUTOSAR AutosarParameterRef."""

    autosar: Optional[DataPrototype]
    local_parameter: Optional[DataPrototype]
    def __init__(self) -> None:
        """Initialize AutosarParameterRef."""
        super().__init__()
        self.autosar: Optional[DataPrototype] = None
        self.local_parameter: Optional[DataPrototype] = None


class AutosarParameterRefBuilder:
    """Builder for AutosarParameterRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AutosarParameterRef = AutosarParameterRef()

    def build(self) -> AutosarParameterRef:
        """Build and return AutosarParameterRef object.

        Returns:
            AutosarParameterRef instance
        """
        # TODO: Add validation
        return self._obj
