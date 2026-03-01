"""DocumentationContext AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 327)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_DocumentationOnM1.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.multilanguage_referrable import (
    MultilanguageReferrable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.multilanguage_referrable import MultilanguageReferrableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DocumentationContext(MultilanguageReferrable):
    """AUTOSAR DocumentationContext."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DOCUMENTATION-CONTEXT"


    feature: Optional[AtpFeature]
    identifiable_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "FEATURE": ("_POLYMORPHIC", "feature", ["AtpPrototype", "AtpStructureElement"]),
        "IDENTIFIABLE-REF": ("_POLYMORPHIC", "identifiable_ref", ["ARPackage", "AbstractDoIpLogicAddressProps", "AbstractEvent", "AbstractImplementationDataTypeElement", "AbstractSecurityEventFilter", "AbstractSecurityIdsmInstanceFilter", "AbstractServiceInstance", "AppOsTaskProxyToEcuTaskProxyMapping", "ApplicationEndpoint", "ApplicationError", "ApplicationPartitionToEcuPartitionMapping", "AppliedStandard", "AsynchronousServerCallResultPoint", "AtpBlueprint", "AtpBlueprintable", "AtpClassifier", "AtpFeature", "AutosarOperationArgumentInstance", "AutosarVariableInstance", "BinaryManifestAddressableObject", "BinaryManifestItemDefinition", "BinaryManifestResource", "BinaryManifestResourceDefinition", "BlockState", "BswInternalTriggeringPoint", "BswModuleDependency", "BuildActionEntity", "BuildActionEnvironment", "CanTpAddress", "CanTpChannel", "CanTpNode", "Chapter", "ClassContentConditional", "ClientIdDefinition", "ClientServerOperation", "Code", "CollectableElement", "ComManagementMapping", "CommConnectorPort", "CommunicationConnector", "CommunicationController", "Compiler", "ConsistencyNeeds", "ConsumedEventGroup", "CouplingElementAbstractDetails", "CouplingPort", "CouplingPortAbstractShaper", "CouplingPortStructuralElement", "CpSoftwareClusterResource", "CpSoftwareClusterResourceToApplicationPartitionMapping", "CpSoftwareClusterToApplicationPartitionMapping", "CpSoftwareClusterToEcuInstanceMapping", "CpSoftwareClusterToResourceMapping", "CryptoServiceMapping", "DataPrototypeGroup", "Data", "Transformation", "DdsCpDomain", "DdsCpPartition", "DdsCpQosProfile", "DdsCpTopic", "DependencyOnArtifact", "DiagEventDebounceAlgorithm", "DiagnosticAuthTransmitCertificateEvaluation", "DiagnosticConnectedIndicator", "DiagnosticDataElement", "DiagnosticDebounceAlgorithmProps", "DiagnosticFunctionInhibitSource", "DiagnosticParameterElement", "DiagnosticRoutineSubfunction", "DltApplication", "DltArgument", "DltLogChannel", "DltMessage", "DoIpInterface", "DoIpLogicAddress", "DoIpRoutingActivation", "ECUMapping", "EOCExecutableEntityRefAbstract", "EcuPartition", "EcucContainerValue", "EcucDefinitionElement", "EcucDestinationUriDef", "EcucEnumerationLiteralDef", "EcucQuery", "EcucValidationCondition", "EndToEndProtection", "EthernetWakeupSleepOnDatalineConfig", "EventHandler", "ExclusiveArea", "ExecutableEntity", "ExecutionTime", "FMAttributeDef", "FMFeatureMapAssertion", "FMFeatureMapCondition", "FMFeatureMapElement", "FMFeatureRelation", "FMFeatureRestriction", "FMFeatureSelection", "FlatInstanceDescriptor", "FlexrayArTpNode", "FlexrayTpConnectionControl", "FlexrayTpNode", "FlexrayTpPduPool", "FrameTriggering", "GeneralParameter", "GlobalTimeGateway", "GlobalTimeMaster", "GlobalTimeSlave", "HeapUsage", "HwAttributeDef", "HwAttributeLiteralDef", "HwPin", "HwPinGroup", "IEEE1722TpAcfBus", "IEEE1722TpAcfBusPart", "IPSecRule", "IPv6ExtHeaderFilterList", "ISignalToIPduMapping", "ISignalTriggering", "IdentCaption", "ImpositionTime", "InternalTriggeringPoint", "J1939SharedAddressCluster", "J1939TpNode", "Keyword", "LifeCycleState", "LinScheduleTable", "LinTpNode", "Linker", "MacMulticastGroup", "MacSecKayParticipant", "McDataInstance", "MemorySection", "ModeDeclaration", "ModeDeclarationMapping", "ModeSwitchPoint", "NetworkEndpoint", "NmCluster", "NmEcu", "NmNode", "NvBlockDescriptor", "PackageableElement", "ParameterAccess", "PduActivationRoutingGroup", "PduToFrameMapping", "PduTriggering", "PerInstanceMemory", "PhysicalChannel", "PortElementToCommunicationResourceMapping", "PortGroup", "PortInterfaceMapping", "PossibleErrorReaction", "ResourceConsumption", "RootSwCompositionPrototype", "RptComponent", "RptContainer", "RptExecutableEntity", "RptExecutableEntityEvent", "RptExecutionContext", "RptProfile", "RptServicePoint", "RteEventInCompositionSeparation", "RteEventInCompositionToOsTaskProxyMapping", "RteEventInSystemSeparation", "RteEventInSystemToOsTaskProxyMapping", "RunnableEntityGroup", "SdgAttribute", "SdgClass", "SecureCommunicationAuthenticationProps", "SecureCommunicationFreshnessProps", "SecurityEventContextProps", "ServerCallPoint", "ServiceNeeds", "SignalServiceTranslationElementProps", "SignalServiceTranslationEventProps", "SignalServiceTranslationProps", "SocketAddress", "SomeipTpChannel", "SpecElementReference", "StackUsage", "StaticSocketConnection", "StructuredReq", "SwGenericAxisParamType", "SwServiceArg", "SwcServiceDependency", "SwcToApplicationPartitionMapping", "SwcToEcuMapping", "SwcToImplMapping", "SwitchAsynchronousTrafficShaperGroupEntry", "SwitchFlowMeteringEntry", "SwitchStreamFilterActionDestPortModification", "SwitchStreamFilterEntry", "SwitchStreamFilterRule", "SwitchStreamGateEntry", "SwitchStreamIdentification", "SystemMapping", "SystemSignalGroupToCommunicationResourceMapping", "SystemSignalToCommunicationResourceMapping", "TDCpSoftwareClusterMapping", "TDCpSoftwareClusterResourceMapping", "TcpOptionFilterList", "TimingClock", "TimingClockSyncAccuracy", "TimingCondition", "TimingConstraint", "TimingDescription", "TimingExtensionResource", "TimingModeInstance", "TlsCryptoCipherSuite", "TlsCryptoCipherSuiteProps", "Topic1", "TpAddress", "TraceableTable", "TraceableText", "TracedFailure", "TransformationProps", "TransformationTechnology", "Trigger", "VariableAccess", "VariationPointProxy", "ViewMap", "VlanConfig", "WaitPoint"]),
    }


    def __init__(self) -> None:
        """Initialize DocumentationContext."""
        super().__init__()
        self.feature: Optional[AtpFeature] = None
        self.identifiable_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DocumentationContext to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DocumentationContext, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize feature
        if self.feature is not None:
            serialized = SerializationHelper.serialize_item(self.feature, "AtpFeature")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FEATURE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize identifiable_ref
        if self.identifiable_ref is not None:
            serialized = SerializationHelper.serialize_item(self.identifiable_ref, "Identifiable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDENTIFIABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DocumentationContext":
        """Deserialize XML element to DocumentationContext object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DocumentationContext object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DocumentationContext, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "FEATURE":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ATP-PROTOTYPE":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "AtpPrototype"))
                    elif concrete_tag == "ATP-STRUCTURE-ELEMENT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "AtpStructureElement"))
            elif tag == "IDENTIFIABLE-REF":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "AR-PACKAGE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "ARPackage"))
                    elif concrete_tag == "ABSTRACT-DO-IP-LOGIC-ADDRESS-PROPS":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "AbstractDoIpLogicAddressProps"))
                    elif concrete_tag == "ABSTRACT-EVENT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "AbstractEvent"))
                    elif concrete_tag == "ABSTRACT-IMPLEMENTATION-DATA-TYPE-ELEMENT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "AbstractImplementationDataTypeElement"))
                    elif concrete_tag == "ABSTRACT-SECURITY-EVENT-FILTER":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "AbstractSecurityEventFilter"))
                    elif concrete_tag == "ABSTRACT-SECURITY-IDSM-INSTANCE-FILTER":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "AbstractSecurityIdsmInstanceFilter"))
                    elif concrete_tag == "ABSTRACT-SERVICE-INSTANCE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "AbstractServiceInstance"))
                    elif concrete_tag == "APP-OS-TASK-PROXY-TO-ECU-TASK-PROXY-MAPPING":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "AppOsTaskProxyToEcuTaskProxyMapping"))
                    elif concrete_tag == "APPLICATION-ENDPOINT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "ApplicationEndpoint"))
                    elif concrete_tag == "APPLICATION-ERROR":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "ApplicationError"))
                    elif concrete_tag == "APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPING":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "ApplicationPartitionToEcuPartitionMapping"))
                    elif concrete_tag == "APPLIED-STANDARD":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "AppliedStandard"))
                    elif concrete_tag == "ASYNCHRONOUS-SERVER-CALL-RESULT-POINT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "AsynchronousServerCallResultPoint"))
                    elif concrete_tag == "ATP-BLUEPRINT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "AtpBlueprint"))
                    elif concrete_tag == "ATP-BLUEPRINTABLE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "AtpBlueprintable"))
                    elif concrete_tag == "ATP-CLASSIFIER":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "AtpClassifier"))
                    elif concrete_tag == "ATP-FEATURE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "AtpFeature"))
                    elif concrete_tag == "AUTOSAR-OPERATION-ARGUMENT-INSTANCE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "AutosarOperationArgumentInstance"))
                    elif concrete_tag == "AUTOSAR-VARIABLE-INSTANCE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "AutosarVariableInstance"))
                    elif concrete_tag == "BINARY-MANIFEST-ADDRESSABLE-OBJECT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "BinaryManifestAddressableObject"))
                    elif concrete_tag == "BINARY-MANIFEST-ITEM-DEFINITION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "BinaryManifestItemDefinition"))
                    elif concrete_tag == "BINARY-MANIFEST-RESOURCE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "BinaryManifestResource"))
                    elif concrete_tag == "BINARY-MANIFEST-RESOURCE-DEFINITION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "BinaryManifestResourceDefinition"))
                    elif concrete_tag == "BLOCK-STATE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "BlockState"))
                    elif concrete_tag == "BSW-INTERNAL-TRIGGERING-POINT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "BswInternalTriggeringPoint"))
                    elif concrete_tag == "BSW-MODULE-DEPENDENCY":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "BswModuleDependency"))
                    elif concrete_tag == "BUILD-ACTION-ENTITY":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "BuildActionEntity"))
                    elif concrete_tag == "BUILD-ACTION-ENVIRONMENT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "BuildActionEnvironment"))
                    elif concrete_tag == "CAN-TP-ADDRESS":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "CanTpAddress"))
                    elif concrete_tag == "CAN-TP-CHANNEL":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "CanTpChannel"))
                    elif concrete_tag == "CAN-TP-NODE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "CanTpNode"))
                    elif concrete_tag == "CHAPTER":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "Chapter"))
                    elif concrete_tag == "CLASS-CONTENT-CONDITIONAL":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "ClassContentConditional"))
                    elif concrete_tag == "CLIENT-ID-DEFINITION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "ClientIdDefinition"))
                    elif concrete_tag == "CLIENT-SERVER-OPERATION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "ClientServerOperation"))
                    elif concrete_tag == "CODE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "Code"))
                    elif concrete_tag == "COLLECTABLE-ELEMENT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "CollectableElement"))
                    elif concrete_tag == "COM-MANAGEMENT-MAPPING":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "ComManagementMapping"))
                    elif concrete_tag == "COMM-CONNECTOR-PORT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "CommConnectorPort"))
                    elif concrete_tag == "COMMUNICATION-CONNECTOR":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "CommunicationConnector"))
                    elif concrete_tag == "COMMUNICATION-CONTROLLER":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "CommunicationController"))
                    elif concrete_tag == "COMPILER":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "Compiler"))
                    elif concrete_tag == "CONSISTENCY-NEEDS":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "ConsistencyNeeds"))
                    elif concrete_tag == "CONSUMED-EVENT-GROUP":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "ConsumedEventGroup"))
                    elif concrete_tag == "COUPLING-ELEMENT-ABSTRACT-DETAILS":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "CouplingElementAbstractDetails"))
                    elif concrete_tag == "COUPLING-PORT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "CouplingPort"))
                    elif concrete_tag == "COUPLING-PORT-ABSTRACT-SHAPER":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "CouplingPortAbstractShaper"))
                    elif concrete_tag == "COUPLING-PORT-STRUCTURAL-ELEMENT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "CouplingPortStructuralElement"))
                    elif concrete_tag == "CP-SOFTWARE-CLUSTER-RESOURCE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "CpSoftwareClusterResource"))
                    elif concrete_tag == "CP-SOFTWARE-CLUSTER-RESOURCE-TO-APPLICATION-PARTITION-MAPPING":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "CpSoftwareClusterResourceToApplicationPartitionMapping"))
                    elif concrete_tag == "CP-SOFTWARE-CLUSTER-TO-APPLICATION-PARTITION-MAPPING":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "CpSoftwareClusterToApplicationPartitionMapping"))
                    elif concrete_tag == "CP-SOFTWARE-CLUSTER-TO-ECU-INSTANCE-MAPPING":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "CpSoftwareClusterToEcuInstanceMapping"))
                    elif concrete_tag == "CP-SOFTWARE-CLUSTER-TO-RESOURCE-MAPPING":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "CpSoftwareClusterToResourceMapping"))
                    elif concrete_tag == "CRYPTO-SERVICE-MAPPING":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "CryptoServiceMapping"))
                    elif concrete_tag == "DATA-PROTOTYPE-GROUP":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "DataPrototypeGroup"))
                    elif concrete_tag == "DATA":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "Data"))
                    elif concrete_tag == "TRANSFORMATION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "Transformation"))
                    elif concrete_tag == "DDS-CP-DOMAIN":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "DdsCpDomain"))
                    elif concrete_tag == "DDS-CP-PARTITION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "DdsCpPartition"))
                    elif concrete_tag == "DDS-CP-QOS-PROFILE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "DdsCpQosProfile"))
                    elif concrete_tag == "DDS-CP-TOPIC":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "DdsCpTopic"))
                    elif concrete_tag == "DEPENDENCY-ON-ARTIFACT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "DependencyOnArtifact"))
                    elif concrete_tag == "DIAG-EVENT-DEBOUNCE-ALGORITHM":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagEventDebounceAlgorithm"))
                    elif concrete_tag == "DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE-EVALUATION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticAuthTransmitCertificateEvaluation"))
                    elif concrete_tag == "DIAGNOSTIC-CONNECTED-INDICATOR":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticConnectedIndicator"))
                    elif concrete_tag == "DIAGNOSTIC-DATA-ELEMENT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticDataElement"))
                    elif concrete_tag == "DIAGNOSTIC-DEBOUNCE-ALGORITHM-PROPS":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticDebounceAlgorithmProps"))
                    elif concrete_tag == "DIAGNOSTIC-FUNCTION-INHIBIT-SOURCE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticFunctionInhibitSource"))
                    elif concrete_tag == "DIAGNOSTIC-PARAMETER-ELEMENT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticParameterElement"))
                    elif concrete_tag == "DIAGNOSTIC-ROUTINE-SUBFUNCTION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticRoutineSubfunction"))
                    elif concrete_tag == "DLT-APPLICATION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "DltApplication"))
                    elif concrete_tag == "DLT-ARGUMENT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "DltArgument"))
                    elif concrete_tag == "DLT-LOG-CHANNEL":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "DltLogChannel"))
                    elif concrete_tag == "DLT-MESSAGE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "DltMessage"))
                    elif concrete_tag == "DO-IP-INTERFACE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "DoIpInterface"))
                    elif concrete_tag == "DO-IP-LOGIC-ADDRESS":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "DoIpLogicAddress"))
                    elif concrete_tag == "DO-IP-ROUTING-ACTIVATION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "DoIpRoutingActivation"))
                    elif concrete_tag == "E-C-U-MAPPING":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "ECUMapping"))
                    elif concrete_tag == "E-O-C-EXECUTABLE-ENTITY-REF-ABSTRACT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "EOCExecutableEntityRefAbstract"))
                    elif concrete_tag == "ECU-PARTITION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "EcuPartition"))
                    elif concrete_tag == "ECUC-CONTAINER-VALUE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "EcucContainerValue"))
                    elif concrete_tag == "ECUC-DEFINITION-ELEMENT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "EcucDefinitionElement"))
                    elif concrete_tag == "ECUC-DESTINATION-URI-DEF":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "EcucDestinationUriDef"))
                    elif concrete_tag == "ECUC-ENUMERATION-LITERAL-DEF":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "EcucEnumerationLiteralDef"))
                    elif concrete_tag == "ECUC-QUERY":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "EcucQuery"))
                    elif concrete_tag == "ECUC-VALIDATION-CONDITION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "EcucValidationCondition"))
                    elif concrete_tag == "END-TO-END-PROTECTION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "EndToEndProtection"))
                    elif concrete_tag == "ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "EthernetWakeupSleepOnDatalineConfig"))
                    elif concrete_tag == "EVENT-HANDLER":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "EventHandler"))
                    elif concrete_tag == "EXCLUSIVE-AREA":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "ExclusiveArea"))
                    elif concrete_tag == "EXECUTABLE-ENTITY":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "ExecutableEntity"))
                    elif concrete_tag == "EXECUTION-TIME":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "ExecutionTime"))
                    elif concrete_tag == "F-M-ATTRIBUTE-DEF":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "FMAttributeDef"))
                    elif concrete_tag == "F-M-FEATURE-MAP-ASSERTION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "FMFeatureMapAssertion"))
                    elif concrete_tag == "F-M-FEATURE-MAP-CONDITION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "FMFeatureMapCondition"))
                    elif concrete_tag == "F-M-FEATURE-MAP-ELEMENT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "FMFeatureMapElement"))
                    elif concrete_tag == "F-M-FEATURE-RELATION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "FMFeatureRelation"))
                    elif concrete_tag == "F-M-FEATURE-RESTRICTION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "FMFeatureRestriction"))
                    elif concrete_tag == "F-M-FEATURE-SELECTION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "FMFeatureSelection"))
                    elif concrete_tag == "FLAT-INSTANCE-DESCRIPTOR":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "FlatInstanceDescriptor"))
                    elif concrete_tag == "FLEXRAY-AR-TP-NODE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "FlexrayArTpNode"))
                    elif concrete_tag == "FLEXRAY-TP-CONNECTION-CONTROL":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "FlexrayTpConnectionControl"))
                    elif concrete_tag == "FLEXRAY-TP-NODE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "FlexrayTpNode"))
                    elif concrete_tag == "FLEXRAY-TP-PDU-POOL":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "FlexrayTpPduPool"))
                    elif concrete_tag == "FRAME-TRIGGERING":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "FrameTriggering"))
                    elif concrete_tag == "GENERAL-PARAMETER":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "GeneralParameter"))
                    elif concrete_tag == "GLOBAL-TIME-GATEWAY":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "GlobalTimeGateway"))
                    elif concrete_tag == "GLOBAL-TIME-MASTER":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "GlobalTimeMaster"))
                    elif concrete_tag == "GLOBAL-TIME-SLAVE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "GlobalTimeSlave"))
                    elif concrete_tag == "HEAP-USAGE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "HeapUsage"))
                    elif concrete_tag == "HW-ATTRIBUTE-DEF":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "HwAttributeDef"))
                    elif concrete_tag == "HW-ATTRIBUTE-LITERAL-DEF":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "HwAttributeLiteralDef"))
                    elif concrete_tag == "HW-PIN":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "HwPin"))
                    elif concrete_tag == "HW-PIN-GROUP":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "HwPinGroup"))
                    elif concrete_tag == "I-E-E-E1722-TP-ACF-BUS":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "IEEE1722TpAcfBus"))
                    elif concrete_tag == "I-E-E-E1722-TP-ACF-BUS-PART":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "IEEE1722TpAcfBusPart"))
                    elif concrete_tag == "I-P-SEC-RULE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "IPSecRule"))
                    elif concrete_tag == "I-PV6-EXT-HEADER-FILTER-LIST":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "IPv6ExtHeaderFilterList"))
                    elif concrete_tag == "I-SIGNAL-TO-I-PDU-MAPPING":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "ISignalToIPduMapping"))
                    elif concrete_tag == "I-SIGNAL-TRIGGERING":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "ISignalTriggering"))
                    elif concrete_tag == "IDENT-CAPTION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "IdentCaption"))
                    elif concrete_tag == "IMPOSITION-TIME":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "ImpositionTime"))
                    elif concrete_tag == "INTERNAL-TRIGGERING-POINT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "InternalTriggeringPoint"))
                    elif concrete_tag == "J1939-SHARED-ADDRESS-CLUSTER":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "J1939SharedAddressCluster"))
                    elif concrete_tag == "J1939-TP-NODE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "J1939TpNode"))
                    elif concrete_tag == "KEYWORD":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "Keyword"))
                    elif concrete_tag == "LIFE-CYCLE-STATE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "LifeCycleState"))
                    elif concrete_tag == "LIN-SCHEDULE-TABLE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "LinScheduleTable"))
                    elif concrete_tag == "LIN-TP-NODE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "LinTpNode"))
                    elif concrete_tag == "LINKER":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "Linker"))
                    elif concrete_tag == "MAC-MULTICAST-GROUP":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "MacMulticastGroup"))
                    elif concrete_tag == "MAC-SEC-KAY-PARTICIPANT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "MacSecKayParticipant"))
                    elif concrete_tag == "MC-DATA-INSTANCE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "McDataInstance"))
                    elif concrete_tag == "MEMORY-SECTION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "MemorySection"))
                    elif concrete_tag == "MODE-DECLARATION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "ModeDeclaration"))
                    elif concrete_tag == "MODE-DECLARATION-MAPPING":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "ModeDeclarationMapping"))
                    elif concrete_tag == "MODE-SWITCH-POINT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "ModeSwitchPoint"))
                    elif concrete_tag == "NETWORK-ENDPOINT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "NetworkEndpoint"))
                    elif concrete_tag == "NM-CLUSTER":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "NmCluster"))
                    elif concrete_tag == "NM-ECU":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "NmEcu"))
                    elif concrete_tag == "NM-NODE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "NmNode"))
                    elif concrete_tag == "NV-BLOCK-DESCRIPTOR":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "NvBlockDescriptor"))
                    elif concrete_tag == "PACKAGEABLE-ELEMENT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "PackageableElement"))
                    elif concrete_tag == "PARAMETER-ACCESS":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "ParameterAccess"))
                    elif concrete_tag == "PDU-ACTIVATION-ROUTING-GROUP":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "PduActivationRoutingGroup"))
                    elif concrete_tag == "PDU-TO-FRAME-MAPPING":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "PduToFrameMapping"))
                    elif concrete_tag == "PDU-TRIGGERING":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "PduTriggering"))
                    elif concrete_tag == "PER-INSTANCE-MEMORY":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "PerInstanceMemory"))
                    elif concrete_tag == "PHYSICAL-CHANNEL":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "PhysicalChannel"))
                    elif concrete_tag == "PORT-ELEMENT-TO-COMMUNICATION-RESOURCE-MAPPING":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "PortElementToCommunicationResourceMapping"))
                    elif concrete_tag == "PORT-GROUP":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "PortGroup"))
                    elif concrete_tag == "PORT-INTERFACE-MAPPING":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "PortInterfaceMapping"))
                    elif concrete_tag == "POSSIBLE-ERROR-REACTION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "PossibleErrorReaction"))
                    elif concrete_tag == "RESOURCE-CONSUMPTION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "ResourceConsumption"))
                    elif concrete_tag == "ROOT-SW-COMPOSITION-PROTOTYPE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "RootSwCompositionPrototype"))
                    elif concrete_tag == "RPT-COMPONENT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "RptComponent"))
                    elif concrete_tag == "RPT-CONTAINER":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "RptContainer"))
                    elif concrete_tag == "RPT-EXECUTABLE-ENTITY":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "RptExecutableEntity"))
                    elif concrete_tag == "RPT-EXECUTABLE-ENTITY-EVENT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "RptExecutableEntityEvent"))
                    elif concrete_tag == "RPT-EXECUTION-CONTEXT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "RptExecutionContext"))
                    elif concrete_tag == "RPT-PROFILE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "RptProfile"))
                    elif concrete_tag == "RPT-SERVICE-POINT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "RptServicePoint"))
                    elif concrete_tag == "RTE-EVENT-IN-COMPOSITION-SEPARATION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "RteEventInCompositionSeparation"))
                    elif concrete_tag == "RTE-EVENT-IN-COMPOSITION-TO-OS-TASK-PROXY-MAPPING":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "RteEventInCompositionToOsTaskProxyMapping"))
                    elif concrete_tag == "RTE-EVENT-IN-SYSTEM-SEPARATION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "RteEventInSystemSeparation"))
                    elif concrete_tag == "RTE-EVENT-IN-SYSTEM-TO-OS-TASK-PROXY-MAPPING":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "RteEventInSystemToOsTaskProxyMapping"))
                    elif concrete_tag == "RUNNABLE-ENTITY-GROUP":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "RunnableEntityGroup"))
                    elif concrete_tag == "SDG-ATTRIBUTE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "SdgAttribute"))
                    elif concrete_tag == "SDG-CLASS":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "SdgClass"))
                    elif concrete_tag == "SECURE-COMMUNICATION-AUTHENTICATION-PROPS":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "SecureCommunicationAuthenticationProps"))
                    elif concrete_tag == "SECURE-COMMUNICATION-FRESHNESS-PROPS":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "SecureCommunicationFreshnessProps"))
                    elif concrete_tag == "SECURITY-EVENT-CONTEXT-PROPS":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "SecurityEventContextProps"))
                    elif concrete_tag == "SERVER-CALL-POINT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "ServerCallPoint"))
                    elif concrete_tag == "SERVICE-NEEDS":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "ServiceNeeds"))
                    elif concrete_tag == "SIGNAL-SERVICE-TRANSLATION-ELEMENT-PROPS":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "SignalServiceTranslationElementProps"))
                    elif concrete_tag == "SIGNAL-SERVICE-TRANSLATION-EVENT-PROPS":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "SignalServiceTranslationEventProps"))
                    elif concrete_tag == "SIGNAL-SERVICE-TRANSLATION-PROPS":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "SignalServiceTranslationProps"))
                    elif concrete_tag == "SOCKET-ADDRESS":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "SocketAddress"))
                    elif concrete_tag == "SOMEIP-TP-CHANNEL":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "SomeipTpChannel"))
                    elif concrete_tag == "SPEC-ELEMENT-REFERENCE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "SpecElementReference"))
                    elif concrete_tag == "STACK-USAGE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "StackUsage"))
                    elif concrete_tag == "STATIC-SOCKET-CONNECTION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "StaticSocketConnection"))
                    elif concrete_tag == "STRUCTURED-REQ":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "StructuredReq"))
                    elif concrete_tag == "SW-GENERIC-AXIS-PARAM-TYPE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "SwGenericAxisParamType"))
                    elif concrete_tag == "SW-SERVICE-ARG":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "SwServiceArg"))
                    elif concrete_tag == "SWC-SERVICE-DEPENDENCY":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "SwcServiceDependency"))
                    elif concrete_tag == "SWC-TO-APPLICATION-PARTITION-MAPPING":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "SwcToApplicationPartitionMapping"))
                    elif concrete_tag == "SWC-TO-ECU-MAPPING":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "SwcToEcuMapping"))
                    elif concrete_tag == "SWC-TO-IMPL-MAPPING":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "SwcToImplMapping"))
                    elif concrete_tag == "SWITCH-ASYNCHRONOUS-TRAFFIC-SHAPER-GROUP-ENTRY":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "SwitchAsynchronousTrafficShaperGroupEntry"))
                    elif concrete_tag == "SWITCH-FLOW-METERING-ENTRY":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "SwitchFlowMeteringEntry"))
                    elif concrete_tag == "SWITCH-STREAM-FILTER-ACTION-DEST-PORT-MODIFICATION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "SwitchStreamFilterActionDestPortModification"))
                    elif concrete_tag == "SWITCH-STREAM-FILTER-ENTRY":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "SwitchStreamFilterEntry"))
                    elif concrete_tag == "SWITCH-STREAM-FILTER-RULE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "SwitchStreamFilterRule"))
                    elif concrete_tag == "SWITCH-STREAM-GATE-ENTRY":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "SwitchStreamGateEntry"))
                    elif concrete_tag == "SWITCH-STREAM-IDENTIFICATION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "SwitchStreamIdentification"))
                    elif concrete_tag == "SYSTEM-MAPPING":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "SystemMapping"))
                    elif concrete_tag == "SYSTEM-SIGNAL-GROUP-TO-COMMUNICATION-RESOURCE-MAPPING":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "SystemSignalGroupToCommunicationResourceMapping"))
                    elif concrete_tag == "SYSTEM-SIGNAL-TO-COMMUNICATION-RESOURCE-MAPPING":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "SystemSignalToCommunicationResourceMapping"))
                    elif concrete_tag == "T-D-CP-SOFTWARE-CLUSTER-MAPPING":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "TDCpSoftwareClusterMapping"))
                    elif concrete_tag == "T-D-CP-SOFTWARE-CLUSTER-RESOURCE-MAPPING":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "TDCpSoftwareClusterResourceMapping"))
                    elif concrete_tag == "TCP-OPTION-FILTER-LIST":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "TcpOptionFilterList"))
                    elif concrete_tag == "TIMING-CLOCK":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "TimingClock"))
                    elif concrete_tag == "TIMING-CLOCK-SYNC-ACCURACY":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "TimingClockSyncAccuracy"))
                    elif concrete_tag == "TIMING-CONDITION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "TimingCondition"))
                    elif concrete_tag == "TIMING-CONSTRAINT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "TimingConstraint"))
                    elif concrete_tag == "TIMING-DESCRIPTION":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "TimingDescription"))
                    elif concrete_tag == "TIMING-EXTENSION-RESOURCE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "TimingExtensionResource"))
                    elif concrete_tag == "TIMING-MODE-INSTANCE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "TimingModeInstance"))
                    elif concrete_tag == "TLS-CRYPTO-CIPHER-SUITE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "TlsCryptoCipherSuite"))
                    elif concrete_tag == "TLS-CRYPTO-CIPHER-SUITE-PROPS":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "TlsCryptoCipherSuiteProps"))
                    elif concrete_tag == "TOPIC1":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "Topic1"))
                    elif concrete_tag == "TP-ADDRESS":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "TpAddress"))
                    elif concrete_tag == "TRACEABLE-TABLE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "TraceableTable"))
                    elif concrete_tag == "TRACEABLE-TEXT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "TraceableText"))
                    elif concrete_tag == "TRACED-FAILURE":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "TracedFailure"))
                    elif concrete_tag == "TRANSFORMATION-PROPS":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "TransformationProps"))
                    elif concrete_tag == "TRANSFORMATION-TECHNOLOGY":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "TransformationTechnology"))
                    elif concrete_tag == "TRIGGER":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "Trigger"))
                    elif concrete_tag == "VARIABLE-ACCESS":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "VariableAccess"))
                    elif concrete_tag == "VARIATION-POINT-PROXY":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "VariationPointProxy"))
                    elif concrete_tag == "VIEW-MAP":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "ViewMap"))
                    elif concrete_tag == "VLAN-CONFIG":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "VlanConfig"))
                    elif concrete_tag == "WAIT-POINT":
                        setattr(obj, "identifiable_ref", SerializationHelper.deserialize_by_tag(child[0], "WaitPoint"))

        return obj



class DocumentationContextBuilder(MultilanguageReferrableBuilder):
    """Builder for DocumentationContext with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DocumentationContext = DocumentationContext()


    def with_feature(self, value: Optional[AtpFeature]) -> "DocumentationContextBuilder":
        """Set feature attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.feature = value
        return self

    def with_identifiable(self, value: Optional[Identifiable]) -> "DocumentationContextBuilder":
        """Set identifiable attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.identifiable = value
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


    def build(self) -> DocumentationContext:
        """Build and return the DocumentationContext instance with validation."""
        self._validate_instance()
        pass
        return self._obj