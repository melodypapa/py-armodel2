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
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall.server_call_point import (
    ServerCallPoint,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.variable_access import (
    VariableAccess,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.parameter_access import (
        ParameterAccess,
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
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RunnableEntity, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize arguments (list to container "ARGUMENTS")
        if self.arguments:
            wrapper = ET.Element("ARGUMENTS")
            for item in self.arguments:
                serialized = ARObject._serialize_item(item, "RunnableEntity")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize asynchronous_servers (list to container "ASYNCHRONOUS-SERVERS")
        if self.asynchronous_servers:
            wrapper = ET.Element("ASYNCHRONOUS-SERVERS")
            for item in self.asynchronous_servers:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize can_be_invoked
        if self.can_be_invoked is not None:
            serialized = ARObject._serialize_item(self.can_be_invoked, "Boolean")
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
                serialized = ARObject._serialize_item(item, "VariableAccess")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize data_receives (list to container "DATA-RECEIVES")
        if self.data_receives:
            wrapper = ET.Element("DATA-RECEIVES")
            for item in self.data_receives:
                serialized = ARObject._serialize_item(item, "VariableAccess")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize data_send_points (list to container "DATA-SEND-POINTS")
        if self.data_send_points:
            wrapper = ET.Element("DATA-SEND-POINTS")
            for item in self.data_send_points:
                serialized = ARObject._serialize_item(item, "VariableAccess")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize data_writes (list to container "DATA-WRITES")
        if self.data_writes:
            wrapper = ET.Element("DATA-WRITES")
            for item in self.data_writes:
                serialized = ARObject._serialize_item(item, "VariableAccess")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize external_refs (list to container "EXTERNALS")
        if self.external_refs:
            wrapper = ET.Element("EXTERNALS")
            for item in self.external_refs:
                serialized = ARObject._serialize_item(item, "ExternalTriggeringPoint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize internal_refs (list to container "INTERNALS")
        if self.internal_refs:
            wrapper = ET.Element("INTERNALS")
            for item in self.internal_refs:
                serialized = ARObject._serialize_item(item, "InternalTriggeringPoint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mode_access_points (list to container "MODE-ACCESS-POINTS")
        if self.mode_access_points:
            wrapper = ET.Element("MODE-ACCESS-POINTS")
            for item in self.mode_access_points:
                serialized = ARObject._serialize_item(item, "ModeAccessPoint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mode_switch_points (list to container "MODE-SWITCH-POINTS")
        if self.mode_switch_points:
            wrapper = ET.Element("MODE-SWITCH-POINTS")
            for item in self.mode_switch_points:
                serialized = ARObject._serialize_item(item, "ModeSwitchPoint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize parameter_accesses (list to container "PARAMETER-ACCESSES")
        if self.parameter_accesses:
            wrapper = ET.Element("PARAMETER-ACCESSES")
            for item in self.parameter_accesses:
                serialized = ARObject._serialize_item(item, "ParameterAccess")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize read_locals (list to container "READ-LOCALS")
        if self.read_locals:
            wrapper = ET.Element("READ-LOCALS")
            for item in self.read_locals:
                serialized = ARObject._serialize_item(item, "VariableAccess")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize server_call_points (list to container "SERVER-CALL-POINTS")
        if self.server_call_points:
            wrapper = ET.Element("SERVER-CALL-POINTS")
            for item in self.server_call_points:
                serialized = ARObject._serialize_item(item, "ServerCallPoint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize symbol
        if self.symbol is not None:
            serialized = ARObject._serialize_item(self.symbol, "CIdentifier")
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
                serialized = ARObject._serialize_item(item, "WaitPoint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize written_locals (list to container "WRITTEN-LOCALS")
        if self.written_locals:
            wrapper = ET.Element("WRITTEN-LOCALS")
            for item in self.written_locals:
                serialized = ARObject._serialize_item(item, "VariableAccess")
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
        container = ARObject._find_child_element(element, "ARGUMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.arguments.append(child_value)

        # Parse asynchronous_servers (list from container "ASYNCHRONOUS-SERVERS")
        obj.asynchronous_servers = []
        container = ARObject._find_child_element(element, "ASYNCHRONOUS-SERVERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.asynchronous_servers.append(child_value)

        # Parse can_be_invoked
        child = ARObject._find_child_element(element, "CAN-BE-INVOKED")
        if child is not None:
            can_be_invoked_value = child.text
            obj.can_be_invoked = can_be_invoked_value

        # Parse data_reads (list from container "DATA-READS")
        obj.data_reads = []
        container = ARObject._find_child_element(element, "DATA-READS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_reads.append(child_value)

        # Parse data_receives (list from container "DATA-RECEIVES")
        obj.data_receives = []
        container = ARObject._find_child_element(element, "DATA-RECEIVES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_receives.append(child_value)

        # Parse data_send_points (list from container "DATA-SEND-POINTS")
        obj.data_send_points = []
        container = ARObject._find_child_element(element, "DATA-SEND-POINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_send_points.append(child_value)

        # Parse data_writes (list from container "DATA-WRITES")
        obj.data_writes = []
        container = ARObject._find_child_element(element, "DATA-WRITES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_writes.append(child_value)

        # Parse external_refs (list from container "EXTERNALS")
        obj.external_refs = []
        container = ARObject._find_child_element(element, "EXTERNALS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.external_refs.append(child_value)

        # Parse internal_refs (list from container "INTERNALS")
        obj.internal_refs = []
        container = ARObject._find_child_element(element, "INTERNALS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.internal_refs.append(child_value)

        # Parse mode_access_points (list from container "MODE-ACCESS-POINTS")
        obj.mode_access_points = []
        container = ARObject._find_child_element(element, "MODE-ACCESS-POINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mode_access_points.append(child_value)

        # Parse mode_switch_points (list from container "MODE-SWITCH-POINTS")
        obj.mode_switch_points = []
        container = ARObject._find_child_element(element, "MODE-SWITCH-POINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mode_switch_points.append(child_value)

        # Parse parameter_accesses (list from container "PARAMETER-ACCESSES")
        obj.parameter_accesses = []
        container = ARObject._find_child_element(element, "PARAMETER-ACCESSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.parameter_accesses.append(child_value)

        # Parse read_locals (list from container "READ-LOCALS")
        obj.read_locals = []
        container = ARObject._find_child_element(element, "READ-LOCALS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.read_locals.append(child_value)

        # Parse server_call_points (list from container "SERVER-CALL-POINTS")
        obj.server_call_points = []
        container = ARObject._find_child_element(element, "SERVER-CALL-POINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.server_call_points.append(child_value)

        # Parse symbol
        child = ARObject._find_child_element(element, "SYMBOL")
        if child is not None:
            symbol_value = ARObject._deserialize_by_tag(child, "CIdentifier")
            obj.symbol = symbol_value

        # Parse wait_points (list from container "WAIT-POINTS")
        obj.wait_points = []
        container = ARObject._find_child_element(element, "WAIT-POINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.wait_points.append(child_value)

        # Parse written_locals (list from container "WRITTEN-LOCALS")
        obj.written_locals = []
        container = ARObject._find_child_element(element, "WRITTEN-LOCALS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.written_locals.append(child_value)

        return obj



class RunnableEntityBuilder:
    """Builder for RunnableEntity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RunnableEntity = RunnableEntity()

    def build(self) -> RunnableEntity:
        """Build and return RunnableEntity object.

        Returns:
            RunnableEntity instance
        """
        # TODO: Add validation
        return self._obj
