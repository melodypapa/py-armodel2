"""AutosarDataPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 305)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 301)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 306)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2001)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_DataPrototypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.autosar_data_type import (
    AutosarDataType,
)


class AutosarDataPrototype(DataPrototype):
    """AUTOSAR AutosarDataPrototype."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize AutosarDataPrototype."""
        super().__init__()
        self.type: Optional[AutosarDataType] = None


class AutosarDataPrototypeBuilder:
    """Builder for AutosarDataPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AutosarDataPrototype = AutosarDataPrototype()

    def build(self) -> AutosarDataPrototype:
        """Build and return AutosarDataPrototype object.

        Returns:
            AutosarDataPrototype instance
        """
        # TODO: Add validation
        return self._obj
