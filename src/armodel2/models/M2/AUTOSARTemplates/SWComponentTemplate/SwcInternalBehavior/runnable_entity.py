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
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import xml_element_name

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import ExecutableEntityBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    CIdentifier,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall.asynchronous_server_call_result_point import (
    AsynchronousServerCallResultPoint,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.Trigger.external_triggering_point import (
    ExternalTriggeringPoint,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.Trigger.internal_triggering_point import (
    InternalTriggeringPoint,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup.mode_access_point import (
    ModeAccessPoint,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup.mode_switch_point import (
    ModeSwitchPoint,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.parameter_access import (
        ParameterAccess,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall.server_call_point import (
        ServerCallPoint,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.variable_access import (
        VariableAccess,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.wait_point import (
        WaitPoint,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class RunnableEntity(ExecutableEntity):
    """AUTOSAR RunnableEntity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "RUNNABLE-ENTITY"


    arguments: list[RunnableEntity]
    asynchronous_server_call_result_points: list[AsynchronousServerCallResultPoint]
    can_be_invoked_concurrently: Optional[Boolean]
    data_read_accesses: list[VariableAccess]
    _data_receive_point_by_arguments: list[VariableAccess]
    data_receive_point_by_values: list[VariableAccess]
    data_send_points: list[VariableAccess]
    _data_write_accesses: list[VariableAccess]
    external_triggering_point_refs: list[ARRef]
    internal_triggering_point_refs: list[ARRef]
    mode_access_points: list[ModeAccessPoint]
    mode_switch_points: list[ModeSwitchPoint]
    parameter_accesses: list[ParameterAccess]
    _read_local_variables: list[VariableAccess]
    server_call_points: list[ServerCallPoint]
    symbol: Optional[CIdentifier]
    wait_points: list[WaitPoint]
    _written_local_variables: list[VariableAccess]
    _DESERIALIZE_DISPATCH = {
        "ARGUMENTS": lambda obj, elem: obj.arguments.append(SerializationHelper.deserialize_by_tag(elem, "RunnableEntity")),
        "ASYNCHRONOUS-SERVER-CALL-RESULT-POINTS": lambda obj, elem: obj.asynchronous_server_call_result_points.append(SerializationHelper.deserialize_by_tag(elem, "AsynchronousServerCallResultPoint")),
        "CAN-BE-INVOKED-CONCURRENTLY": lambda obj, elem: setattr(obj, "can_be_invoked_concurrently", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "DATA-READ-ACCESSS": lambda obj, elem: obj.data_read_accesses.append(SerializationHelper.deserialize_by_tag(elem, "VariableAccess")),
        "DATA-RECEIVE-POINT-BY-ARGUMENTS": lambda obj, elem: obj._data_receive_point_by_arguments.append(SerializationHelper.deserialize_by_tag(elem, "VariableAccess")),
        "DATA-RECEIVE-POINT-BY-VALUES": lambda obj, elem: obj.data_receive_point_by_values.append(SerializationHelper.deserialize_by_tag(elem, "VariableAccess")),
        "DATA-SEND-POINTS": lambda obj, elem: obj.data_send_points.append(SerializationHelper.deserialize_by_tag(elem, "VariableAccess")),
        "DATA-WRITE-ACCESSS": lambda obj, elem: obj._data_write_accesses.append(SerializationHelper.deserialize_by_tag(elem, "VariableAccess")),
        "EXTERNAL-TRIGGERING-POINT-REFS": lambda obj, elem: [obj.external_triggering_point_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "INTERNAL-TRIGGERING-POINT-REFS": lambda obj, elem: [obj.internal_triggering_point_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "MODE-ACCESS-POINTS": lambda obj, elem: obj.mode_access_points.append(SerializationHelper.deserialize_by_tag(elem, "ModeAccessPoint")),
        "MODE-SWITCH-POINTS": lambda obj, elem: obj.mode_switch_points.append(SerializationHelper.deserialize_by_tag(elem, "ModeSwitchPoint")),
        "PARAMETER-ACCESSS": lambda obj, elem: obj.parameter_accesses.append(SerializationHelper.deserialize_by_tag(elem, "ParameterAccess")),
        "READ-LOCAL-VARIABLES": lambda obj, elem: obj._read_local_variables.append(SerializationHelper.deserialize_by_tag(elem, "VariableAccess")),
        "SERVER-CALL-POINTS": ("_POLYMORPHIC_LIST", "server_call_points", ["AsynchronousServerCallPoint", "SynchronousServerCallPoint"]),
        "SYMBOL": lambda obj, elem: setattr(obj, "symbol", SerializationHelper.deserialize_by_tag(elem, "CIdentifier")),
        "WAIT-POINTS": lambda obj, elem: obj.wait_points.append(SerializationHelper.deserialize_by_tag(elem, "WaitPoint")),
        "WRITTEN-LOCAL-VARIABLES": lambda obj, elem: obj._written_local_variables.append(SerializationHelper.deserialize_by_tag(elem, "VariableAccess")),
    }


    def __init__(self) -> None:
        """Initialize RunnableEntity."""
        super().__init__()
        self.arguments: list[RunnableEntity] = []
        self.asynchronous_server_call_result_points: list[AsynchronousServerCallResultPoint] = []
        self.can_be_invoked_concurrently: Optional[Boolean] = None
        self.data_read_accesses: list[VariableAccess] = []
        self._data_receive_point_by_arguments: list[VariableAccess] = []
        self.data_receive_point_by_values: list[VariableAccess] = []
        self.data_send_points: list[VariableAccess] = []
        self._data_write_accesses: list[VariableAccess] = []
        self.external_triggering_point_refs: list[ARRef] = []
        self.internal_triggering_point_refs: list[ARRef] = []
        self.mode_access_points: list[ModeAccessPoint] = []
        self.mode_switch_points: list[ModeSwitchPoint] = []
        self.parameter_accesses: list[ParameterAccess] = []
        self._read_local_variables: list[VariableAccess] = []
        self.server_call_points: list[ServerCallPoint] = []
        self.symbol: Optional[CIdentifier] = None
        self.wait_points: list[WaitPoint] = []
        self._written_local_variables: list[VariableAccess] = []
    @property
    @xml_element_name("DATA-RECEIVE-POINT-BY-ARGUMENTS")
    def data_receive_point_by_arguments(self) -> list[VariableAccess]:
        """Get data_receive_point_by_arguments with custom XML element name."""
        return self._data_receive_point_by_arguments

    @data_receive_point_by_arguments.setter
    def data_receive_point_by_arguments(self, value: list[VariableAccess]) -> None:
        """Set data_receive_point_by_arguments with custom XML element name."""
        self._data_receive_point_by_arguments = value

    @property
    @xml_element_name("DATA-WRITE-ACCESSS")
    def data_write_accesses(self) -> list[VariableAccess]:
        """Get data_write_accesses with custom XML element name."""
        return self._data_write_accesses

    @data_write_accesses.setter
    def data_write_accesses(self, value: list[VariableAccess]) -> None:
        """Set data_write_accesses with custom XML element name."""
        self._data_write_accesses = value

    @property
    @xml_element_name("READ-LOCAL-VARIABLES")
    def read_local_variables(self) -> list[VariableAccess]:
        """Get read_local_variables with custom XML element name."""
        return self._read_local_variables

    @read_local_variables.setter
    def read_local_variables(self, value: list[VariableAccess]) -> None:
        """Set read_local_variables with custom XML element name."""
        self._read_local_variables = value

    @property
    @xml_element_name("WRITTEN-LOCAL-VARIABLES")
    def written_local_variables(self) -> list[VariableAccess]:
        """Get written_local_variables with custom XML element name."""
        return self._written_local_variables

    @written_local_variables.setter
    def written_local_variables(self, value: list[VariableAccess]) -> None:
        """Set written_local_variables with custom XML element name."""
        self._written_local_variables = value


    def serialize(self) -> ET.Element:
        """Serialize RunnableEntity to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Serialize asynchronous_server_call_result_points (list to container "ASYNCHRONOUS-SERVER-CALL-RESULT-POINTS")
        if self.asynchronous_server_call_result_points:
            wrapper = ET.Element("ASYNCHRONOUS-SERVER-CALL-RESULT-POINTS")
            for item in self.asynchronous_server_call_result_points:
                serialized = SerializationHelper.serialize_item(item, "AsynchronousServerCallResultPoint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize can_be_invoked_concurrently
        if self.can_be_invoked_concurrently is not None:
            serialized = SerializationHelper.serialize_item(self.can_be_invoked_concurrently, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAN-BE-INVOKED-CONCURRENTLY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize data_read_accesses (list to container "DATA-READ-ACCESSS")
        if self.data_read_accesses:
            wrapper = ET.Element("DATA-READ-ACCESSS")
            for item in self.data_read_accesses:
                serialized = SerializationHelper.serialize_item(item, "VariableAccess")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize data_receive_point_by_arguments (list to container "DATA-RECEIVE-POINT-BY-ARGUMENTS")
        if self.data_receive_point_by_arguments:
            wrapper = ET.Element("DATA-RECEIVE-POINT-BY-ARGUMENTS")
            for item in self.data_receive_point_by_arguments:
                serialized = SerializationHelper.serialize_item(item, "VariableAccess")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize data_receive_point_by_values (list to container "DATA-RECEIVE-POINT-BY-VALUES")
        if self.data_receive_point_by_values:
            wrapper = ET.Element("DATA-RECEIVE-POINT-BY-VALUES")
            for item in self.data_receive_point_by_values:
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

        # Serialize data_write_accesses (list to container "DATA-WRITE-ACCESSS")
        if self.data_write_accesses:
            wrapper = ET.Element("DATA-WRITE-ACCESSS")
            for item in self.data_write_accesses:
                serialized = SerializationHelper.serialize_item(item, "VariableAccess")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize external_triggering_point_refs (list to container "EXTERNAL-TRIGGERING-POINT-REFS")
        if self.external_triggering_point_refs:
            wrapper = ET.Element("EXTERNAL-TRIGGERING-POINT-REFS")
            for item in self.external_triggering_point_refs:
                serialized = SerializationHelper.serialize_item(item, "ExternalTriggeringPoint")
                if serialized is not None:
                    child_elem = ET.Element("EXTERNAL-TRIGGERING-POINT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize internal_triggering_point_refs (list to container "INTERNAL-TRIGGERING-POINT-REFS")
        if self.internal_triggering_point_refs:
            wrapper = ET.Element("INTERNAL-TRIGGERING-POINT-REFS")
            for item in self.internal_triggering_point_refs:
                serialized = SerializationHelper.serialize_item(item, "InternalTriggeringPoint")
                if serialized is not None:
                    child_elem = ET.Element("INTERNAL-TRIGGERING-POINT-REF")
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

        # Serialize parameter_accesses (list to container "PARAMETER-ACCESSS")
        if self.parameter_accesses:
            wrapper = ET.Element("PARAMETER-ACCESSS")
            for item in self.parameter_accesses:
                serialized = SerializationHelper.serialize_item(item, "ParameterAccess")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize read_local_variables (list to container "READ-LOCAL-VARIABLES")
        if self.read_local_variables:
            wrapper = ET.Element("READ-LOCAL-VARIABLES")
            for item in self.read_local_variables:
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

        # Serialize written_local_variables (list to container "WRITTEN-LOCAL-VARIABLES")
        if self.written_local_variables:
            wrapper = ET.Element("WRITTEN-LOCAL-VARIABLES")
            for item in self.written_local_variables:
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ARGUMENTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.arguments.append(SerializationHelper.deserialize_by_tag(item_elem, "RunnableEntity"))
            elif tag == "ASYNCHRONOUS-SERVER-CALL-RESULT-POINTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.asynchronous_server_call_result_points.append(SerializationHelper.deserialize_by_tag(item_elem, "AsynchronousServerCallResultPoint"))
            elif tag == "CAN-BE-INVOKED-CONCURRENTLY":
                setattr(obj, "can_be_invoked_concurrently", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "DATA-READ-ACCESSS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.data_read_accesses.append(SerializationHelper.deserialize_by_tag(item_elem, "VariableAccess"))
            elif tag == "DATA-RECEIVE-POINT-BY-ARGUMENTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj._data_receive_point_by_arguments.append(SerializationHelper.deserialize_by_tag(item_elem, "VariableAccess"))
            elif tag == "DATA-RECEIVE-POINT-BY-VALUES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.data_receive_point_by_values.append(SerializationHelper.deserialize_by_tag(item_elem, "VariableAccess"))
            elif tag == "DATA-SEND-POINTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.data_send_points.append(SerializationHelper.deserialize_by_tag(item_elem, "VariableAccess"))
            elif tag == "DATA-WRITE-ACCESSS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj._data_write_accesses.append(SerializationHelper.deserialize_by_tag(item_elem, "VariableAccess"))
            elif tag == "EXTERNAL-TRIGGERING-POINT-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.external_triggering_point_refs.append(ARRef.deserialize(item_elem))
            elif tag == "INTERNAL-TRIGGERING-POINT-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.internal_triggering_point_refs.append(ARRef.deserialize(item_elem))
            elif tag == "MODE-ACCESS-POINTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.mode_access_points.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeAccessPoint"))
            elif tag == "MODE-SWITCH-POINTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.mode_switch_points.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeSwitchPoint"))
            elif tag == "PARAMETER-ACCESSS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.parameter_accesses.append(SerializationHelper.deserialize_by_tag(item_elem, "ParameterAccess"))
            elif tag == "READ-LOCAL-VARIABLES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj._read_local_variables.append(SerializationHelper.deserialize_by_tag(item_elem, "VariableAccess"))
            elif tag == "SERVER-CALL-POINTS":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "ASYNCHRONOUS-SERVER-CALL-POINT":
                        obj.server_call_points.append(SerializationHelper.deserialize_by_tag(item_elem, "AsynchronousServerCallPoint"))
                    elif concrete_tag == "SYNCHRONOUS-SERVER-CALL-POINT":
                        obj.server_call_points.append(SerializationHelper.deserialize_by_tag(item_elem, "SynchronousServerCallPoint"))
            elif tag == "SYMBOL":
                setattr(obj, "symbol", SerializationHelper.deserialize_by_tag(child, "CIdentifier"))
            elif tag == "WAIT-POINTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.wait_points.append(SerializationHelper.deserialize_by_tag(item_elem, "WaitPoint"))
            elif tag == "WRITTEN-LOCAL-VARIABLES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj._written_local_variables.append(SerializationHelper.deserialize_by_tag(item_elem, "VariableAccess"))

        return obj



class RunnableEntityBuilder(ExecutableEntityBuilder):
    """Builder for RunnableEntity with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RunnableEntity = RunnableEntity()


    def with_arguments(self, items: list[RunnableEntity]) -> "RunnableEntityBuilder":
        """Set arguments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.arguments = list(items) if items else []
        return self

    def with_asynchronous_server_call_result_points(self, items: list[AsynchronousServerCallResultPoint]) -> "RunnableEntityBuilder":
        """Set asynchronous_server_call_result_points list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.asynchronous_server_call_result_points = list(items) if items else []
        return self

    def with_can_be_invoked_concurrently(self, value: Optional[Boolean]) -> "RunnableEntityBuilder":
        """Set can_be_invoked_concurrently attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.can_be_invoked_concurrently = value
        return self

    def with_data_read_accesses(self, items: list[VariableAccess]) -> "RunnableEntityBuilder":
        """Set data_read_accesses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_read_accesses = list(items) if items else []
        return self

    def with_data_receive_point_by_arguments(self, items: list[VariableAccess]) -> "RunnableEntityBuilder":
        """Set data_receive_point_by_arguments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_receive_point_by_arguments = list(items) if items else []
        return self

    def with_data_receive_point_by_values(self, items: list[VariableAccess]) -> "RunnableEntityBuilder":
        """Set data_receive_point_by_values list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_receive_point_by_values = list(items) if items else []
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

    def with_data_write_accesses(self, items: list[VariableAccess]) -> "RunnableEntityBuilder":
        """Set data_write_accesses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_write_accesses = list(items) if items else []
        return self

    def with_external_triggering_points(self, items: list[ExternalTriggeringPoint]) -> "RunnableEntityBuilder":
        """Set external_triggering_points list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.external_triggering_points = list(items) if items else []
        return self

    def with_internal_triggering_points(self, items: list[InternalTriggeringPoint]) -> "RunnableEntityBuilder":
        """Set internal_triggering_points list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.internal_triggering_points = list(items) if items else []
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

    def with_read_local_variables(self, items: list[VariableAccess]) -> "RunnableEntityBuilder":
        """Set read_local_variables list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.read_local_variables = list(items) if items else []
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

    def with_written_local_variables(self, items: list[VariableAccess]) -> "RunnableEntityBuilder":
        """Set written_local_variables list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.written_local_variables = list(items) if items else []
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

    def add_asynchronous_server_call_result_point(self, item: AsynchronousServerCallResultPoint) -> "RunnableEntityBuilder":
        """Add a single item to asynchronous_server_call_result_points list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.asynchronous_server_call_result_points.append(item)
        return self

    def clear_asynchronous_server_call_result_points(self) -> "RunnableEntityBuilder":
        """Clear all items from asynchronous_server_call_result_points list.

        Returns:
            self for method chaining
        """
        self._obj.asynchronous_server_call_result_points = []
        return self

    def add_data_read_access(self, item: VariableAccess) -> "RunnableEntityBuilder":
        """Add a single item to data_read_accesses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_read_accesses.append(item)
        return self

    def clear_data_read_accesses(self) -> "RunnableEntityBuilder":
        """Clear all items from data_read_accesses list.

        Returns:
            self for method chaining
        """
        self._obj.data_read_accesses = []
        return self

    def add_data_receive_point_by_argument(self, item: VariableAccess) -> "RunnableEntityBuilder":
        """Add a single item to data_receive_point_by_arguments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_receive_point_by_arguments.append(item)
        return self

    def clear_data_receive_point_by_arguments(self) -> "RunnableEntityBuilder":
        """Clear all items from data_receive_point_by_arguments list.

        Returns:
            self for method chaining
        """
        self._obj.data_receive_point_by_arguments = []
        return self

    def add_data_receive_point_by_value(self, item: VariableAccess) -> "RunnableEntityBuilder":
        """Add a single item to data_receive_point_by_values list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_receive_point_by_values.append(item)
        return self

    def clear_data_receive_point_by_values(self) -> "RunnableEntityBuilder":
        """Clear all items from data_receive_point_by_values list.

        Returns:
            self for method chaining
        """
        self._obj.data_receive_point_by_values = []
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

    def add_data_write_access(self, item: VariableAccess) -> "RunnableEntityBuilder":
        """Add a single item to data_write_accesses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_write_accesses.append(item)
        return self

    def clear_data_write_accesses(self) -> "RunnableEntityBuilder":
        """Clear all items from data_write_accesses list.

        Returns:
            self for method chaining
        """
        self._obj.data_write_accesses = []
        return self

    def add_external_triggering_point(self, item: ExternalTriggeringPoint) -> "RunnableEntityBuilder":
        """Add a single item to external_triggering_points list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.external_triggering_points.append(item)
        return self

    def clear_external_triggering_points(self) -> "RunnableEntityBuilder":
        """Clear all items from external_triggering_points list.

        Returns:
            self for method chaining
        """
        self._obj.external_triggering_points = []
        return self

    def add_internal_triggering_point(self, item: InternalTriggeringPoint) -> "RunnableEntityBuilder":
        """Add a single item to internal_triggering_points list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.internal_triggering_points.append(item)
        return self

    def clear_internal_triggering_points(self) -> "RunnableEntityBuilder":
        """Clear all items from internal_triggering_points list.

        Returns:
            self for method chaining
        """
        self._obj.internal_triggering_points = []
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

    def add_parameter_access(self, item: ParameterAccess) -> "RunnableEntityBuilder":
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

    def add_read_local_variable(self, item: VariableAccess) -> "RunnableEntityBuilder":
        """Add a single item to read_local_variables list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.read_local_variables.append(item)
        return self

    def clear_read_local_variables(self) -> "RunnableEntityBuilder":
        """Clear all items from read_local_variables list.

        Returns:
            self for method chaining
        """
        self._obj.read_local_variables = []
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

    def add_written_local_variable(self, item: VariableAccess) -> "RunnableEntityBuilder":
        """Add a single item to written_local_variables list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.written_local_variables.append(item)
        return self

    def clear_written_local_variables(self) -> "RunnableEntityBuilder":
        """Clear all items from written_local_variables list.

        Returns:
            self for method chaining
        """
        self._obj.written_local_variables = []
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


    def build(self) -> RunnableEntity:
        """Build and return the RunnableEntity instance with validation."""
        self._validate_instance()
        pass
        return self._obj