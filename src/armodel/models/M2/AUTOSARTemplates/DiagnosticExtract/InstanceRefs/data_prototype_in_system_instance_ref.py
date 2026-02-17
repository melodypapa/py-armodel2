"""DataPrototypeInSystemInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 368)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.root_sw_composition_prototype import (
    RootSwCompositionPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)


class DataPrototypeInSystemInstanceRef(ARObject):
    """AUTOSAR DataPrototypeInSystemInstanceRef."""

    def __init__(self) -> None:
        """Initialize DataPrototypeInSystemInstanceRef."""
        super().__init__()
        self.base: Optional[System] = None
        self.contexts: list[Any] = []
        self.context_datas: list[Any] = []
        self.context_port: Optional[PortPrototype] = None
        self.context_root: Optional[RootSwCompositionPrototype] = None
        self.root_data_prototype: Optional[AutosarDataPrototype] = None
        self.target_data: Optional[DataPrototype] = None


class DataPrototypeInSystemInstanceRefBuilder:
    """Builder for DataPrototypeInSystemInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeInSystemInstanceRef = DataPrototypeInSystemInstanceRef()

    def build(self) -> DataPrototypeInSystemInstanceRef:
        """Build and return DataPrototypeInSystemInstanceRef object.

        Returns:
            DataPrototypeInSystemInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
