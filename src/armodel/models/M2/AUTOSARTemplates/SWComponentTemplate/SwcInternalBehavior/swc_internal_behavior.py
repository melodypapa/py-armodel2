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
from armodel.serialization.decorators import xml_element_name

from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.internal_behavior import (
    InternalBehavior,
)
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.internal_behavior import InternalBehaviorBuilder
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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


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
    _per_instance_memories: list[PerInstanceMemory]
    per_instances: list[ParameterDataPrototype]
    port_api_options: list[PortAPIOption]
    runnables: list[RunnableEntity]
    services: list[Any]
    shareds: list[ParameterDataPrototype]
    supports: Optional[Boolean]
    _variation_point_proxies: list[VariationPointProxy]
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
        self._per_instance_memories: list[PerInstanceMemory] = []
        self.per_instances: list[ParameterDataPrototype] = []
        self.port_api_options: list[PortAPIOption] = []
        self.runnables: list[RunnableEntity] = []
        self.services: list[Any] = []
        self.shareds: list[ParameterDataPrototype] = []
        self.supports: Optional[Boolean] = None
        self._variation_point_proxies: list[VariationPointProxy] = []
    @property
    @xml_element_name("PER-INSTANCE-MEMORYS")
    def per_instance_memories(self) -> list[PerInstanceMemory]:
        """Get per_instance_memories with custom XML element name."""
        return self._per_instance_memories

    @per_instance_memories.setter
    def per_instance_memories(self, value: list[PerInstanceMemory]) -> None:
        """Set per_instance_memories with custom XML element name."""
        self._per_instance_memories = value

    @property
    @xml_element_name("VARIATION-POINT-PROXYS")
    def variation_point_proxies(self) -> list[VariationPointProxy]:
        """Get variation_point_proxies with custom XML element name."""
        return self._variation_point_proxies

    @variation_point_proxies.setter
    def variation_point_proxies(self, value: list[VariationPointProxy]) -> None:
        """Set variation_point_proxies with custom XML element name."""
        self._variation_point_proxies = value


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

        # Serialize ar_typed_per_refs (list to container "AR-TYPED-PER-REFS")
        if self.ar_typed_per_refs:
            wrapper = ET.Element("AR-TYPED-PER-REFS")
            for item in self.ar_typed_per_refs:
                serialized = SerializationHelper.serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    child_elem = ET.Element("AR-TYPED-PER-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
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

        # Serialize exclusive_areas (list to container "EXCLUSIVE-AREAS")
        if self.exclusive_areas:
            wrapper = ET.Element("EXCLUSIVE-AREAS")
            for item in self.exclusive_areas:
                serialized = SerializationHelper.serialize_item(item, "SwcExclusiveAreaPolicy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize explicit_inter_refs (list to container "EXPLICIT-INTER-REFS")
        if self.explicit_inter_refs:
            wrapper = ET.Element("EXPLICIT-INTER-REFS")
            for item in self.explicit_inter_refs:
                serialized = SerializationHelper.serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    child_elem = ET.Element("EXPLICIT-INTER-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize implicit_inter_refs (list to container "IMPLICIT-INTER-REFS")
        if self.implicit_inter_refs:
            wrapper = ET.Element("IMPLICIT-INTER-REFS")
            for item in self.implicit_inter_refs:
                serialized = SerializationHelper.serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    child_elem = ET.Element("IMPLICIT-INTER-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize included_data_type_set_refs (list to container "INCLUDED-DATA-TYPE-SET-REFS")
        if self.included_data_type_set_refs:
            wrapper = ET.Element("INCLUDED-DATA-TYPE-SET-REFS")
            for item in self.included_data_type_set_refs:
                serialized = SerializationHelper.serialize_item(item, "IncludedDataTypeSet")
                if serialized is not None:
                    child_elem = ET.Element("INCLUDED-DATA-TYPE-SET-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize included_modes (list to container "INCLUDED-MODES")
        if self.included_modes:
            wrapper = ET.Element("INCLUDED-MODES")
            for item in self.included_modes:
                serialized = SerializationHelper.serialize_item(item, "IncludedModeDeclarationGroupSet")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize instantiation_data_defs (list to container "INSTANTIATION-DATA-DEFS")
        if self.instantiation_data_defs:
            wrapper = ET.Element("INSTANTIATION-DATA-DEFS")
            for item in self.instantiation_data_defs:
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

        # Serialize per_instances (list to container "PER-INSTANCES")
        if self.per_instances:
            wrapper = ET.Element("PER-INSTANCES")
            for item in self.per_instances:
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

        # Serialize services (list to container "SERVICES")
        if self.services:
            wrapper = ET.Element("SERVICES")
            for item in self.services:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize shareds (list to container "SHAREDS")
        if self.shareds:
            wrapper = ET.Element("SHAREDS")
            for item in self.shareds:
                serialized = SerializationHelper.serialize_item(item, "ParameterDataPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize supports
        if self.supports is not None:
            serialized = SerializationHelper.serialize_item(self.supports, "Boolean")
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

        # Parse ar_typed_per_refs (list from container "AR-TYPED-PER-REFS")
        obj.ar_typed_per_refs = []
        container = SerializationHelper.find_child_element(element, "AR-TYPED-PER-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ar_typed_per_refs.append(child_value)

        # Parse events (list from container "EVENTS")
        obj.events = []
        container = SerializationHelper.find_child_element(element, "EVENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.events.append(child_value)

        # Parse exclusive_areas (list from container "EXCLUSIVE-AREAS")
        obj.exclusive_areas = []
        container = SerializationHelper.find_child_element(element, "EXCLUSIVE-AREAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.exclusive_areas.append(child_value)

        # Parse explicit_inter_refs (list from container "EXPLICIT-INTER-REFS")
        obj.explicit_inter_refs = []
        container = SerializationHelper.find_child_element(element, "EXPLICIT-INTER-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.explicit_inter_refs.append(child_value)

        # Parse implicit_inter_refs (list from container "IMPLICIT-INTER-REFS")
        obj.implicit_inter_refs = []
        container = SerializationHelper.find_child_element(element, "IMPLICIT-INTER-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.implicit_inter_refs.append(child_value)

        # Parse included_data_type_set_refs (list from container "INCLUDED-DATA-TYPE-SET-REFS")
        obj.included_data_type_set_refs = []
        container = SerializationHelper.find_child_element(element, "INCLUDED-DATA-TYPE-SET-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.included_data_type_set_refs.append(child_value)

        # Parse included_modes (list from container "INCLUDED-MODES")
        obj.included_modes = []
        container = SerializationHelper.find_child_element(element, "INCLUDED-MODES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.included_modes.append(child_value)

        # Parse instantiation_data_defs (list from container "INSTANTIATION-DATA-DEFS")
        obj.instantiation_data_defs = []
        container = SerializationHelper.find_child_element(element, "INSTANTIATION-DATA-DEFS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.instantiation_data_defs.append(child_value)

        # Parse per_instance_memories (list from container "PER-INSTANCE-MEMORYS")
        obj.per_instance_memories = []
        container = SerializationHelper.find_child_element(element, "PER-INSTANCE-MEMORYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.per_instance_memories.append(child_value)

        # Parse per_instances (list from container "PER-INSTANCES")
        obj.per_instances = []
        container = SerializationHelper.find_child_element(element, "PER-INSTANCES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.per_instances.append(child_value)

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

        # Parse services (list from container "SERVICES")
        obj.services = []
        container = SerializationHelper.find_child_element(element, "SERVICES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.services.append(child_value)

        # Parse shareds (list from container "SHAREDS")
        obj.shareds = []
        container = SerializationHelper.find_child_element(element, "SHAREDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.shareds.append(child_value)

        # Parse supports
        child = SerializationHelper.find_child_element(element, "SUPPORTS")
        if child is not None:
            supports_value = child.text
            obj.supports = supports_value

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


    def with_ar_typed_pers(self, items: list[VariableDataPrototype]) -> "SwcInternalBehaviorBuilder":
        """Set ar_typed_pers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.ar_typed_pers = list(items) if items else []
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

    def with_exclusive_areas(self, items: list[SwcExclusiveAreaPolicy]) -> "SwcInternalBehaviorBuilder":
        """Set exclusive_areas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.exclusive_areas = list(items) if items else []
        return self

    def with_explicit_inters(self, items: list[VariableDataPrototype]) -> "SwcInternalBehaviorBuilder":
        """Set explicit_inters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.explicit_inters = list(items) if items else []
        return self

    def with_implicit_inters(self, items: list[VariableDataPrototype]) -> "SwcInternalBehaviorBuilder":
        """Set implicit_inters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.implicit_inters = list(items) if items else []
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

    def with_included_modes(self, items: list[IncludedModeDeclarationGroupSet]) -> "SwcInternalBehaviorBuilder":
        """Set included_modes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.included_modes = list(items) if items else []
        return self

    def with_instantiation_data_defs(self, items: list[InstantiationDataDefProps]) -> "SwcInternalBehaviorBuilder":
        """Set instantiation_data_defs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.instantiation_data_defs = list(items) if items else []
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

    def with_per_instances(self, items: list[ParameterDataPrototype]) -> "SwcInternalBehaviorBuilder":
        """Set per_instances list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.per_instances = list(items) if items else []
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

    def with_services(self, items: list[any (SwcService)]) -> "SwcInternalBehaviorBuilder":
        """Set services list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.services = list(items) if items else []
        return self

    def with_shareds(self, items: list[ParameterDataPrototype]) -> "SwcInternalBehaviorBuilder":
        """Set shareds list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.shareds = list(items) if items else []
        return self

    def with_supports(self, value: Optional[Boolean]) -> "SwcInternalBehaviorBuilder":
        """Set supports attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.supports = value
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


    def add_ar_typed_per(self, item: VariableDataPrototype) -> "SwcInternalBehaviorBuilder":
        """Add a single item to ar_typed_pers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.ar_typed_pers.append(item)
        return self

    def clear_ar_typed_pers(self) -> "SwcInternalBehaviorBuilder":
        """Clear all items from ar_typed_pers list.

        Returns:
            self for method chaining
        """
        self._obj.ar_typed_pers = []
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

    def add_exclusive_area(self, item: SwcExclusiveAreaPolicy) -> "SwcInternalBehaviorBuilder":
        """Add a single item to exclusive_areas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.exclusive_areas.append(item)
        return self

    def clear_exclusive_areas(self) -> "SwcInternalBehaviorBuilder":
        """Clear all items from exclusive_areas list.

        Returns:
            self for method chaining
        """
        self._obj.exclusive_areas = []
        return self

    def add_explicit_inter(self, item: VariableDataPrototype) -> "SwcInternalBehaviorBuilder":
        """Add a single item to explicit_inters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.explicit_inters.append(item)
        return self

    def clear_explicit_inters(self) -> "SwcInternalBehaviorBuilder":
        """Clear all items from explicit_inters list.

        Returns:
            self for method chaining
        """
        self._obj.explicit_inters = []
        return self

    def add_implicit_inter(self, item: VariableDataPrototype) -> "SwcInternalBehaviorBuilder":
        """Add a single item to implicit_inters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.implicit_inters.append(item)
        return self

    def clear_implicit_inters(self) -> "SwcInternalBehaviorBuilder":
        """Clear all items from implicit_inters list.

        Returns:
            self for method chaining
        """
        self._obj.implicit_inters = []
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

    def add_included_mode(self, item: IncludedModeDeclarationGroupSet) -> "SwcInternalBehaviorBuilder":
        """Add a single item to included_modes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.included_modes.append(item)
        return self

    def clear_included_modes(self) -> "SwcInternalBehaviorBuilder":
        """Clear all items from included_modes list.

        Returns:
            self for method chaining
        """
        self._obj.included_modes = []
        return self

    def add_instantiation_data_def(self, item: InstantiationDataDefProps) -> "SwcInternalBehaviorBuilder":
        """Add a single item to instantiation_data_defs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.instantiation_data_defs.append(item)
        return self

    def clear_instantiation_data_defs(self) -> "SwcInternalBehaviorBuilder":
        """Clear all items from instantiation_data_defs list.

        Returns:
            self for method chaining
        """
        self._obj.instantiation_data_defs = []
        return self

    def add_per_instance_memorie(self, item: PerInstanceMemory) -> "SwcInternalBehaviorBuilder":
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

    def add_per_instance(self, item: ParameterDataPrototype) -> "SwcInternalBehaviorBuilder":
        """Add a single item to per_instances list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.per_instances.append(item)
        return self

    def clear_per_instances(self) -> "SwcInternalBehaviorBuilder":
        """Clear all items from per_instances list.

        Returns:
            self for method chaining
        """
        self._obj.per_instances = []
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

    def add_service(self, item: any (SwcService)) -> "SwcInternalBehaviorBuilder":
        """Add a single item to services list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.services.append(item)
        return self

    def clear_services(self) -> "SwcInternalBehaviorBuilder":
        """Clear all items from services list.

        Returns:
            self for method chaining
        """
        self._obj.services = []
        return self

    def add_shared(self, item: ParameterDataPrototype) -> "SwcInternalBehaviorBuilder":
        """Add a single item to shareds list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.shareds.append(item)
        return self

    def clear_shareds(self) -> "SwcInternalBehaviorBuilder":
        """Clear all items from shareds list.

        Returns:
            self for method chaining
        """
        self._obj.shareds = []
        return self

    def add_variation_point_proxie(self, item: VariationPointProxy) -> "SwcInternalBehaviorBuilder":
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
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

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