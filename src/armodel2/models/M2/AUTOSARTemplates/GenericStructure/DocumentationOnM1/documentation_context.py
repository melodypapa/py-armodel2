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
        "FEATURE": ("_POLYMORPHIC", "feature", ["ApplicationArrayElement", "ApplicationRecordElement", "ArgumentDataPrototype", "AssemblySwConnector", "AsynchronousServerCallPoint", "AsynchronousServerCallResultPoint", "AsynchronousServerCallReturnsEvent", "AtpPrototype", "AtpStructureElement", "BackgroundEvent", "BswInternalBehavior", "BswModuleDescription", "BswServiceDependencyIdent", "BulkNvDataDescriptor", "ClientServerOperation", "DataPrototypeGroup", "DataReceiveErrorEvent", "DataReceivedEvent", "DataSendCompletedEvent", "DataWriteCompletedEvent", "DelegationSwConnector", "DiagnosticParameterIdent", "ExternalTriggerOccurredEvent", "ExternalTriggeringPointIdent", "ImplementationDataTypeElement", "InitEvent", "InternalTriggerOccurredEvent", "InternalTriggeringPoint", "ModeAccessPointIdent", "ModeDeclaration", "ModeDeclarationGroupPrototype", "ModeDeclarationMapping", "ModeSwitchPoint", "ModeSwitchedAckEvent", "ModeTransition", "NvBlockDescriptor", "OperationInvokedEvent", "OsTaskExecutionEvent", "PPortPrototype", "PRPortPrototype", "ParameterAccess", "ParameterDataPrototype", "PassThroughSwConnector", "PerInstanceMemory", "PortGroup", "PortPrototypeBlueprint", "RPortPrototype", "RootSwCompositionPrototype", "RunnableEntity", "RunnableEntityGroup", "SwcBswMapping", "SwcInternalBehavior", "SwcModeManagerErrorEvent", "SwcModeSwitchEvent", "SwcServiceDependency", "SynchronousServerCallPoint", "System", "TimingEvent", "TransformerHardErrorEvent", "Trigger", "VariableAccess", "VariableDataPrototype"]),
        "IDENTIFIABLE-REF": ("_POLYMORPHIC", "identifiable_ref", ["ARPackage", "AbstractDoIpLogicAddressProps", "AbstractEvent", "AbstractImplementationDataTypeElement", "AbstractSecurityEventFilter", "AbstractSecurityIdsmInstanceFilter", "AbstractServiceInstance", "AclObjectSet", "AclOperation", "AclPermission", "AclRole", "AgeConstraint", "AggregationTailoring", "AliasNameSet", "AnalyzedExecutionTime", "AppOsTaskProxyToEcuTaskProxyMapping", "ApplicationArrayDataType", "ApplicationArrayElement", "ApplicationEndpoint", "ApplicationError", "ApplicationPartition", "ApplicationPartitionToEcuPartitionMapping", "ApplicationPrimitiveDataType", "ApplicationRecordDataType", "ApplicationRecordElement", "ApplicationSwComponentType", "AppliedStandard", "ArbitraryEventTriggering", "ArgumentDataPrototype", "AssemblySwConnector", "AsynchronousServerCallPoint", "AsynchronousServerCallResultPoint", "AsynchronousServerCallReturnsEvent", "AtpBlueprint", "AtpBlueprintable", "AtpClassifier", "AtpFeature", "AutosarOperationArgumentInstance", "AutosarVariableInstance", "BackgroundEvent", "BinaryManifestAddressableObject", "BinaryManifestItem", "BinaryManifestItemDefinition", "BinaryManifestMetaDataField", "BinaryManifestProvideResource", "BinaryManifestRequireResource", "BinaryManifestResource", "BinaryManifestResourceDefinition", "BlockState", "BlueprintMappingSet", "BswAsynchronousServerCallReturnsEvent", "BswBackgroundEvent", "BswCalledEntity", "BswCompositionTiming", "BswDataReceivedEvent", "BswEntryRelationshipSet", "BswExternalTriggerOccurredEvent", "BswImplementation", "BswInternalBehavior", "BswInternalTriggerOccurredEvent", "BswInternalTriggeringPoint", "BswInterruptEntity", "BswInterruptEvent", "BswMgrNeeds", "BswModeManagerErrorEvent", "BswModeSwitchEvent", "BswModeSwitchedAckEvent", "BswModuleDependency", "BswModuleDescription", "BswModuleEntry", "BswModuleTiming", "BswOperationInvokedEvent", "BswOsTaskExecutionEvent", "BswSchedulableEntity", "BswServiceDependencyIdent", "BswTimingEvent", "BuildAction", "BuildActionEntity", "BuildActionEnvironment", "BuildActionManifest", "BulkNvDataDescriptor", "BurstPatternEventTriggering", "BusMirrorChannelMappingCan", "BusMirrorChannelMappingFlexray", "BusMirrorChannelMappingIp", "CalibrationParameterValueSet", "CanCluster", "CanCommunicationConnector", "CanCommunicationController", "CanFrame", "CanFrameTriggering", "CanNmCluster", "CanNmNode", "CanPhysicalChannel", "CanTpAddress", "CanTpChannel", "CanTpConfig", "CanTpNode", "Chapter", "ClassContentConditional", "ClientIdDefinition", "ClientIdDefinitionSet", "ClientServerInterface", "ClientServerInterfaceMapping", "ClientServerInterfaceToBswModuleEntryBlueprintMapping", "ClientServerOperation", "Code", "CollectableElement", "Collection", "ComManagementMapping", "ComMgrUserNeeds", "CommConnectorPort", "CommunicationConnector", "CommunicationController", "Compiler", "ComplexDeviceDriverSwComponentType", "CompositionSwComponentType", "CompuMethod", "ConcreteClassTailoring", "ConcretePatternEventTriggering", "ConsistencyNeeds", "ConsistencyNeedsBlueprintSet", "ConstantSpecification", "ConstantSpecificationMappingSet", "ConstraintTailoring", "ConsumedEventGroup", "ConsumedProvidedServiceInstanceGroup", "ConsumedServiceInstance", "ContainerIPdu", "CouplingElement", "CouplingElementAbstractDetails", "CouplingElementSwitchDetails", "CouplingPort", "CouplingPortAbstractShaper", "CouplingPortFifo", "CouplingPortScheduler", "CouplingPortShaper", "CouplingPortStructuralElement", "CpSoftwareCluster", "CpSoftwareClusterBinaryManifestDescriptor", "CpSoftwareClusterCommunicationResource", "CpSoftwareClusterMappingSet", "CpSoftwareClusterResource", "CpSoftwareClusterResourcePool", "CpSoftwareClusterResourceToApplicationPartitionMapping", "CpSoftwareClusterServiceResource", "CpSoftwareClusterToApplicationPartitionMapping", "CpSoftwareClusterToEcuInstanceMapping", "CpSoftwareClusterToResourceMapping", "CpSwClusterResourceToDiagDataElemMapping", "CpSwClusterResourceToDiagFunctionIdMapping", "CpSwClusterToDiagEventMapping", "CpSwClusterToDiagRoutineSubfunctionMapping", "CryptoEllipticCurveProps", "CryptoKeyManagementNeeds", "CryptoServiceCertificate", "CryptoServiceJobNeeds", "CryptoServiceKey", "CryptoServiceMapping", "CryptoServiceNeeds", "CryptoServicePrimitive", "CryptoServiceQueue", "CryptoSignatureScheme", "Data", "DataConstr", "DataExchangePoint", "DataPrototypeGroup", "DataReceiveErrorEvent", "DataReceivedEvent", "DataSendCompletedEvent", "DataTransformationSet", "DataTypeMappingSet", "DataWriteCompletedEvent", "DcmIPdu", "DdsCpConfig", "DdsCpConsumedServiceInstance", "DdsCpDomain", "DdsCpPartition", "DdsCpProvidedServiceInstance", "DdsCpQosProfile", "DdsCpTopic", "DelegationSwConnector", "DependencyOnArtifact", "DevelopmentError", "DiagEventDebounceAlgorithm", "DiagEventDebounceCounterBased", "DiagEventDebounceMonitorInternal", "DiagnosticAccessPermission", "DiagnosticAging", "DiagnosticAuthRole", "DiagnosticAuthTransmitCertificate", "DiagnosticAuthTransmitCertificateEvaluation", "DiagnosticAuthTransmitCertificateMapping", "DiagnosticAuthenticationClass", "DiagnosticAuthenticationConfiguration", "DiagnosticClearDiagnosticInformation", "DiagnosticClearDiagnosticInformationClass", "DiagnosticClearResetEmissionRelatedInfo", "DiagnosticClearResetEmissionRelatedInfoClass", "DiagnosticComControl", "DiagnosticComControlClass", "DiagnosticCommunicationManagerNeeds", "DiagnosticComponentNeeds", "DiagnosticConnectedIndicator", "DiagnosticConnection", "DiagnosticContributionSet", "DiagnosticControlDTCSetting", "DiagnosticControlDTCSettingClass", "DiagnosticControlNeeds", "DiagnosticCustomServiceClass", "DiagnosticCustomServiceInstance", "DiagnosticDataElement", "DiagnosticDataIdentifier", "DiagnosticDataIdentifierSet", "DiagnosticDataTransfer", "DiagnosticDataTransferClass", "DiagnosticDeAuthentication", "DiagnosticDebounceAlgorithmProps", "DiagnosticDemProvidedDataMapping", "DiagnosticDynamicDataIdentifier", "DiagnosticDynamicallyDefineDataIdentifier", "DiagnosticDynamicallyDefineDataIdentifierClass", "DiagnosticEcuInstanceProps", "DiagnosticEcuReset", "DiagnosticEcuResetClass", "DiagnosticEnableCondition", "DiagnosticEnableConditionGroup", "DiagnosticEnableConditionNeeds", "DiagnosticEnableConditionPortMapping", "DiagnosticEnvironmentalCondition", "DiagnosticEvent", "DiagnosticEventInfoNeeds", "DiagnosticEventManagerNeeds", "DiagnosticEventNeeds", "DiagnosticEventPortMapping", "DiagnosticEventToDebounceAlgorithmMapping", "DiagnosticEventToEnableConditionGroupMapping", "DiagnosticEventToOperationCycleMapping", "DiagnosticEventToSecurityEventMapping", "DiagnosticEventToStorageConditionGroupMapping", "DiagnosticEventToTroubleCodeJ1939Mapping", "DiagnosticEventToTroubleCodeUdsMapping", "DiagnosticExtendedDataRecord", "DiagnosticFimAliasEvent", "DiagnosticFimAliasEventGroup", "DiagnosticFimAliasEventGroupMapping", "DiagnosticFimAliasEventMapping", "DiagnosticFimEventGroup", "DiagnosticFimFunctionMapping", "DiagnosticFreezeFrame", "DiagnosticFunctionIdentifier", "DiagnosticFunctionIdentifierInhibit", "DiagnosticFunctionInhibitSource", "DiagnosticIOControl", "DiagnosticIndicator", "DiagnosticInfoType", "DiagnosticInhibitSourceEventMapping", "DiagnosticIoControlClass", "DiagnosticIoControlNeeds", "DiagnosticIumpr", "DiagnosticIumprDenominatorGroup", "DiagnosticIumprGroup", "DiagnosticIumprToFunctionIdentifierMapping", "DiagnosticJ1939ExpandedFreezeFrame", "DiagnosticJ1939FreezeFrame", "DiagnosticJ1939Node", "DiagnosticJ1939Spn", "DiagnosticJ1939SpnMapping", "DiagnosticJ1939SwMapping", "DiagnosticMasterToSlaveEventMapping", "DiagnosticMeasurementIdentifier", "DiagnosticMemoryDestinationPrimary", "DiagnosticMemoryDestinationUserDefined", "DiagnosticMemoryIdentifier", "DiagnosticOperationCycle", "DiagnosticOperationCycleNeeds", "DiagnosticOperationCyclePortMapping", "DiagnosticParameterElement", "DiagnosticParameterIdent", "DiagnosticParameterIdentifier", "DiagnosticPowertrainFreezeFrame", "DiagnosticProofOfOwnership", "DiagnosticProtocol", "DiagnosticReadDTCInformation", "DiagnosticReadDTCInformationClass", "DiagnosticReadDataByIdentifier", "DiagnosticReadDataByIdentifierClass", "DiagnosticReadDataByPeriodicID", "DiagnosticReadDataByPeriodicIDClass", "DiagnosticReadMemoryByAddress", "DiagnosticReadMemoryByAddressClass", "DiagnosticReadScalingDataByIdentifier", "DiagnosticReadScalingDataByIdentifierClass", "DiagnosticRequestControlOfOnBoardDevice", "DiagnosticRequestControlOfOnBoardDeviceClass", "DiagnosticRequestCurrentPowertrainData", "DiagnosticRequestCurrentPowertrainDataClass", "DiagnosticRequestDownload", "DiagnosticRequestDownloadClass", "DiagnosticRequestEmissionRelatedDTC", "DiagnosticRequestEmissionRelatedDTCClass", "DiagnosticRequestEmissionRelatedDTCPermanentStatus", "DiagnosticRequestEmissionRelatedDTCPermanentStatusClass", "DiagnosticRequestFileTransfer", "DiagnosticRequestFileTransferClass", "DiagnosticRequestFileTransferNeeds", "DiagnosticRequestOnBoardMonitoringTestResults", "DiagnosticRequestOnBoardMonitoringTestResultsClass", "DiagnosticRequestPowertrainFreezeFrameData", "DiagnosticRequestPowertrainFreezeFrameDataClass", "DiagnosticRequestRoutineResults", "DiagnosticRequestUpload", "DiagnosticRequestUploadClass", "DiagnosticRequestVehicleInfo", "DiagnosticRequestVehicleInfoClass", "DiagnosticResponseOnEvent", "DiagnosticResponseOnEventClass", "DiagnosticRoutine", "DiagnosticRoutineControl", "DiagnosticRoutineControlClass", "DiagnosticRoutineNeeds", "DiagnosticRoutineSubfunction", "DiagnosticSecureCodingMapping", "DiagnosticSecurityAccess", "DiagnosticSecurityAccessClass", "DiagnosticSecurityEventReportingModeMapping", "DiagnosticSecurityLevel", "DiagnosticServiceDataMapping", "DiagnosticServiceSwMapping", "DiagnosticServiceTable", "DiagnosticSession", "DiagnosticSessionControl", "DiagnosticSessionControlClass", "DiagnosticStartRoutine", "DiagnosticStopRoutine", "DiagnosticStorageCondition", "DiagnosticStorageConditionGroup", "DiagnosticStorageConditionNeeds", "DiagnosticStorageConditionPortMapping", "DiagnosticTestResult", "DiagnosticTestRoutineIdentifier", "DiagnosticTransferExit", "DiagnosticTransferExitClass", "DiagnosticTroubleCodeGroup", "DiagnosticTroubleCodeJ1939", "DiagnosticTroubleCodeObd", "DiagnosticTroubleCodeProps", "DiagnosticTroubleCodeUds", "DiagnosticTroubleCodeUdsToTroubleCodeObdMapping", "DiagnosticUploadDownloadNeeds", "DiagnosticValueNeeds", "DiagnosticVerifyCertificateBidirectional", "DiagnosticWriteDataByIdentifierClass", "DiagnosticWriteMemoryByAddressClass", "DiagnosticsCommunicationSecurityNeeds", "DltApplication", "DltArgument", "DltContext", "DltEcu", "DltLogChannel", "DltMessage", "DltUserNeeds", "DoIpActivationLineNeeds", "DoIpGidNeeds", "DoIpGidSynchronizationNeeds", "DoIpInterface", "DoIpLogicAddress", "DoIpLogicTargetAddressProps", "DoIpLogicTesterAddressProps", "DoIpPowerModeStatusNeeds", "DoIpRoutingActivation", "DoIpRoutingActivationAuthenticationNeeds", "DoIpRoutingActivationConfirmationNeeds", "DoIpTpConfig", "DocumentElementScope", "Documentation", "DtcStatusChangeNotificationNeeds", "E2EProfileCompatibilityProps", "ECUMapping", "EOCEventRef", "EOCExecutableEntityRef", "EOCExecutableEntityRefAbstract", "EOCExecutableEntityRefGroup", "EcuAbstractionSwComponentType", "EcuInstance", "EcuPartition", "EcuStateMgrUserNeeds", "EcuTiming", "EcucAddInfoParamDef", "EcucBooleanParamDef", "EcucChoiceContainerDef", "EcucChoiceReferenceDef", "EcucContainerValue", "EcucDefinitionCollection", "EcucDefinitionElement", "EcucDestinationUriDef", "EcucDestinationUriDefSet", "EcucEnumerationLiteralDef", "EcucEnumerationParamDef", "EcucFloatParamDef", "EcucForeignReferenceDef", "EcucFunctionNameDef", "EcucInstanceReferenceDef", "EcucIntegerParamDef", "EcucLinkerSymbolDef", "EcucModuleConfigurationValues", "EcucModuleDef", "EcucMultilineStringParamDef", "EcucParamConfContainerDef", "EcucQuery", "EcucReferenceDef", "EcucStringParamDef", "EcucUriReferenceDef", "EcucValidationCondition", "EcucValueCollection", "EndToEndProtection", "EndToEndProtectionSet", "EnumerationMappingTable", "ErrorTracerNeeds", "EthIpProps", "EthTcpIpIcmpProps", "EthTcpIpProps", "EthTpConfig", "EthernetCluster", "EthernetCommunicationConnector", "EthernetCommunicationController", "EthernetFrameTriggering", "EthernetPhysicalChannel", "EthernetWakeupSleepOnDatalineConfig", "EthernetWakeupSleepOnDatalineConfigSet", "EvaluatedVariantSet", "EventHandler", "ExclusiveArea", "ExecutableEntity", "ExecutionOrderConstraint", "ExecutionTime", "ExecutionTimeConstraint", "ExternalTriggerOccurredEvent", "ExternalTriggeringPointIdent", "FMAttributeDef", "FMFeature", "FMFeatureMap", "FMFeatureMapAssertion", "FMFeatureMapCondition", "FMFeatureMapElement", "FMFeatureModel", "FMFeatureRelation", "FMFeatureRestriction", "FMFeatureSelection", "FMFeatureSelectionSet", "FirewallRule", "FlatInstanceDescriptor", "FlatMap", "FlexrayArTpConfig", "FlexrayArTpNode", "FlexrayCluster", "FlexrayCommunicationConnector", "FlexrayCommunicationController", "FlexrayFrame", "FlexrayFrameTriggering", "FlexrayNmCluster", "FlexrayNmNode", "FlexrayPhysicalChannel", "FlexrayTpConfig", "FlexrayTpConnectionControl", "FlexrayTpNode", "FlexrayTpPduPool", "FramePort", "FrameTriggering", "FunctionInhibitionAvailabilityNeeds", "FunctionInhibitionNeeds", "Gateway", "GeneralParameter", "GeneralPurposeConnection", "GeneralPurposeIPdu", "GeneralPurposePdu", "GenericEthernetFrame", "GlobalSupervisionNeeds", "GlobalTimeCanMaster", "GlobalTimeCanSlave", "GlobalTimeDomain", "GlobalTimeEthMaster", "GlobalTimeEthSlave", "GlobalTimeFrMaster", "GlobalTimeFrSlave", "GlobalTimeGateway", "GlobalTimeMaster", "GlobalTimeSlave", "HardwareTestNeeds", "HeapUsage", "HwAttributeDef", "HwAttributeLiteralDef", "HwCategory", "HwElement", "HwPin", "HwPinGroup", "HwType", "IEEE1722TpAafConnection", "IEEE1722TpAcfBus", "IEEE1722TpAcfBusPart", "IEEE1722TpAcfCan", "IEEE1722TpAcfCanPart", "IEEE1722TpAcfConnection", "IEEE1722TpAcfLin", "IEEE1722TpAcfLinPart", "IEEE1722TpConfig", "IEEE1722TpCrfConnection", "IEEE1722TpIidcConnection", "IPSecConfigProps", "IPSecRule", "IPduPort", "IPv6ExtHeaderFilterList", "IPv6ExtHeaderFilterSet", "ISignal", "ISignalGroup", "ISignalIPdu", "ISignalIPduGroup", "ISignalPort", "ISignalToIPduMapping", "ISignalTriggering", "IdentCaption", "IdsDesign", "IdsMgrCustomTimestampNeeds", "IdsMgrNeeds", "IdsmInstance", "IdsmProperties", "Ieee1722TpEthernetFrame", "ImplementationDataType", "ImplementationDataTypeElement", "ImpositionTime", "IndicatorStatusNeeds", "InitEvent", "InternalTriggerOccurredEvent", "InternalTriggeringPoint", "InterpolationRoutineMappingSet", "J1939Cluster", "J1939ControllerApplication", "J1939DcmDm19Support", "J1939DcmIPdu", "J1939NmCluster", "J1939NmNode", "J1939RmIncomingRequestServiceNeeds", "J1939RmOutgoingRequestServiceNeeds", "J1939SharedAddressCluster", "J1939TpConfig", "J1939TpNode", "Keyword", "KeywordSet", "LatencyTimingConstraint", "LifeCycleInfoSet", "LifeCycleState", "LifeCycleStateDefinitionGroup", "LinCluster", "LinCommunicationConnector", "LinEventTriggeredFrame", "LinFrameTriggering", "LinMaster", "LinPhysicalChannel", "LinScheduleTable", "LinSlave", "LinSporadicFrame", "LinTpConfig", "LinTpNode", "LinUnconditionalFrame", "Linker", "LogAndTraceMessageCollectionSet", "MacMulticastGroup", "MacSecGlobalKayProps", "MacSecKayParticipant", "MacSecParticipantSet", "McDataInstance", "McFunction", "McGroup", "MeasuredExecutionTime", "MeasuredHeapUsage", "MeasuredStackUsage", "MemorySection", "ModeAccessPointIdent", "ModeDeclaration", "ModeDeclarationGroup", "ModeDeclarationGroupPrototype", "ModeDeclarationMapping", "ModeDeclarationMappingSet", "ModeInterfaceMapping", "ModeSwitchInterface", "ModeSwitchPoint", "ModeSwitchedAckEvent", "ModeTransition", "MultiplexedIPdu", "NPdu", "NetworkEndpoint", "NmCluster", "NmConfig", "NmEcu", "NmNode", "NmPdu", "NvBlockDescriptor", "NvBlockNeeds", "NvBlockSwComponentType", "NvDataInterface", "ObdControlServiceNeeds", "ObdInfoServiceNeeds", "ObdMonitorServiceNeeds", "ObdPidServiceNeeds", "ObdRatioDenominatorNeeds", "ObdRatioServiceNeeds", "OffsetTimingConstraint", "OperationInvokedEvent", "OsTaskExecutionEvent", "OsTaskProxy", "PPortPrototype", "PRPortPrototype", "PackageableElement", "ParameterAccess", "ParameterDataPrototype", "ParameterInterface", "ParameterSwComponentType", "PassThroughSwConnector", "PduActivationRoutingGroup", "PduToFrameMapping", "PduTriggering", "PdurIPduGroup", "PerInstanceMemory", "PeriodicEventTriggering", "PhysicalChannel", "PhysicalDimension", "PhysicalDimensionMappingSet", "PortElementToCommunicationResourceMapping", "PortGroup", "PortInterfaceMapping", "PortInterfaceMappingSet", "PortPrototypeBlueprint", "PossibleErrorReaction", "PostBuildVariantCriterion", "PostBuildVariantCriterionValueSet", "PredefinedVariant", "PrimitiveAttributeTailoring", "ProvidedServiceInstance", "RPortPrototype", "RapidPrototypingScenario", "ReferenceTailoring", "ResourceConsumption", "RootSwCompositionPrototype", "RoughEstimateHeapUsage", "RoughEstimateOfExecutionTime", "RoughEstimateStackUsage", "RptComponent", "RptContainer", "RptExecutableEntity", "RptExecutableEntityEvent", "RptExecutionContext", "RptProfile", "RptServicePoint", "RteEventInCompositionSeparation", "RteEventInCompositionToOsTaskProxyMapping", "RteEventInSystemSeparation", "RteEventInSystemToOsTaskProxyMapping", "RunnableEntity", "RunnableEntityGroup", "RuntimeError", "SOMEIPTransformationProps", "Sdg", "SdgAggregationWithVariation", "SdgAttribute", "SdgClass", "SdgDef", "SdgForeignReference", "SdgForeignReferenceWithVariation", "SdgPrimitiveAttribute", "SdgPrimitiveAttributeWithVariation", "SdgTailoring", "SecOcCryptoServiceMapping", "SecureCommunicationAuthenticationProps", "SecureCommunicationFreshnessProps", "SecureCommunicationPropsSet", "SecureOnBoardCommunicationNeeds", "SecuredIPdu", "SecurityEventAggregationFilter", "SecurityEventContextMappingApplication", "SecurityEventContextMappingBswModule", "SecurityEventContextMappingCommConnector", "SecurityEventContextMappingFunctionalCluster", "SecurityEventContextProps", "SecurityEventDefinition", "SecurityEventFilterChain", "SecurityEventOneEveryNFilter", "SecurityEventStateFilter", "SenderReceiverInterface", "SensorActuatorSwComponentType", "ServerCallPoint", "ServiceInstanceCollectionSet", "ServiceNeeds", "ServiceProxySwComponentType", "ServiceSwComponentType", "SignalServiceTranslationElementProps", "SignalServiceTranslationEventProps", "SignalServiceTranslationProps", "SignalServiceTranslationPropsSet", "SoAdRoutingGroup", "SocketAddress", "SocketConnectionIpduIdentifierSet", "SomeipSdClientServiceInstanceConfig", "SomeipSdServerEventGroupTimingConfig", "SomeipSdServerServiceInstanceConfig", "SomeipTpChannel", "SomeipTpConfig", "SpecElementReference", "SpecificationDocumentScope", "SporadicEventTriggering", "StackUsage", "StaticSocketConnection", "StructuredReq", "SupervisedEntityCheckpointNeeds", "SupervisedEntityNeeds", "SwAddrMethod", "SwAxisType", "SwBaseType", "SwGenericAxisParamType", "SwRecordLayout", "SwServiceArg", "SwSystemconst", "SwSystemconstantValueSet", "SwcBswMapping", "SwcImplementation", "SwcInternalBehavior", "SwcModeManagerErrorEvent", "SwcModeSwitchEvent", "SwcServiceDependency", "SwcTiming", "SwcToApplicationPartitionMapping", "SwcToEcuMapping", "SwcToImplMapping", "SwitchAsynchronousTrafficShaperGroupEntry", "SwitchFlowMeteringEntry", "SwitchStreamFilterActionDestPortModification", "SwitchStreamFilterEntry", "SwitchStreamFilterRule", "SwitchStreamGateEntry", "SwitchStreamIdentification", "SyncTimeBaseMgrUserNeeds", "SynchronizationPointConstraint", "SynchronousServerCallPoint", "System", "SystemMapping", "SystemSignal", "SystemSignalGroup", "SystemSignalGroupToCommunicationResourceMapping", "SystemSignalToCommunicationResourceMapping", "SystemTiming", "TDCpSoftwareClusterMapping", "TDCpSoftwareClusterMappingSet", "TDCpSoftwareClusterResourceMapping", "TDEventBswInternalBehavior", "TDEventBswModeDeclaration", "TDEventBswModule", "TDEventComplex", "TDEventFrClusterCycleStart", "TDEventFrame", "TDEventFrameEthernet", "TDEventIPdu", "TDEventISignal", "TDEventModeDeclaration", "TDEventOperation", "TDEventSLLETPort", "TDEventSwcInternalBehavior", "TDEventSwcInternalBehaviorReference", "TDEventTTCanCycleStart", "TDEventTrigger", "TDEventVariableDataPrototype", "TDEventVfbReference", "TDLETZoneClock", "TcpOptionFilterList", "TcpOptionFilterSet", "TimingClock", "TimingClockSyncAccuracy", "TimingCondition", "TimingConstraint", "TimingDescription", "TimingDescriptionEventChain", "TimingEvent", "TimingExtensionResource", "TimingModeInstance", "TlsCryptoCipherSuite", "TlsCryptoCipherSuiteProps", "TlsCryptoServiceMapping", "TlvDataIdDefinitionSet", "Topic1", "TpAddress", "TraceableTable", "TraceableText", "TracedFailure", "Transformation", "TransformationProps", "TransformationPropsSet", "TransformationTechnology", "TransformerHardErrorEvent", "TransientFault", "Trigger", "TriggerInterface", "TriggerInterfaceMapping", "TtcanCluster", "TtcanCommunicationConnector", "TtcanCommunicationController", "TtcanPhysicalChannel", "UdpNmCluster", "UdpNmNode", "Unit", "UnitGroup", "UserDefinedCluster", "UserDefinedCommunicationConnector", "UserDefinedCommunicationController", "UserDefinedEthernetFrame", "UserDefinedGlobalTimeMaster", "UserDefinedGlobalTimeSlave", "UserDefinedIPdu", "UserDefinedPdu", "UserDefinedTransformationProps", "V2xDataManagerNeeds", "V2xFacUserNeeds", "V2xMUserNeeds", "VariableAccess", "VariableDataPrototype", "VariationPointProxy", "VendorSpecificServiceNeeds", "VfbTiming", "ViewMap", "ViewMapSet", "VlanConfig", "WaitPoint", "WorstCaseHeapUsage", "WorstCaseStackUsage"]),
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
                    if concrete_tag == "APPLICATION-ARRAY-ELEMENT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "ApplicationArrayElement"))
                    elif concrete_tag == "APPLICATION-RECORD-ELEMENT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "ApplicationRecordElement"))
                    elif concrete_tag == "ARGUMENT-DATA-PROTOTYPE":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "ArgumentDataPrototype"))
                    elif concrete_tag == "ASSEMBLY-SW-CONNECTOR":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "AssemblySwConnector"))
                    elif concrete_tag == "ASYNCHRONOUS-SERVER-CALL-POINT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "AsynchronousServerCallPoint"))
                    elif concrete_tag == "ASYNCHRONOUS-SERVER-CALL-RESULT-POINT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "AsynchronousServerCallResultPoint"))
                    elif concrete_tag == "ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "AsynchronousServerCallReturnsEvent"))
                    elif concrete_tag == "ATP-PROTOTYPE":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "AtpPrototype"))
                    elif concrete_tag == "ATP-STRUCTURE-ELEMENT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "AtpStructureElement"))
                    elif concrete_tag == "BACKGROUND-EVENT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "BackgroundEvent"))
                    elif concrete_tag == "BSW-INTERNAL-BEHAVIOR":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "BswInternalBehavior"))
                    elif concrete_tag == "BSW-MODULE-DESCRIPTION":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "BswModuleDescription"))
                    elif concrete_tag == "BSW-SERVICE-DEPENDENCY-IDENT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "BswServiceDependencyIdent"))
                    elif concrete_tag == "BULK-NV-DATA-DESCRIPTOR":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "BulkNvDataDescriptor"))
                    elif concrete_tag == "CLIENT-SERVER-OPERATION":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "ClientServerOperation"))
                    elif concrete_tag == "DATA-PROTOTYPE-GROUP":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "DataPrototypeGroup"))
                    elif concrete_tag == "DATA-RECEIVE-ERROR-EVENT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "DataReceiveErrorEvent"))
                    elif concrete_tag == "DATA-RECEIVED-EVENT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "DataReceivedEvent"))
                    elif concrete_tag == "DATA-SEND-COMPLETED-EVENT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "DataSendCompletedEvent"))
                    elif concrete_tag == "DATA-WRITE-COMPLETED-EVENT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "DataWriteCompletedEvent"))
                    elif concrete_tag == "DELEGATION-SW-CONNECTOR":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "DelegationSwConnector"))
                    elif concrete_tag == "DIAGNOSTIC-PARAMETER-IDENT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticParameterIdent"))
                    elif concrete_tag == "EXTERNAL-TRIGGER-OCCURRED-EVENT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "ExternalTriggerOccurredEvent"))
                    elif concrete_tag == "EXTERNAL-TRIGGERING-POINT-IDENT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "ExternalTriggeringPointIdent"))
                    elif concrete_tag == "IMPLEMENTATION-DATA-TYPE-ELEMENT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "ImplementationDataTypeElement"))
                    elif concrete_tag == "INIT-EVENT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "InitEvent"))
                    elif concrete_tag == "INTERNAL-TRIGGER-OCCURRED-EVENT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "InternalTriggerOccurredEvent"))
                    elif concrete_tag == "INTERNAL-TRIGGERING-POINT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "InternalTriggeringPoint"))
                    elif concrete_tag == "MODE-ACCESS-POINT-IDENT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "ModeAccessPointIdent"))
                    elif concrete_tag == "MODE-DECLARATION":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "ModeDeclaration"))
                    elif concrete_tag == "MODE-DECLARATION-GROUP-PROTOTYPE":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "ModeDeclarationGroupPrototype"))
                    elif concrete_tag == "MODE-DECLARATION-MAPPING":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "ModeDeclarationMapping"))
                    elif concrete_tag == "MODE-SWITCH-POINT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "ModeSwitchPoint"))
                    elif concrete_tag == "MODE-SWITCHED-ACK-EVENT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "ModeSwitchedAckEvent"))
                    elif concrete_tag == "MODE-TRANSITION":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "ModeTransition"))
                    elif concrete_tag == "NV-BLOCK-DESCRIPTOR":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "NvBlockDescriptor"))
                    elif concrete_tag == "OPERATION-INVOKED-EVENT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "OperationInvokedEvent"))
                    elif concrete_tag == "OS-TASK-EXECUTION-EVENT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "OsTaskExecutionEvent"))
                    elif concrete_tag == "P-PORT-PROTOTYPE":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "PPortPrototype"))
                    elif concrete_tag == "P-R-PORT-PROTOTYPE":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "PRPortPrototype"))
                    elif concrete_tag == "PARAMETER-ACCESS":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "ParameterAccess"))
                    elif concrete_tag == "PARAMETER-DATA-PROTOTYPE":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "ParameterDataPrototype"))
                    elif concrete_tag == "PASS-THROUGH-SW-CONNECTOR":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "PassThroughSwConnector"))
                    elif concrete_tag == "PER-INSTANCE-MEMORY":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "PerInstanceMemory"))
                    elif concrete_tag == "PORT-GROUP":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "PortGroup"))
                    elif concrete_tag == "PORT-PROTOTYPE-BLUEPRINT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "PortPrototypeBlueprint"))
                    elif concrete_tag == "R-PORT-PROTOTYPE":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "RPortPrototype"))
                    elif concrete_tag == "ROOT-SW-COMPOSITION-PROTOTYPE":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "RootSwCompositionPrototype"))
                    elif concrete_tag == "RUNNABLE-ENTITY":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "RunnableEntity"))
                    elif concrete_tag == "RUNNABLE-ENTITY-GROUP":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "RunnableEntityGroup"))
                    elif concrete_tag == "SWC-BSW-MAPPING":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "SwcBswMapping"))
                    elif concrete_tag == "SWC-INTERNAL-BEHAVIOR":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "SwcInternalBehavior"))
                    elif concrete_tag == "SWC-MODE-MANAGER-ERROR-EVENT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "SwcModeManagerErrorEvent"))
                    elif concrete_tag == "SWC-MODE-SWITCH-EVENT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "SwcModeSwitchEvent"))
                    elif concrete_tag == "SWC-SERVICE-DEPENDENCY":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "SwcServiceDependency"))
                    elif concrete_tag == "SYNCHRONOUS-SERVER-CALL-POINT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "SynchronousServerCallPoint"))
                    elif concrete_tag == "SYSTEM":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "System"))
                    elif concrete_tag == "TIMING-EVENT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "TimingEvent"))
                    elif concrete_tag == "TRANSFORMER-HARD-ERROR-EVENT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "TransformerHardErrorEvent"))
                    elif concrete_tag == "TRIGGER":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "Trigger"))
                    elif concrete_tag == "VARIABLE-ACCESS":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "VariableAccess"))
                    elif concrete_tag == "VARIABLE-DATA-PROTOTYPE":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "VariableDataPrototype"))
            elif tag == "IDENTIFIABLE-REF":
                setattr(obj, "identifiable_ref", ARRef.deserialize(child))

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