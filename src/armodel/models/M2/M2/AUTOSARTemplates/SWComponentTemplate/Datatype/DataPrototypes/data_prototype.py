"""DataPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 311)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 311)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 305)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2013)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_DataPrototypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



class DataPrototype(Identifiable):
    """AUTOSAR DataPrototype."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize DataPrototype."""
        super().__init__()
        self.sw_data_def: Optional[SwDataDefProps] = None


class DataPrototypeBuilder:
    """Builder for DataPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototype = DataPrototype()

    def build(self) -> DataPrototype:
        """Build and return DataPrototype object.

        Returns:
            DataPrototype instance
        """
        # TODO: Add validation
        return self._obj
