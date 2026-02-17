"""FlatInstanceDescriptor AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 316)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 989)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 966)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_FlatMap.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.rte_plugin_props import (
    RtePluginProps,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



class FlatInstanceDescriptor(Identifiable):
    """AUTOSAR FlatInstanceDescriptor."""

    ecu_extract: Optional[AtpFeature]
    role: Optional[Identifier]
    rte_plugin_props: Optional[RtePluginProps]
    sw_data_def: Optional[SwDataDefProps]
    upstream: Optional[AtpFeature]
    def __init__(self) -> None:
        """Initialize FlatInstanceDescriptor."""
        super().__init__()
        self.ecu_extract: Optional[AtpFeature] = None
        self.role: Optional[Identifier] = None
        self.rte_plugin_props: Optional[RtePluginProps] = None
        self.sw_data_def: Optional[SwDataDefProps] = None
        self.upstream: Optional[AtpFeature] = None


class FlatInstanceDescriptorBuilder:
    """Builder for FlatInstanceDescriptor."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlatInstanceDescriptor = FlatInstanceDescriptor()

    def build(self) -> FlatInstanceDescriptor:
        """Build and return FlatInstanceDescriptor object.

        Returns:
            FlatInstanceDescriptor instance
        """
        # TODO: Add validation
        return self._obj
