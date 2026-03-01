"""EcucInstanceReferenceValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 134)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_abstract_reference_value import (
    EcucAbstractReferenceValue,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_abstract_reference_value import EcucAbstractReferenceValueBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EcucInstanceReferenceValue(EcucAbstractReferenceValue):
    """AUTOSAR EcucInstanceReferenceValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ECUC-INSTANCE-REFERENCE-VALUE"


    value: Optional[AtpFeature]
    _DESERIALIZE_DISPATCH = {
        "VALUE": ("_POLYMORPHIC", "value", ["ApplicationArrayElement", "ApplicationRecordElement", "ArgumentDataPrototype", "AssemblySwConnector", "AsynchronousServerCallPoint", "AsynchronousServerCallResultPoint", "AsynchronousServerCallReturnsEvent", "AtpPrototype", "AtpStructureElement", "BackgroundEvent", "BswInternalBehavior", "BswModuleDescription", "BswServiceDependencyIdent", "BulkNvDataDescriptor", "ClientServerOperation", "DataPrototypeGroup", "DataReceiveErrorEvent", "DataReceivedEvent", "DataSendCompletedEvent", "DataWriteCompletedEvent", "DelegationSwConnector", "DiagnosticParameterIdent", "ExternalTriggerOccurredEvent", "ExternalTriggeringPointIdent", "ImplementationDataTypeElement", "InitEvent", "InternalTriggerOccurredEvent", "InternalTriggeringPoint", "ModeAccessPointIdent", "ModeDeclaration", "ModeDeclarationGroupPrototype", "ModeDeclarationMapping", "ModeSwitchPoint", "ModeSwitchedAckEvent", "ModeTransition", "NvBlockDescriptor", "OperationInvokedEvent", "OsTaskExecutionEvent", "PPortPrototype", "PRPortPrototype", "ParameterAccess", "ParameterDataPrototype", "PassThroughSwConnector", "PerInstanceMemory", "PortGroup", "PortPrototypeBlueprint", "RPortPrototype", "RootSwCompositionPrototype", "RunnableEntity", "RunnableEntityGroup", "SwcBswMapping", "SwcInternalBehavior", "SwcModeManagerErrorEvent", "SwcModeSwitchEvent", "SwcServiceDependency", "SynchronousServerCallPoint", "System", "TimingEvent", "TransformerHardErrorEvent", "Trigger", "VariableAccess", "VariableDataPrototype"]),
    }


    def __init__(self) -> None:
        """Initialize EcucInstanceReferenceValue."""
        super().__init__()
        self.value: Optional[AtpFeature] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucInstanceReferenceValue to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucInstanceReferenceValue, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize value
        if self.value is not None:
            serialized = SerializationHelper.serialize_item(self.value, "AtpFeature")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucInstanceReferenceValue":
        """Deserialize XML element to EcucInstanceReferenceValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucInstanceReferenceValue object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucInstanceReferenceValue, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "VALUE":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "APPLICATION-ARRAY-ELEMENT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "ApplicationArrayElement"))
                    elif concrete_tag == "APPLICATION-RECORD-ELEMENT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "ApplicationRecordElement"))
                    elif concrete_tag == "ARGUMENT-DATA-PROTOTYPE":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "ArgumentDataPrototype"))
                    elif concrete_tag == "ASSEMBLY-SW-CONNECTOR":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "AssemblySwConnector"))
                    elif concrete_tag == "ASYNCHRONOUS-SERVER-CALL-POINT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "AsynchronousServerCallPoint"))
                    elif concrete_tag == "ASYNCHRONOUS-SERVER-CALL-RESULT-POINT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "AsynchronousServerCallResultPoint"))
                    elif concrete_tag == "ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "AsynchronousServerCallReturnsEvent"))
                    elif concrete_tag == "ATP-PROTOTYPE":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "AtpPrototype"))
                    elif concrete_tag == "ATP-STRUCTURE-ELEMENT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "AtpStructureElement"))
                    elif concrete_tag == "BACKGROUND-EVENT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "BackgroundEvent"))
                    elif concrete_tag == "BSW-INTERNAL-BEHAVIOR":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "BswInternalBehavior"))
                    elif concrete_tag == "BSW-MODULE-DESCRIPTION":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "BswModuleDescription"))
                    elif concrete_tag == "BSW-SERVICE-DEPENDENCY-IDENT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "BswServiceDependencyIdent"))
                    elif concrete_tag == "BULK-NV-DATA-DESCRIPTOR":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "BulkNvDataDescriptor"))
                    elif concrete_tag == "CLIENT-SERVER-OPERATION":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "ClientServerOperation"))
                    elif concrete_tag == "DATA-PROTOTYPE-GROUP":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "DataPrototypeGroup"))
                    elif concrete_tag == "DATA-RECEIVE-ERROR-EVENT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "DataReceiveErrorEvent"))
                    elif concrete_tag == "DATA-RECEIVED-EVENT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "DataReceivedEvent"))
                    elif concrete_tag == "DATA-SEND-COMPLETED-EVENT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "DataSendCompletedEvent"))
                    elif concrete_tag == "DATA-WRITE-COMPLETED-EVENT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "DataWriteCompletedEvent"))
                    elif concrete_tag == "DELEGATION-SW-CONNECTOR":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "DelegationSwConnector"))
                    elif concrete_tag == "DIAGNOSTIC-PARAMETER-IDENT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticParameterIdent"))
                    elif concrete_tag == "EXTERNAL-TRIGGER-OCCURRED-EVENT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "ExternalTriggerOccurredEvent"))
                    elif concrete_tag == "EXTERNAL-TRIGGERING-POINT-IDENT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "ExternalTriggeringPointIdent"))
                    elif concrete_tag == "IMPLEMENTATION-DATA-TYPE-ELEMENT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "ImplementationDataTypeElement"))
                    elif concrete_tag == "INIT-EVENT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "InitEvent"))
                    elif concrete_tag == "INTERNAL-TRIGGER-OCCURRED-EVENT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "InternalTriggerOccurredEvent"))
                    elif concrete_tag == "INTERNAL-TRIGGERING-POINT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "InternalTriggeringPoint"))
                    elif concrete_tag == "MODE-ACCESS-POINT-IDENT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "ModeAccessPointIdent"))
                    elif concrete_tag == "MODE-DECLARATION":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "ModeDeclaration"))
                    elif concrete_tag == "MODE-DECLARATION-GROUP-PROTOTYPE":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "ModeDeclarationGroupPrototype"))
                    elif concrete_tag == "MODE-DECLARATION-MAPPING":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "ModeDeclarationMapping"))
                    elif concrete_tag == "MODE-SWITCH-POINT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "ModeSwitchPoint"))
                    elif concrete_tag == "MODE-SWITCHED-ACK-EVENT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "ModeSwitchedAckEvent"))
                    elif concrete_tag == "MODE-TRANSITION":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "ModeTransition"))
                    elif concrete_tag == "NV-BLOCK-DESCRIPTOR":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "NvBlockDescriptor"))
                    elif concrete_tag == "OPERATION-INVOKED-EVENT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "OperationInvokedEvent"))
                    elif concrete_tag == "OS-TASK-EXECUTION-EVENT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "OsTaskExecutionEvent"))
                    elif concrete_tag == "P-PORT-PROTOTYPE":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "PPortPrototype"))
                    elif concrete_tag == "P-R-PORT-PROTOTYPE":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "PRPortPrototype"))
                    elif concrete_tag == "PARAMETER-ACCESS":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "ParameterAccess"))
                    elif concrete_tag == "PARAMETER-DATA-PROTOTYPE":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "ParameterDataPrototype"))
                    elif concrete_tag == "PASS-THROUGH-SW-CONNECTOR":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "PassThroughSwConnector"))
                    elif concrete_tag == "PER-INSTANCE-MEMORY":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "PerInstanceMemory"))
                    elif concrete_tag == "PORT-GROUP":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "PortGroup"))
                    elif concrete_tag == "PORT-PROTOTYPE-BLUEPRINT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "PortPrototypeBlueprint"))
                    elif concrete_tag == "R-PORT-PROTOTYPE":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "RPortPrototype"))
                    elif concrete_tag == "ROOT-SW-COMPOSITION-PROTOTYPE":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "RootSwCompositionPrototype"))
                    elif concrete_tag == "RUNNABLE-ENTITY":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "RunnableEntity"))
                    elif concrete_tag == "RUNNABLE-ENTITY-GROUP":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "RunnableEntityGroup"))
                    elif concrete_tag == "SWC-BSW-MAPPING":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "SwcBswMapping"))
                    elif concrete_tag == "SWC-INTERNAL-BEHAVIOR":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "SwcInternalBehavior"))
                    elif concrete_tag == "SWC-MODE-MANAGER-ERROR-EVENT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "SwcModeManagerErrorEvent"))
                    elif concrete_tag == "SWC-MODE-SWITCH-EVENT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "SwcModeSwitchEvent"))
                    elif concrete_tag == "SWC-SERVICE-DEPENDENCY":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "SwcServiceDependency"))
                    elif concrete_tag == "SYNCHRONOUS-SERVER-CALL-POINT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "SynchronousServerCallPoint"))
                    elif concrete_tag == "SYSTEM":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "System"))
                    elif concrete_tag == "TIMING-EVENT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "TimingEvent"))
                    elif concrete_tag == "TRANSFORMER-HARD-ERROR-EVENT":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "TransformerHardErrorEvent"))
                    elif concrete_tag == "TRIGGER":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "Trigger"))
                    elif concrete_tag == "VARIABLE-ACCESS":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "VariableAccess"))
                    elif concrete_tag == "VARIABLE-DATA-PROTOTYPE":
                        setattr(obj, "value", SerializationHelper.deserialize_by_tag(child[0], "VariableDataPrototype"))

        return obj



class EcucInstanceReferenceValueBuilder(EcucAbstractReferenceValueBuilder):
    """Builder for EcucInstanceReferenceValue with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucInstanceReferenceValue = EcucInstanceReferenceValue()


    def with_value(self, value: Optional[AtpFeature]) -> "EcucInstanceReferenceValueBuilder":
        """Set value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.value = value
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


    def build(self) -> EcucInstanceReferenceValue:
        """Build and return the EcucInstanceReferenceValue instance with validation."""
        self._validate_instance()
        pass
        return self._obj