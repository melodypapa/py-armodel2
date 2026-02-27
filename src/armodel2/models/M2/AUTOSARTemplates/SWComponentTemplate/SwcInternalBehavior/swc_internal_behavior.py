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
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.internal_behavior import (
    InternalBehavior,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.internal_behavior import InternalBehaviorBuilder
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import (
    HandleTerminationAndRestartEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup.included_mode_declaration_group_set import (
    IncludedModeDeclarationGroupSet,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.swc_exclusive_area_policy import (
    SwcExclusiveAreaPolicy,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.IncludedDataTypes.included_data_type_set import (
        IncludedDataTypeSet,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstantiationDataDefProps.instantiation_data_def_props import (
        InstantiationDataDefProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
        ParameterDataPrototype,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PerInstanceMemory.per_instance_memory import (
        PerInstanceMemory,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.port_api_option import (
        PortAPIOption,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
        RTEEvent,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.runnable_entity import (
        RunnableEntity,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping.swc_service_dependency import (
        SwcServiceDependency,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
        VariableDataPrototype,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.VariantHandling.variation_point_proxy import (
        VariationPointProxy,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class SwcInternalBehavior(InternalBehavior):
    """AUTOSAR SwcInternalBehavior."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ar_typed_per_instance_memories: list[VariableDataPrototype]
    events: list[RTEEvent]
    exclusive_area_policies: list[SwcExclusiveAreaPolicy]
    explicit_inter_runnable_variables: list[VariableDataPrototype]
    handle_termination_and_restart: Optional[HandleTerminationAndRestartEnum]
    implicit_inter_runnable_variables: list[VariableDataPrototype]
    included_data_type_sets: list[IncludedDataTypeSet]
    included_mode_declaration_group_sets: list[IncludedModeDeclarationGroupSet]
    instantiation_data_def_props: list[InstantiationDataDefProps]
    per_instance_memories: list[PerInstanceMemory]
    per_instance_parameters: list[ParameterDataPrototype]
    port_api_options: list[PortAPIOption]
    runnables: list[RunnableEntity]
    service_dependencies: list[SwcServiceDependency]
    shared_parameters: list[ParameterDataPrototype]
    support_multiple_instantiations: Optional[Boolean]
    variation_point_proxies: list[VariationPointProxy]
    def __init__(self) -> None:
        """Initialize SwcInternalBehavior."""
        super().__init__()
        self.ar_typed_per_instance_memories: list[VariableDataPrototype] = []
        self.events: list[RTEEvent] = []
        self.exclusive_area_policies: list[SwcExclusiveAreaPolicy] = []
        self.explicit_inter_runnable_variables: list[VariableDataPrototype] = []
        self.handle_termination_and_restart: Optional[HandleTerminationAndRestartEnum] = None
        self.implicit_inter_runnable_variables: list[VariableDataPrototype] = []
        self.included_data_type_sets: list[IncludedDataTypeSet] = []
        self.included_mode_declaration_group_sets: list[IncludedModeDeclarationGroupSet] = []
        self.instantiation_data_def_props: list[InstantiationDataDefProps] = []
        self.per_instance_memories: list[PerInstanceMemory] = []
        self.per_instance_parameters: list[ParameterDataPrototype] = []
        self.port_api_options: list[PortAPIOption] = []
        self.runnables: list[RunnableEntity] = []
        self.service_dependencies: list[SwcServiceDependency] = []
        self.shared_parameters: list[ParameterDataPrototype] = []
        self.support_multiple_instantiations: Optional[Boolean] = None
        self.variation_point_proxies: list[VariationPointProxy] = []

    def serialize(self) -> ET.Element:
        """Serialize SwcInternalBehavior to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwcInternalBehavior, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ar_typed_per_instance_memories (list to container "AR-TYPED-PER-INSTANCE-MEMORYS")
        if self.ar_typed_per_instance_memories:
            wrapper = ET.Element("AR-TYPED-PER-INSTANCE-MEMORYS")
            for item in self.ar_typed_per_instance_memories:
                serialized = SerializationHelper.serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize events (list to container "EVENTS")
        if self.events:
            wrapper = ET.Element("EVENTS")
            for item in self.events:
                serialized = SerializationHelper.serialize_item(item, "RTEEvent")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize exclusive_area_policies (list to container "EXCLUSIVE-AREA-POLICYS")
        if self.exclusive_area_policies:
            wrapper = ET.Element("EXCLUSIVE-AREA-POLICYS")
            for item in self.exclusive_area_policies:
                serialized = SerializationHelper.serialize_item(item, "SwcExclusiveAreaPolicy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize explicit_inter_runnable_variables (list to container "EXPLICIT-INTER-RUNNABLE-VARIABLES")
        if self.explicit_inter_runnable_variables:
            wrapper = ET.Element("EXPLICIT-INTER-RUNNABLE-VARIABLES")
            for item in self.explicit_inter_runnable_variables:
                serialized = SerializationHelper.serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize handle_termination_and_restart
        if self.handle_termination_and_restart is not None:
            serialized = SerializationHelper.serialize_item(self.handle_termination_and_restart, "HandleTerminationAndRestartEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HANDLE-TERMINATION-AND-RESTART")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize implicit_inter_runnable_variables (list to container "IMPLICIT-INTER-RUNNABLE-VARIABLES")
        if self.implicit_inter_runnable_variables:
            wrapper = ET.Element("IMPLICIT-INTER-RUNNABLE-VARIABLES")
            for item in self.implicit_inter_runnable_variables:
                serialized = SerializationHelper.serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize included_data_type_sets (list to container "INCLUDED-DATA-TYPE-SETS")
        if self.included_data_type_sets:
            wrapper = ET.Element("INCLUDED-DATA-TYPE-SETS")
            for item in self.included_data_type_sets:
                serialized = SerializationHelper.serialize_item(item, "IncludedDataTypeSet")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize included_mode_declaration_group_sets (list to container "INCLUDED-MODE-DECLARATION-GROUP-SETS")
        if self.included_mode_declaration_group_sets:
            wrapper = ET.Element("INCLUDED-MODE-DECLARATION-GROUP-SETS")
            for item in self.included_mode_declaration_group_sets:
                serialized = SerializationHelper.serialize_item(item, "IncludedModeDeclarationGroupSet")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize instantiation_data_def_props (list to container "INSTANTIATION-DATA-DEF-PROPS")
        if self.instantiation_data_def_props:
            wrapper = ET.Element("INSTANTIATION-DATA-DEF-PROPS")
            for item in self.instantiation_data_def_props:
                serialized = SerializationHelper.serialize_item(item, "InstantiationDataDefProps")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize per_instance_memories (list to container "PER-INSTANCE-MEMORYS")
        if self.per_instance_memories:
            wrapper = ET.Element("PER-INSTANCE-MEMORYS")
            for item in self.per_instance_memories:
                serialized = SerializationHelper.serialize_item(item, "PerInstanceMemory")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize per_instance_parameters (list to container "PER-INSTANCE-PARAMETERS")
        if self.per_instance_parameters:
            wrapper = ET.Element("PER-INSTANCE-PARAMETERS")
            for item in self.per_instance_parameters:
                serialized = SerializationHelper.serialize_item(item, "ParameterDataPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize port_api_options (list to container "PORT-API-OPTIONS")
        if self.port_api_options:
            wrapper = ET.Element("PORT-API-OPTIONS")
            for item in self.port_api_options:
                serialized = SerializationHelper.serialize_item(item, "PortAPIOption")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize runnables (list to container "RUNNABLES")
        if self.runnables:
            wrapper = ET.Element("RUNNABLES")
            for item in self.runnables:
                serialized = SerializationHelper.serialize_item(item, "RunnableEntity")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize service_dependencies (list to container "SERVICE-DEPENDENCYS")
        if self.service_dependencies:
            wrapper = ET.Element("SERVICE-DEPENDENCYS")
            for item in self.service_dependencies:
                serialized = SerializationHelper.serialize_item(item, "SwcServiceDependency")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize shared_parameters (list to container "SHARED-PARAMETERS")
        if self.shared_parameters:
            wrapper = ET.Element("SHARED-PARAMETERS")
            for item in self.shared_parameters:
                serialized = SerializationHelper.serialize_item(item, "ParameterDataPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize support_multiple_instantiations
        if self.support_multiple_instantiations is not None:
            serialized = SerializationHelper.serialize_item(self.support_multiple_instantiations, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUPPORT-MULTIPLE-INSTANTIATIONS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize variation_point_proxies (list to container "VARIATION-POINT-PROXYS")
        if self.variation_point_proxies:
            wrapper = ET.Element("VARIATION-POINT-PROXYS")
            for item in self.variation_point_proxies:
                serialized = SerializationHelper.serialize_item(item, "VariationPointProxy")
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

        # Parse ar_typed_per_instance_memories (list from container "AR-TYPED-PER-INSTANCE-MEMORYS")
        obj.ar_typed_per_instance_memories = []
        container = SerializationHelper.find_child_element(element, "AR-TYPED-PER-INSTANCE-MEMORYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ar_typed_per_instance_memories.append(child_value)

        # Parse events (list from container "EVENTS")
        obj.events = []
        container = SerializationHelper.find_child_element(element, "EVENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.events.append(child_value)

        # Parse exclusive_area_policies (list from container "EXCLUSIVE-AREA-POLICYS")
        obj.exclusive_area_policies = []
        container = SerializationHelper.find_child_element(element, "EXCLUSIVE-AREA-POLICYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.exclusive_area_policies.append(child_value)

        # Parse explicit_inter_runnable_variables (list from container "EXPLICIT-INTER-RUNNABLE-VARIABLES")
        obj.explicit_inter_runnable_variables = []
        container = SerializationHelper.find_child_element(element, "EXPLICIT-INTER-RUNNABLE-VARIABLES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.explicit_inter_runnable_variables.append(child_value)

        # Parse handle_termination_and_restart
        child = SerializationHelper.find_child_element(element, "HANDLE-TERMINATION-AND-RESTART")
        if child is not None:
            handle_termination_and_restart_value = HandleTerminationAndRestartEnum.deserialize(child)
            obj.handle_termination_and_restart = handle_termination_and_restart_value

        # Parse implicit_inter_runnable_variables (list from container "IMPLICIT-INTER-RUNNABLE-VARIABLES")
        obj.implicit_inter_runnable_variables = []
        container = SerializationHelper.find_child_element(element, "IMPLICIT-INTER-RUNNABLE-VARIABLES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.implicit_inter_runnable_variables.append(child_value)

        # Parse included_data_type_sets (list from container "INCLUDED-DATA-TYPE-SETS")
        obj.included_data_type_sets = []
        container = SerializationHelper.find_child_element(element, "INCLUDED-DATA-TYPE-SETS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.included_data_type_sets.append(child_value)

        # Parse included_mode_declaration_group_sets (list from container "INCLUDED-MODE-DECLARATION-GROUP-SETS")
        obj.included_mode_declaration_group_sets = []
        container = SerializationHelper.find_child_element(element, "INCLUDED-MODE-DECLARATION-GROUP-SETS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.included_mode_declaration_group_sets.append(child_value)

        # Parse instantiation_data_def_props (list from container "INSTANTIATION-DATA-DEF-PROPS")
        obj.instantiation_data_def_props = []
        container = SerializationHelper.find_child_element(element, "INSTANTIATION-DATA-DEF-PROPS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.instantiation_data_def_props.append(child_value)

        # Parse per_instance_memories (list from container "PER-INSTANCE-MEMORYS")
        obj.per_instance_memories = []
        container = SerializationHelper.find_child_element(element, "PER-INSTANCE-MEMORYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.per_instance_memories.append(child_value)

        # Parse per_instance_parameters (list from container "PER-INSTANCE-PARAMETERS")
        obj.per_instance_parameters = []
        container = SerializationHelper.find_child_element(element, "PER-INSTANCE-PARAMETERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.per_instance_parameters.append(child_value)

        # Parse port_api_options (list from container "PORT-API-OPTIONS")
        obj.port_api_options = []
        container = SerializationHelper.find_child_element(element, "PORT-API-OPTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.port_api_options.append(child_value)

        # Parse runnables (list from container "RUNNABLES")
        obj.runnables = []
        container = SerializationHelper.find_child_element(element, "RUNNABLES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.runnables.append(child_value)

        # Parse service_dependencies (list from container "SERVICE-DEPENDENCYS")
        obj.service_dependencies = []
        container = SerializationHelper.find_child_element(element, "SERVICE-DEPENDENCYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.service_dependencies.append(child_value)

        # Parse shared_parameters (list from container "SHARED-PARAMETERS")
        obj.shared_parameters = []
        container = SerializationHelper.find_child_element(element, "SHARED-PARAMETERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.shared_parameters.append(child_value)

        # Parse support_multiple_instantiations
        child = SerializationHelper.find_child_element(element, "SUPPORT-MULTIPLE-INSTANTIATIONS")
        if child is not None:
            support_multiple_instantiations_value = child.text
            obj.support_multiple_instantiations = support_multiple_instantiations_value

        # Parse variation_point_proxies (list from container "VARIATION-POINT-PROXYS")
        obj.variation_point_proxies = []
        container = SerializationHelper.find_child_element(element, "VARIATION-POINT-PROXYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.variation_point_proxies.append(child_value)

        return obj



class SwcInternalBehaviorBuilder(InternalBehaviorBuilder):
    """Builder for SwcInternalBehavior with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwcInternalBehavior = SwcInternalBehavior()


    def with_ar_typed_per_instance_memories(self, items: list[VariableDataPrototype]) -> "SwcInternalBehaviorBuilder":
        """Set ar_typed_per_instance_memories list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.ar_typed_per_instance_memories = list(items) if items else []
        return self

    def with_events(self, items: list[RTEEvent]) -> "SwcInternalBehaviorBuilder":
        """Set events list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.events = list(items) if items else []
        return self

    def with_exclusive_area_policies(self, items: list[SwcExclusiveAreaPolicy]) -> "SwcInternalBehaviorBuilder":
        """Set exclusive_area_policies list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.exclusive_area_policies = list(items) if items else []
        return self

    def with_explicit_inter_runnable_variables(self, items: list[VariableDataPrototype]) -> "SwcInternalBehaviorBuilder":
        """Set explicit_inter_runnable_variables list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.explicit_inter_runnable_variables = list(items) if items else []
        return self

    def with_handle_termination_and_restart(self, value: Optional[HandleTerminationAndRestartEnum]) -> "SwcInternalBehaviorBuilder":
        """Set handle_termination_and_restart attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.handle_termination_and_restart = value
        return self

    def with_implicit_inter_runnable_variables(self, items: list[VariableDataPrototype]) -> "SwcInternalBehaviorBuilder":
        """Set implicit_inter_runnable_variables list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.implicit_inter_runnable_variables = list(items) if items else []
        return self

    def with_included_data_type_sets(self, items: list[IncludedDataTypeSet]) -> "SwcInternalBehaviorBuilder":
        """Set included_data_type_sets list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.included_data_type_sets = list(items) if items else []
        return self

    def with_included_mode_declaration_group_sets(self, items: list[IncludedModeDeclarationGroupSet]) -> "SwcInternalBehaviorBuilder":
        """Set included_mode_declaration_group_sets list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.included_mode_declaration_group_sets = list(items) if items else []
        return self

    def with_instantiation_data_def_props(self, items: list[InstantiationDataDefProps]) -> "SwcInternalBehaviorBuilder":
        """Set instantiation_data_def_props list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.instantiation_data_def_props = list(items) if items else []
        return self

    def with_per_instance_memories(self, items: list[PerInstanceMemory]) -> "SwcInternalBehaviorBuilder":
        """Set per_instance_memories list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.per_instance_memories = list(items) if items else []
        return self

    def with_per_instance_parameters(self, items: list[ParameterDataPrototype]) -> "SwcInternalBehaviorBuilder":
        """Set per_instance_parameters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.per_instance_parameters = list(items) if items else []
        return self

    def with_port_api_options(self, items: list[PortAPIOption]) -> "SwcInternalBehaviorBuilder":
        """Set port_api_options list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.port_api_options = list(items) if items else []
        return self

    def with_runnables(self, items: list[RunnableEntity]) -> "SwcInternalBehaviorBuilder":
        """Set runnables list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.runnables = list(items) if items else []
        return self

    def with_service_dependencies(self, items: list[SwcServiceDependency]) -> "SwcInternalBehaviorBuilder":
        """Set service_dependencies list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.service_dependencies = list(items) if items else []
        return self

    def with_shared_parameters(self, items: list[ParameterDataPrototype]) -> "SwcInternalBehaviorBuilder":
        """Set shared_parameters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.shared_parameters = list(items) if items else []
        return self

    def with_support_multiple_instantiations(self, value: Optional[Boolean]) -> "SwcInternalBehaviorBuilder":
        """Set support_multiple_instantiations attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.support_multiple_instantiations = value
        return self

    def with_variation_point_proxies(self, items: list[VariationPointProxy]) -> "SwcInternalBehaviorBuilder":
        """Set variation_point_proxies list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.variation_point_proxies = list(items) if items else []
        return self


    def add_ar_typed_per_instance_memory(self, item: VariableDataPrototype) -> "SwcInternalBehaviorBuilder":
        """Add a single item to ar_typed_per_instance_memories list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.ar_typed_per_instance_memories.append(item)
        return self

    def clear_ar_typed_per_instance_memories(self) -> "SwcInternalBehaviorBuilder":
        """Clear all items from ar_typed_per_instance_memories list.

        Returns:
            self for method chaining
        """
        self._obj.ar_typed_per_instance_memories = []
        return self

    def add_event(self, item: RTEEvent) -> "SwcInternalBehaviorBuilder":
        """Add a single item to events list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.events.append(item)
        return self

    def clear_events(self) -> "SwcInternalBehaviorBuilder":
        """Clear all items from events list.

        Returns:
            self for method chaining
        """
        self._obj.events = []
        return self

    def add_exclusive_area_policy(self, item: SwcExclusiveAreaPolicy) -> "SwcInternalBehaviorBuilder":
        """Add a single item to exclusive_area_policies list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.exclusive_area_policies.append(item)
        return self

    def clear_exclusive_area_policies(self) -> "SwcInternalBehaviorBuilder":
        """Clear all items from exclusive_area_policies list.

        Returns:
            self for method chaining
        """
        self._obj.exclusive_area_policies = []
        return self

    def add_explicit_inter_runnable_variable(self, item: VariableDataPrototype) -> "SwcInternalBehaviorBuilder":
        """Add a single item to explicit_inter_runnable_variables list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.explicit_inter_runnable_variables.append(item)
        return self

    def clear_explicit_inter_runnable_variables(self) -> "SwcInternalBehaviorBuilder":
        """Clear all items from explicit_inter_runnable_variables list.

        Returns:
            self for method chaining
        """
        self._obj.explicit_inter_runnable_variables = []
        return self

    def add_implicit_inter_runnable_variable(self, item: VariableDataPrototype) -> "SwcInternalBehaviorBuilder":
        """Add a single item to implicit_inter_runnable_variables list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.implicit_inter_runnable_variables.append(item)
        return self

    def clear_implicit_inter_runnable_variables(self) -> "SwcInternalBehaviorBuilder":
        """Clear all items from implicit_inter_runnable_variables list.

        Returns:
            self for method chaining
        """
        self._obj.implicit_inter_runnable_variables = []
        return self

    def add_included_data_type_set(self, item: IncludedDataTypeSet) -> "SwcInternalBehaviorBuilder":
        """Add a single item to included_data_type_sets list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.included_data_type_sets.append(item)
        return self

    def clear_included_data_type_sets(self) -> "SwcInternalBehaviorBuilder":
        """Clear all items from included_data_type_sets list.

        Returns:
            self for method chaining
        """
        self._obj.included_data_type_sets = []
        return self

    def add_included_mode_declaration_group_set(self, item: IncludedModeDeclarationGroupSet) -> "SwcInternalBehaviorBuilder":
        """Add a single item to included_mode_declaration_group_sets list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.included_mode_declaration_group_sets.append(item)
        return self

    def clear_included_mode_declaration_group_sets(self) -> "SwcInternalBehaviorBuilder":
        """Clear all items from included_mode_declaration_group_sets list.

        Returns:
            self for method chaining
        """
        self._obj.included_mode_declaration_group_sets = []
        return self

    def add_instantiation_data_def_prop(self, item: InstantiationDataDefProps) -> "SwcInternalBehaviorBuilder":
        """Add a single item to instantiation_data_def_props list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.instantiation_data_def_props.append(item)
        return self

    def clear_instantiation_data_def_props(self) -> "SwcInternalBehaviorBuilder":
        """Clear all items from instantiation_data_def_props list.

        Returns:
            self for method chaining
        """
        self._obj.instantiation_data_def_props = []
        return self

    def add_per_instance_memory(self, item: PerInstanceMemory) -> "SwcInternalBehaviorBuilder":
        """Add a single item to per_instance_memories list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.per_instance_memories.append(item)
        return self

    def clear_per_instance_memories(self) -> "SwcInternalBehaviorBuilder":
        """Clear all items from per_instance_memories list.

        Returns:
            self for method chaining
        """
        self._obj.per_instance_memories = []
        return self

    def add_per_instance_parameter(self, item: ParameterDataPrototype) -> "SwcInternalBehaviorBuilder":
        """Add a single item to per_instance_parameters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.per_instance_parameters.append(item)
        return self

    def clear_per_instance_parameters(self) -> "SwcInternalBehaviorBuilder":
        """Clear all items from per_instance_parameters list.

        Returns:
            self for method chaining
        """
        self._obj.per_instance_parameters = []
        return self

    def add_port_api_option(self, item: PortAPIOption) -> "SwcInternalBehaviorBuilder":
        """Add a single item to port_api_options list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.port_api_options.append(item)
        return self

    def clear_port_api_options(self) -> "SwcInternalBehaviorBuilder":
        """Clear all items from port_api_options list.

        Returns:
            self for method chaining
        """
        self._obj.port_api_options = []
        return self

    def add_runnable(self, item: RunnableEntity) -> "SwcInternalBehaviorBuilder":
        """Add a single item to runnables list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.runnables.append(item)
        return self

    def clear_runnables(self) -> "SwcInternalBehaviorBuilder":
        """Clear all items from runnables list.

        Returns:
            self for method chaining
        """
        self._obj.runnables = []
        return self

    def add_service_dependency(self, item: SwcServiceDependency) -> "SwcInternalBehaviorBuilder":
        """Add a single item to service_dependencies list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.service_dependencies.append(item)
        return self

    def clear_service_dependencies(self) -> "SwcInternalBehaviorBuilder":
        """Clear all items from service_dependencies list.

        Returns:
            self for method chaining
        """
        self._obj.service_dependencies = []
        return self

    def add_shared_parameter(self, item: ParameterDataPrototype) -> "SwcInternalBehaviorBuilder":
        """Add a single item to shared_parameters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.shared_parameters.append(item)
        return self

    def clear_shared_parameters(self) -> "SwcInternalBehaviorBuilder":
        """Clear all items from shared_parameters list.

        Returns:
            self for method chaining
        """
        self._obj.shared_parameters = []
        return self

    def add_variation_point_proxy(self, item: VariationPointProxy) -> "SwcInternalBehaviorBuilder":
        """Add a single item to variation_point_proxies list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.variation_point_proxies.append(item)
        return self

    def clear_variation_point_proxies(self) -> "SwcInternalBehaviorBuilder":
        """Clear all items from variation_point_proxies list.

        Returns:
            self for method chaining
        """
        self._obj.variation_point_proxies = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> SwcInternalBehavior:
        """Build and return the SwcInternalBehavior instance with validation."""
        self._validate_instance()
        pass
        return self._obj