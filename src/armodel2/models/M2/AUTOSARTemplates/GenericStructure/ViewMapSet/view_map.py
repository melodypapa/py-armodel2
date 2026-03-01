"""ViewMap AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2079)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 401)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_ViewMapSet.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ViewMap(Identifiable):
    """AUTOSAR ViewMap."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "VIEW-MAP"


    first_elements: list[AtpFeature]
    role: Optional[Identifier]
    second_elements: list[AtpFeature]
    _DESERIALIZE_DISPATCH = {
        "FIRST-ELEMENTS": ("_POLYMORPHIC_LIST", "first_elements", ["ApplicationArrayElement", "ApplicationRecordElement", "ArgumentDataPrototype", "AssemblySwConnector", "AsynchronousServerCallPoint", "AsynchronousServerCallResultPoint", "AsynchronousServerCallReturnsEvent", "AtpPrototype", "AtpStructureElement", "BackgroundEvent", "BswInternalBehavior", "BswModuleDescription", "BswServiceDependencyIdent", "BulkNvDataDescriptor", "ClientServerOperation", "DataPrototypeGroup", "DataReceiveErrorEvent", "DataReceivedEvent", "DataSendCompletedEvent", "DataWriteCompletedEvent", "DelegationSwConnector", "DiagnosticParameterIdent", "ExternalTriggerOccurredEvent", "ExternalTriggeringPointIdent", "ImplementationDataTypeElement", "InitEvent", "InternalTriggerOccurredEvent", "InternalTriggeringPoint", "ModeAccessPointIdent", "ModeDeclaration", "ModeDeclarationGroupPrototype", "ModeDeclarationMapping", "ModeSwitchPoint", "ModeSwitchedAckEvent", "ModeTransition", "NvBlockDescriptor", "OperationInvokedEvent", "OsTaskExecutionEvent", "PPortPrototype", "PRPortPrototype", "ParameterAccess", "ParameterDataPrototype", "PassThroughSwConnector", "PerInstanceMemory", "PortGroup", "PortPrototypeBlueprint", "RPortPrototype", "RootSwCompositionPrototype", "RunnableEntity", "RunnableEntityGroup", "SwcBswMapping", "SwcInternalBehavior", "SwcModeManagerErrorEvent", "SwcModeSwitchEvent", "SwcServiceDependency", "SynchronousServerCallPoint", "System", "TimingEvent", "TransformerHardErrorEvent", "Trigger", "VariableAccess", "VariableDataPrototype"]),
        "ROLE": lambda obj, elem: setattr(obj, "role", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
        "SECOND-ELEMENTS": ("_POLYMORPHIC_LIST", "second_elements", ["ApplicationArrayElement", "ApplicationRecordElement", "ArgumentDataPrototype", "AssemblySwConnector", "AsynchronousServerCallPoint", "AsynchronousServerCallResultPoint", "AsynchronousServerCallReturnsEvent", "AtpPrototype", "AtpStructureElement", "BackgroundEvent", "BswInternalBehavior", "BswModuleDescription", "BswServiceDependencyIdent", "BulkNvDataDescriptor", "ClientServerOperation", "DataPrototypeGroup", "DataReceiveErrorEvent", "DataReceivedEvent", "DataSendCompletedEvent", "DataWriteCompletedEvent", "DelegationSwConnector", "DiagnosticParameterIdent", "ExternalTriggerOccurredEvent", "ExternalTriggeringPointIdent", "ImplementationDataTypeElement", "InitEvent", "InternalTriggerOccurredEvent", "InternalTriggeringPoint", "ModeAccessPointIdent", "ModeDeclaration", "ModeDeclarationGroupPrototype", "ModeDeclarationMapping", "ModeSwitchPoint", "ModeSwitchedAckEvent", "ModeTransition", "NvBlockDescriptor", "OperationInvokedEvent", "OsTaskExecutionEvent", "PPortPrototype", "PRPortPrototype", "ParameterAccess", "ParameterDataPrototype", "PassThroughSwConnector", "PerInstanceMemory", "PortGroup", "PortPrototypeBlueprint", "RPortPrototype", "RootSwCompositionPrototype", "RunnableEntity", "RunnableEntityGroup", "SwcBswMapping", "SwcInternalBehavior", "SwcModeManagerErrorEvent", "SwcModeSwitchEvent", "SwcServiceDependency", "SynchronousServerCallPoint", "System", "TimingEvent", "TransformerHardErrorEvent", "Trigger", "VariableAccess", "VariableDataPrototype"]),
    }


    def __init__(self) -> None:
        """Initialize ViewMap."""
        super().__init__()
        self.first_elements: list[AtpFeature] = []
        self.role: Optional[Identifier] = None
        self.second_elements: list[AtpFeature] = []

    def serialize(self) -> ET.Element:
        """Serialize ViewMap to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ViewMap, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize first_elements (list to container "FIRST-ELEMENTS")
        if self.first_elements:
            wrapper = ET.Element("FIRST-ELEMENTS")
            for item in self.first_elements:
                serialized = SerializationHelper.serialize_item(item, "AtpFeature")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize role
        if self.role is not None:
            serialized = SerializationHelper.serialize_item(self.role, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize second_elements (list to container "SECOND-ELEMENTS")
        if self.second_elements:
            wrapper = ET.Element("SECOND-ELEMENTS")
            for item in self.second_elements:
                serialized = SerializationHelper.serialize_item(item, "AtpFeature")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ViewMap":
        """Deserialize XML element to ViewMap object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ViewMap object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ViewMap, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "FIRST-ELEMENTS":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "APPLICATION-ARRAY-ELEMENT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ApplicationArrayElement"))
                    elif concrete_tag == "APPLICATION-RECORD-ELEMENT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ApplicationRecordElement"))
                    elif concrete_tag == "ARGUMENT-DATA-PROTOTYPE":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ArgumentDataPrototype"))
                    elif concrete_tag == "ASSEMBLY-SW-CONNECTOR":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "AssemblySwConnector"))
                    elif concrete_tag == "ASYNCHRONOUS-SERVER-CALL-POINT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "AsynchronousServerCallPoint"))
                    elif concrete_tag == "ASYNCHRONOUS-SERVER-CALL-RESULT-POINT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "AsynchronousServerCallResultPoint"))
                    elif concrete_tag == "ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "AsynchronousServerCallReturnsEvent"))
                    elif concrete_tag == "ATP-PROTOTYPE":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "AtpPrototype"))
                    elif concrete_tag == "ATP-STRUCTURE-ELEMENT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "AtpStructureElement"))
                    elif concrete_tag == "BACKGROUND-EVENT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "BackgroundEvent"))
                    elif concrete_tag == "BSW-INTERNAL-BEHAVIOR":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "BswInternalBehavior"))
                    elif concrete_tag == "BSW-MODULE-DESCRIPTION":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "BswModuleDescription"))
                    elif concrete_tag == "BSW-SERVICE-DEPENDENCY-IDENT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "BswServiceDependencyIdent"))
                    elif concrete_tag == "BULK-NV-DATA-DESCRIPTOR":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "BulkNvDataDescriptor"))
                    elif concrete_tag == "CLIENT-SERVER-OPERATION":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ClientServerOperation"))
                    elif concrete_tag == "DATA-PROTOTYPE-GROUP":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "DataPrototypeGroup"))
                    elif concrete_tag == "DATA-RECEIVE-ERROR-EVENT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "DataReceiveErrorEvent"))
                    elif concrete_tag == "DATA-RECEIVED-EVENT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "DataReceivedEvent"))
                    elif concrete_tag == "DATA-SEND-COMPLETED-EVENT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "DataSendCompletedEvent"))
                    elif concrete_tag == "DATA-WRITE-COMPLETED-EVENT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "DataWriteCompletedEvent"))
                    elif concrete_tag == "DELEGATION-SW-CONNECTOR":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "DelegationSwConnector"))
                    elif concrete_tag == "DIAGNOSTIC-PARAMETER-IDENT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticParameterIdent"))
                    elif concrete_tag == "EXTERNAL-TRIGGER-OCCURRED-EVENT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ExternalTriggerOccurredEvent"))
                    elif concrete_tag == "EXTERNAL-TRIGGERING-POINT-IDENT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ExternalTriggeringPointIdent"))
                    elif concrete_tag == "IMPLEMENTATION-DATA-TYPE-ELEMENT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ImplementationDataTypeElement"))
                    elif concrete_tag == "INIT-EVENT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "InitEvent"))
                    elif concrete_tag == "INTERNAL-TRIGGER-OCCURRED-EVENT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "InternalTriggerOccurredEvent"))
                    elif concrete_tag == "INTERNAL-TRIGGERING-POINT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "InternalTriggeringPoint"))
                    elif concrete_tag == "MODE-ACCESS-POINT-IDENT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeAccessPointIdent"))
                    elif concrete_tag == "MODE-DECLARATION":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeDeclaration"))
                    elif concrete_tag == "MODE-DECLARATION-GROUP-PROTOTYPE":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeDeclarationGroupPrototype"))
                    elif concrete_tag == "MODE-DECLARATION-MAPPING":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeDeclarationMapping"))
                    elif concrete_tag == "MODE-SWITCH-POINT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeSwitchPoint"))
                    elif concrete_tag == "MODE-SWITCHED-ACK-EVENT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeSwitchedAckEvent"))
                    elif concrete_tag == "MODE-TRANSITION":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeTransition"))
                    elif concrete_tag == "NV-BLOCK-DESCRIPTOR":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "NvBlockDescriptor"))
                    elif concrete_tag == "OPERATION-INVOKED-EVENT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "OperationInvokedEvent"))
                    elif concrete_tag == "OS-TASK-EXECUTION-EVENT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "OsTaskExecutionEvent"))
                    elif concrete_tag == "P-PORT-PROTOTYPE":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "PPortPrototype"))
                    elif concrete_tag == "P-R-PORT-PROTOTYPE":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "PRPortPrototype"))
                    elif concrete_tag == "PARAMETER-ACCESS":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ParameterAccess"))
                    elif concrete_tag == "PARAMETER-DATA-PROTOTYPE":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ParameterDataPrototype"))
                    elif concrete_tag == "PASS-THROUGH-SW-CONNECTOR":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "PassThroughSwConnector"))
                    elif concrete_tag == "PER-INSTANCE-MEMORY":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "PerInstanceMemory"))
                    elif concrete_tag == "PORT-GROUP":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "PortGroup"))
                    elif concrete_tag == "PORT-PROTOTYPE-BLUEPRINT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "PortPrototypeBlueprint"))
                    elif concrete_tag == "R-PORT-PROTOTYPE":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "RPortPrototype"))
                    elif concrete_tag == "ROOT-SW-COMPOSITION-PROTOTYPE":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "RootSwCompositionPrototype"))
                    elif concrete_tag == "RUNNABLE-ENTITY":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "RunnableEntity"))
                    elif concrete_tag == "RUNNABLE-ENTITY-GROUP":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "RunnableEntityGroup"))
                    elif concrete_tag == "SWC-BSW-MAPPING":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "SwcBswMapping"))
                    elif concrete_tag == "SWC-INTERNAL-BEHAVIOR":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "SwcInternalBehavior"))
                    elif concrete_tag == "SWC-MODE-MANAGER-ERROR-EVENT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "SwcModeManagerErrorEvent"))
                    elif concrete_tag == "SWC-MODE-SWITCH-EVENT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "SwcModeSwitchEvent"))
                    elif concrete_tag == "SWC-SERVICE-DEPENDENCY":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "SwcServiceDependency"))
                    elif concrete_tag == "SYNCHRONOUS-SERVER-CALL-POINT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "SynchronousServerCallPoint"))
                    elif concrete_tag == "SYSTEM":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "System"))
                    elif concrete_tag == "TIMING-EVENT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "TimingEvent"))
                    elif concrete_tag == "TRANSFORMER-HARD-ERROR-EVENT":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "TransformerHardErrorEvent"))
                    elif concrete_tag == "TRIGGER":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "Trigger"))
                    elif concrete_tag == "VARIABLE-ACCESS":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "VariableAccess"))
                    elif concrete_tag == "VARIABLE-DATA-PROTOTYPE":
                        obj.first_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "VariableDataPrototype"))
            elif tag == "ROLE":
                setattr(obj, "role", SerializationHelper.deserialize_by_tag(child, "Identifier"))
            elif tag == "SECOND-ELEMENTS":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "APPLICATION-ARRAY-ELEMENT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ApplicationArrayElement"))
                    elif concrete_tag == "APPLICATION-RECORD-ELEMENT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ApplicationRecordElement"))
                    elif concrete_tag == "ARGUMENT-DATA-PROTOTYPE":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ArgumentDataPrototype"))
                    elif concrete_tag == "ASSEMBLY-SW-CONNECTOR":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "AssemblySwConnector"))
                    elif concrete_tag == "ASYNCHRONOUS-SERVER-CALL-POINT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "AsynchronousServerCallPoint"))
                    elif concrete_tag == "ASYNCHRONOUS-SERVER-CALL-RESULT-POINT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "AsynchronousServerCallResultPoint"))
                    elif concrete_tag == "ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "AsynchronousServerCallReturnsEvent"))
                    elif concrete_tag == "ATP-PROTOTYPE":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "AtpPrototype"))
                    elif concrete_tag == "ATP-STRUCTURE-ELEMENT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "AtpStructureElement"))
                    elif concrete_tag == "BACKGROUND-EVENT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "BackgroundEvent"))
                    elif concrete_tag == "BSW-INTERNAL-BEHAVIOR":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "BswInternalBehavior"))
                    elif concrete_tag == "BSW-MODULE-DESCRIPTION":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "BswModuleDescription"))
                    elif concrete_tag == "BSW-SERVICE-DEPENDENCY-IDENT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "BswServiceDependencyIdent"))
                    elif concrete_tag == "BULK-NV-DATA-DESCRIPTOR":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "BulkNvDataDescriptor"))
                    elif concrete_tag == "CLIENT-SERVER-OPERATION":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ClientServerOperation"))
                    elif concrete_tag == "DATA-PROTOTYPE-GROUP":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "DataPrototypeGroup"))
                    elif concrete_tag == "DATA-RECEIVE-ERROR-EVENT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "DataReceiveErrorEvent"))
                    elif concrete_tag == "DATA-RECEIVED-EVENT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "DataReceivedEvent"))
                    elif concrete_tag == "DATA-SEND-COMPLETED-EVENT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "DataSendCompletedEvent"))
                    elif concrete_tag == "DATA-WRITE-COMPLETED-EVENT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "DataWriteCompletedEvent"))
                    elif concrete_tag == "DELEGATION-SW-CONNECTOR":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "DelegationSwConnector"))
                    elif concrete_tag == "DIAGNOSTIC-PARAMETER-IDENT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticParameterIdent"))
                    elif concrete_tag == "EXTERNAL-TRIGGER-OCCURRED-EVENT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ExternalTriggerOccurredEvent"))
                    elif concrete_tag == "EXTERNAL-TRIGGERING-POINT-IDENT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ExternalTriggeringPointIdent"))
                    elif concrete_tag == "IMPLEMENTATION-DATA-TYPE-ELEMENT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ImplementationDataTypeElement"))
                    elif concrete_tag == "INIT-EVENT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "InitEvent"))
                    elif concrete_tag == "INTERNAL-TRIGGER-OCCURRED-EVENT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "InternalTriggerOccurredEvent"))
                    elif concrete_tag == "INTERNAL-TRIGGERING-POINT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "InternalTriggeringPoint"))
                    elif concrete_tag == "MODE-ACCESS-POINT-IDENT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeAccessPointIdent"))
                    elif concrete_tag == "MODE-DECLARATION":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeDeclaration"))
                    elif concrete_tag == "MODE-DECLARATION-GROUP-PROTOTYPE":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeDeclarationGroupPrototype"))
                    elif concrete_tag == "MODE-DECLARATION-MAPPING":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeDeclarationMapping"))
                    elif concrete_tag == "MODE-SWITCH-POINT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeSwitchPoint"))
                    elif concrete_tag == "MODE-SWITCHED-ACK-EVENT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeSwitchedAckEvent"))
                    elif concrete_tag == "MODE-TRANSITION":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeTransition"))
                    elif concrete_tag == "NV-BLOCK-DESCRIPTOR":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "NvBlockDescriptor"))
                    elif concrete_tag == "OPERATION-INVOKED-EVENT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "OperationInvokedEvent"))
                    elif concrete_tag == "OS-TASK-EXECUTION-EVENT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "OsTaskExecutionEvent"))
                    elif concrete_tag == "P-PORT-PROTOTYPE":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "PPortPrototype"))
                    elif concrete_tag == "P-R-PORT-PROTOTYPE":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "PRPortPrototype"))
                    elif concrete_tag == "PARAMETER-ACCESS":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ParameterAccess"))
                    elif concrete_tag == "PARAMETER-DATA-PROTOTYPE":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ParameterDataPrototype"))
                    elif concrete_tag == "PASS-THROUGH-SW-CONNECTOR":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "PassThroughSwConnector"))
                    elif concrete_tag == "PER-INSTANCE-MEMORY":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "PerInstanceMemory"))
                    elif concrete_tag == "PORT-GROUP":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "PortGroup"))
                    elif concrete_tag == "PORT-PROTOTYPE-BLUEPRINT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "PortPrototypeBlueprint"))
                    elif concrete_tag == "R-PORT-PROTOTYPE":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "RPortPrototype"))
                    elif concrete_tag == "ROOT-SW-COMPOSITION-PROTOTYPE":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "RootSwCompositionPrototype"))
                    elif concrete_tag == "RUNNABLE-ENTITY":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "RunnableEntity"))
                    elif concrete_tag == "RUNNABLE-ENTITY-GROUP":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "RunnableEntityGroup"))
                    elif concrete_tag == "SWC-BSW-MAPPING":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "SwcBswMapping"))
                    elif concrete_tag == "SWC-INTERNAL-BEHAVIOR":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "SwcInternalBehavior"))
                    elif concrete_tag == "SWC-MODE-MANAGER-ERROR-EVENT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "SwcModeManagerErrorEvent"))
                    elif concrete_tag == "SWC-MODE-SWITCH-EVENT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "SwcModeSwitchEvent"))
                    elif concrete_tag == "SWC-SERVICE-DEPENDENCY":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "SwcServiceDependency"))
                    elif concrete_tag == "SYNCHRONOUS-SERVER-CALL-POINT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "SynchronousServerCallPoint"))
                    elif concrete_tag == "SYSTEM":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "System"))
                    elif concrete_tag == "TIMING-EVENT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "TimingEvent"))
                    elif concrete_tag == "TRANSFORMER-HARD-ERROR-EVENT":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "TransformerHardErrorEvent"))
                    elif concrete_tag == "TRIGGER":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "Trigger"))
                    elif concrete_tag == "VARIABLE-ACCESS":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "VariableAccess"))
                    elif concrete_tag == "VARIABLE-DATA-PROTOTYPE":
                        obj.second_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "VariableDataPrototype"))

        return obj



