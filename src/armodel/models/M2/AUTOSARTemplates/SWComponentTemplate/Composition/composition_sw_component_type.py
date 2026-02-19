"""CompositionSwComponentType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 307)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 291)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 75)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 895)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 219)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 21)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 434)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import (
    SwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.constant_specification import (
    ConstantSpecification,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.data_type_mapping_set import (
    DataTypeMappingSet,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.instantiation_rte_event_props import (
    InstantiationRTEEventProps,
)
from armodel.models.M2.MSR.AsamHdo.Units.physical_dimension import (
    PhysicalDimension,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_connector import (
    SwConnector,
)


class CompositionSwComponentType(SwComponentType):
    """AUTOSAR CompositionSwComponentType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    components: list[Any]
    connectors: list[SwConnector]
    constant_values: list[ConstantSpecification]
    data_type_refs: list[ARRef]
    instantiation_rte_events: list[InstantiationRTEEventProps]
    physical: Optional[PhysicalDimension]
    def __init__(self) -> None:
        """Initialize CompositionSwComponentType."""
        super().__init__()
        self.components: list[Any] = []
        self.connectors: list[SwConnector] = []
        self.constant_values: list[ConstantSpecification] = []
        self.data_type_refs: list[ARRef] = []
        self.instantiation_rte_events: list[InstantiationRTEEventProps] = []
        self.physical: Optional[PhysicalDimension] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompositionSwComponentType":
        """Deserialize XML element to CompositionSwComponentType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CompositionSwComponentType object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse components (list)
        obj.components = []
        for child in ARObject._find_all_child_elements(element, "COMPONENTS"):
            components_value = child.text
            obj.components.append(components_value)

        # Parse connectors (list)
        obj.connectors = []
        for child in ARObject._find_all_child_elements(element, "CONNECTORS"):
            connectors_value = ARObject._deserialize_by_tag(child, "SwConnector")
            obj.connectors.append(connectors_value)

        # Parse constant_values (list)
        obj.constant_values = []
        for child in ARObject._find_all_child_elements(element, "CONSTANT-VALUES"):
            constant_values_value = ARObject._deserialize_by_tag(child, "ConstantSpecification")
            obj.constant_values.append(constant_values_value)

        # Parse data_type_refs (list)
        obj.data_type_refs = []
        for child in ARObject._find_all_child_elements(element, "DATA-TYPES"):
            data_type_refs_value = ARObject._deserialize_by_tag(child, "DataTypeMappingSet")
            obj.data_type_refs.append(data_type_refs_value)

        # Parse instantiation_rte_events (list)
        obj.instantiation_rte_events = []
        for child in ARObject._find_all_child_elements(element, "INSTANTIATION-RTE-EVENTS"):
            instantiation_rte_events_value = ARObject._deserialize_by_tag(child, "InstantiationRTEEventProps")
            obj.instantiation_rte_events.append(instantiation_rte_events_value)

        # Parse physical
        child = ARObject._find_child_element(element, "PHYSICAL")
        if child is not None:
            physical_value = ARObject._deserialize_by_tag(child, "PhysicalDimension")
            obj.physical = physical_value

        return obj



class CompositionSwComponentTypeBuilder:
    """Builder for CompositionSwComponentType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompositionSwComponentType = CompositionSwComponentType()

    def build(self) -> CompositionSwComponentType:
        """Build and return CompositionSwComponentType object.

        Returns:
            CompositionSwComponentType instance
        """
        # TODO: Add validation
        return self._obj
