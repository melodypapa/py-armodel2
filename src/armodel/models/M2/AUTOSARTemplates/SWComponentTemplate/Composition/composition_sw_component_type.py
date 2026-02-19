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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CompositionSwComponentType, cls).deserialize(element)

        # Parse components (list from container "COMPONENTS")
        obj.components = []
        container = ARObject._find_child_element(element, "COMPONENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.components.append(child_value)

        # Parse connectors (list from container "CONNECTORS")
        obj.connectors = []
        container = ARObject._find_child_element(element, "CONNECTORS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.connectors.append(child_value)

        # Parse constant_values (list from container "CONSTANT-VALUES")
        obj.constant_values = []
        container = ARObject._find_child_element(element, "CONSTANT-VALUES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.constant_values.append(child_value)

        # Parse data_type_refs (list from container "DATA-TYPES")
        obj.data_type_refs = []
        container = ARObject._find_child_element(element, "DATA-TYPES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_type_refs.append(child_value)

        # Parse instantiation_rte_events (list from container "INSTANTIATION-RTE-EVENTS")
        obj.instantiation_rte_events = []
        container = ARObject._find_child_element(element, "INSTANTIATION-RTE-EVENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.instantiation_rte_events.append(child_value)

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