class ViewMapBuilder(IdentifiableBuilder):
    """Builder for ViewMap with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ViewMap = ViewMap()


    def with_first_elements(self, items: list[AtpFeature]) -> "ViewMapBuilder":
        """Set first_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.first_elements = list(items) if items else []
        return self

    def with_role(self, value: Optional[Identifier]) -> "ViewMapBuilder":
        """Set role attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.role = value
        return self

    def with_second_elements(self, items: list[AtpFeature]) -> "ViewMapBuilder":
        """Set second_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.second_elements = list(items) if items else []
        return self


    def add_first_element(self, item: AtpFeature) -> "ViewMapBuilder":
        """Add a single item to first_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.first_elements.append(item)
        return self

    def clear_first_elements(self) -> "ViewMapBuilder":
        """Clear all items from first_elements list.

        Returns:
            self for method chaining
        """
        self._obj.first_elements = []
        return self

    def add_second_element(self, item: AtpFeature) -> "ViewMapBuilder":
        """Add a single item to second_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.second_elements.append(item)
        return self

    def clear_second_elements(self) -> "ViewMapBuilder":
        """Clear all items from second_elements list.

        Returns:
            self for method chaining
        """
        self._obj.second_elements = []
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


    def build(self) -> ViewMap:
        """Build and return the ViewMap instance with validation."""
        self._validate_instance()
        pass
        return self._obj