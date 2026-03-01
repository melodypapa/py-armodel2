"""RptContainer AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 847)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_RPTScenario.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_executable_entity import (
    RptExecutableEntity,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.rpt_hook import (
    RptHook,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.rpt_impl_policy import (
    RptImplPolicy,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.rpt_profile import (
    RptProfile,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_sw_prototyping_access import (
    RptSwPrototypingAccess,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class RptContainer(Identifiable):
    """AUTOSAR RptContainer."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "RPT-CONTAINER"


    by_pass_points: list[AtpFeature]
    explicit_rpt_refs: list[ARRef]
    rpt_containers: list[RptContainer]
    rpt_executable_entity: Optional[RptExecutableEntity]
    rpt_hook: Optional[RptHook]
    rpt_impl_policy: Optional[RptImplPolicy]
    rpt_sw: Optional[RptSwPrototypingAccess]
    _DESERIALIZE_DISPATCH = {
        "BY-PASS-POINTS": ("_POLYMORPHIC_LIST", "by_pass_points", ["ApplicationArrayElement", "ApplicationRecordElement", "ArgumentDataPrototype", "AssemblySwConnector", "AsynchronousServerCallPoint", "AsynchronousServerCallResultPoint", "AsynchronousServerCallReturnsEvent", "AtpPrototype", "AtpStructureElement", "BackgroundEvent", "BswInternalBehavior", "BswModuleDescription", "BswServiceDependencyIdent", "BulkNvDataDescriptor", "ClientServerOperation", "DataPrototypeGroup", "DataReceiveErrorEvent", "DataReceivedEvent", "DataSendCompletedEvent", "DataWriteCompletedEvent", "DelegationSwConnector", "DiagnosticParameterIdent", "ExternalTriggerOccurredEvent", "ExternalTriggeringPointIdent", "ImplementationDataTypeElement", "InitEvent", "InternalTriggerOccurredEvent", "InternalTriggeringPoint", "ModeAccessPointIdent", "ModeDeclaration", "ModeDeclarationGroupPrototype", "ModeDeclarationMapping", "ModeSwitchPoint", "ModeSwitchedAckEvent", "ModeTransition", "NvBlockDescriptor", "OperationInvokedEvent", "OsTaskExecutionEvent", "PPortPrototype", "PRPortPrototype", "ParameterAccess", "ParameterDataPrototype", "PassThroughSwConnector", "PerInstanceMemory", "PortGroup", "PortPrototypeBlueprint", "RPortPrototype", "RootSwCompositionPrototype", "RunnableEntity", "RunnableEntityGroup", "SwcBswMapping", "SwcInternalBehavior", "SwcModeManagerErrorEvent", "SwcModeSwitchEvent", "SwcServiceDependency", "SynchronousServerCallPoint", "System", "TimingEvent", "TransformerHardErrorEvent", "Trigger", "VariableAccess", "VariableDataPrototype"]),
        "EXPLICIT-RPT-REFS": lambda obj, elem: [obj.explicit_rpt_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "RPT-CONTAINERS": lambda obj, elem: obj.rpt_containers.append(SerializationHelper.deserialize_by_tag(elem, "RptContainer")),
        "RPT-EXECUTABLE-ENTITY": lambda obj, elem: setattr(obj, "rpt_executable_entity", SerializationHelper.deserialize_by_tag(elem, "RptExecutableEntity")),
        "RPT-HOOK": lambda obj, elem: setattr(obj, "rpt_hook", SerializationHelper.deserialize_by_tag(elem, "RptHook")),
        "RPT-IMPL-POLICY": lambda obj, elem: setattr(obj, "rpt_impl_policy", SerializationHelper.deserialize_by_tag(elem, "RptImplPolicy")),
        "RPT-SW": lambda obj, elem: setattr(obj, "rpt_sw", SerializationHelper.deserialize_by_tag(elem, "RptSwPrototypingAccess")),
    }


    def __init__(self) -> None:
        """Initialize RptContainer."""
        super().__init__()
        self.by_pass_points: list[AtpFeature] = []
        self.explicit_rpt_refs: list[ARRef] = []
        self.rpt_containers: list[RptContainer] = []
        self.rpt_executable_entity: Optional[RptExecutableEntity] = None
        self.rpt_hook: Optional[RptHook] = None
        self.rpt_impl_policy: Optional[RptImplPolicy] = None
        self.rpt_sw: Optional[RptSwPrototypingAccess] = None

    def serialize(self) -> ET.Element:
        """Serialize RptContainer to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RptContainer, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize by_pass_points (list to container "BY-PASS-POINTS")
        if self.by_pass_points:
            wrapper = ET.Element("BY-PASS-POINTS")
            for item in self.by_pass_points:
                serialized = SerializationHelper.serialize_item(item, "AtpFeature")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize explicit_rpt_refs (list to container "EXPLICIT-RPT-REFS")
        if self.explicit_rpt_refs:
            wrapper = ET.Element("EXPLICIT-RPT-REFS")
            for item in self.explicit_rpt_refs:
                serialized = SerializationHelper.serialize_item(item, "RptProfile")
                if serialized is not None:
                    child_elem = ET.Element("EXPLICIT-RPT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rpt_containers (list to container "RPT-CONTAINERS")
        if self.rpt_containers:
            wrapper = ET.Element("RPT-CONTAINERS")
            for item in self.rpt_containers:
                serialized = SerializationHelper.serialize_item(item, "RptContainer")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rpt_executable_entity
        if self.rpt_executable_entity is not None:
            serialized = SerializationHelper.serialize_item(self.rpt_executable_entity, "RptExecutableEntity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RPT-EXECUTABLE-ENTITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rpt_hook
        if self.rpt_hook is not None:
            serialized = SerializationHelper.serialize_item(self.rpt_hook, "RptHook")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RPT-HOOK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rpt_impl_policy
        if self.rpt_impl_policy is not None:
            serialized = SerializationHelper.serialize_item(self.rpt_impl_policy, "RptImplPolicy")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RPT-IMPL-POLICY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rpt_sw
        if self.rpt_sw is not None:
            serialized = SerializationHelper.serialize_item(self.rpt_sw, "RptSwPrototypingAccess")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RPT-SW")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptContainer":
        """Deserialize XML element to RptContainer object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RptContainer object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RptContainer, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BY-PASS-POINTS":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "APPLICATION-ARRAY-ELEMENT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "ApplicationArrayElement"))
                    elif concrete_tag == "APPLICATION-RECORD-ELEMENT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "ApplicationRecordElement"))
                    elif concrete_tag == "ARGUMENT-DATA-PROTOTYPE":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "ArgumentDataPrototype"))
                    elif concrete_tag == "ASSEMBLY-SW-CONNECTOR":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "AssemblySwConnector"))
                    elif concrete_tag == "ASYNCHRONOUS-SERVER-CALL-POINT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "AsynchronousServerCallPoint"))
                    elif concrete_tag == "ASYNCHRONOUS-SERVER-CALL-RESULT-POINT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "AsynchronousServerCallResultPoint"))
                    elif concrete_tag == "ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "AsynchronousServerCallReturnsEvent"))
                    elif concrete_tag == "ATP-PROTOTYPE":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "AtpPrototype"))
                    elif concrete_tag == "ATP-STRUCTURE-ELEMENT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "AtpStructureElement"))
                    elif concrete_tag == "BACKGROUND-EVENT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "BackgroundEvent"))
                    elif concrete_tag == "BSW-INTERNAL-BEHAVIOR":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "BswInternalBehavior"))
                    elif concrete_tag == "BSW-MODULE-DESCRIPTION":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "BswModuleDescription"))
                    elif concrete_tag == "BSW-SERVICE-DEPENDENCY-IDENT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "BswServiceDependencyIdent"))
                    elif concrete_tag == "BULK-NV-DATA-DESCRIPTOR":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "BulkNvDataDescriptor"))
                    elif concrete_tag == "CLIENT-SERVER-OPERATION":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "ClientServerOperation"))
                    elif concrete_tag == "DATA-PROTOTYPE-GROUP":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "DataPrototypeGroup"))
                    elif concrete_tag == "DATA-RECEIVE-ERROR-EVENT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "DataReceiveErrorEvent"))
                    elif concrete_tag == "DATA-RECEIVED-EVENT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "DataReceivedEvent"))
                    elif concrete_tag == "DATA-SEND-COMPLETED-EVENT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "DataSendCompletedEvent"))
                    elif concrete_tag == "DATA-WRITE-COMPLETED-EVENT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "DataWriteCompletedEvent"))
                    elif concrete_tag == "DELEGATION-SW-CONNECTOR":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "DelegationSwConnector"))
                    elif concrete_tag == "DIAGNOSTIC-PARAMETER-IDENT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticParameterIdent"))
                    elif concrete_tag == "EXTERNAL-TRIGGER-OCCURRED-EVENT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "ExternalTriggerOccurredEvent"))
                    elif concrete_tag == "EXTERNAL-TRIGGERING-POINT-IDENT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "ExternalTriggeringPointIdent"))
                    elif concrete_tag == "IMPLEMENTATION-DATA-TYPE-ELEMENT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "ImplementationDataTypeElement"))
                    elif concrete_tag == "INIT-EVENT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "InitEvent"))
                    elif concrete_tag == "INTERNAL-TRIGGER-OCCURRED-EVENT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "InternalTriggerOccurredEvent"))
                    elif concrete_tag == "INTERNAL-TRIGGERING-POINT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "InternalTriggeringPoint"))
                    elif concrete_tag == "MODE-ACCESS-POINT-IDENT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeAccessPointIdent"))
                    elif concrete_tag == "MODE-DECLARATION":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeDeclaration"))
                    elif concrete_tag == "MODE-DECLARATION-GROUP-PROTOTYPE":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeDeclarationGroupPrototype"))
                    elif concrete_tag == "MODE-DECLARATION-MAPPING":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeDeclarationMapping"))
                    elif concrete_tag == "MODE-SWITCH-POINT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeSwitchPoint"))
                    elif concrete_tag == "MODE-SWITCHED-ACK-EVENT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeSwitchedAckEvent"))
                    elif concrete_tag == "MODE-TRANSITION":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeTransition"))
                    elif concrete_tag == "NV-BLOCK-DESCRIPTOR":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "NvBlockDescriptor"))
                    elif concrete_tag == "OPERATION-INVOKED-EVENT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "OperationInvokedEvent"))
                    elif concrete_tag == "OS-TASK-EXECUTION-EVENT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "OsTaskExecutionEvent"))
                    elif concrete_tag == "P-PORT-PROTOTYPE":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "PPortPrototype"))
                    elif concrete_tag == "P-R-PORT-PROTOTYPE":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "PRPortPrototype"))
                    elif concrete_tag == "PARAMETER-ACCESS":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "ParameterAccess"))
                    elif concrete_tag == "PARAMETER-DATA-PROTOTYPE":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "ParameterDataPrototype"))
                    elif concrete_tag == "PASS-THROUGH-SW-CONNECTOR":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "PassThroughSwConnector"))
                    elif concrete_tag == "PER-INSTANCE-MEMORY":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "PerInstanceMemory"))
                    elif concrete_tag == "PORT-GROUP":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "PortGroup"))
                    elif concrete_tag == "PORT-PROTOTYPE-BLUEPRINT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "PortPrototypeBlueprint"))
                    elif concrete_tag == "R-PORT-PROTOTYPE":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "RPortPrototype"))
                    elif concrete_tag == "ROOT-SW-COMPOSITION-PROTOTYPE":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "RootSwCompositionPrototype"))
                    elif concrete_tag == "RUNNABLE-ENTITY":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "RunnableEntity"))
                    elif concrete_tag == "RUNNABLE-ENTITY-GROUP":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "RunnableEntityGroup"))
                    elif concrete_tag == "SWC-BSW-MAPPING":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "SwcBswMapping"))
                    elif concrete_tag == "SWC-INTERNAL-BEHAVIOR":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "SwcInternalBehavior"))
                    elif concrete_tag == "SWC-MODE-MANAGER-ERROR-EVENT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "SwcModeManagerErrorEvent"))
                    elif concrete_tag == "SWC-MODE-SWITCH-EVENT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "SwcModeSwitchEvent"))
                    elif concrete_tag == "SWC-SERVICE-DEPENDENCY":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "SwcServiceDependency"))
                    elif concrete_tag == "SYNCHRONOUS-SERVER-CALL-POINT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "SynchronousServerCallPoint"))
                    elif concrete_tag == "SYSTEM":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "System"))
                    elif concrete_tag == "TIMING-EVENT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "TimingEvent"))
                    elif concrete_tag == "TRANSFORMER-HARD-ERROR-EVENT":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "TransformerHardErrorEvent"))
                    elif concrete_tag == "TRIGGER":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "Trigger"))
                    elif concrete_tag == "VARIABLE-ACCESS":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "VariableAccess"))
                    elif concrete_tag == "VARIABLE-DATA-PROTOTYPE":
                        obj.by_pass_points.append(SerializationHelper.deserialize_by_tag(item_elem, "VariableDataPrototype"))
            elif tag == "EXPLICIT-RPT-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.explicit_rpt_refs.append(ARRef.deserialize(item_elem))
            elif tag == "RPT-CONTAINERS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.rpt_containers.append(SerializationHelper.deserialize_by_tag(item_elem, "RptContainer"))
            elif tag == "RPT-EXECUTABLE-ENTITY":
                setattr(obj, "rpt_executable_entity", SerializationHelper.deserialize_by_tag(child, "RptExecutableEntity"))
            elif tag == "RPT-HOOK":
                setattr(obj, "rpt_hook", SerializationHelper.deserialize_by_tag(child, "RptHook"))
            elif tag == "RPT-IMPL-POLICY":
                setattr(obj, "rpt_impl_policy", SerializationHelper.deserialize_by_tag(child, "RptImplPolicy"))
            elif tag == "RPT-SW":
                setattr(obj, "rpt_sw", SerializationHelper.deserialize_by_tag(child, "RptSwPrototypingAccess"))

        return obj



