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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlatInstanceDescriptor":
        """Deserialize XML element to FlatInstanceDescriptor object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlatInstanceDescriptor object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlatInstanceDescriptor, cls).deserialize(element)

        # Parse ecu_extract
        child = ARObject._find_child_element(element, "ECU-EXTRACT")
        if child is not None:
            ecu_extract_value = ARObject._deserialize_by_tag(child, "AtpFeature")
            obj.ecu_extract = ecu_extract_value

        # Parse role
        child = ARObject._find_child_element(element, "ROLE")
        if child is not None:
            role_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.role = role_value

        # Parse rte_plugin_props
        child = ARObject._find_child_element(element, "RTE-PLUGIN-PROPS")
        if child is not None:
            rte_plugin_props_value = ARObject._deserialize_by_tag(child, "RtePluginProps")
            obj.rte_plugin_props = rte_plugin_props_value

        # Parse sw_data_def
        child = ARObject._find_child_element(element, "SW-DATA-DEF")
        if child is not None:
            sw_data_def_value = ARObject._deserialize_by_tag(child, "SwDataDefProps")
            obj.sw_data_def = sw_data_def_value

        # Parse upstream
        child = ARObject._find_child_element(element, "UPSTREAM")
        if child is not None:
            upstream_value = ARObject._deserialize_by_tag(child, "AtpFeature")
            obj.upstream = upstream_value

        return obj



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
