"""SwcInternalBehavior AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 345)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 518)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2070)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 246)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 472)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 217)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.internal_behavior import (
    InternalBehavior,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.IncludedDataTypes.included_data_type_set import (
    IncludedDataTypeSet,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup.included_mode_declaration_group_set import (
    IncludedModeDeclarationGroupSet,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstantiationDataDefProps.instantiation_data_def_props import (
    InstantiationDataDefProps,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PerInstanceMemory.per_instance_memory import (
    PerInstanceMemory,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.port_api_option import (
    PortAPIOption,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.runnable_entity import (
    RunnableEntity,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.swc_exclusive_area_policy import (
    SwcExclusiveAreaPolicy,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.VariantHandling.variation_point_proxy import (
    VariationPointProxy,
)


class SwcInternalBehavior(InternalBehavior):
    """AUTOSAR SwcInternalBehavior."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ar_typed_per_refs: list[ARRef]
    events: list[RTEEvent]
    exclusive_areas: list[SwcExclusiveAreaPolicy]
    explicit_inter_refs: list[ARRef]
    implicit_inter_refs: list[ARRef]
    included_data_type_set_refs: list[ARRef]
    included_modes: list[IncludedModeDeclarationGroupSet]
    instantiation_data_defs: list[InstantiationDataDefProps]
    per_instance_memories: list[PerInstanceMemory]
    per_instances: list[ParameterDataPrototype]
    port_api_options: list[PortAPIOption]
    runnables: list[RunnableEntity]
    services: list[Any]
    shareds: list[ParameterDataPrototype]
    supports: Optional[Boolean]
    variation_point_proxies: list[VariationPointProxy]
    def __init__(self) -> None:
        """Initialize SwcInternalBehavior."""
        super().__init__()
        self.ar_typed_per_refs: list[ARRef] = []
        self.events: list[RTEEvent] = []
        self.exclusive_areas: list[SwcExclusiveAreaPolicy] = []
        self.explicit_inter_refs: list[ARRef] = []
        self.implicit_inter_refs: list[ARRef] = []
        self.included_data_type_set_refs: list[ARRef] = []
        self.included_modes: list[IncludedModeDeclarationGroupSet] = []
        self.instantiation_data_defs: list[InstantiationDataDefProps] = []
        self.per_instance_memories: list[PerInstanceMemory] = []
        self.per_instances: list[ParameterDataPrototype] = []
        self.port_api_options: list[PortAPIOption] = []
        self.runnables: list[RunnableEntity] = []
        self.services: list[Any] = []
        self.shareds: list[ParameterDataPrototype] = []
        self.supports: Optional[Boolean] = None
        self.variation_point_proxies: list[VariationPointProxy] = []

    def serialize(self) -> ET.Element:
        """Serialize SwcInternalBehavior to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwcInternalBehavior, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ar_typed_per_refs (list to container "AR-TYPED-PERS")
        if self.ar_typed_per_refs:
            wrapper = ET.Element("AR-TYPED-PERS")
            for item in self.ar_typed_per_refs:
                serialized = ARObject._serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize events (list to container "EVENTS")
        if self.events:
            wrapper = ET.Element("EVENTS")
            for item in self.events:
                serialized = ARObject._serialize_item(item, "RTEEvent")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize exclusive_areas (list to container "EXCLUSIVE-AREAS")
        if self.exclusive_areas:
            wrapper = ET.Element("EXCLUSIVE-AREAS")
            for item in self.exclusive_areas:
                serialized = ARObject._serialize_item(item, "SwcExclusiveAreaPolicy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize explicit_inter_refs (list to container "EXPLICIT-INTERS")
        if self.explicit_inter_refs:
            wrapper = ET.Element("EXPLICIT-INTERS")
            for item in self.explicit_inter_refs:
                serialized = ARObject._serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize implicit_inter_refs (list to container "IMPLICIT-INTERS")
        if self.implicit_inter_refs:
            wrapper = ET.Element("IMPLICIT-INTERS")
            for item in self.implicit_inter_refs:
                serialized = ARObject._serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize included_data_type_set_refs (list to container "INCLUDED-DATA-TYPE-SETS")
        if self.included_data_type_set_refs:
            wrapper = ET.Element("INCLUDED-DATA-TYPE-SETS")
            for item in self.included_data_type_set_refs:
                serialized = ARObject._serialize_item(item, "IncludedDataTypeSet")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize included_modes (list to container "INCLUDED-MODES")
        if self.included_modes:
            wrapper = ET.Element("INCLUDED-MODES")
            for item in self.included_modes:
                serialized = ARObject._serialize_item(item, "IncludedModeDeclarationGroupSet")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize instantiation_data_defs (list to container "INSTANTIATION-DATA-DEFS")
        if self.instantiation_data_defs:
            wrapper = ET.Element("INSTANTIATION-DATA-DEFS")
            for item in self.instantiation_data_defs:
                serialized = ARObject._serialize_item(item, "InstantiationDataDefProps")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize per_instance_memories (list to container "PER-INSTANCE-MEMORIES")
        if self.per_instance_memories:
            wrapper = ET.Element("PER-INSTANCE-MEMORIES")
            for item in self.per_instance_memories:
                serialized = ARObject._serialize_item(item, "PerInstanceMemory")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize per_instances (list to container "PER-INSTANCES")
        if self.per_instances:
            wrapper = ET.Element("PER-INSTANCES")
            for item in self.per_instances:
                serialized = ARObject._serialize_item(item, "ParameterDataPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize port_api_options (list to container "PORT-API-OPTIONS")
        if self.port_api_options:
            wrapper = ET.Element("PORT-API-OPTIONS")
            for item in self.port_api_options:
                serialized = ARObject._serialize_item(item, "PortAPIOption")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize runnables (list to container "RUNNABLES")
        if self.runnables:
            wrapper = ET.Element("RUNNABLES")
            for item in self.runnables:
                serialized = ARObject._serialize_item(item, "RunnableEntity")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize services (list to container "SERVICES")
        if self.services:
            wrapper = ET.Element("SERVICES")
            for item in self.services:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize shareds (list to container "SHAREDS")
        if self.shareds:
            wrapper = ET.Element("SHAREDS")
            for item in self.shareds:
                serialized = ARObject._serialize_item(item, "ParameterDataPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize supports
        if self.supports is not None:
            serialized = ARObject._serialize_item(self.supports, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUPPORTS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize variation_point_proxies (list to container "VARIATION-POINT-PROXIES")
        if self.variation_point_proxies:
            wrapper = ET.Element("VARIATION-POINT-PROXIES")
            for item in self.variation_point_proxies:
                serialized = ARObject._serialize_item(item, "VariationPointProxy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcInternalBehavior":
        """Deserialize XML element to SwcInternalBehavior object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcInternalBehavior object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwcInternalBehavior, cls).deserialize(element)

        # Parse ar_typed_per_refs (list from container "AR-TYPED-PERS")
        obj.ar_typed_per_refs = []
        container = ARObject._find_child_element(element, "AR-TYPED-PERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ar_typed_per_refs.append(child_value)

        # Parse events (list from container "EVENTS")
        obj.events = []
        container = ARObject._find_child_element(element, "EVENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.events.append(child_value)

        # Parse exclusive_areas (list from container "EXCLUSIVE-AREAS")
        obj.exclusive_areas = []
        container = ARObject._find_child_element(element, "EXCLUSIVE-AREAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.exclusive_areas.append(child_value)

        # Parse explicit_inter_refs (list from container "EXPLICIT-INTERS")
        obj.explicit_inter_refs = []
        container = ARObject._find_child_element(element, "EXPLICIT-INTERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.explicit_inter_refs.append(child_value)

        # Parse implicit_inter_refs (list from container "IMPLICIT-INTERS")
        obj.implicit_inter_refs = []
        container = ARObject._find_child_element(element, "IMPLICIT-INTERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.implicit_inter_refs.append(child_value)

        # Parse included_data_type_set_refs (list from container "INCLUDED-DATA-TYPE-SETS")
        obj.included_data_type_set_refs = []
        container = ARObject._find_child_element(element, "INCLUDED-DATA-TYPE-SETS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.included_data_type_set_refs.append(child_value)

        # Parse included_modes (list from container "INCLUDED-MODES")
        obj.included_modes = []
        container = ARObject._find_child_element(element, "INCLUDED-MODES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.included_modes.append(child_value)

        # Parse instantiation_data_defs (list from container "INSTANTIATION-DATA-DEFS")
        obj.instantiation_data_defs = []
        container = ARObject._find_child_element(element, "INSTANTIATION-DATA-DEFS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.instantiation_data_defs.append(child_value)

        # Parse per_instance_memories (list from container "PER-INSTANCE-MEMORIES")
        obj.per_instance_memories = []
        container = ARObject._find_child_element(element, "PER-INSTANCE-MEMORIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.per_instance_memories.append(child_value)

        # Parse per_instances (list from container "PER-INSTANCES")
        obj.per_instances = []
        container = ARObject._find_child_element(element, "PER-INSTANCES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.per_instances.append(child_value)

        # Parse port_api_options (list from container "PORT-API-OPTIONS")
        obj.port_api_options = []
        container = ARObject._find_child_element(element, "PORT-API-OPTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.port_api_options.append(child_value)

        # Parse runnables (list from container "RUNNABLES")
        obj.runnables = []
        container = ARObject._find_child_element(element, "RUNNABLES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.runnables.append(child_value)

        # Parse services (list from container "SERVICES")
        obj.services = []
        container = ARObject._find_child_element(element, "SERVICES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.services.append(child_value)

        # Parse shareds (list from container "SHAREDS")
        obj.shareds = []
        container = ARObject._find_child_element(element, "SHAREDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.shareds.append(child_value)

        # Parse supports
        child = ARObject._find_child_element(element, "SUPPORTS")
        if child is not None:
            supports_value = child.text
            obj.supports = supports_value

        # Parse variation_point_proxies (list from container "VARIATION-POINT-PROXIES")
        obj.variation_point_proxies = []
        container = ARObject._find_child_element(element, "VARIATION-POINT-PROXIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.variation_point_proxies.append(child_value)

        return obj



class SwcInternalBehaviorBuilder:
    """Builder for SwcInternalBehavior."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcInternalBehavior = SwcInternalBehavior()

    def build(self) -> SwcInternalBehavior:
        """Build and return SwcInternalBehavior object.

        Returns:
            SwcInternalBehavior instance
        """
        # TODO: Add validation
        return self._obj