class RptContainerBuilder(IdentifiableBuilder):
    """Builder for RptContainer with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RptContainer = RptContainer()


    def with_by_pass_points(self, items: list[AtpFeature]) -> "RptContainerBuilder":
        """Set by_pass_points list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.by_pass_points = list(items) if items else []
        return self

    def with_explicit_rpts(self, items: list[RptProfile]) -> "RptContainerBuilder":
        """Set explicit_rpts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.explicit_rpts = list(items) if items else []
        return self

    def with_rpt_containers(self, items: list[RptContainer]) -> "RptContainerBuilder":
        """Set rpt_containers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.rpt_containers = list(items) if items else []
        return self

    def with_rpt_executable_entity(self, value: Optional[RptExecutableEntity]) -> "RptContainerBuilder":
        """Set rpt_executable_entity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rpt_executable_entity = value
        return self

    def with_rpt_hook(self, value: Optional[RptHook]) -> "RptContainerBuilder":
        """Set rpt_hook attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rpt_hook = value
        return self

    def with_rpt_impl_policy(self, value: Optional[RptImplPolicy]) -> "RptContainerBuilder":
        """Set rpt_impl_policy attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rpt_impl_policy = value
        return self

    def with_rpt_sw(self, value: Optional[RptSwPrototypingAccess]) -> "RptContainerBuilder":
        """Set rpt_sw attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rpt_sw = value
        return self


    def add_by_pass_point(self, item: AtpFeature) -> "RptContainerBuilder":
        """Add a single item to by_pass_points list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.by_pass_points.append(item)
        return self

    def clear_by_pass_points(self) -> "RptContainerBuilder":
        """Clear all items from by_pass_points list.

        Returns:
            self for method chaining
        """
        self._obj.by_pass_points = []
        return self

    def add_explicit_rpt(self, item: RptProfile) -> "RptContainerBuilder":
        """Add a single item to explicit_rpts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.explicit_rpts.append(item)
        return self

    def clear_explicit_rpts(self) -> "RptContainerBuilder":
        """Clear all items from explicit_rpts list.

        Returns:
            self for method chaining
        """
        self._obj.explicit_rpts = []
        return self

    def add_rpt_container(self, item: RptContainer) -> "RptContainerBuilder":
        """Add a single item to rpt_containers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.rpt_containers.append(item)
        return self

    def clear_rpt_containers(self) -> "RptContainerBuilder":
        """Clear all items from rpt_containers list.

        Returns:
            self for method chaining
        """
        self._obj.rpt_containers = []
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


    def build(self) -> RptContainer:
        """Build and return the RptContainer instance with validation."""
        self._validate_instance()
        pass
        return self._obj