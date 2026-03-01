"""Collection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2009)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 398)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 175)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ElementCollection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import instance_ref
from armodel2.serialization.decorators import ref_conditional

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import (
    AutoCollectEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    NameToken,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef.any_instance_ref import (
    AnyInstanceRef,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Collection(ARElement):
    """AUTOSAR Collection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "COLLECTION"


    auto_collect: Optional[AutoCollectEnum]
    _collected_instance_irefs: list[AnyInstanceRef]
    collection_semantics: Optional[NameToken]
    element_role: Optional[Identifier]
    element_refs: list[ARRef]
    source_element_refs: list[ARRef]
    _source_instance_irefs: list[AnyInstanceRef]
    _DESERIALIZE_DISPATCH = {
        "AUTO-COLLECT": lambda obj, elem: setattr(obj, "auto_collect", AutoCollectEnum.deserialize(elem)),
        "COLLECTED-INSTANCES": lambda obj, elem: obj._collected_instance_irefs.append(ARRef.deserialize(elem)),
        "COLLECTION-SEMANTICS": lambda obj, elem: setattr(obj, "collection_semantics", SerializationHelper.deserialize_by_tag(elem, "NameToken")),
        "ELEMENT-ROLE": lambda obj, elem: setattr(obj, "element_role", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
        "ELEMENTS": ("_POLYMORPHIC_LIST", "element_refs", ["ARPackage", "AbstractDoIpLogicAddressProps", "AbstractEvent", "AbstractImplementationDataTypeElement", "AbstractSecurityEventFilter", "AbstractSecurityIdsmInstanceFilter", "AbstractServiceInstance", "AppOsTaskProxyToEcuTaskProxyMapping", "ApplicationEndpoint", "ApplicationError", "ApplicationPartitionToEcuPartitionMapping", "AppliedStandard", "AsynchronousServerCallResultPoint", "AtpBlueprint", "AtpBlueprintable", "AtpClassifier", "AtpFeature", "AutosarOperationArgumentInstance", "AutosarVariableInstance", "BinaryManifestAddressableObject", "BinaryManifestItemDefinition", "BinaryManifestResource", "BinaryManifestResourceDefinition", "BlockState", "BswInternalTriggeringPoint", "BswModuleDependency", "BuildActionEntity", "BuildActionEnvironment", "CanTpAddress", "CanTpChannel", "CanTpNode", "Chapter", "ClassContentConditional", "ClientIdDefinition", "ClientServerOperation", "Code", "CollectableElement", "ComManagementMapping", "CommConnectorPort", "CommunicationConnector", "CommunicationController", "Compiler", "ConsistencyNeeds", "ConsumedEventGroup", "CouplingElementAbstractDetails", "CouplingPort", "CouplingPortAbstractShaper", "CouplingPortStructuralElement", "CpSoftwareClusterResource", "CpSoftwareClusterResourceToApplicationPartitionMapping", "CpSoftwareClusterToApplicationPartitionMapping", "CpSoftwareClusterToEcuInstanceMapping", "CpSoftwareClusterToResourceMapping", "CryptoServiceMapping", "DataPrototypeGroup", "Data", "Transformation", "DdsCpDomain", "DdsCpPartition", "DdsCpQosProfile", "DdsCpTopic", "DependencyOnArtifact", "DiagEventDebounceAlgorithm", "DiagnosticAuthTransmitCertificateEvaluation", "DiagnosticConnectedIndicator", "DiagnosticDataElement", "DiagnosticDebounceAlgorithmProps", "DiagnosticFunctionInhibitSource", "DiagnosticParameterElement", "DiagnosticRoutineSubfunction", "DltApplication", "DltArgument", "DltLogChannel", "DltMessage", "DoIpInterface", "DoIpLogicAddress", "DoIpRoutingActivation", "ECUMapping", "EOCExecutableEntityRefAbstract", "EcuPartition", "EcucContainerValue", "EcucDefinitionElement", "EcucDestinationUriDef", "EcucEnumerationLiteralDef", "EcucQuery", "EcucValidationCondition", "EndToEndProtection", "EthernetWakeupSleepOnDatalineConfig", "EventHandler", "ExclusiveArea", "ExecutableEntity", "ExecutionTime", "FMAttributeDef", "FMFeatureMapAssertion", "FMFeatureMapCondition", "FMFeatureMapElement", "FMFeatureRelation", "FMFeatureRestriction", "FMFeatureSelection", "FlatInstanceDescriptor", "FlexrayArTpNode", "FlexrayTpConnectionControl", "FlexrayTpNode", "FlexrayTpPduPool", "FrameTriggering", "GeneralParameter", "GlobalTimeGateway", "GlobalTimeMaster", "GlobalTimeSlave", "HeapUsage", "HwAttributeDef", "HwAttributeLiteralDef", "HwPin", "HwPinGroup", "IEEE1722TpAcfBus", "IEEE1722TpAcfBusPart", "IPSecRule", "IPv6ExtHeaderFilterList", "ISignalToIPduMapping", "ISignalTriggering", "IdentCaption", "ImpositionTime", "InternalTriggeringPoint", "J1939SharedAddressCluster", "J1939TpNode", "Keyword", "LifeCycleState", "LinScheduleTable", "LinTpNode", "Linker", "MacMulticastGroup", "MacSecKayParticipant", "McDataInstance", "MemorySection", "ModeDeclaration", "ModeDeclarationMapping", "ModeSwitchPoint", "NetworkEndpoint", "NmCluster", "NmEcu", "NmNode", "NvBlockDescriptor", "PackageableElement", "ParameterAccess", "PduActivationRoutingGroup", "PduToFrameMapping", "PduTriggering", "PerInstanceMemory", "PhysicalChannel", "PortElementToCommunicationResourceMapping", "PortGroup", "PortInterfaceMapping", "PossibleErrorReaction", "ResourceConsumption", "RootSwCompositionPrototype", "RptComponent", "RptContainer", "RptExecutableEntity", "RptExecutableEntityEvent", "RptExecutionContext", "RptProfile", "RptServicePoint", "RteEventInCompositionSeparation", "RteEventInCompositionToOsTaskProxyMapping", "RteEventInSystemSeparation", "RteEventInSystemToOsTaskProxyMapping", "RunnableEntityGroup", "SdgAttribute", "SdgClass", "SecureCommunicationAuthenticationProps", "SecureCommunicationFreshnessProps", "SecurityEventContextProps", "ServerCallPoint", "ServiceNeeds", "SignalServiceTranslationElementProps", "SignalServiceTranslationEventProps", "SignalServiceTranslationProps", "SocketAddress", "SomeipTpChannel", "SpecElementReference", "StackUsage", "StaticSocketConnection", "StructuredReq", "SwGenericAxisParamType", "SwServiceArg", "SwcServiceDependency", "SwcToApplicationPartitionMapping", "SwcToEcuMapping", "SwcToImplMapping", "SwitchAsynchronousTrafficShaperGroupEntry", "SwitchFlowMeteringEntry", "SwitchStreamFilterActionDestPortModification", "SwitchStreamFilterEntry", "SwitchStreamFilterRule", "SwitchStreamGateEntry", "SwitchStreamIdentification", "SystemMapping", "SystemSignalGroupToCommunicationResourceMapping", "SystemSignalToCommunicationResourceMapping", "TDCpSoftwareClusterMapping", "TDCpSoftwareClusterResourceMapping", "TcpOptionFilterList", "TimingClock", "TimingClockSyncAccuracy", "TimingCondition", "TimingConstraint", "TimingDescription", "TimingExtensionResource", "TimingModeInstance", "TlsCryptoCipherSuite", "TlsCryptoCipherSuiteProps", "Topic1", "TpAddress", "TraceableTable", "TraceableText", "TracedFailure", "TransformationProps", "TransformationTechnology", "Trigger", "VariableAccess", "VariationPointProxy", "ViewMap", "VlanConfig", "WaitPoint"]),
        "SOURCE-ELEMENTS": ("_POLYMORPHIC_LIST", "source_element_refs", ["ARPackage", "AbstractDoIpLogicAddressProps", "AbstractEvent", "AbstractImplementationDataTypeElement", "AbstractSecurityEventFilter", "AbstractSecurityIdsmInstanceFilter", "AbstractServiceInstance", "AppOsTaskProxyToEcuTaskProxyMapping", "ApplicationEndpoint", "ApplicationError", "ApplicationPartitionToEcuPartitionMapping", "AppliedStandard", "AsynchronousServerCallResultPoint", "AtpBlueprint", "AtpBlueprintable", "AtpClassifier", "AtpFeature", "AutosarOperationArgumentInstance", "AutosarVariableInstance", "BinaryManifestAddressableObject", "BinaryManifestItemDefinition", "BinaryManifestResource", "BinaryManifestResourceDefinition", "BlockState", "BswInternalTriggeringPoint", "BswModuleDependency", "BuildActionEntity", "BuildActionEnvironment", "CanTpAddress", "CanTpChannel", "CanTpNode", "Chapter", "ClassContentConditional", "ClientIdDefinition", "ClientServerOperation", "Code", "CollectableElement", "ComManagementMapping", "CommConnectorPort", "CommunicationConnector", "CommunicationController", "Compiler", "ConsistencyNeeds", "ConsumedEventGroup", "CouplingElementAbstractDetails", "CouplingPort", "CouplingPortAbstractShaper", "CouplingPortStructuralElement", "CpSoftwareClusterResource", "CpSoftwareClusterResourceToApplicationPartitionMapping", "CpSoftwareClusterToApplicationPartitionMapping", "CpSoftwareClusterToEcuInstanceMapping", "CpSoftwareClusterToResourceMapping", "CryptoServiceMapping", "DataPrototypeGroup", "Data", "Transformation", "DdsCpDomain", "DdsCpPartition", "DdsCpQosProfile", "DdsCpTopic", "DependencyOnArtifact", "DiagEventDebounceAlgorithm", "DiagnosticAuthTransmitCertificateEvaluation", "DiagnosticConnectedIndicator", "DiagnosticDataElement", "DiagnosticDebounceAlgorithmProps", "DiagnosticFunctionInhibitSource", "DiagnosticParameterElement", "DiagnosticRoutineSubfunction", "DltApplication", "DltArgument", "DltLogChannel", "DltMessage", "DoIpInterface", "DoIpLogicAddress", "DoIpRoutingActivation", "ECUMapping", "EOCExecutableEntityRefAbstract", "EcuPartition", "EcucContainerValue", "EcucDefinitionElement", "EcucDestinationUriDef", "EcucEnumerationLiteralDef", "EcucQuery", "EcucValidationCondition", "EndToEndProtection", "EthernetWakeupSleepOnDatalineConfig", "EventHandler", "ExclusiveArea", "ExecutableEntity", "ExecutionTime", "FMAttributeDef", "FMFeatureMapAssertion", "FMFeatureMapCondition", "FMFeatureMapElement", "FMFeatureRelation", "FMFeatureRestriction", "FMFeatureSelection", "FlatInstanceDescriptor", "FlexrayArTpNode", "FlexrayTpConnectionControl", "FlexrayTpNode", "FlexrayTpPduPool", "FrameTriggering", "GeneralParameter", "GlobalTimeGateway", "GlobalTimeMaster", "GlobalTimeSlave", "HeapUsage", "HwAttributeDef", "HwAttributeLiteralDef", "HwPin", "HwPinGroup", "IEEE1722TpAcfBus", "IEEE1722TpAcfBusPart", "IPSecRule", "IPv6ExtHeaderFilterList", "ISignalToIPduMapping", "ISignalTriggering", "IdentCaption", "ImpositionTime", "InternalTriggeringPoint", "J1939SharedAddressCluster", "J1939TpNode", "Keyword", "LifeCycleState", "LinScheduleTable", "LinTpNode", "Linker", "MacMulticastGroup", "MacSecKayParticipant", "McDataInstance", "MemorySection", "ModeDeclaration", "ModeDeclarationMapping", "ModeSwitchPoint", "NetworkEndpoint", "NmCluster", "NmEcu", "NmNode", "NvBlockDescriptor", "PackageableElement", "ParameterAccess", "PduActivationRoutingGroup", "PduToFrameMapping", "PduTriggering", "PerInstanceMemory", "PhysicalChannel", "PortElementToCommunicationResourceMapping", "PortGroup", "PortInterfaceMapping", "PossibleErrorReaction", "ResourceConsumption", "RootSwCompositionPrototype", "RptComponent", "RptContainer", "RptExecutableEntity", "RptExecutableEntityEvent", "RptExecutionContext", "RptProfile", "RptServicePoint", "RteEventInCompositionSeparation", "RteEventInCompositionToOsTaskProxyMapping", "RteEventInSystemSeparation", "RteEventInSystemToOsTaskProxyMapping", "RunnableEntityGroup", "SdgAttribute", "SdgClass", "SecureCommunicationAuthenticationProps", "SecureCommunicationFreshnessProps", "SecurityEventContextProps", "ServerCallPoint", "ServiceNeeds", "SignalServiceTranslationElementProps", "SignalServiceTranslationEventProps", "SignalServiceTranslationProps", "SocketAddress", "SomeipTpChannel", "SpecElementReference", "StackUsage", "StaticSocketConnection", "StructuredReq", "SwGenericAxisParamType", "SwServiceArg", "SwcServiceDependency", "SwcToApplicationPartitionMapping", "SwcToEcuMapping", "SwcToImplMapping", "SwitchAsynchronousTrafficShaperGroupEntry", "SwitchFlowMeteringEntry", "SwitchStreamFilterActionDestPortModification", "SwitchStreamFilterEntry", "SwitchStreamFilterRule", "SwitchStreamGateEntry", "SwitchStreamIdentification", "SystemMapping", "SystemSignalGroupToCommunicationResourceMapping", "SystemSignalToCommunicationResourceMapping", "TDCpSoftwareClusterMapping", "TDCpSoftwareClusterResourceMapping", "TcpOptionFilterList", "TimingClock", "TimingClockSyncAccuracy", "TimingCondition", "TimingConstraint", "TimingDescription", "TimingExtensionResource", "TimingModeInstance", "TlsCryptoCipherSuite", "TlsCryptoCipherSuiteProps", "Topic1", "TpAddress", "TraceableTable", "TraceableText", "TracedFailure", "TransformationProps", "TransformationTechnology", "Trigger", "VariableAccess", "VariationPointProxy", "ViewMap", "VlanConfig", "WaitPoint"]),
        "SOURCE-INSTANCES": lambda obj, elem: obj._source_instance_irefs.append(ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize Collection."""
        super().__init__()
        self.auto_collect: Optional[AutoCollectEnum] = None
        self._collected_instance_irefs: list[AnyInstanceRef] = []
        self.collection_semantics: Optional[NameToken] = None
        self.element_role: Optional[Identifier] = None
        self.element_refs: list[ARRef] = []
        self.source_element_refs: list[ARRef] = []
        self._source_instance_irefs: list[AnyInstanceRef] = []
    @property
    @instance_ref(flatten=True)
    def collected_instance_irefs(self) -> list[AnyInstanceRef]:
        """Get collected_instance_irefs instance reference."""
        return self._collected_instance_irefs

    @collected_instance_irefs.setter
    def collected_instance_irefs(self, value: list[AnyInstanceRef]) -> None:
        """Set collected_instance_irefs instance reference."""
        self._collected_instance_irefs = value

    @property
    @instance_ref(flatten=True)
    def source_instance_irefs(self) -> list[AnyInstanceRef]:
        """Get source_instance_irefs instance reference."""
        return self._source_instance_irefs

    @source_instance_irefs.setter
    def source_instance_irefs(self, value: list[AnyInstanceRef]) -> None:
        """Set source_instance_irefs instance reference."""
        self._source_instance_irefs = value


    def serialize(self) -> ET.Element:
        """Serialize Collection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Collection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize auto_collect
        if self.auto_collect is not None:
            serialized = SerializationHelper.serialize_item(self.auto_collect, "AutoCollectEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AUTO-COLLECT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize collected_instance_irefs (list of instance references with wrapper "COLLECTED-INSTANCES-IREF")
        if self.collected_instance_irefs:
            serialized = SerializationHelper.serialize_item(self.collected_instance_irefs, "AnyInstanceRef")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("COLLECTED-INSTANCES-IREF")
                # Flatten: append children of serialized element directly to iref wrapper
                for child in serialized:
                    iref_wrapper.append(child)
                elem.append(iref_wrapper)

        # Serialize collection_semantics
        if self.collection_semantics is not None:
            serialized = SerializationHelper.serialize_item(self.collection_semantics, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COLLECTION-SEMANTICS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize element_role
        if self.element_role is not None:
            serialized = SerializationHelper.serialize_item(self.element_role, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ELEMENT-ROLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize element_refs (list to container "ELEMENT-REFS")
        if self.element_refs:
            wrapper = ET.Element("ELEMENT-REFS")
            for item in self.element_refs:
                serialized = SerializationHelper.serialize_item(item, "Identifiable")
                if serialized is not None:
                    child_elem = ET.Element("ELEMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize source_element_refs (list to container "SOURCE-ELEMENT-REFS")
        if self.source_element_refs:
            wrapper = ET.Element("SOURCE-ELEMENT-REFS")
            for item in self.source_element_refs:
                serialized = SerializationHelper.serialize_item(item, "Identifiable")
                if serialized is not None:
                    child_elem = ET.Element("SOURCE-ELEMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize source_instance_irefs (list of instance references with wrapper "SOURCE-INSTANCES-IREF")
        if self.source_instance_irefs:
            serialized = SerializationHelper.serialize_item(self.source_instance_irefs, "AnyInstanceRef")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("SOURCE-INSTANCES-IREF")
                # Flatten: append children of serialized element directly to iref wrapper
                for child in serialized:
                    iref_wrapper.append(child)
                elem.append(iref_wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Collection":
        """Deserialize XML element to Collection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Collection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Collection, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "AUTO-COLLECT":
                setattr(obj, "auto_collect", AutoCollectEnum.deserialize(child))
            elif tag == "COLLECTED-INSTANCES":
                obj._collected_instance_irefs.append(ARRef.deserialize(child))
            elif tag == "COLLECTION-SEMANTICS":
                setattr(obj, "collection_semantics", SerializationHelper.deserialize_by_tag(child, "NameToken"))
            elif tag == "ELEMENT-ROLE":
                setattr(obj, "element_role", SerializationHelper.deserialize_by_tag(child, "Identifier"))
            elif tag == "ELEMENTS":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "AR-PACKAGE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ARPackage"))
                    elif concrete_tag == "ABSTRACT-DO-IP-LOGIC-ADDRESS-PROPS":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AbstractDoIpLogicAddressProps"))
                    elif concrete_tag == "ABSTRACT-EVENT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AbstractEvent"))
                    elif concrete_tag == "ABSTRACT-IMPLEMENTATION-DATA-TYPE-ELEMENT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AbstractImplementationDataTypeElement"))
                    elif concrete_tag == "ABSTRACT-SECURITY-EVENT-FILTER":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AbstractSecurityEventFilter"))
                    elif concrete_tag == "ABSTRACT-SECURITY-IDSM-INSTANCE-FILTER":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AbstractSecurityIdsmInstanceFilter"))
                    elif concrete_tag == "ABSTRACT-SERVICE-INSTANCE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AbstractServiceInstance"))
                    elif concrete_tag == "APP-OS-TASK-PROXY-TO-ECU-TASK-PROXY-MAPPING":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AppOsTaskProxyToEcuTaskProxyMapping"))
                    elif concrete_tag == "APPLICATION-ENDPOINT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ApplicationEndpoint"))
                    elif concrete_tag == "APPLICATION-ERROR":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ApplicationError"))
                    elif concrete_tag == "APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPING":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ApplicationPartitionToEcuPartitionMapping"))
                    elif concrete_tag == "APPLIED-STANDARD":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AppliedStandard"))
                    elif concrete_tag == "ASYNCHRONOUS-SERVER-CALL-RESULT-POINT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AsynchronousServerCallResultPoint"))
                    elif concrete_tag == "ATP-BLUEPRINT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AtpBlueprint"))
                    elif concrete_tag == "ATP-BLUEPRINTABLE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AtpBlueprintable"))
                    elif concrete_tag == "ATP-CLASSIFIER":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AtpClassifier"))
                    elif concrete_tag == "ATP-FEATURE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AtpFeature"))
                    elif concrete_tag == "AUTOSAR-OPERATION-ARGUMENT-INSTANCE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AutosarOperationArgumentInstance"))
                    elif concrete_tag == "AUTOSAR-VARIABLE-INSTANCE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AutosarVariableInstance"))
                    elif concrete_tag == "BINARY-MANIFEST-ADDRESSABLE-OBJECT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BinaryManifestAddressableObject"))
                    elif concrete_tag == "BINARY-MANIFEST-ITEM-DEFINITION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BinaryManifestItemDefinition"))
                    elif concrete_tag == "BINARY-MANIFEST-RESOURCE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BinaryManifestResource"))
                    elif concrete_tag == "BINARY-MANIFEST-RESOURCE-DEFINITION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BinaryManifestResourceDefinition"))
                    elif concrete_tag == "BLOCK-STATE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BlockState"))
                    elif concrete_tag == "BSW-INTERNAL-TRIGGERING-POINT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BswInternalTriggeringPoint"))
                    elif concrete_tag == "BSW-MODULE-DEPENDENCY":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BswModuleDependency"))
                    elif concrete_tag == "BUILD-ACTION-ENTITY":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BuildActionEntity"))
                    elif concrete_tag == "BUILD-ACTION-ENVIRONMENT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BuildActionEnvironment"))
                    elif concrete_tag == "CAN-TP-ADDRESS":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CanTpAddress"))
                    elif concrete_tag == "CAN-TP-CHANNEL":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CanTpChannel"))
                    elif concrete_tag == "CAN-TP-NODE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CanTpNode"))
                    elif concrete_tag == "CHAPTER":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "Chapter"))
                    elif concrete_tag == "CLASS-CONTENT-CONDITIONAL":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ClassContentConditional"))
                    elif concrete_tag == "CLIENT-ID-DEFINITION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ClientIdDefinition"))
                    elif concrete_tag == "CLIENT-SERVER-OPERATION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ClientServerOperation"))
                    elif concrete_tag == "CODE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "Code"))
                    elif concrete_tag == "COLLECTABLE-ELEMENT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CollectableElement"))
                    elif concrete_tag == "COM-MANAGEMENT-MAPPING":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ComManagementMapping"))
                    elif concrete_tag == "COMM-CONNECTOR-PORT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CommConnectorPort"))
                    elif concrete_tag == "COMMUNICATION-CONNECTOR":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CommunicationConnector"))
                    elif concrete_tag == "COMMUNICATION-CONTROLLER":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CommunicationController"))
                    elif concrete_tag == "COMPILER":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "Compiler"))
                    elif concrete_tag == "CONSISTENCY-NEEDS":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ConsistencyNeeds"))
                    elif concrete_tag == "CONSUMED-EVENT-GROUP":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ConsumedEventGroup"))
                    elif concrete_tag == "COUPLING-ELEMENT-ABSTRACT-DETAILS":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CouplingElementAbstractDetails"))
                    elif concrete_tag == "COUPLING-PORT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CouplingPort"))
                    elif concrete_tag == "COUPLING-PORT-ABSTRACT-SHAPER":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CouplingPortAbstractShaper"))
                    elif concrete_tag == "COUPLING-PORT-STRUCTURAL-ELEMENT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CouplingPortStructuralElement"))
                    elif concrete_tag == "CP-SOFTWARE-CLUSTER-RESOURCE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CpSoftwareClusterResource"))
                    elif concrete_tag == "CP-SOFTWARE-CLUSTER-RESOURCE-TO-APPLICATION-PARTITION-MAPPING":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CpSoftwareClusterResourceToApplicationPartitionMapping"))
                    elif concrete_tag == "CP-SOFTWARE-CLUSTER-TO-APPLICATION-PARTITION-MAPPING":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CpSoftwareClusterToApplicationPartitionMapping"))
                    elif concrete_tag == "CP-SOFTWARE-CLUSTER-TO-ECU-INSTANCE-MAPPING":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CpSoftwareClusterToEcuInstanceMapping"))
                    elif concrete_tag == "CP-SOFTWARE-CLUSTER-TO-RESOURCE-MAPPING":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CpSoftwareClusterToResourceMapping"))
                    elif concrete_tag == "CRYPTO-SERVICE-MAPPING":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CryptoServiceMapping"))
                    elif concrete_tag == "DATA-PROTOTYPE-GROUP":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DataPrototypeGroup"))
                    elif concrete_tag == "DATA":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "Data"))
                    elif concrete_tag == "TRANSFORMATION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "Transformation"))
                    elif concrete_tag == "DDS-CP-DOMAIN":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DdsCpDomain"))
                    elif concrete_tag == "DDS-CP-PARTITION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DdsCpPartition"))
                    elif concrete_tag == "DDS-CP-QOS-PROFILE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DdsCpQosProfile"))
                    elif concrete_tag == "DDS-CP-TOPIC":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DdsCpTopic"))
                    elif concrete_tag == "DEPENDENCY-ON-ARTIFACT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DependencyOnArtifact"))
                    elif concrete_tag == "DIAG-EVENT-DEBOUNCE-ALGORITHM":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DiagEventDebounceAlgorithm"))
                    elif concrete_tag == "DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE-EVALUATION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DiagnosticAuthTransmitCertificateEvaluation"))
                    elif concrete_tag == "DIAGNOSTIC-CONNECTED-INDICATOR":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DiagnosticConnectedIndicator"))
                    elif concrete_tag == "DIAGNOSTIC-DATA-ELEMENT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DiagnosticDataElement"))
                    elif concrete_tag == "DIAGNOSTIC-DEBOUNCE-ALGORITHM-PROPS":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DiagnosticDebounceAlgorithmProps"))
                    elif concrete_tag == "DIAGNOSTIC-FUNCTION-INHIBIT-SOURCE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DiagnosticFunctionInhibitSource"))
                    elif concrete_tag == "DIAGNOSTIC-PARAMETER-ELEMENT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DiagnosticParameterElement"))
                    elif concrete_tag == "DIAGNOSTIC-ROUTINE-SUBFUNCTION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DiagnosticRoutineSubfunction"))
                    elif concrete_tag == "DLT-APPLICATION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DltApplication"))
                    elif concrete_tag == "DLT-ARGUMENT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DltArgument"))
                    elif concrete_tag == "DLT-LOG-CHANNEL":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DltLogChannel"))
                    elif concrete_tag == "DLT-MESSAGE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DltMessage"))
                    elif concrete_tag == "DO-IP-INTERFACE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DoIpInterface"))
                    elif concrete_tag == "DO-IP-LOGIC-ADDRESS":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DoIpLogicAddress"))
                    elif concrete_tag == "DO-IP-ROUTING-ACTIVATION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DoIpRoutingActivation"))
                    elif concrete_tag == "E-C-U-MAPPING":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ECUMapping"))
                    elif concrete_tag == "E-O-C-EXECUTABLE-ENTITY-REF-ABSTRACT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EOCExecutableEntityRefAbstract"))
                    elif concrete_tag == "ECU-PARTITION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EcuPartition"))
                    elif concrete_tag == "ECUC-CONTAINER-VALUE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EcucContainerValue"))
                    elif concrete_tag == "ECUC-DEFINITION-ELEMENT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EcucDefinitionElement"))
                    elif concrete_tag == "ECUC-DESTINATION-URI-DEF":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EcucDestinationUriDef"))
                    elif concrete_tag == "ECUC-ENUMERATION-LITERAL-DEF":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EcucEnumerationLiteralDef"))
                    elif concrete_tag == "ECUC-QUERY":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EcucQuery"))
                    elif concrete_tag == "ECUC-VALIDATION-CONDITION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EcucValidationCondition"))
                    elif concrete_tag == "END-TO-END-PROTECTION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EndToEndProtection"))
                    elif concrete_tag == "ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EthernetWakeupSleepOnDatalineConfig"))
                    elif concrete_tag == "EVENT-HANDLER":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EventHandler"))
                    elif concrete_tag == "EXCLUSIVE-AREA":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ExclusiveArea"))
                    elif concrete_tag == "EXECUTABLE-ENTITY":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ExecutableEntity"))
                    elif concrete_tag == "EXECUTION-TIME":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ExecutionTime"))
                    elif concrete_tag == "F-M-ATTRIBUTE-DEF":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FMAttributeDef"))
                    elif concrete_tag == "F-M-FEATURE-MAP-ASSERTION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FMFeatureMapAssertion"))
                    elif concrete_tag == "F-M-FEATURE-MAP-CONDITION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FMFeatureMapCondition"))
                    elif concrete_tag == "F-M-FEATURE-MAP-ELEMENT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FMFeatureMapElement"))
                    elif concrete_tag == "F-M-FEATURE-RELATION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FMFeatureRelation"))
                    elif concrete_tag == "F-M-FEATURE-RESTRICTION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FMFeatureRestriction"))
                    elif concrete_tag == "F-M-FEATURE-SELECTION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FMFeatureSelection"))
                    elif concrete_tag == "FLAT-INSTANCE-DESCRIPTOR":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FlatInstanceDescriptor"))
                    elif concrete_tag == "FLEXRAY-AR-TP-NODE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FlexrayArTpNode"))
                    elif concrete_tag == "FLEXRAY-TP-CONNECTION-CONTROL":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FlexrayTpConnectionControl"))
                    elif concrete_tag == "FLEXRAY-TP-NODE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FlexrayTpNode"))
                    elif concrete_tag == "FLEXRAY-TP-PDU-POOL":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FlexrayTpPduPool"))
                    elif concrete_tag == "FRAME-TRIGGERING":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FrameTriggering"))
                    elif concrete_tag == "GENERAL-PARAMETER":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "GeneralParameter"))
                    elif concrete_tag == "GLOBAL-TIME-GATEWAY":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "GlobalTimeGateway"))
                    elif concrete_tag == "GLOBAL-TIME-MASTER":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "GlobalTimeMaster"))
                    elif concrete_tag == "GLOBAL-TIME-SLAVE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "GlobalTimeSlave"))
                    elif concrete_tag == "HEAP-USAGE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "HeapUsage"))
                    elif concrete_tag == "HW-ATTRIBUTE-DEF":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "HwAttributeDef"))
                    elif concrete_tag == "HW-ATTRIBUTE-LITERAL-DEF":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "HwAttributeLiteralDef"))
                    elif concrete_tag == "HW-PIN":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "HwPin"))
                    elif concrete_tag == "HW-PIN-GROUP":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "HwPinGroup"))
                    elif concrete_tag == "I-E-E-E1722-TP-ACF-BUS":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "IEEE1722TpAcfBus"))
                    elif concrete_tag == "I-E-E-E1722-TP-ACF-BUS-PART":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "IEEE1722TpAcfBusPart"))
                    elif concrete_tag == "I-P-SEC-RULE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "IPSecRule"))
                    elif concrete_tag == "I-PV6-EXT-HEADER-FILTER-LIST":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "IPv6ExtHeaderFilterList"))
                    elif concrete_tag == "I-SIGNAL-TO-I-PDU-MAPPING":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ISignalToIPduMapping"))
                    elif concrete_tag == "I-SIGNAL-TRIGGERING":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ISignalTriggering"))
                    elif concrete_tag == "IDENT-CAPTION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "IdentCaption"))
                    elif concrete_tag == "IMPOSITION-TIME":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ImpositionTime"))
                    elif concrete_tag == "INTERNAL-TRIGGERING-POINT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "InternalTriggeringPoint"))
                    elif concrete_tag == "J1939-SHARED-ADDRESS-CLUSTER":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "J1939SharedAddressCluster"))
                    elif concrete_tag == "J1939-TP-NODE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "J1939TpNode"))
                    elif concrete_tag == "KEYWORD":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "Keyword"))
                    elif concrete_tag == "LIFE-CYCLE-STATE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "LifeCycleState"))
                    elif concrete_tag == "LIN-SCHEDULE-TABLE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "LinScheduleTable"))
                    elif concrete_tag == "LIN-TP-NODE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "LinTpNode"))
                    elif concrete_tag == "LINKER":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "Linker"))
                    elif concrete_tag == "MAC-MULTICAST-GROUP":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "MacMulticastGroup"))
                    elif concrete_tag == "MAC-SEC-KAY-PARTICIPANT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "MacSecKayParticipant"))
                    elif concrete_tag == "MC-DATA-INSTANCE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "McDataInstance"))
                    elif concrete_tag == "MEMORY-SECTION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "MemorySection"))
                    elif concrete_tag == "MODE-DECLARATION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ModeDeclaration"))
                    elif concrete_tag == "MODE-DECLARATION-MAPPING":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ModeDeclarationMapping"))
                    elif concrete_tag == "MODE-SWITCH-POINT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ModeSwitchPoint"))
                    elif concrete_tag == "NETWORK-ENDPOINT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "NetworkEndpoint"))
                    elif concrete_tag == "NM-CLUSTER":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "NmCluster"))
                    elif concrete_tag == "NM-ECU":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "NmEcu"))
                    elif concrete_tag == "NM-NODE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "NmNode"))
                    elif concrete_tag == "NV-BLOCK-DESCRIPTOR":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "NvBlockDescriptor"))
                    elif concrete_tag == "PACKAGEABLE-ELEMENT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "PackageableElement"))
                    elif concrete_tag == "PARAMETER-ACCESS":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ParameterAccess"))
                    elif concrete_tag == "PDU-ACTIVATION-ROUTING-GROUP":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "PduActivationRoutingGroup"))
                    elif concrete_tag == "PDU-TO-FRAME-MAPPING":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "PduToFrameMapping"))
                    elif concrete_tag == "PDU-TRIGGERING":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "PduTriggering"))
                    elif concrete_tag == "PER-INSTANCE-MEMORY":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "PerInstanceMemory"))
                    elif concrete_tag == "PHYSICAL-CHANNEL":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "PhysicalChannel"))
                    elif concrete_tag == "PORT-ELEMENT-TO-COMMUNICATION-RESOURCE-MAPPING":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "PortElementToCommunicationResourceMapping"))
                    elif concrete_tag == "PORT-GROUP":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "PortGroup"))
                    elif concrete_tag == "PORT-INTERFACE-MAPPING":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "PortInterfaceMapping"))
                    elif concrete_tag == "POSSIBLE-ERROR-REACTION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "PossibleErrorReaction"))
                    elif concrete_tag == "RESOURCE-CONSUMPTION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ResourceConsumption"))
                    elif concrete_tag == "ROOT-SW-COMPOSITION-PROTOTYPE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "RootSwCompositionPrototype"))
                    elif concrete_tag == "RPT-COMPONENT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "RptComponent"))
                    elif concrete_tag == "RPT-CONTAINER":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "RptContainer"))
                    elif concrete_tag == "RPT-EXECUTABLE-ENTITY":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "RptExecutableEntity"))
                    elif concrete_tag == "RPT-EXECUTABLE-ENTITY-EVENT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "RptExecutableEntityEvent"))
                    elif concrete_tag == "RPT-EXECUTION-CONTEXT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "RptExecutionContext"))
                    elif concrete_tag == "RPT-PROFILE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "RptProfile"))
                    elif concrete_tag == "RPT-SERVICE-POINT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "RptServicePoint"))
                    elif concrete_tag == "RTE-EVENT-IN-COMPOSITION-SEPARATION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "RteEventInCompositionSeparation"))
                    elif concrete_tag == "RTE-EVENT-IN-COMPOSITION-TO-OS-TASK-PROXY-MAPPING":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "RteEventInCompositionToOsTaskProxyMapping"))
                    elif concrete_tag == "RTE-EVENT-IN-SYSTEM-SEPARATION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "RteEventInSystemSeparation"))
                    elif concrete_tag == "RTE-EVENT-IN-SYSTEM-TO-OS-TASK-PROXY-MAPPING":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "RteEventInSystemToOsTaskProxyMapping"))
                    elif concrete_tag == "RUNNABLE-ENTITY-GROUP":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "RunnableEntityGroup"))
                    elif concrete_tag == "SDG-ATTRIBUTE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SdgAttribute"))
                    elif concrete_tag == "SDG-CLASS":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SdgClass"))
                    elif concrete_tag == "SECURE-COMMUNICATION-AUTHENTICATION-PROPS":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SecureCommunicationAuthenticationProps"))
                    elif concrete_tag == "SECURE-COMMUNICATION-FRESHNESS-PROPS":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SecureCommunicationFreshnessProps"))
                    elif concrete_tag == "SECURITY-EVENT-CONTEXT-PROPS":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SecurityEventContextProps"))
                    elif concrete_tag == "SERVER-CALL-POINT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ServerCallPoint"))
                    elif concrete_tag == "SERVICE-NEEDS":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ServiceNeeds"))
                    elif concrete_tag == "SIGNAL-SERVICE-TRANSLATION-ELEMENT-PROPS":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SignalServiceTranslationElementProps"))
                    elif concrete_tag == "SIGNAL-SERVICE-TRANSLATION-EVENT-PROPS":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SignalServiceTranslationEventProps"))
                    elif concrete_tag == "SIGNAL-SERVICE-TRANSLATION-PROPS":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SignalServiceTranslationProps"))
                    elif concrete_tag == "SOCKET-ADDRESS":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SocketAddress"))
                    elif concrete_tag == "SOMEIP-TP-CHANNEL":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SomeipTpChannel"))
                    elif concrete_tag == "SPEC-ELEMENT-REFERENCE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SpecElementReference"))
                    elif concrete_tag == "STACK-USAGE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "StackUsage"))
                    elif concrete_tag == "STATIC-SOCKET-CONNECTION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "StaticSocketConnection"))
                    elif concrete_tag == "STRUCTURED-REQ":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "StructuredReq"))
                    elif concrete_tag == "SW-GENERIC-AXIS-PARAM-TYPE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwGenericAxisParamType"))
                    elif concrete_tag == "SW-SERVICE-ARG":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwServiceArg"))
                    elif concrete_tag == "SWC-SERVICE-DEPENDENCY":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwcServiceDependency"))
                    elif concrete_tag == "SWC-TO-APPLICATION-PARTITION-MAPPING":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwcToApplicationPartitionMapping"))
                    elif concrete_tag == "SWC-TO-ECU-MAPPING":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwcToEcuMapping"))
                    elif concrete_tag == "SWC-TO-IMPL-MAPPING":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwcToImplMapping"))
                    elif concrete_tag == "SWITCH-ASYNCHRONOUS-TRAFFIC-SHAPER-GROUP-ENTRY":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwitchAsynchronousTrafficShaperGroupEntry"))
                    elif concrete_tag == "SWITCH-FLOW-METERING-ENTRY":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwitchFlowMeteringEntry"))
                    elif concrete_tag == "SWITCH-STREAM-FILTER-ACTION-DEST-PORT-MODIFICATION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwitchStreamFilterActionDestPortModification"))
                    elif concrete_tag == "SWITCH-STREAM-FILTER-ENTRY":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwitchStreamFilterEntry"))
                    elif concrete_tag == "SWITCH-STREAM-FILTER-RULE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwitchStreamFilterRule"))
                    elif concrete_tag == "SWITCH-STREAM-GATE-ENTRY":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwitchStreamGateEntry"))
                    elif concrete_tag == "SWITCH-STREAM-IDENTIFICATION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwitchStreamIdentification"))
                    elif concrete_tag == "SYSTEM-MAPPING":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SystemMapping"))
                    elif concrete_tag == "SYSTEM-SIGNAL-GROUP-TO-COMMUNICATION-RESOURCE-MAPPING":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SystemSignalGroupToCommunicationResourceMapping"))
                    elif concrete_tag == "SYSTEM-SIGNAL-TO-COMMUNICATION-RESOURCE-MAPPING":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SystemSignalToCommunicationResourceMapping"))
                    elif concrete_tag == "T-D-CP-SOFTWARE-CLUSTER-MAPPING":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TDCpSoftwareClusterMapping"))
                    elif concrete_tag == "T-D-CP-SOFTWARE-CLUSTER-RESOURCE-MAPPING":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TDCpSoftwareClusterResourceMapping"))
                    elif concrete_tag == "TCP-OPTION-FILTER-LIST":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TcpOptionFilterList"))
                    elif concrete_tag == "TIMING-CLOCK":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TimingClock"))
                    elif concrete_tag == "TIMING-CLOCK-SYNC-ACCURACY":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TimingClockSyncAccuracy"))
                    elif concrete_tag == "TIMING-CONDITION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TimingCondition"))
                    elif concrete_tag == "TIMING-CONSTRAINT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TimingConstraint"))
                    elif concrete_tag == "TIMING-DESCRIPTION":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TimingDescription"))
                    elif concrete_tag == "TIMING-EXTENSION-RESOURCE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TimingExtensionResource"))
                    elif concrete_tag == "TIMING-MODE-INSTANCE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TimingModeInstance"))
                    elif concrete_tag == "TLS-CRYPTO-CIPHER-SUITE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TlsCryptoCipherSuite"))
                    elif concrete_tag == "TLS-CRYPTO-CIPHER-SUITE-PROPS":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TlsCryptoCipherSuiteProps"))
                    elif concrete_tag == "TOPIC1":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "Topic1"))
                    elif concrete_tag == "TP-ADDRESS":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TpAddress"))
                    elif concrete_tag == "TRACEABLE-TABLE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TraceableTable"))
                    elif concrete_tag == "TRACEABLE-TEXT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TraceableText"))
                    elif concrete_tag == "TRACED-FAILURE":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TracedFailure"))
                    elif concrete_tag == "TRANSFORMATION-PROPS":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TransformationProps"))
                    elif concrete_tag == "TRANSFORMATION-TECHNOLOGY":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TransformationTechnology"))
                    elif concrete_tag == "TRIGGER":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "Trigger"))
                    elif concrete_tag == "VARIABLE-ACCESS":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "VariableAccess"))
                    elif concrete_tag == "VARIATION-POINT-PROXY":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "VariationPointProxy"))
                    elif concrete_tag == "VIEW-MAP":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ViewMap"))
                    elif concrete_tag == "VLAN-CONFIG":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "VlanConfig"))
                    elif concrete_tag == "WAIT-POINT":
                        obj.element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "WaitPoint"))
            elif tag == "SOURCE-ELEMENTS":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "AR-PACKAGE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ARPackage"))
                    elif concrete_tag == "ABSTRACT-DO-IP-LOGIC-ADDRESS-PROPS":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AbstractDoIpLogicAddressProps"))
                    elif concrete_tag == "ABSTRACT-EVENT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AbstractEvent"))
                    elif concrete_tag == "ABSTRACT-IMPLEMENTATION-DATA-TYPE-ELEMENT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AbstractImplementationDataTypeElement"))
                    elif concrete_tag == "ABSTRACT-SECURITY-EVENT-FILTER":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AbstractSecurityEventFilter"))
                    elif concrete_tag == "ABSTRACT-SECURITY-IDSM-INSTANCE-FILTER":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AbstractSecurityIdsmInstanceFilter"))
                    elif concrete_tag == "ABSTRACT-SERVICE-INSTANCE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AbstractServiceInstance"))
                    elif concrete_tag == "APP-OS-TASK-PROXY-TO-ECU-TASK-PROXY-MAPPING":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AppOsTaskProxyToEcuTaskProxyMapping"))
                    elif concrete_tag == "APPLICATION-ENDPOINT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ApplicationEndpoint"))
                    elif concrete_tag == "APPLICATION-ERROR":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ApplicationError"))
                    elif concrete_tag == "APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPING":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ApplicationPartitionToEcuPartitionMapping"))
                    elif concrete_tag == "APPLIED-STANDARD":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AppliedStandard"))
                    elif concrete_tag == "ASYNCHRONOUS-SERVER-CALL-RESULT-POINT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AsynchronousServerCallResultPoint"))
                    elif concrete_tag == "ATP-BLUEPRINT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AtpBlueprint"))
                    elif concrete_tag == "ATP-BLUEPRINTABLE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AtpBlueprintable"))
                    elif concrete_tag == "ATP-CLASSIFIER":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AtpClassifier"))
                    elif concrete_tag == "ATP-FEATURE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AtpFeature"))
                    elif concrete_tag == "AUTOSAR-OPERATION-ARGUMENT-INSTANCE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AutosarOperationArgumentInstance"))
                    elif concrete_tag == "AUTOSAR-VARIABLE-INSTANCE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AutosarVariableInstance"))
                    elif concrete_tag == "BINARY-MANIFEST-ADDRESSABLE-OBJECT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BinaryManifestAddressableObject"))
                    elif concrete_tag == "BINARY-MANIFEST-ITEM-DEFINITION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BinaryManifestItemDefinition"))
                    elif concrete_tag == "BINARY-MANIFEST-RESOURCE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BinaryManifestResource"))
                    elif concrete_tag == "BINARY-MANIFEST-RESOURCE-DEFINITION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BinaryManifestResourceDefinition"))
                    elif concrete_tag == "BLOCK-STATE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BlockState"))
                    elif concrete_tag == "BSW-INTERNAL-TRIGGERING-POINT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BswInternalTriggeringPoint"))
                    elif concrete_tag == "BSW-MODULE-DEPENDENCY":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BswModuleDependency"))
                    elif concrete_tag == "BUILD-ACTION-ENTITY":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BuildActionEntity"))
                    elif concrete_tag == "BUILD-ACTION-ENVIRONMENT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BuildActionEnvironment"))
                    elif concrete_tag == "CAN-TP-ADDRESS":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CanTpAddress"))
                    elif concrete_tag == "CAN-TP-CHANNEL":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CanTpChannel"))
                    elif concrete_tag == "CAN-TP-NODE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CanTpNode"))
                    elif concrete_tag == "CHAPTER":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "Chapter"))
                    elif concrete_tag == "CLASS-CONTENT-CONDITIONAL":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ClassContentConditional"))
                    elif concrete_tag == "CLIENT-ID-DEFINITION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ClientIdDefinition"))
                    elif concrete_tag == "CLIENT-SERVER-OPERATION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ClientServerOperation"))
                    elif concrete_tag == "CODE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "Code"))
                    elif concrete_tag == "COLLECTABLE-ELEMENT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CollectableElement"))
                    elif concrete_tag == "COM-MANAGEMENT-MAPPING":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ComManagementMapping"))
                    elif concrete_tag == "COMM-CONNECTOR-PORT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CommConnectorPort"))
                    elif concrete_tag == "COMMUNICATION-CONNECTOR":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CommunicationConnector"))
                    elif concrete_tag == "COMMUNICATION-CONTROLLER":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CommunicationController"))
                    elif concrete_tag == "COMPILER":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "Compiler"))
                    elif concrete_tag == "CONSISTENCY-NEEDS":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ConsistencyNeeds"))
                    elif concrete_tag == "CONSUMED-EVENT-GROUP":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ConsumedEventGroup"))
                    elif concrete_tag == "COUPLING-ELEMENT-ABSTRACT-DETAILS":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CouplingElementAbstractDetails"))
                    elif concrete_tag == "COUPLING-PORT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CouplingPort"))
                    elif concrete_tag == "COUPLING-PORT-ABSTRACT-SHAPER":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CouplingPortAbstractShaper"))
                    elif concrete_tag == "COUPLING-PORT-STRUCTURAL-ELEMENT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CouplingPortStructuralElement"))
                    elif concrete_tag == "CP-SOFTWARE-CLUSTER-RESOURCE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CpSoftwareClusterResource"))
                    elif concrete_tag == "CP-SOFTWARE-CLUSTER-RESOURCE-TO-APPLICATION-PARTITION-MAPPING":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CpSoftwareClusterResourceToApplicationPartitionMapping"))
                    elif concrete_tag == "CP-SOFTWARE-CLUSTER-TO-APPLICATION-PARTITION-MAPPING":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CpSoftwareClusterToApplicationPartitionMapping"))
                    elif concrete_tag == "CP-SOFTWARE-CLUSTER-TO-ECU-INSTANCE-MAPPING":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CpSoftwareClusterToEcuInstanceMapping"))
                    elif concrete_tag == "CP-SOFTWARE-CLUSTER-TO-RESOURCE-MAPPING":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CpSoftwareClusterToResourceMapping"))
                    elif concrete_tag == "CRYPTO-SERVICE-MAPPING":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CryptoServiceMapping"))
                    elif concrete_tag == "DATA-PROTOTYPE-GROUP":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DataPrototypeGroup"))
                    elif concrete_tag == "DATA":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "Data"))
                    elif concrete_tag == "TRANSFORMATION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "Transformation"))
                    elif concrete_tag == "DDS-CP-DOMAIN":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DdsCpDomain"))
                    elif concrete_tag == "DDS-CP-PARTITION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DdsCpPartition"))
                    elif concrete_tag == "DDS-CP-QOS-PROFILE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DdsCpQosProfile"))
                    elif concrete_tag == "DDS-CP-TOPIC":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DdsCpTopic"))
                    elif concrete_tag == "DEPENDENCY-ON-ARTIFACT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DependencyOnArtifact"))
                    elif concrete_tag == "DIAG-EVENT-DEBOUNCE-ALGORITHM":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DiagEventDebounceAlgorithm"))
                    elif concrete_tag == "DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE-EVALUATION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DiagnosticAuthTransmitCertificateEvaluation"))
                    elif concrete_tag == "DIAGNOSTIC-CONNECTED-INDICATOR":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DiagnosticConnectedIndicator"))
                    elif concrete_tag == "DIAGNOSTIC-DATA-ELEMENT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DiagnosticDataElement"))
                    elif concrete_tag == "DIAGNOSTIC-DEBOUNCE-ALGORITHM-PROPS":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DiagnosticDebounceAlgorithmProps"))
                    elif concrete_tag == "DIAGNOSTIC-FUNCTION-INHIBIT-SOURCE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DiagnosticFunctionInhibitSource"))
                    elif concrete_tag == "DIAGNOSTIC-PARAMETER-ELEMENT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DiagnosticParameterElement"))
                    elif concrete_tag == "DIAGNOSTIC-ROUTINE-SUBFUNCTION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DiagnosticRoutineSubfunction"))
                    elif concrete_tag == "DLT-APPLICATION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DltApplication"))
                    elif concrete_tag == "DLT-ARGUMENT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DltArgument"))
                    elif concrete_tag == "DLT-LOG-CHANNEL":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DltLogChannel"))
                    elif concrete_tag == "DLT-MESSAGE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DltMessage"))
                    elif concrete_tag == "DO-IP-INTERFACE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DoIpInterface"))
                    elif concrete_tag == "DO-IP-LOGIC-ADDRESS":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DoIpLogicAddress"))
                    elif concrete_tag == "DO-IP-ROUTING-ACTIVATION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DoIpRoutingActivation"))
                    elif concrete_tag == "E-C-U-MAPPING":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ECUMapping"))
                    elif concrete_tag == "E-O-C-EXECUTABLE-ENTITY-REF-ABSTRACT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EOCExecutableEntityRefAbstract"))
                    elif concrete_tag == "ECU-PARTITION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EcuPartition"))
                    elif concrete_tag == "ECUC-CONTAINER-VALUE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EcucContainerValue"))
                    elif concrete_tag == "ECUC-DEFINITION-ELEMENT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EcucDefinitionElement"))
                    elif concrete_tag == "ECUC-DESTINATION-URI-DEF":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EcucDestinationUriDef"))
                    elif concrete_tag == "ECUC-ENUMERATION-LITERAL-DEF":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EcucEnumerationLiteralDef"))
                    elif concrete_tag == "ECUC-QUERY":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EcucQuery"))
                    elif concrete_tag == "ECUC-VALIDATION-CONDITION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EcucValidationCondition"))
                    elif concrete_tag == "END-TO-END-PROTECTION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EndToEndProtection"))
                    elif concrete_tag == "ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EthernetWakeupSleepOnDatalineConfig"))
                    elif concrete_tag == "EVENT-HANDLER":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EventHandler"))
                    elif concrete_tag == "EXCLUSIVE-AREA":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ExclusiveArea"))
                    elif concrete_tag == "EXECUTABLE-ENTITY":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ExecutableEntity"))
                    elif concrete_tag == "EXECUTION-TIME":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ExecutionTime"))
                    elif concrete_tag == "F-M-ATTRIBUTE-DEF":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FMAttributeDef"))
                    elif concrete_tag == "F-M-FEATURE-MAP-ASSERTION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FMFeatureMapAssertion"))
                    elif concrete_tag == "F-M-FEATURE-MAP-CONDITION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FMFeatureMapCondition"))
                    elif concrete_tag == "F-M-FEATURE-MAP-ELEMENT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FMFeatureMapElement"))
                    elif concrete_tag == "F-M-FEATURE-RELATION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FMFeatureRelation"))
                    elif concrete_tag == "F-M-FEATURE-RESTRICTION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FMFeatureRestriction"))
                    elif concrete_tag == "F-M-FEATURE-SELECTION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FMFeatureSelection"))
                    elif concrete_tag == "FLAT-INSTANCE-DESCRIPTOR":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FlatInstanceDescriptor"))
                    elif concrete_tag == "FLEXRAY-AR-TP-NODE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FlexrayArTpNode"))
                    elif concrete_tag == "FLEXRAY-TP-CONNECTION-CONTROL":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FlexrayTpConnectionControl"))
                    elif concrete_tag == "FLEXRAY-TP-NODE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FlexrayTpNode"))
                    elif concrete_tag == "FLEXRAY-TP-PDU-POOL":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FlexrayTpPduPool"))
                    elif concrete_tag == "FRAME-TRIGGERING":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FrameTriggering"))
                    elif concrete_tag == "GENERAL-PARAMETER":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "GeneralParameter"))
                    elif concrete_tag == "GLOBAL-TIME-GATEWAY":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "GlobalTimeGateway"))
                    elif concrete_tag == "GLOBAL-TIME-MASTER":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "GlobalTimeMaster"))
                    elif concrete_tag == "GLOBAL-TIME-SLAVE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "GlobalTimeSlave"))
                    elif concrete_tag == "HEAP-USAGE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "HeapUsage"))
                    elif concrete_tag == "HW-ATTRIBUTE-DEF":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "HwAttributeDef"))
                    elif concrete_tag == "HW-ATTRIBUTE-LITERAL-DEF":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "HwAttributeLiteralDef"))
                    elif concrete_tag == "HW-PIN":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "HwPin"))
                    elif concrete_tag == "HW-PIN-GROUP":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "HwPinGroup"))
                    elif concrete_tag == "I-E-E-E1722-TP-ACF-BUS":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "IEEE1722TpAcfBus"))
                    elif concrete_tag == "I-E-E-E1722-TP-ACF-BUS-PART":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "IEEE1722TpAcfBusPart"))
                    elif concrete_tag == "I-P-SEC-RULE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "IPSecRule"))
                    elif concrete_tag == "I-PV6-EXT-HEADER-FILTER-LIST":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "IPv6ExtHeaderFilterList"))
                    elif concrete_tag == "I-SIGNAL-TO-I-PDU-MAPPING":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ISignalToIPduMapping"))
                    elif concrete_tag == "I-SIGNAL-TRIGGERING":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ISignalTriggering"))
                    elif concrete_tag == "IDENT-CAPTION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "IdentCaption"))
                    elif concrete_tag == "IMPOSITION-TIME":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ImpositionTime"))
                    elif concrete_tag == "INTERNAL-TRIGGERING-POINT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "InternalTriggeringPoint"))
                    elif concrete_tag == "J1939-SHARED-ADDRESS-CLUSTER":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "J1939SharedAddressCluster"))
                    elif concrete_tag == "J1939-TP-NODE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "J1939TpNode"))
                    elif concrete_tag == "KEYWORD":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "Keyword"))
                    elif concrete_tag == "LIFE-CYCLE-STATE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "LifeCycleState"))
                    elif concrete_tag == "LIN-SCHEDULE-TABLE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "LinScheduleTable"))
                    elif concrete_tag == "LIN-TP-NODE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "LinTpNode"))
                    elif concrete_tag == "LINKER":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "Linker"))
                    elif concrete_tag == "MAC-MULTICAST-GROUP":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "MacMulticastGroup"))
                    elif concrete_tag == "MAC-SEC-KAY-PARTICIPANT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "MacSecKayParticipant"))
                    elif concrete_tag == "MC-DATA-INSTANCE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "McDataInstance"))
                    elif concrete_tag == "MEMORY-SECTION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "MemorySection"))
                    elif concrete_tag == "MODE-DECLARATION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ModeDeclaration"))
                    elif concrete_tag == "MODE-DECLARATION-MAPPING":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ModeDeclarationMapping"))
                    elif concrete_tag == "MODE-SWITCH-POINT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ModeSwitchPoint"))
                    elif concrete_tag == "NETWORK-ENDPOINT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "NetworkEndpoint"))
                    elif concrete_tag == "NM-CLUSTER":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "NmCluster"))
                    elif concrete_tag == "NM-ECU":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "NmEcu"))
                    elif concrete_tag == "NM-NODE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "NmNode"))
                    elif concrete_tag == "NV-BLOCK-DESCRIPTOR":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "NvBlockDescriptor"))
                    elif concrete_tag == "PACKAGEABLE-ELEMENT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "PackageableElement"))
                    elif concrete_tag == "PARAMETER-ACCESS":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ParameterAccess"))
                    elif concrete_tag == "PDU-ACTIVATION-ROUTING-GROUP":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "PduActivationRoutingGroup"))
                    elif concrete_tag == "PDU-TO-FRAME-MAPPING":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "PduToFrameMapping"))
                    elif concrete_tag == "PDU-TRIGGERING":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "PduTriggering"))
                    elif concrete_tag == "PER-INSTANCE-MEMORY":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "PerInstanceMemory"))
                    elif concrete_tag == "PHYSICAL-CHANNEL":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "PhysicalChannel"))
                    elif concrete_tag == "PORT-ELEMENT-TO-COMMUNICATION-RESOURCE-MAPPING":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "PortElementToCommunicationResourceMapping"))
                    elif concrete_tag == "PORT-GROUP":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "PortGroup"))
                    elif concrete_tag == "PORT-INTERFACE-MAPPING":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "PortInterfaceMapping"))
                    elif concrete_tag == "POSSIBLE-ERROR-REACTION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "PossibleErrorReaction"))
                    elif concrete_tag == "RESOURCE-CONSUMPTION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ResourceConsumption"))
                    elif concrete_tag == "ROOT-SW-COMPOSITION-PROTOTYPE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "RootSwCompositionPrototype"))
                    elif concrete_tag == "RPT-COMPONENT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "RptComponent"))
                    elif concrete_tag == "RPT-CONTAINER":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "RptContainer"))
                    elif concrete_tag == "RPT-EXECUTABLE-ENTITY":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "RptExecutableEntity"))
                    elif concrete_tag == "RPT-EXECUTABLE-ENTITY-EVENT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "RptExecutableEntityEvent"))
                    elif concrete_tag == "RPT-EXECUTION-CONTEXT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "RptExecutionContext"))
                    elif concrete_tag == "RPT-PROFILE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "RptProfile"))
                    elif concrete_tag == "RPT-SERVICE-POINT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "RptServicePoint"))
                    elif concrete_tag == "RTE-EVENT-IN-COMPOSITION-SEPARATION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "RteEventInCompositionSeparation"))
                    elif concrete_tag == "RTE-EVENT-IN-COMPOSITION-TO-OS-TASK-PROXY-MAPPING":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "RteEventInCompositionToOsTaskProxyMapping"))
                    elif concrete_tag == "RTE-EVENT-IN-SYSTEM-SEPARATION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "RteEventInSystemSeparation"))
                    elif concrete_tag == "RTE-EVENT-IN-SYSTEM-TO-OS-TASK-PROXY-MAPPING":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "RteEventInSystemToOsTaskProxyMapping"))
                    elif concrete_tag == "RUNNABLE-ENTITY-GROUP":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "RunnableEntityGroup"))
                    elif concrete_tag == "SDG-ATTRIBUTE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SdgAttribute"))
                    elif concrete_tag == "SDG-CLASS":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SdgClass"))
                    elif concrete_tag == "SECURE-COMMUNICATION-AUTHENTICATION-PROPS":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SecureCommunicationAuthenticationProps"))
                    elif concrete_tag == "SECURE-COMMUNICATION-FRESHNESS-PROPS":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SecureCommunicationFreshnessProps"))
                    elif concrete_tag == "SECURITY-EVENT-CONTEXT-PROPS":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SecurityEventContextProps"))
                    elif concrete_tag == "SERVER-CALL-POINT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ServerCallPoint"))
                    elif concrete_tag == "SERVICE-NEEDS":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ServiceNeeds"))
                    elif concrete_tag == "SIGNAL-SERVICE-TRANSLATION-ELEMENT-PROPS":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SignalServiceTranslationElementProps"))
                    elif concrete_tag == "SIGNAL-SERVICE-TRANSLATION-EVENT-PROPS":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SignalServiceTranslationEventProps"))
                    elif concrete_tag == "SIGNAL-SERVICE-TRANSLATION-PROPS":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SignalServiceTranslationProps"))
                    elif concrete_tag == "SOCKET-ADDRESS":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SocketAddress"))
                    elif concrete_tag == "SOMEIP-TP-CHANNEL":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SomeipTpChannel"))
                    elif concrete_tag == "SPEC-ELEMENT-REFERENCE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SpecElementReference"))
                    elif concrete_tag == "STACK-USAGE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "StackUsage"))
                    elif concrete_tag == "STATIC-SOCKET-CONNECTION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "StaticSocketConnection"))
                    elif concrete_tag == "STRUCTURED-REQ":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "StructuredReq"))
                    elif concrete_tag == "SW-GENERIC-AXIS-PARAM-TYPE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwGenericAxisParamType"))
                    elif concrete_tag == "SW-SERVICE-ARG":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwServiceArg"))
                    elif concrete_tag == "SWC-SERVICE-DEPENDENCY":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwcServiceDependency"))
                    elif concrete_tag == "SWC-TO-APPLICATION-PARTITION-MAPPING":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwcToApplicationPartitionMapping"))
                    elif concrete_tag == "SWC-TO-ECU-MAPPING":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwcToEcuMapping"))
                    elif concrete_tag == "SWC-TO-IMPL-MAPPING":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwcToImplMapping"))
                    elif concrete_tag == "SWITCH-ASYNCHRONOUS-TRAFFIC-SHAPER-GROUP-ENTRY":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwitchAsynchronousTrafficShaperGroupEntry"))
                    elif concrete_tag == "SWITCH-FLOW-METERING-ENTRY":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwitchFlowMeteringEntry"))
                    elif concrete_tag == "SWITCH-STREAM-FILTER-ACTION-DEST-PORT-MODIFICATION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwitchStreamFilterActionDestPortModification"))
                    elif concrete_tag == "SWITCH-STREAM-FILTER-ENTRY":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwitchStreamFilterEntry"))
                    elif concrete_tag == "SWITCH-STREAM-FILTER-RULE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwitchStreamFilterRule"))
                    elif concrete_tag == "SWITCH-STREAM-GATE-ENTRY":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwitchStreamGateEntry"))
                    elif concrete_tag == "SWITCH-STREAM-IDENTIFICATION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwitchStreamIdentification"))
                    elif concrete_tag == "SYSTEM-MAPPING":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SystemMapping"))
                    elif concrete_tag == "SYSTEM-SIGNAL-GROUP-TO-COMMUNICATION-RESOURCE-MAPPING":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SystemSignalGroupToCommunicationResourceMapping"))
                    elif concrete_tag == "SYSTEM-SIGNAL-TO-COMMUNICATION-RESOURCE-MAPPING":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SystemSignalToCommunicationResourceMapping"))
                    elif concrete_tag == "T-D-CP-SOFTWARE-CLUSTER-MAPPING":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TDCpSoftwareClusterMapping"))
                    elif concrete_tag == "T-D-CP-SOFTWARE-CLUSTER-RESOURCE-MAPPING":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TDCpSoftwareClusterResourceMapping"))
                    elif concrete_tag == "TCP-OPTION-FILTER-LIST":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TcpOptionFilterList"))
                    elif concrete_tag == "TIMING-CLOCK":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TimingClock"))
                    elif concrete_tag == "TIMING-CLOCK-SYNC-ACCURACY":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TimingClockSyncAccuracy"))
                    elif concrete_tag == "TIMING-CONDITION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TimingCondition"))
                    elif concrete_tag == "TIMING-CONSTRAINT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TimingConstraint"))
                    elif concrete_tag == "TIMING-DESCRIPTION":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TimingDescription"))
                    elif concrete_tag == "TIMING-EXTENSION-RESOURCE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TimingExtensionResource"))
                    elif concrete_tag == "TIMING-MODE-INSTANCE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TimingModeInstance"))
                    elif concrete_tag == "TLS-CRYPTO-CIPHER-SUITE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TlsCryptoCipherSuite"))
                    elif concrete_tag == "TLS-CRYPTO-CIPHER-SUITE-PROPS":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TlsCryptoCipherSuiteProps"))
                    elif concrete_tag == "TOPIC1":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "Topic1"))
                    elif concrete_tag == "TP-ADDRESS":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TpAddress"))
                    elif concrete_tag == "TRACEABLE-TABLE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TraceableTable"))
                    elif concrete_tag == "TRACEABLE-TEXT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TraceableText"))
                    elif concrete_tag == "TRACED-FAILURE":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TracedFailure"))
                    elif concrete_tag == "TRANSFORMATION-PROPS":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TransformationProps"))
                    elif concrete_tag == "TRANSFORMATION-TECHNOLOGY":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TransformationTechnology"))
                    elif concrete_tag == "TRIGGER":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "Trigger"))
                    elif concrete_tag == "VARIABLE-ACCESS":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "VariableAccess"))
                    elif concrete_tag == "VARIATION-POINT-PROXY":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "VariationPointProxy"))
                    elif concrete_tag == "VIEW-MAP":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ViewMap"))
                    elif concrete_tag == "VLAN-CONFIG":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "VlanConfig"))
                    elif concrete_tag == "WAIT-POINT":
                        obj.source_element_refs.append(SerializationHelper.deserialize_by_tag(child[0], "WaitPoint"))
            elif tag == "SOURCE-INSTANCES":
                obj._source_instance_irefs.append(ARRef.deserialize(child))

        return obj



class CollectionBuilder(ARElementBuilder):
    """Builder for Collection with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Collection = Collection()


    def with_auto_collect(self, value: Optional[AutoCollectEnum]) -> "CollectionBuilder":
        """Set auto_collect attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.auto_collect = value
        return self

    def with_collected_instances(self, items: list[AnyInstanceRef]) -> "CollectionBuilder":
        """Set collected_instances list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.collected_instances = list(items) if items else []
        return self

    def with_collection_semantics(self, value: Optional[NameToken]) -> "CollectionBuilder":
        """Set collection_semantics attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.collection_semantics = value
        return self

    def with_element_role(self, value: Optional[Identifier]) -> "CollectionBuilder":
        """Set element_role attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.element_role = value
        return self

    def with_elements(self, items: list[Identifiable]) -> "CollectionBuilder":
        """Set elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.elements = list(items) if items else []
        return self

    def with_source_elements(self, items: list[Identifiable]) -> "CollectionBuilder":
        """Set source_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.source_elements = list(items) if items else []
        return self

    def with_source_instances(self, items: list[AnyInstanceRef]) -> "CollectionBuilder":
        """Set source_instances list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.source_instances = list(items) if items else []
        return self


    def add_collected_instance(self, item: AnyInstanceRef) -> "CollectionBuilder":
        """Add a single item to collected_instances list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.collected_instances.append(item)
        return self

    def clear_collected_instances(self) -> "CollectionBuilder":
        """Clear all items from collected_instances list.

        Returns:
            self for method chaining
        """
        self._obj.collected_instances = []
        return self

    def add_element(self, item: Identifiable) -> "CollectionBuilder":
        """Add a single item to elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.elements.append(item)
        return self

    def clear_elements(self) -> "CollectionBuilder":
        """Clear all items from elements list.

        Returns:
            self for method chaining
        """
        self._obj.elements = []
        return self

    def add_source_element(self, item: Identifiable) -> "CollectionBuilder":
        """Add a single item to source_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.source_elements.append(item)
        return self

    def clear_source_elements(self) -> "CollectionBuilder":
        """Clear all items from source_elements list.

        Returns:
            self for method chaining
        """
        self._obj.source_elements = []
        return self

    def add_source_instance(self, item: AnyInstanceRef) -> "CollectionBuilder":
        """Add a single item to source_instances list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.source_instances.append(item)
        return self

    def clear_source_instances(self) -> "CollectionBuilder":
        """Clear all items from source_instances list.

        Returns:
            self for method chaining
        """
        self._obj.source_instances = []
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


    def build(self) -> Collection:
        """Build and return the Collection instance with validation."""
        self._validate_instance()
        pass
        return self._obj