"""RunnableEntity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 331)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 524)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2050)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 240)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 461)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 203)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    CIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.Trigger.external_triggering_point import (
    ExternalTriggeringPoint,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.Trigger.internal_triggering_point import (
    InternalTriggeringPoint,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup.mode_access_point import (
    ModeAccessPoint,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup.mode_switch_point import (
    ModeSwitchPoint,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.parameter_access import (
        ParameterAccess,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall.server_call_point import (
        ServerCallPoint,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.variable_access import (
        VariableAccess,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.wait_point import (
        WaitPoint,
    )



class RunnableEntity(ExecutableEntity):
    """AUTOSAR RunnableEntity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    arguments: list[RunnableEntity]
    asynchronous_servers: list[Any]
    can_be_invoked: Optional[Boolean]
    data_reads: list[VariableAccess]
    data_receives: list[VariableAccess]
    data_send_points: list[VariableAccess]
    data_writes: list[VariableAccess]
    external_refs: list[ARRef]
    internal_refs: list[ARRef]
    mode_access_points: list[ModeAccessPoint]
    mode_switch_points: list[ModeSwitchPoint]
    parameter_accesses: list[ParameterAccess]
    read_locals: list[VariableAccess]
    server_call_points: list[ServerCallPoint]
    symbol: Optional[CIdentifier]
    wait_points: list[WaitPoint]
    written_locals: list[VariableAccess]
    def __init__(self) -> None:
        """Initialize RunnableEntity."""
        super().__init__()
        self.arguments: list[RunnableEntity] = []
        self.asynchronous_servers: list[Any] = []
        self.can_be_invoked: Optional[Boolean] = None
        self.data_reads: list[VariableAccess] = []
        self.data_receives: list[VariableAccess] = []
        self.data_send_points: list[VariableAccess] = []
        self.data_writes: list[VariableAccess] = []
        self.external_refs: list[ARRef] = []
        self.internal_refs: list[ARRef] = []
        self.mode_access_points: list[ModeAccessPoint] = []
        self.mode_switch_points: list[ModeSwitchPoint] = []
        self.parameter_accesses: list[ParameterAccess] = []
        self.read_locals: list[VariableAccess] = []
        self.server_call_points: list[ServerCallPoint] = []
        self.symbol: Optional[CIdentifier] = None
        self.wait_points: list[WaitPoint] = []
        self.written_locals: list[VariableAccess] = []

    def serialize(self) -> ET.Element:
        """Serialize RunnableEntity to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RunnableEntity, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize arguments (list to container "ARGUMENTS")
        if self.arguments:
            wrapper = ET.Element("ARGUMENTS")
            for item in self.arguments:
                serialized = SerializationHelper.serialize_item(item, "RunnableEntity")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize asynchronous_servers (list to container "ASYNCHRONOUS-SERVERS")
        if self.asynchronous_servers:
            wrapper = ET.Element("ASYNCHRONOUS-SERVERS")
            for item in self.asynchronous_servers:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize can_be_invoked
        if self.can_be_invoked is not None:
            serialized = SerializationHelper.serialize_item(self.can_be_invoked, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAN-BE-INVOKED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize data_reads (list to container "DATA-READS")
        if self.data_reads:
            wrapper = ET.Element("DATA-READS")
            for item in self.data_reads:
                serialized = SerializationHelper.serialize_item(item, "VariableAccess")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize data_receives (list to container "DATA-RECEIVES")
        if self.data_receives:
            wrapper = ET.Element("DATA-RECEIVES")
            for item in self.data_receives:
                serialized = SerializationHelper.serialize_item(item, "VariableAccess")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize data_send_points (list to container "DATA-SEND-POINTS")
        if self.data_send_points:
            wrapper = ET.Element("DATA-SEND-POINTS")
            for item in self.data_send_points:
                serialized = SerializationHelper.serialize_item(item, "VariableAccess")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize data_writes (list to container "DATA-WRITES")
        if self.data_writes:
            wrapper = ET.Element("DATA-WRITES")
            for item in self.data_writes:
                serialized = SerializationHelper.serialize_item(item, "VariableAccess")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize external_refs (list to container "EXTERNAL-REFS")
        if self.external_refs:
            wrapper = ET.Element("EXTERNAL-REFS")
            for item in self.external_refs:
                serialized = SerializationHelper.serialize_item(item, "ExternalTriggeringPoint")
                if serialized is not None:
                    child_elem = ET.Element("EXTERNAL-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize internal_refs (list to container "INTERNAL-REFS")
        if self.internal_refs:
            wrapper = ET.Element("INTERNAL-REFS")
            for item in self.internal_refs:
                serialized = SerializationHelper.serialize_item(item, "InternalTriggeringPoint")
                if serialized is not None:
                    child_elem = ET.Element("INTERNAL-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mode_access_points (list to container "MODE-ACCESS-POINTS")
        if self.mode_access_points:
            wrapper = ET.Element("MODE-ACCESS-POINTS")
            for item in self.mode_access_points:
                serialized = SerializationHelper.serialize_item(item, "ModeAccessPoint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mode_switch_points (list to container "MODE-SWITCH-POINTS")
        if self.mode_switch_points:
            wrapper = ET.Element("MODE-SWITCH-POINTS")
            for item in self.mode_switch_points:
                serialized = SerializationHelper.serialize_item(item, "ModeSwitchPoint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize parameter_accesses (list to container "PARAMETER-ACCESSES")
        if self.parameter_accesses:
            wrapper = ET.Element("PARAMETER-ACCESSES")
            for item in self.parameter_accesses:
                serialized = SerializationHelper.serialize_item(item, "ParameterAccess")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize read_locals (list to container "READ-LOCALS")
        if self.read_locals:
            wrapper = ET.Element("READ-LOCALS")
            for item in self.read_locals:
                serialized = SerializationHelper.serialize_item(item, "VariableAccess")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize server_call_points (list to container "SERVER-CALL-POINTS")
        if self.server_call_points:
            wrapper = ET.Element("SERVER-CALL-POINTS")
            for item in self.server_call_points:
                serialized = SerializationHelper.serialize_item(item, "ServerCallPoint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize symbol
        if self.symbol is not None:
            serialized = SerializationHelper.serialize_item(self.symbol, "CIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYMBOL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize wait_points (list to container "WAIT-POINTS")
        if self.wait_points:
            wrapper = ET.Element("WAIT-POINTS")
            for item in self.wait_points:
                serialized = SerializationHelper.serialize_item(item, "WaitPoint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize written_locals (list to container "WRITTEN-LOCALS")
        if self.written_locals:
            wrapper = ET.Element("WRITTEN-LOCALS")
            for item in self.written_locals:
                serialized = SerializationHelper.serialize_item(item, "VariableAccess")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RunnableEntity":
        """Deserialize XML element to RunnableEntity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RunnableEntity object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RunnableEntity, cls).deserialize(element)

        # Parse arguments (list from container "ARGUMENTS")
        obj.arguments = []
        container = SerializationHelper.find_child_element(element, "ARGUMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.arguments.append(child_value)

        # Parse asynchronous_servers (list from container "ASYNCHRONOUS-SERVERS")
        obj.asynchronous_servers = []
        container = SerializationHelper.find_child_element(element, "ASYNCHRONOUS-SERVERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.asynchronous_servers.append(child_value)

        # Parse can_be_invoked
        child = SerializationHelper.find_child_element(element, "CAN-BE-INVOKED")
        if child is not None:
            can_be_invoked_value = child.text
            obj.can_be_invoked = can_be_invoked_value

        # Parse data_reads (list from container "DATA-READS")
        obj.data_reads = []
        container = SerializationHelper.find_child_element(element, "DATA-READS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_reads.append(child_value)

        # Parse data_receives (list from container "DATA-RECEIVES")
        obj.data_receives = []
        container = SerializationHelper.find_child_element(element, "DATA-RECEIVES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_receives.append(child_value)

        # Parse data_send_points (list from container "DATA-SEND-POINTS")
        obj.data_send_points = []
        container = SerializationHelper.find_child_element(element, "DATA-SEND-POINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_send_points.append(child_value)

        # Parse data_writes (list from container "DATA-WRITES")
        obj.data_writes = []
        container = SerializationHelper.find_child_element(element, "DATA-WRITES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_writes.append(child_value)

        # Parse external_refs (list from container "EXTERNAL-REFS")
        obj.external_refs = []
        container = SerializationHelper.find_child_element(element, "EXTERNAL-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.external_refs.append(child_value)

        # Parse internal_refs (list from container "INTERNAL-REFS")
        obj.internal_refs = []
        container = SerializationHelper.find_child_element(element, "INTERNAL-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.internal_refs.append(child_value)

        # Parse mode_access_points (list from container "MODE-ACCESS-POINTS")
        obj.mode_access_points = []
        container = SerializationHelper.find_child_element(element, "MODE-ACCESS-POINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mode_access_points.append(child_value)

        # Parse mode_switch_points (list from container "MODE-SWITCH-POINTS")
        obj.mode_switch_points = []
        container = SerializationHelper.find_child_element(element, "MODE-SWITCH-POINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mode_switch_points.append(child_value)

        # Parse parameter_accesses (list from container "PARAMETER-ACCESSES")
        obj.parameter_accesses = []
        container = SerializationHelper.find_child_element(element, "PARAMETER-ACCESSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.parameter_accesses.append(child_value)

        # Parse read_locals (list from container "READ-LOCALS")
        obj.read_locals = []
        container = SerializationHelper.find_child_element(element, "READ-LOCALS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.read_locals.append(child_value)

        # Parse server_call_points (list from container "SERVER-CALL-POINTS")
        obj.server_call_points = []
        container = SerializationHelper.find_child_element(element, "SERVER-CALL-POINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.server_call_points.append(child_value)

        # Parse symbol
        child = SerializationHelper.find_child_element(element, "SYMBOL")
        if child is not None:
            symbol_value = SerializationHelper.deserialize_by_tag(child, "CIdentifier")
            obj.symbol = symbol_value

        # Parse wait_points (list from container "WAIT-POINTS")
        obj.wait_points = []
        container = SerializationHelper.find_child_element(element, "WAIT-POINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.wait_points.append(child_value)

        # Parse written_locals (list from container "WRITTEN-LOCALS")
        obj.written_locals = []
        container = SerializationHelper.find_child_element(element, "WRITTEN-LOCALS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.written_locals.append(child_value)

        return obj



class RunnableEntityBuilder:
    """Builder for RunnableEntity with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: RunnableEntity = RunnableEntity()


    def with_short_name(self, value: Identifier) -> "RunnableEntityBuilder":
        """Set short_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_name = value
        return self

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "RunnableEntityBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "RunnableEntityBuilder":
        """Set long_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.long_name = value
        return self

    def with_admin_data(self, value: Optional[AdminData]) -> "RunnableEntityBuilder":
        """Set admin_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.admin_data = value
        return self

    def with_annotations(self, items: list[Annotation]) -> "RunnableEntityBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "RunnableEntityBuilder":
        """Set desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_category(self, value: Optional[CategoryString]) -> "RunnableEntityBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "RunnableEntityBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.introduction = value
        return self

    def with_uuid(self, value: Optional[String]) -> "RunnableEntityBuilder":
        """Set uuid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uuid = value
        return self

    def with_activations(self, items: list[ExecutableEntity]) -> "RunnableEntityBuilder":
        """Set activations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.activations = list(items) if items else []
        return self

    def with_can_enters(self, items: list[ExclusiveArea]) -> "RunnableEntityBuilder":
        """Set can_enters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.can_enters = list(items) if items else []
        return self

    def with_exclusive_area_nestings(self, items: list[ExclusiveAreaNestingOrder]) -> "RunnableEntityBuilder":
        """Set exclusive_area_nestings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.exclusive_area_nestings = list(items) if items else []
        return self

    def with_minimum_start(self, value: Optional[TimeValue]) -> "RunnableEntityBuilder":
        """Set minimum_start attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.minimum_start = value
        return self

    def with_reentrancy_level_enum(self, value: Optional[ReentrancyLevelEnum]) -> "RunnableEntityBuilder":
        """Set reentrancy_level_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.reentrancy_level_enum = value
        return self

    def with_runs_insides(self, items: list[ExclusiveArea]) -> "RunnableEntityBuilder":
        """Set runs_insides list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.runs_insides = list(items) if items else []
        return self

    def with_sw_addr_method(self, value: Optional[SwAddrMethod]) -> "RunnableEntityBuilder":
        """Set sw_addr_method attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_addr_method = value
        return self

    def with_arguments(self, items: list[RunnableEntity]) -> "RunnableEntityBuilder":
        """Set arguments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.arguments = list(items) if items else []
        return self

    def with_asynchronous_servers(self, items: list[any (AsynchronousServer)]) -> "RunnableEntityBuilder":
        """Set asynchronous_servers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.asynchronous_servers = list(items) if items else []
        return self

    def with_can_be_invoked(self, value: Optional[Boolean]) -> "RunnableEntityBuilder":
        """Set can_be_invoked attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.can_be_invoked = value
        return self

    def with_data_reads(self, items: list[VariableAccess]) -> "RunnableEntityBuilder":
        """Set data_reads list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_reads = list(items) if items else []
        return self

    def with_data_receives(self, items: list[VariableAccess]) -> "RunnableEntityBuilder":
        """Set data_receives list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_receives = list(items) if items else []
        return self

    def with_data_send_points(self, items: list[VariableAccess]) -> "RunnableEntityBuilder":
        """Set data_send_points list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_send_points = list(items) if items else []
        return self

    def with_data_writes(self, items: list[VariableAccess]) -> "RunnableEntityBuilder":
        """Set data_writes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_writes = list(items) if items else []
        return self

    def with_externals(self, items: list[ExternalTriggeringPoint]) -> "RunnableEntityBuilder":
        """Set externals list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.externals = list(items) if items else []
        return self

    def with_internals(self, items: list[InternalTriggeringPoint]) -> "RunnableEntityBuilder":
        """Set internals list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.internals = list(items) if items else []
        return self

    def with_mode_access_points(self, items: list[ModeAccessPoint]) -> "RunnableEntityBuilder":
        """Set mode_access_points list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mode_access_points = list(items) if items else []
        return self

    def with_mode_switch_points(self, items: list[ModeSwitchPoint]) -> "RunnableEntityBuilder":
        """Set mode_switch_points list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mode_switch_points = list(items) if items else []
        return self

    def with_parameter_accesses(self, items: list[ParameterAccess]) -> "RunnableEntityBuilder":
        """Set parameter_accesses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.parameter_accesses = list(items) if items else []
        return self

    def with_read_locals(self, items: list[VariableAccess]) -> "RunnableEntityBuilder":
        """Set read_locals list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.read_locals = list(items) if items else []
        return self

    def with_server_call_points(self, items: list[ServerCallPoint]) -> "RunnableEntityBuilder":
        """Set server_call_points list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.server_call_points = list(items) if items else []
        return self

    def with_symbol(self, value: Optional[CIdentifier]) -> "RunnableEntityBuilder":
        """Set symbol attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.symbol = value
        return self

    def with_wait_points(self, items: list[WaitPoint]) -> "RunnableEntityBuilder":
        """Set wait_points list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.wait_points = list(items) if items else []
        return self

    def with_written_locals(self, items: list[VariableAccess]) -> "RunnableEntityBuilder":
        """Set written_locals list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.written_locals = list(items) if items else []
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "RunnableEntityBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "RunnableEntityBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "RunnableEntityBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "RunnableEntityBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_activation(self, item: ExecutableEntity) -> "RunnableEntityBuilder":
        """Add a single item to activations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.activations.append(item)
        return self

    def clear_activations(self) -> "RunnableEntityBuilder":
        """Clear all items from activations list.

        Returns:
            self for method chaining
        """
        self._obj.activations = []
        return self

    def add_can_enter(self, item: ExclusiveArea) -> "RunnableEntityBuilder":
        """Add a single item to can_enters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.can_enters.append(item)
        return self

    def clear_can_enters(self) -> "RunnableEntityBuilder":
        """Clear all items from can_enters list.

        Returns:
            self for method chaining
        """
        self._obj.can_enters = []
        return self

    def add_exclusive_area_nesting(self, item: ExclusiveAreaNestingOrder) -> "RunnableEntityBuilder":
        """Add a single item to exclusive_area_nestings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.exclusive_area_nestings.append(item)
        return self

    def clear_exclusive_area_nestings(self) -> "RunnableEntityBuilder":
        """Clear all items from exclusive_area_nestings list.

        Returns:
            self for method chaining
        """
        self._obj.exclusive_area_nestings = []
        return self

    def add_runs_inside(self, item: ExclusiveArea) -> "RunnableEntityBuilder":
        """Add a single item to runs_insides list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.runs_insides.append(item)
        return self

    def clear_runs_insides(self) -> "RunnableEntityBuilder":
        """Clear all items from runs_insides list.

        Returns:
            self for method chaining
        """
        self._obj.runs_insides = []
        return self

    def add_argument(self, item: RunnableEntity) -> "RunnableEntityBuilder":
        """Add a single item to arguments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.arguments.append(item)
        return self

    def clear_arguments(self) -> "RunnableEntityBuilder":
        """Clear all items from arguments list.

        Returns:
            self for method chaining
        """
        self._obj.arguments = []
        return self

    def add_asynchronous_server(self, item: any (AsynchronousServer)) -> "RunnableEntityBuilder":
        """Add a single item to asynchronous_servers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.asynchronous_servers.append(item)
        return self

    def clear_asynchronous_servers(self) -> "RunnableEntityBuilder":
        """Clear all items from asynchronous_servers list.

        Returns:
            self for method chaining
        """
        self._obj.asynchronous_servers = []
        return self

    def add_data_read(self, item: VariableAccess) -> "RunnableEntityBuilder":
        """Add a single item to data_reads list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_reads.append(item)
        return self

    def clear_data_reads(self) -> "RunnableEntityBuilder":
        """Clear all items from data_reads list.

        Returns:
            self for method chaining
        """
        self._obj.data_reads = []
        return self

    def add_data_receive(self, item: VariableAccess) -> "RunnableEntityBuilder":
        """Add a single item to data_receives list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_receives.append(item)
        return self

    def clear_data_receives(self) -> "RunnableEntityBuilder":
        """Clear all items from data_receives list.

        Returns:
            self for method chaining
        """
        self._obj.data_receives = []
        return self

    def add_data_send_point(self, item: VariableAccess) -> "RunnableEntityBuilder":
        """Add a single item to data_send_points list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_send_points.append(item)
        return self

    def clear_data_send_points(self) -> "RunnableEntityBuilder":
        """Clear all items from data_send_points list.

        Returns:
            self for method chaining
        """
        self._obj.data_send_points = []
        return self

    def add_data_write(self, item: VariableAccess) -> "RunnableEntityBuilder":
        """Add a single item to data_writes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_writes.append(item)
        return self

    def clear_data_writes(self) -> "RunnableEntityBuilder":
        """Clear all items from data_writes list.

        Returns:
            self for method chaining
        """
        self._obj.data_writes = []
        return self

    def add_external(self, item: ExternalTriggeringPoint) -> "RunnableEntityBuilder":
        """Add a single item to externals list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.externals.append(item)
        return self

    def clear_externals(self) -> "RunnableEntityBuilder":
        """Clear all items from externals list.

        Returns:
            self for method chaining
        """
        self._obj.externals = []
        return self

    def add_internal(self, item: InternalTriggeringPoint) -> "RunnableEntityBuilder":
        """Add a single item to internals list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.internals.append(item)
        return self

    def clear_internals(self) -> "RunnableEntityBuilder":
        """Clear all items from internals list.

        Returns:
            self for method chaining
        """
        self._obj.internals = []
        return self

    def add_mode_access_point(self, item: ModeAccessPoint) -> "RunnableEntityBuilder":
        """Add a single item to mode_access_points list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mode_access_points.append(item)
        return self

    def clear_mode_access_points(self) -> "RunnableEntityBuilder":
        """Clear all items from mode_access_points list.

        Returns:
            self for method chaining
        """
        self._obj.mode_access_points = []
        return self

    def add_mode_switch_point(self, item: ModeSwitchPoint) -> "RunnableEntityBuilder":
        """Add a single item to mode_switch_points list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mode_switch_points.append(item)
        return self

    def clear_mode_switch_points(self) -> "RunnableEntityBuilder":
        """Clear all items from mode_switch_points list.

        Returns:
            self for method chaining
        """
        self._obj.mode_switch_points = []
        return self

    def add_parameter_accesse(self, item: ParameterAccess) -> "RunnableEntityBuilder":
        """Add a single item to parameter_accesses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.parameter_accesses.append(item)
        return self

    def clear_parameter_accesses(self) -> "RunnableEntityBuilder":
        """Clear all items from parameter_accesses list.

        Returns:
            self for method chaining
        """
        self._obj.parameter_accesses = []
        return self

    def add_read_local(self, item: VariableAccess) -> "RunnableEntityBuilder":
        """Add a single item to read_locals list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.read_locals.append(item)
        return self

    def clear_read_locals(self) -> "RunnableEntityBuilder":
        """Clear all items from read_locals list.

        Returns:
            self for method chaining
        """
        self._obj.read_locals = []
        return self

    def add_server_call_point(self, item: ServerCallPoint) -> "RunnableEntityBuilder":
        """Add a single item to server_call_points list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.server_call_points.append(item)
        return self

    def clear_server_call_points(self) -> "RunnableEntityBuilder":
        """Clear all items from server_call_points list.

        Returns:
            self for method chaining
        """
        self._obj.server_call_points = []
        return self

    def add_wait_point(self, item: WaitPoint) -> "RunnableEntityBuilder":
        """Add a single item to wait_points list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.wait_points.append(item)
        return self

    def clear_wait_points(self) -> "RunnableEntityBuilder":
        """Clear all items from wait_points list.

        Returns:
            self for method chaining
        """
        self._obj.wait_points = []
        return self

    def add_written_local(self, item: VariableAccess) -> "RunnableEntityBuilder":
        """Add a single item to written_locals list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.written_locals.append(item)
        return self

    def clear_written_locals(self) -> "RunnableEntityBuilder":
        """Clear all items from written_locals list.

        Returns:
            self for method chaining
        """
        self._obj.written_locals = []
        return self


    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")


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


    def build(self) -> RunnableEntity:
        """Build and return the RunnableEntity instance with validation."""
        self._validate_instance()
        pass
        return self._obj