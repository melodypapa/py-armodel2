"""LifeCycleInfo AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 392)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 195)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_LifeCycles.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_period import (
    LifeCyclePeriod,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_state import (
    LifeCycleState,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class LifeCycleInfo(ARObject):
    """AUTOSAR LifeCycleInfo."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "LIFE-CYCLE-INFO"


    lc_object_ref: ARRef
    lc_state_ref: Optional[ARRef]
    period_begin: Optional[LifeCyclePeriod]
    period_end: Optional[LifeCyclePeriod]
    remark: Optional[DocumentationBlock]
    use_instead_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "LC-OBJECT-REF": ("_POLYMORPHIC", "lc_object_ref", ["ARPackage", "AclObjectSet", "AclOperation", "AclPermission", "AclRole", "AgeConstraint", "AggregationTailoring", "AliasNameSet", "AnalyzedExecutionTime", "AppOsTaskProxyToEcuTaskProxyMapping", "ApplicationArrayDataType", "ApplicationArrayElement", "ApplicationEndpoint", "ApplicationError", "ApplicationPartition", "ApplicationPartitionToEcuPartitionMapping", "ApplicationPrimitiveDataType", "ApplicationRecordDataType", "ApplicationRecordElement", "ApplicationSwComponentType", "ArbitraryEventTriggering", "ArgumentDataPrototype", "AssemblySwConnector", "AsynchronousServerCallPoint", "AsynchronousServerCallResultPoint", "AsynchronousServerCallReturnsEvent", "AtpDefinition", "AutosarOperationArgumentInstance", "AutosarVariableInstance", "BackgroundEvent", "BinaryManifestItem", "BinaryManifestItemDefinition", "BinaryManifestMetaDataField", "BinaryManifestProvideResource", "BinaryManifestRequireResource", "BinaryManifestResourceDefinition", "BlockState", "BlueprintMappingSet", "BswAsynchronousServerCallPoint", "BswAsynchronousServerCallResultPoint", "BswAsynchronousServerCallReturnsEvent", "BswBackgroundEvent", "BswCalledEntity", "BswCompositionTiming", "BswDataReceivedEvent", "BswDirectCallPoint", "BswDistinguishedPartition", "BswEntryRelationshipSet", "BswExternalTriggerOccurredEvent", "BswImplementation", "BswInternalBehavior", "BswInternalTriggerOccurredEvent", "BswInternalTriggeringPoint", "BswInterruptEntity", "BswInterruptEvent", "BswMgrNeeds", "BswModeManagerErrorEvent", "BswModeSwitchEvent", "BswModeSwitchedAckEvent", "BswModuleCallPoint", "BswModuleClientServerEntry", "BswModuleDependency", "BswModuleDescription", "BswModuleEntry", "BswModuleTiming", "BswOperationInvokedEvent", "BswOsTaskExecutionEvent", "BswSchedulableEntity", "BswSchedulerNamePrefix", "BswServiceDependencyIdent", "BswTimingEvent", "BswVariableAccess", "BuildAction", "BuildActionEnvironment", "BuildActionManifest", "BulkNvDataDescriptor", "BurstPatternEventTriggering", "BusMirrorChannelMappingCan", "BusMirrorChannelMappingFlexray", "BusMirrorChannelMappingIp", "CalibrationParameterValueSet", "CanCluster", "CanCommunicationConnector", "CanCommunicationController", "CanFrame", "CanFrameTriggering", "CanNmCluster", "CanNmNode", "CanPhysicalChannel", "CanTpAddress", "CanTpChannel", "CanTpConfig", "CanTpNode", "Caption", "Chapter", "ClassContentConditional", "ClientIdDefinition", "ClientIdDefinitionSet", "ClientServerInterface", "ClientServerInterfaceMapping", "ClientServerInterfaceToBswModuleEntryBlueprintMapping", "ClientServerOperation", "Code", "Collection", "ComManagementMapping", "ComMgrUserNeeds", "Compiler", "ComplexDeviceDriverSwComponentType", "CompositionSwComponentType", "CompuMethod", "ConcreteClassTailoring", "ConcretePatternEventTriggering", "ConsistencyNeeds", "ConsistencyNeedsBlueprintSet", "ConstantSpecification", "ConstantSpecificationMappingSet", "ConstraintTailoring", "ConsumedEventGroup", "ConsumedProvidedServiceInstanceGroup", "ConsumedServiceInstance", "ContainerIPdu", "CouplingElement", "CouplingElementSwitchDetails", "CouplingPort", "CouplingPortFifo", "CouplingPortScheduler", "CouplingPortShaper", "CouplingPortTrafficClassAssignment", "CpSoftwareCluster", "CpSoftwareClusterBinaryManifestDescriptor", "CpSoftwareClusterCommunicationResource", "CpSoftwareClusterMappingSet", "CpSoftwareClusterResourcePool", "CpSoftwareClusterResourceToApplicationPartitionMapping", "CpSoftwareClusterServiceResource", "CpSoftwareClusterToApplicationPartitionMapping", "CpSoftwareClusterToEcuInstanceMapping", "CpSoftwareClusterToResourceMapping", "CpSwClusterResourceToDiagDataElemMapping", "CpSwClusterResourceToDiagFunctionIdMapping", "CpSwClusterToDiagEventMapping", "CpSwClusterToDiagRoutineSubfunctionMapping", "CryptoEllipticCurveProps", "CryptoKeyManagementNeeds", "CryptoServiceCertificate", "CryptoServiceJobNeeds", "CryptoServiceKey", "CryptoServiceNeeds", "CryptoServicePrimitive", "CryptoServiceQueue", "CryptoSignatureScheme", "DataConstr", "DataExchangePoint", "DataPrototypeGroup", "DataReceiveErrorEvent", "DataReceivedEvent", "DataSendCompletedEvent", "DataTransformationSet", "DataTypeMappingSet", "DataWriteCompletedEvent", "DcmIPdu", "DdsCpConfig", "DdsCpConsumedServiceInstance", "DdsCpDomain", "DdsCpPartition", "DdsCpProvidedServiceInstance", "DdsCpQosProfile", "DdsCpTopic", "DefItem", "DelegationSwConnector", "DependencyOnArtifact", "DevelopmentError", "DiagEventDebounceCounterBased", "DiagEventDebounceMonitorInternal", "DiagnosticAccessPermission", "DiagnosticAging", "DiagnosticAuthRole", "DiagnosticAuthTransmitCertificate", "DiagnosticAuthTransmitCertificateEvaluation", "DiagnosticAuthTransmitCertificateMapping", "DiagnosticAuthenticationClass", "DiagnosticAuthenticationConfiguration", "DiagnosticClearDiagnosticInformation", "DiagnosticClearDiagnosticInformationClass", "DiagnosticClearResetEmissionRelatedInfo", "DiagnosticClearResetEmissionRelatedInfoClass", "DiagnosticComControl", "DiagnosticComControlClass", "DiagnosticCommunicationManagerNeeds", "DiagnosticComponentNeeds", "DiagnosticConnectedIndicator", "DiagnosticConnection", "DiagnosticContributionSet", "DiagnosticControlDTCSetting", "DiagnosticControlDTCSettingClass", "DiagnosticControlNeeds", "DiagnosticCustomServiceClass", "DiagnosticCustomServiceInstance", "DiagnosticDataElement", "DiagnosticDataIdentifier", "DiagnosticDataIdentifierSet", "DiagnosticDataTransfer", "DiagnosticDataTransferClass", "DiagnosticDeAuthentication", "DiagnosticDebounceAlgorithmProps", "DiagnosticDemProvidedDataMapping", "DiagnosticDynamicDataIdentifier", "DiagnosticDynamicallyDefineDataIdentifier", "DiagnosticDynamicallyDefineDataIdentifierClass", "DiagnosticEcuInstanceProps", "DiagnosticEcuReset", "DiagnosticEcuResetClass", "DiagnosticEnableCondition", "DiagnosticEnableConditionGroup", "DiagnosticEnableConditionNeeds", "DiagnosticEnableConditionPortMapping", "DiagnosticEnvBswModeElement", "DiagnosticEnvModeElement", "DiagnosticEnvSwcModeElement", "DiagnosticEnvironmentalCondition", "DiagnosticEvent", "DiagnosticEventInfoNeeds", "DiagnosticEventManagerNeeds", "DiagnosticEventNeeds", "DiagnosticEventPortMapping", "DiagnosticEventToDebounceAlgorithmMapping", "DiagnosticEventToEnableConditionGroupMapping", "DiagnosticEventToOperationCycleMapping", "DiagnosticEventToSecurityEventMapping", "DiagnosticEventToStorageConditionGroupMapping", "DiagnosticEventToTroubleCodeJ1939Mapping", "DiagnosticEventToTroubleCodeUdsMapping", "DiagnosticExtendedDataRecord", "DiagnosticFimAliasEvent", "DiagnosticFimAliasEventGroup", "DiagnosticFimAliasEventGroupMapping", "DiagnosticFimAliasEventMapping", "DiagnosticFimEventGroup", "DiagnosticFimFunctionMapping", "DiagnosticFreezeFrame", "DiagnosticFunctionIdentifier", "DiagnosticFunctionIdentifierInhibit", "DiagnosticFunctionInhibitSource", "DiagnosticIOControl", "DiagnosticIndicator", "DiagnosticInfoType", "DiagnosticInhibitSourceEventMapping", "DiagnosticIoControlClass", "DiagnosticIoControlNeeds", "DiagnosticIumpr", "DiagnosticIumprDenominatorGroup", "DiagnosticIumprGroup", "DiagnosticIumprToFunctionIdentifierMapping", "DiagnosticJ1939ExpandedFreezeFrame", "DiagnosticJ1939FreezeFrame", "DiagnosticJ1939Node", "DiagnosticJ1939Spn", "DiagnosticJ1939SpnMapping", "DiagnosticJ1939SwMapping", "DiagnosticMasterToSlaveEventMapping", "DiagnosticMeasurementIdentifier", "DiagnosticMemoryDestinationPrimary", "DiagnosticMemoryDestinationUserDefined", "DiagnosticMemoryIdentifier", "DiagnosticOperationCycle", "DiagnosticOperationCycleNeeds", "DiagnosticOperationCyclePortMapping", "DiagnosticParameterElement", "DiagnosticParameterIdent", "DiagnosticParameterIdentifier", "DiagnosticPowertrainFreezeFrame", "DiagnosticProofOfOwnership", "DiagnosticProtocol", "DiagnosticReadDTCInformation", "DiagnosticReadDTCInformationClass", "DiagnosticReadDataByIdentifier", "DiagnosticReadDataByIdentifierClass", "DiagnosticReadDataByPeriodicID", "DiagnosticReadDataByPeriodicIDClass", "DiagnosticReadMemoryByAddress", "DiagnosticReadMemoryByAddressClass", "DiagnosticReadScalingDataByIdentifier", "DiagnosticReadScalingDataByIdentifierClass", "DiagnosticRequestControlOfOnBoardDevice", "DiagnosticRequestControlOfOnBoardDeviceClass", "DiagnosticRequestCurrentPowertrainData", "DiagnosticRequestCurrentPowertrainDataClass", "DiagnosticRequestDownload", "DiagnosticRequestDownloadClass", "DiagnosticRequestEmissionRelatedDTC", "DiagnosticRequestEmissionRelatedDTCClass", "DiagnosticRequestEmissionRelatedDTCPermanentStatus", "DiagnosticRequestEmissionRelatedDTCPermanentStatusClass", "DiagnosticRequestFileTransfer", "DiagnosticRequestFileTransferClass", "DiagnosticRequestFileTransferNeeds", "DiagnosticRequestOnBoardMonitoringTestResults", "DiagnosticRequestOnBoardMonitoringTestResultsClass", "DiagnosticRequestPowertrainFreezeFrameData", "DiagnosticRequestPowertrainFreezeFrameDataClass", "DiagnosticRequestRoutineResults", "DiagnosticRequestUpload", "DiagnosticRequestUploadClass", "DiagnosticRequestVehicleInfo", "DiagnosticRequestVehicleInfoClass", "DiagnosticResponseOnEvent", "DiagnosticResponseOnEventClass", "DiagnosticRoutine", "DiagnosticRoutineControl", "DiagnosticRoutineControlClass", "DiagnosticRoutineNeeds", "DiagnosticSecureCodingMapping", "DiagnosticSecurityAccess", "DiagnosticSecurityAccessClass", "DiagnosticSecurityEventReportingModeMapping", "DiagnosticSecurityLevel", "DiagnosticServiceDataMapping", "DiagnosticServiceSwMapping", "DiagnosticServiceTable", "DiagnosticSession", "DiagnosticSessionControl", "DiagnosticSessionControlClass", "DiagnosticStartRoutine", "DiagnosticStopRoutine", "DiagnosticStorageCondition", "DiagnosticStorageConditionGroup", "DiagnosticStorageConditionNeeds", "DiagnosticStorageConditionPortMapping", "DiagnosticTestResult", "DiagnosticTestRoutineIdentifier", "DiagnosticTransferExit", "DiagnosticTransferExitClass", "DiagnosticTroubleCodeGroup", "DiagnosticTroubleCodeJ1939", "DiagnosticTroubleCodeObd", "DiagnosticTroubleCodeProps", "DiagnosticTroubleCodeUds", "DiagnosticTroubleCodeUdsToTroubleCodeObdMapping", "DiagnosticUploadDownloadNeeds", "DiagnosticValueNeeds", "DiagnosticVerifyCertificateBidirectional", "DiagnosticWriteDataByIdentifierClass", "DiagnosticWriteMemoryByAddressClass", "DiagnosticsCommunicationSecurityNeeds", "DltApplication", "DltArgument", "DltContext", "DltEcu", "DltLogChannel", "DltMessage", "DltUserNeeds", "DoIpActivationLineNeeds", "DoIpGidNeeds", "DoIpGidSynchronizationNeeds", "DoIpInterface", "DoIpLogicAddress", "DoIpLogicTargetAddressProps", "DoIpLogicTesterAddressProps", "DoIpPowerModeStatusNeeds", "DoIpRoutingActivation", "DoIpRoutingActivationAuthenticationNeeds", "DoIpRoutingActivationConfirmationNeeds", "DoIpTpConfig", "DocumentElementScope", "Documentation", "DocumentationContext", "DtcStatusChangeNotificationNeeds", "E2EProfileCompatibilityProps", "ECUMapping", "EOCEventRef", "EOCExecutableEntityRef", "EOCExecutableEntityRefGroup", "EcuAbstractionSwComponentType", "EcuInstance", "EcuPartition", "EcuStateMgrUserNeeds", "EcuTiming", "EcucAddInfoParamDef", "EcucBooleanParamDef", "EcucChoiceContainerDef", "EcucChoiceReferenceDef", "EcucContainerValue", "EcucDefinitionCollection", "EcucDestinationUriDef", "EcucDestinationUriDefSet", "EcucEnumerationLiteralDef", "EcucEnumerationParamDef", "EcucFloatParamDef", "EcucForeignReferenceDef", "EcucFunctionNameDef", "EcucInstanceReferenceDef", "EcucIntegerParamDef", "EcucLinkerSymbolDef", "EcucModuleConfigurationValues", "EcucModuleDef", "EcucMultilineStringParamDef", "EcucParamConfContainerDef", "EcucQuery", "EcucReferenceDef", "EcucStringParamDef", "EcucUriReferenceDef", "EcucValidationCondition", "EcucValueCollection", "EndToEndProtection", "EndToEndProtectionSet", "EnumerationMappingTable", "ErrorTracerNeeds", "EthIpProps", "EthTcpIpIcmpProps", "EthTcpIpProps", "EthTpConfig", "EthernetCluster", "EthernetCommunicationConnector", "EthernetCommunicationController", "EthernetFrameTriggering", "EthernetPhysicalChannel", "EthernetPriorityRegeneration", "EthernetWakeupSleepOnDatalineConfig", "EthernetWakeupSleepOnDatalineConfigSet", "EvaluatedVariantSet", "EventHandler", "ExclusiveArea", "ExclusiveAreaNestingOrder", "ExecutableEntityActivationReason", "ExecutionOrderConstraint", "ExecutionTimeConstraint", "ExternalTriggerOccurredEvent", "ExternalTriggeringPointIdent", "FMAttributeDef", "FMFeature", "FMFeatureMap", "FMFeatureMapAssertion", "FMFeatureMapCondition", "FMFeatureMapElement", "FMFeatureModel", "FMFeatureRelation", "FMFeatureRestriction", "FMFeatureSelection", "FMFeatureSelectionSet", "FirewallRule", "FlatInstanceDescriptor", "FlatMap", "FlexrayArTpConfig", "FlexrayArTpNode", "FlexrayCluster", "FlexrayCommunicationConnector", "FlexrayCommunicationController", "FlexrayFrame", "FlexrayFrameTriggering", "FlexrayNmCluster", "FlexrayNmNode", "FlexrayPhysicalChannel", "FlexrayTpConfig", "FlexrayTpConnectionControl", "FlexrayTpNode", "FlexrayTpPduPool", "FramePort", "FunctionInhibitionAvailabilityNeeds", "FunctionInhibitionNeeds", "Gateway", "GeneralPurposeConnection", "GeneralPurposeIPdu", "GeneralPurposePdu", "GenericEthernetFrame", "GlobalSupervisionNeeds", "GlobalTimeCanMaster", "GlobalTimeCanSlave", "GlobalTimeDomain", "GlobalTimeEthMaster", "GlobalTimeEthSlave", "GlobalTimeFrMaster", "GlobalTimeFrSlave", "GlobalTimeGateway", "HardwareTestNeeds", "HwAttributeDef", "HwAttributeLiteralDef", "HwCategory", "HwDescriptionEntity", "HwElement", "HwPin", "HwPinGroup", "HwType", "IEEE1722TpAafConnection", "IEEE1722TpAcfCan", "IEEE1722TpAcfCanPart", "IEEE1722TpAcfConnection", "IEEE1722TpAcfLin", "IEEE1722TpAcfLinPart", "IEEE1722TpConfig", "IEEE1722TpCrfConnection", "IEEE1722TpIidcConnection", "IPSecConfigProps", "IPSecRule", "IPduPort", "IPv6ExtHeaderFilterList", "IPv6ExtHeaderFilterSet", "ISignal", "ISignalGroup", "ISignalIPdu", "ISignalIPduGroup", "ISignalPort", "ISignalToIPduMapping", "ISignalTriggering", "IdsDesign", "IdsMgrCustomTimestampNeeds", "IdsMgrNeeds", "IdsmInstance", "IdsmProperties", "Ieee1722TpEthernetFrame", "ImplementationDataType", "ImplementationDataTypeElement", "ImplementationProps", "ImpositionTime", "IndicatorStatusNeeds", "InitEvent", "InternalTriggerOccurredEvent", "InternalTriggeringPoint", "InterpolationRoutineMappingSet", "J1939Cluster", "J1939ControllerApplication", "J1939DcmDm19Support", "J1939DcmIPdu", "J1939NmCluster", "J1939NmNode", "J1939RmIncomingRequestServiceNeeds", "J1939RmOutgoingRequestServiceNeeds", "J1939SharedAddressCluster", "J1939TpConfig", "J1939TpNode", "Keyword", "KeywordSet", "LatencyTimingConstraint", "LifeCycleInfoSet", "LifeCycleState", "LifeCycleStateDefinitionGroup", "LinCluster", "LinCommunicationConnector", "LinEventTriggeredFrame", "LinFrameTriggering", "LinMaster", "LinPhysicalChannel", "LinScheduleTable", "LinSlave", "LinSlaveConfigIdent", "LinSporadicFrame", "LinTpConfig", "LinTpNode", "LinUnconditionalFrame", "Linker", "LogAndTraceMessageCollectionSet", "MacMulticastGroup", "MacSecGlobalKayProps", "MacSecKayParticipant", "MacSecParticipantSet", "McDataInstance", "McFunction", "McGroup", "MeasuredExecutionTime", "MeasuredHeapUsage", "MeasuredStackUsage", "MemorySection", "ModeAccessPointIdent", "ModeDeclaration", "ModeDeclarationGroup", "ModeDeclarationGroupPrototype", "ModeDeclarationMapping", "ModeDeclarationMappingSet", "ModeInterfaceMapping", "ModeSwitchInterface", "ModeSwitchPoint", "ModeSwitchedAckEvent", "ModeTransition", "MultilanguageReferrable", "MultiplexedIPdu", "NPdu", "NetworkEndpoint", "NmConfig", "NmEcu", "NmPdu", "NvBlockDescriptor", "NvBlockNeeds", "NvBlockSwComponentType", "NvDataInterface", "ObdControlServiceNeeds", "ObdInfoServiceNeeds", "ObdMonitorServiceNeeds", "ObdPidServiceNeeds", "ObdRatioDenominatorNeeds", "ObdRatioServiceNeeds", "OffsetTimingConstraint", "OperationInvokedEvent", "OsTaskExecutionEvent", "OsTaskProxy", "PPortPrototype", "PRPortPrototype", "ParameterAccess", "ParameterDataPrototype", "ParameterInterface", "ParameterSwComponentType", "PassThroughSwConnector", "PduActivationRoutingGroup", "PduToFrameMapping", "PduTriggering", "PdurIPduGroup", "PerInstanceMemory", "PeriodicEventTriggering", "PhysicalDimension", "PhysicalDimensionMappingSet", "PncMappingIdent", "PortElementToCommunicationResourceMapping", "PortGroup", "PortInterfaceMappingSet", "PortPrototypeBlueprint", "PostBuildVariantCriterion", "PostBuildVariantCriterionValueSet", "PredefinedVariant", "PrimitiveAttributeTailoring", "ProvidedServiceInstance", "RPortPrototype", "RapidPrototypingScenario", "ReferenceTailoring", "ResourceConsumption", "RootSwCompositionPrototype", "RoughEstimateHeapUsage", "RoughEstimateOfExecutionTime", "RoughEstimateStackUsage", "RptComponent", "RptContainer", "RptExecutableEntity", "RptExecutableEntityEvent", "RptExecutionContext", "RptProfile", "RptServicePoint", "RteEventInCompositionSeparation", "RteEventInCompositionToOsTaskProxyMapping", "RteEventInSystemSeparation", "RteEventInSystemToOsTaskProxyMapping", "RunnableEntity", "RunnableEntityGroup", "RuntimeError", "SOMEIPTransformationProps", "Sdg", "SdgAggregationWithVariation", "SdgCaption", "SdgClass", "SdgDef", "SdgForeignReference", "SdgForeignReferenceWithVariation", "SdgPrimitiveAttribute", "SdgPrimitiveAttributeWithVariation", "SdgTailoring", "SecOcCryptoServiceMapping", "SectionNamePrefix", "SecureCommunicationAuthenticationProps", "SecureCommunicationFreshnessProps", "SecureCommunicationPropsSet", "SecureOnBoardCommunicationNeeds", "SecuredIPdu", "SecurityEventAggregationFilter", "SecurityEventContextMappingApplication", "SecurityEventContextMappingBswModule", "SecurityEventContextMappingCommConnector", "SecurityEventContextMappingFunctionalCluster", "SecurityEventContextProps", "SecurityEventDefinition", "SecurityEventFilterChain", "SecurityEventOneEveryNFilter", "SecurityEventStateFilter", "SenderReceiverInterface", "SensorActuatorSwComponentType", "ServiceInstanceCollectionSet", "ServiceProxySwComponentType", "ServiceSwComponentType", "SignalServiceTranslationElementProps", "SignalServiceTranslationEventProps", "SignalServiceTranslationProps", "SignalServiceTranslationPropsSet", "SingleLanguageReferrable", "SoAdRoutingGroup", "SoConIPduIdentifier", "SocketAddress", "SocketConnectionBundle", "SocketConnectionIpduIdentifierSet", "SomeipSdClientServiceInstanceConfig", "SomeipSdServerEventGroupTimingConfig", "SomeipSdServerServiceInstanceConfig", "SomeipTpChannel", "SomeipTpConfig", "SpecificationDocumentScope", "SporadicEventTriggering", "StaticSocketConnection", "Std", "StructuredReq", "SupervisedEntityCheckpointNeeds", "SupervisedEntityNeeds", "SwAddrMethod", "SwAxisType", "SwBaseType", "SwGenericAxisParamType", "SwRecordLayout", "SwServiceArg", "SwSystemconst", "SwSystemconstantValueSet", "SwcBswMapping", "SwcImplementation", "SwcInternalBehavior", "SwcModeManagerErrorEvent", "SwcModeSwitchEvent", "SwcServiceDependency", "SwcTiming", "SwcToApplicationPartitionMapping", "SwcToEcuMapping", "SwcToImplMapping", "SwitchAsynchronousTrafficShaperGroupEntry", "SwitchFlowMeteringEntry", "SwitchStreamFilterActionDestPortModification", "SwitchStreamFilterEntry", "SwitchStreamFilterRule", "SwitchStreamGateEntry", "SwitchStreamIdentification", "SymbolProps", "SyncTimeBaseMgrUserNeeds", "SynchronizationPointConstraint", "SynchronousServerCallPoint", "System", "SystemMapping", "SystemSignal", "SystemSignalGroup", "SystemSignalGroupToCommunicationResourceMapping", "SystemSignalToCommunicationResourceMapping", "SystemTiming", "TDCpSoftwareClusterMapping", "TDCpSoftwareClusterMappingSet", "TDCpSoftwareClusterResourceMapping", "TDEventBswInternalBehavior", "TDEventBswModeDeclaration", "TDEventBswModule", "TDEventComplex", "TDEventFrClusterCycleStart", "TDEventFrame", "TDEventFrameEthernet", "TDEventIPdu", "TDEventISignal", "TDEventModeDeclaration", "TDEventOperation", "TDEventSLLETPort", "TDEventSwcInternalBehavior", "TDEventSwcInternalBehaviorReference", "TDEventTTCanCycleStart", "TDEventTrigger", "TDEventVariableDataPrototype", "TDEventVfbReference", "TDLETZoneClock", "TcpOptionFilterList", "TcpOptionFilterSet", "TimeSyncServerConfiguration", "TimingClockSyncAccuracy", "TimingCondition", "TimingDescriptionEventChain", "TimingEvent", "TimingExtensionResource", "TimingModeInstance", "TlsCryptoCipherSuite", "TlsCryptoCipherSuiteProps", "TlsCryptoServiceMapping", "TlvDataIdDefinitionSet", "Topic1", "TpAddress", "TpConnectionIdent", "TraceableText", "TransformationPropsSet", "TransformationTechnology", "TransformerHardErrorEvent", "TransientFault", "Trigger", "TriggerInterface", "TriggerInterfaceMapping", "TtcanCluster", "TtcanCommunicationConnector", "TtcanCommunicationController", "TtcanPhysicalChannel", "UdpNmCluster", "UdpNmNode", "Unit", "UnitGroup", "UserDefinedCluster", "UserDefinedCommunicationConnector", "UserDefinedCommunicationController", "UserDefinedEthernetFrame", "UserDefinedGlobalTimeMaster", "UserDefinedGlobalTimeSlave", "UserDefinedIPdu", "UserDefinedPdu", "UserDefinedTransformationProps", "V2xDataManagerNeeds", "V2xFacUserNeeds", "V2xMUserNeeds", "VariableAccess", "VariableDataPrototype", "VariationPointProxy", "VendorSpecificServiceNeeds", "VfbTiming", "ViewMap", "ViewMapSet", "VlanConfig", "WaitPoint", "WorstCaseHeapUsage", "WorstCaseStackUsage", "Xdoc", "Xfile", "XrefTarget"]),
        "LC-STATE-REF": lambda obj, elem: setattr(obj, "lc_state_ref", ARRef.deserialize(elem)),
        "PERIOD-BEGIN": lambda obj, elem: setattr(obj, "period_begin", SerializationHelper.deserialize_by_tag(elem, "LifeCyclePeriod")),
        "PERIOD-END": lambda obj, elem: setattr(obj, "period_end", SerializationHelper.deserialize_by_tag(elem, "LifeCyclePeriod")),
        "REMARK": lambda obj, elem: setattr(obj, "remark", SerializationHelper.deserialize_by_tag(elem, "DocumentationBlock")),
        "USE-INSTEAD-REFS": ("_POLYMORPHIC_LIST", "use_instead_refs", ["ARPackage", "AclObjectSet", "AclOperation", "AclPermission", "AclRole", "AgeConstraint", "AggregationTailoring", "AliasNameSet", "AnalyzedExecutionTime", "AppOsTaskProxyToEcuTaskProxyMapping", "ApplicationArrayDataType", "ApplicationArrayElement", "ApplicationEndpoint", "ApplicationError", "ApplicationPartition", "ApplicationPartitionToEcuPartitionMapping", "ApplicationPrimitiveDataType", "ApplicationRecordDataType", "ApplicationRecordElement", "ApplicationSwComponentType", "ArbitraryEventTriggering", "ArgumentDataPrototype", "AssemblySwConnector", "AsynchronousServerCallPoint", "AsynchronousServerCallResultPoint", "AsynchronousServerCallReturnsEvent", "AtpDefinition", "AutosarOperationArgumentInstance", "AutosarVariableInstance", "BackgroundEvent", "BinaryManifestItem", "BinaryManifestItemDefinition", "BinaryManifestMetaDataField", "BinaryManifestProvideResource", "BinaryManifestRequireResource", "BinaryManifestResourceDefinition", "BlockState", "BlueprintMappingSet", "BswAsynchronousServerCallPoint", "BswAsynchronousServerCallResultPoint", "BswAsynchronousServerCallReturnsEvent", "BswBackgroundEvent", "BswCalledEntity", "BswCompositionTiming", "BswDataReceivedEvent", "BswDirectCallPoint", "BswDistinguishedPartition", "BswEntryRelationshipSet", "BswExternalTriggerOccurredEvent", "BswImplementation", "BswInternalBehavior", "BswInternalTriggerOccurredEvent", "BswInternalTriggeringPoint", "BswInterruptEntity", "BswInterruptEvent", "BswMgrNeeds", "BswModeManagerErrorEvent", "BswModeSwitchEvent", "BswModeSwitchedAckEvent", "BswModuleCallPoint", "BswModuleClientServerEntry", "BswModuleDependency", "BswModuleDescription", "BswModuleEntry", "BswModuleTiming", "BswOperationInvokedEvent", "BswOsTaskExecutionEvent", "BswSchedulableEntity", "BswSchedulerNamePrefix", "BswServiceDependencyIdent", "BswTimingEvent", "BswVariableAccess", "BuildAction", "BuildActionEnvironment", "BuildActionManifest", "BulkNvDataDescriptor", "BurstPatternEventTriggering", "BusMirrorChannelMappingCan", "BusMirrorChannelMappingFlexray", "BusMirrorChannelMappingIp", "CalibrationParameterValueSet", "CanCluster", "CanCommunicationConnector", "CanCommunicationController", "CanFrame", "CanFrameTriggering", "CanNmCluster", "CanNmNode", "CanPhysicalChannel", "CanTpAddress", "CanTpChannel", "CanTpConfig", "CanTpNode", "Caption", "Chapter", "ClassContentConditional", "ClientIdDefinition", "ClientIdDefinitionSet", "ClientServerInterface", "ClientServerInterfaceMapping", "ClientServerInterfaceToBswModuleEntryBlueprintMapping", "ClientServerOperation", "Code", "Collection", "ComManagementMapping", "ComMgrUserNeeds", "Compiler", "ComplexDeviceDriverSwComponentType", "CompositionSwComponentType", "CompuMethod", "ConcreteClassTailoring", "ConcretePatternEventTriggering", "ConsistencyNeeds", "ConsistencyNeedsBlueprintSet", "ConstantSpecification", "ConstantSpecificationMappingSet", "ConstraintTailoring", "ConsumedEventGroup", "ConsumedProvidedServiceInstanceGroup", "ConsumedServiceInstance", "ContainerIPdu", "CouplingElement", "CouplingElementSwitchDetails", "CouplingPort", "CouplingPortFifo", "CouplingPortScheduler", "CouplingPortShaper", "CouplingPortTrafficClassAssignment", "CpSoftwareCluster", "CpSoftwareClusterBinaryManifestDescriptor", "CpSoftwareClusterCommunicationResource", "CpSoftwareClusterMappingSet", "CpSoftwareClusterResourcePool", "CpSoftwareClusterResourceToApplicationPartitionMapping", "CpSoftwareClusterServiceResource", "CpSoftwareClusterToApplicationPartitionMapping", "CpSoftwareClusterToEcuInstanceMapping", "CpSoftwareClusterToResourceMapping", "CpSwClusterResourceToDiagDataElemMapping", "CpSwClusterResourceToDiagFunctionIdMapping", "CpSwClusterToDiagEventMapping", "CpSwClusterToDiagRoutineSubfunctionMapping", "CryptoEllipticCurveProps", "CryptoKeyManagementNeeds", "CryptoServiceCertificate", "CryptoServiceJobNeeds", "CryptoServiceKey", "CryptoServiceNeeds", "CryptoServicePrimitive", "CryptoServiceQueue", "CryptoSignatureScheme", "DataConstr", "DataExchangePoint", "DataPrototypeGroup", "DataReceiveErrorEvent", "DataReceivedEvent", "DataSendCompletedEvent", "DataTransformationSet", "DataTypeMappingSet", "DataWriteCompletedEvent", "DcmIPdu", "DdsCpConfig", "DdsCpConsumedServiceInstance", "DdsCpDomain", "DdsCpPartition", "DdsCpProvidedServiceInstance", "DdsCpQosProfile", "DdsCpTopic", "DefItem", "DelegationSwConnector", "DependencyOnArtifact", "DevelopmentError", "DiagEventDebounceCounterBased", "DiagEventDebounceMonitorInternal", "DiagnosticAccessPermission", "DiagnosticAging", "DiagnosticAuthRole", "DiagnosticAuthTransmitCertificate", "DiagnosticAuthTransmitCertificateEvaluation", "DiagnosticAuthTransmitCertificateMapping", "DiagnosticAuthenticationClass", "DiagnosticAuthenticationConfiguration", "DiagnosticClearDiagnosticInformation", "DiagnosticClearDiagnosticInformationClass", "DiagnosticClearResetEmissionRelatedInfo", "DiagnosticClearResetEmissionRelatedInfoClass", "DiagnosticComControl", "DiagnosticComControlClass", "DiagnosticCommunicationManagerNeeds", "DiagnosticComponentNeeds", "DiagnosticConnectedIndicator", "DiagnosticConnection", "DiagnosticContributionSet", "DiagnosticControlDTCSetting", "DiagnosticControlDTCSettingClass", "DiagnosticControlNeeds", "DiagnosticCustomServiceClass", "DiagnosticCustomServiceInstance", "DiagnosticDataElement", "DiagnosticDataIdentifier", "DiagnosticDataIdentifierSet", "DiagnosticDataTransfer", "DiagnosticDataTransferClass", "DiagnosticDeAuthentication", "DiagnosticDebounceAlgorithmProps", "DiagnosticDemProvidedDataMapping", "DiagnosticDynamicDataIdentifier", "DiagnosticDynamicallyDefineDataIdentifier", "DiagnosticDynamicallyDefineDataIdentifierClass", "DiagnosticEcuInstanceProps", "DiagnosticEcuReset", "DiagnosticEcuResetClass", "DiagnosticEnableCondition", "DiagnosticEnableConditionGroup", "DiagnosticEnableConditionNeeds", "DiagnosticEnableConditionPortMapping", "DiagnosticEnvBswModeElement", "DiagnosticEnvModeElement", "DiagnosticEnvSwcModeElement", "DiagnosticEnvironmentalCondition", "DiagnosticEvent", "DiagnosticEventInfoNeeds", "DiagnosticEventManagerNeeds", "DiagnosticEventNeeds", "DiagnosticEventPortMapping", "DiagnosticEventToDebounceAlgorithmMapping", "DiagnosticEventToEnableConditionGroupMapping", "DiagnosticEventToOperationCycleMapping", "DiagnosticEventToSecurityEventMapping", "DiagnosticEventToStorageConditionGroupMapping", "DiagnosticEventToTroubleCodeJ1939Mapping", "DiagnosticEventToTroubleCodeUdsMapping", "DiagnosticExtendedDataRecord", "DiagnosticFimAliasEvent", "DiagnosticFimAliasEventGroup", "DiagnosticFimAliasEventGroupMapping", "DiagnosticFimAliasEventMapping", "DiagnosticFimEventGroup", "DiagnosticFimFunctionMapping", "DiagnosticFreezeFrame", "DiagnosticFunctionIdentifier", "DiagnosticFunctionIdentifierInhibit", "DiagnosticFunctionInhibitSource", "DiagnosticIOControl", "DiagnosticIndicator", "DiagnosticInfoType", "DiagnosticInhibitSourceEventMapping", "DiagnosticIoControlClass", "DiagnosticIoControlNeeds", "DiagnosticIumpr", "DiagnosticIumprDenominatorGroup", "DiagnosticIumprGroup", "DiagnosticIumprToFunctionIdentifierMapping", "DiagnosticJ1939ExpandedFreezeFrame", "DiagnosticJ1939FreezeFrame", "DiagnosticJ1939Node", "DiagnosticJ1939Spn", "DiagnosticJ1939SpnMapping", "DiagnosticJ1939SwMapping", "DiagnosticMasterToSlaveEventMapping", "DiagnosticMeasurementIdentifier", "DiagnosticMemoryDestinationPrimary", "DiagnosticMemoryDestinationUserDefined", "DiagnosticMemoryIdentifier", "DiagnosticOperationCycle", "DiagnosticOperationCycleNeeds", "DiagnosticOperationCyclePortMapping", "DiagnosticParameterElement", "DiagnosticParameterIdent", "DiagnosticParameterIdentifier", "DiagnosticPowertrainFreezeFrame", "DiagnosticProofOfOwnership", "DiagnosticProtocol", "DiagnosticReadDTCInformation", "DiagnosticReadDTCInformationClass", "DiagnosticReadDataByIdentifier", "DiagnosticReadDataByIdentifierClass", "DiagnosticReadDataByPeriodicID", "DiagnosticReadDataByPeriodicIDClass", "DiagnosticReadMemoryByAddress", "DiagnosticReadMemoryByAddressClass", "DiagnosticReadScalingDataByIdentifier", "DiagnosticReadScalingDataByIdentifierClass", "DiagnosticRequestControlOfOnBoardDevice", "DiagnosticRequestControlOfOnBoardDeviceClass", "DiagnosticRequestCurrentPowertrainData", "DiagnosticRequestCurrentPowertrainDataClass", "DiagnosticRequestDownload", "DiagnosticRequestDownloadClass", "DiagnosticRequestEmissionRelatedDTC", "DiagnosticRequestEmissionRelatedDTCClass", "DiagnosticRequestEmissionRelatedDTCPermanentStatus", "DiagnosticRequestEmissionRelatedDTCPermanentStatusClass", "DiagnosticRequestFileTransfer", "DiagnosticRequestFileTransferClass", "DiagnosticRequestFileTransferNeeds", "DiagnosticRequestOnBoardMonitoringTestResults", "DiagnosticRequestOnBoardMonitoringTestResultsClass", "DiagnosticRequestPowertrainFreezeFrameData", "DiagnosticRequestPowertrainFreezeFrameDataClass", "DiagnosticRequestRoutineResults", "DiagnosticRequestUpload", "DiagnosticRequestUploadClass", "DiagnosticRequestVehicleInfo", "DiagnosticRequestVehicleInfoClass", "DiagnosticResponseOnEvent", "DiagnosticResponseOnEventClass", "DiagnosticRoutine", "DiagnosticRoutineControl", "DiagnosticRoutineControlClass", "DiagnosticRoutineNeeds", "DiagnosticSecureCodingMapping", "DiagnosticSecurityAccess", "DiagnosticSecurityAccessClass", "DiagnosticSecurityEventReportingModeMapping", "DiagnosticSecurityLevel", "DiagnosticServiceDataMapping", "DiagnosticServiceSwMapping", "DiagnosticServiceTable", "DiagnosticSession", "DiagnosticSessionControl", "DiagnosticSessionControlClass", "DiagnosticStartRoutine", "DiagnosticStopRoutine", "DiagnosticStorageCondition", "DiagnosticStorageConditionGroup", "DiagnosticStorageConditionNeeds", "DiagnosticStorageConditionPortMapping", "DiagnosticTestResult", "DiagnosticTestRoutineIdentifier", "DiagnosticTransferExit", "DiagnosticTransferExitClass", "DiagnosticTroubleCodeGroup", "DiagnosticTroubleCodeJ1939", "DiagnosticTroubleCodeObd", "DiagnosticTroubleCodeProps", "DiagnosticTroubleCodeUds", "DiagnosticTroubleCodeUdsToTroubleCodeObdMapping", "DiagnosticUploadDownloadNeeds", "DiagnosticValueNeeds", "DiagnosticVerifyCertificateBidirectional", "DiagnosticWriteDataByIdentifierClass", "DiagnosticWriteMemoryByAddressClass", "DiagnosticsCommunicationSecurityNeeds", "DltApplication", "DltArgument", "DltContext", "DltEcu", "DltLogChannel", "DltMessage", "DltUserNeeds", "DoIpActivationLineNeeds", "DoIpGidNeeds", "DoIpGidSynchronizationNeeds", "DoIpInterface", "DoIpLogicAddress", "DoIpLogicTargetAddressProps", "DoIpLogicTesterAddressProps", "DoIpPowerModeStatusNeeds", "DoIpRoutingActivation", "DoIpRoutingActivationAuthenticationNeeds", "DoIpRoutingActivationConfirmationNeeds", "DoIpTpConfig", "DocumentElementScope", "Documentation", "DocumentationContext", "DtcStatusChangeNotificationNeeds", "E2EProfileCompatibilityProps", "ECUMapping", "EOCEventRef", "EOCExecutableEntityRef", "EOCExecutableEntityRefGroup", "EcuAbstractionSwComponentType", "EcuInstance", "EcuPartition", "EcuStateMgrUserNeeds", "EcuTiming", "EcucAddInfoParamDef", "EcucBooleanParamDef", "EcucChoiceContainerDef", "EcucChoiceReferenceDef", "EcucContainerValue", "EcucDefinitionCollection", "EcucDestinationUriDef", "EcucDestinationUriDefSet", "EcucEnumerationLiteralDef", "EcucEnumerationParamDef", "EcucFloatParamDef", "EcucForeignReferenceDef", "EcucFunctionNameDef", "EcucInstanceReferenceDef", "EcucIntegerParamDef", "EcucLinkerSymbolDef", "EcucModuleConfigurationValues", "EcucModuleDef", "EcucMultilineStringParamDef", "EcucParamConfContainerDef", "EcucQuery", "EcucReferenceDef", "EcucStringParamDef", "EcucUriReferenceDef", "EcucValidationCondition", "EcucValueCollection", "EndToEndProtection", "EndToEndProtectionSet", "EnumerationMappingTable", "ErrorTracerNeeds", "EthIpProps", "EthTcpIpIcmpProps", "EthTcpIpProps", "EthTpConfig", "EthernetCluster", "EthernetCommunicationConnector", "EthernetCommunicationController", "EthernetFrameTriggering", "EthernetPhysicalChannel", "EthernetPriorityRegeneration", "EthernetWakeupSleepOnDatalineConfig", "EthernetWakeupSleepOnDatalineConfigSet", "EvaluatedVariantSet", "EventHandler", "ExclusiveArea", "ExclusiveAreaNestingOrder", "ExecutableEntityActivationReason", "ExecutionOrderConstraint", "ExecutionTimeConstraint", "ExternalTriggerOccurredEvent", "ExternalTriggeringPointIdent", "FMAttributeDef", "FMFeature", "FMFeatureMap", "FMFeatureMapAssertion", "FMFeatureMapCondition", "FMFeatureMapElement", "FMFeatureModel", "FMFeatureRelation", "FMFeatureRestriction", "FMFeatureSelection", "FMFeatureSelectionSet", "FirewallRule", "FlatInstanceDescriptor", "FlatMap", "FlexrayArTpConfig", "FlexrayArTpNode", "FlexrayCluster", "FlexrayCommunicationConnector", "FlexrayCommunicationController", "FlexrayFrame", "FlexrayFrameTriggering", "FlexrayNmCluster", "FlexrayNmNode", "FlexrayPhysicalChannel", "FlexrayTpConfig", "FlexrayTpConnectionControl", "FlexrayTpNode", "FlexrayTpPduPool", "FramePort", "FunctionInhibitionAvailabilityNeeds", "FunctionInhibitionNeeds", "Gateway", "GeneralPurposeConnection", "GeneralPurposeIPdu", "GeneralPurposePdu", "GenericEthernetFrame", "GlobalSupervisionNeeds", "GlobalTimeCanMaster", "GlobalTimeCanSlave", "GlobalTimeDomain", "GlobalTimeEthMaster", "GlobalTimeEthSlave", "GlobalTimeFrMaster", "GlobalTimeFrSlave", "GlobalTimeGateway", "HardwareTestNeeds", "HwAttributeDef", "HwAttributeLiteralDef", "HwCategory", "HwDescriptionEntity", "HwElement", "HwPin", "HwPinGroup", "HwType", "IEEE1722TpAafConnection", "IEEE1722TpAcfCan", "IEEE1722TpAcfCanPart", "IEEE1722TpAcfConnection", "IEEE1722TpAcfLin", "IEEE1722TpAcfLinPart", "IEEE1722TpConfig", "IEEE1722TpCrfConnection", "IEEE1722TpIidcConnection", "IPSecConfigProps", "IPSecRule", "IPduPort", "IPv6ExtHeaderFilterList", "IPv6ExtHeaderFilterSet", "ISignal", "ISignalGroup", "ISignalIPdu", "ISignalIPduGroup", "ISignalPort", "ISignalToIPduMapping", "ISignalTriggering", "IdsDesign", "IdsMgrCustomTimestampNeeds", "IdsMgrNeeds", "IdsmInstance", "IdsmProperties", "Ieee1722TpEthernetFrame", "ImplementationDataType", "ImplementationDataTypeElement", "ImplementationProps", "ImpositionTime", "IndicatorStatusNeeds", "InitEvent", "InternalTriggerOccurredEvent", "InternalTriggeringPoint", "InterpolationRoutineMappingSet", "J1939Cluster", "J1939ControllerApplication", "J1939DcmDm19Support", "J1939DcmIPdu", "J1939NmCluster", "J1939NmNode", "J1939RmIncomingRequestServiceNeeds", "J1939RmOutgoingRequestServiceNeeds", "J1939SharedAddressCluster", "J1939TpConfig", "J1939TpNode", "Keyword", "KeywordSet", "LatencyTimingConstraint", "LifeCycleInfoSet", "LifeCycleState", "LifeCycleStateDefinitionGroup", "LinCluster", "LinCommunicationConnector", "LinEventTriggeredFrame", "LinFrameTriggering", "LinMaster", "LinPhysicalChannel", "LinScheduleTable", "LinSlave", "LinSlaveConfigIdent", "LinSporadicFrame", "LinTpConfig", "LinTpNode", "LinUnconditionalFrame", "Linker", "LogAndTraceMessageCollectionSet", "MacMulticastGroup", "MacSecGlobalKayProps", "MacSecKayParticipant", "MacSecParticipantSet", "McDataInstance", "McFunction", "McGroup", "MeasuredExecutionTime", "MeasuredHeapUsage", "MeasuredStackUsage", "MemorySection", "ModeAccessPointIdent", "ModeDeclaration", "ModeDeclarationGroup", "ModeDeclarationGroupPrototype", "ModeDeclarationMapping", "ModeDeclarationMappingSet", "ModeInterfaceMapping", "ModeSwitchInterface", "ModeSwitchPoint", "ModeSwitchedAckEvent", "ModeTransition", "MultilanguageReferrable", "MultiplexedIPdu", "NPdu", "NetworkEndpoint", "NmConfig", "NmEcu", "NmPdu", "NvBlockDescriptor", "NvBlockNeeds", "NvBlockSwComponentType", "NvDataInterface", "ObdControlServiceNeeds", "ObdInfoServiceNeeds", "ObdMonitorServiceNeeds", "ObdPidServiceNeeds", "ObdRatioDenominatorNeeds", "ObdRatioServiceNeeds", "OffsetTimingConstraint", "OperationInvokedEvent", "OsTaskExecutionEvent", "OsTaskProxy", "PPortPrototype", "PRPortPrototype", "ParameterAccess", "ParameterDataPrototype", "ParameterInterface", "ParameterSwComponentType", "PassThroughSwConnector", "PduActivationRoutingGroup", "PduToFrameMapping", "PduTriggering", "PdurIPduGroup", "PerInstanceMemory", "PeriodicEventTriggering", "PhysicalDimension", "PhysicalDimensionMappingSet", "PncMappingIdent", "PortElementToCommunicationResourceMapping", "PortGroup", "PortInterfaceMappingSet", "PortPrototypeBlueprint", "PostBuildVariantCriterion", "PostBuildVariantCriterionValueSet", "PredefinedVariant", "PrimitiveAttributeTailoring", "ProvidedServiceInstance", "RPortPrototype", "RapidPrototypingScenario", "ReferenceTailoring", "ResourceConsumption", "RootSwCompositionPrototype", "RoughEstimateHeapUsage", "RoughEstimateOfExecutionTime", "RoughEstimateStackUsage", "RptComponent", "RptContainer", "RptExecutableEntity", "RptExecutableEntityEvent", "RptExecutionContext", "RptProfile", "RptServicePoint", "RteEventInCompositionSeparation", "RteEventInCompositionToOsTaskProxyMapping", "RteEventInSystemSeparation", "RteEventInSystemToOsTaskProxyMapping", "RunnableEntity", "RunnableEntityGroup", "RuntimeError", "SOMEIPTransformationProps", "Sdg", "SdgAggregationWithVariation", "SdgCaption", "SdgClass", "SdgDef", "SdgForeignReference", "SdgForeignReferenceWithVariation", "SdgPrimitiveAttribute", "SdgPrimitiveAttributeWithVariation", "SdgTailoring", "SecOcCryptoServiceMapping", "SectionNamePrefix", "SecureCommunicationAuthenticationProps", "SecureCommunicationFreshnessProps", "SecureCommunicationPropsSet", "SecureOnBoardCommunicationNeeds", "SecuredIPdu", "SecurityEventAggregationFilter", "SecurityEventContextMappingApplication", "SecurityEventContextMappingBswModule", "SecurityEventContextMappingCommConnector", "SecurityEventContextMappingFunctionalCluster", "SecurityEventContextProps", "SecurityEventDefinition", "SecurityEventFilterChain", "SecurityEventOneEveryNFilter", "SecurityEventStateFilter", "SenderReceiverInterface", "SensorActuatorSwComponentType", "ServiceInstanceCollectionSet", "ServiceProxySwComponentType", "ServiceSwComponentType", "SignalServiceTranslationElementProps", "SignalServiceTranslationEventProps", "SignalServiceTranslationProps", "SignalServiceTranslationPropsSet", "SingleLanguageReferrable", "SoAdRoutingGroup", "SoConIPduIdentifier", "SocketAddress", "SocketConnectionBundle", "SocketConnectionIpduIdentifierSet", "SomeipSdClientServiceInstanceConfig", "SomeipSdServerEventGroupTimingConfig", "SomeipSdServerServiceInstanceConfig", "SomeipTpChannel", "SomeipTpConfig", "SpecificationDocumentScope", "SporadicEventTriggering", "StaticSocketConnection", "Std", "StructuredReq", "SupervisedEntityCheckpointNeeds", "SupervisedEntityNeeds", "SwAddrMethod", "SwAxisType", "SwBaseType", "SwGenericAxisParamType", "SwRecordLayout", "SwServiceArg", "SwSystemconst", "SwSystemconstantValueSet", "SwcBswMapping", "SwcImplementation", "SwcInternalBehavior", "SwcModeManagerErrorEvent", "SwcModeSwitchEvent", "SwcServiceDependency", "SwcTiming", "SwcToApplicationPartitionMapping", "SwcToEcuMapping", "SwcToImplMapping", "SwitchAsynchronousTrafficShaperGroupEntry", "SwitchFlowMeteringEntry", "SwitchStreamFilterActionDestPortModification", "SwitchStreamFilterEntry", "SwitchStreamFilterRule", "SwitchStreamGateEntry", "SwitchStreamIdentification", "SymbolProps", "SyncTimeBaseMgrUserNeeds", "SynchronizationPointConstraint", "SynchronousServerCallPoint", "System", "SystemMapping", "SystemSignal", "SystemSignalGroup", "SystemSignalGroupToCommunicationResourceMapping", "SystemSignalToCommunicationResourceMapping", "SystemTiming", "TDCpSoftwareClusterMapping", "TDCpSoftwareClusterMappingSet", "TDCpSoftwareClusterResourceMapping", "TDEventBswInternalBehavior", "TDEventBswModeDeclaration", "TDEventBswModule", "TDEventComplex", "TDEventFrClusterCycleStart", "TDEventFrame", "TDEventFrameEthernet", "TDEventIPdu", "TDEventISignal", "TDEventModeDeclaration", "TDEventOperation", "TDEventSLLETPort", "TDEventSwcInternalBehavior", "TDEventSwcInternalBehaviorReference", "TDEventTTCanCycleStart", "TDEventTrigger", "TDEventVariableDataPrototype", "TDEventVfbReference", "TDLETZoneClock", "TcpOptionFilterList", "TcpOptionFilterSet", "TimeSyncServerConfiguration", "TimingClockSyncAccuracy", "TimingCondition", "TimingDescriptionEventChain", "TimingEvent", "TimingExtensionResource", "TimingModeInstance", "TlsCryptoCipherSuite", "TlsCryptoCipherSuiteProps", "TlsCryptoServiceMapping", "TlvDataIdDefinitionSet", "Topic1", "TpAddress", "TpConnectionIdent", "TraceableText", "TransformationPropsSet", "TransformationTechnology", "TransformerHardErrorEvent", "TransientFault", "Trigger", "TriggerInterface", "TriggerInterfaceMapping", "TtcanCluster", "TtcanCommunicationConnector", "TtcanCommunicationController", "TtcanPhysicalChannel", "UdpNmCluster", "UdpNmNode", "Unit", "UnitGroup", "UserDefinedCluster", "UserDefinedCommunicationConnector", "UserDefinedCommunicationController", "UserDefinedEthernetFrame", "UserDefinedGlobalTimeMaster", "UserDefinedGlobalTimeSlave", "UserDefinedIPdu", "UserDefinedPdu", "UserDefinedTransformationProps", "V2xDataManagerNeeds", "V2xFacUserNeeds", "V2xMUserNeeds", "VariableAccess", "VariableDataPrototype", "VariationPointProxy", "VendorSpecificServiceNeeds", "VfbTiming", "ViewMap", "ViewMapSet", "VlanConfig", "WaitPoint", "WorstCaseHeapUsage", "WorstCaseStackUsage", "Xdoc", "Xfile", "XrefTarget"]),
    }


    def __init__(self) -> None:
        """Initialize LifeCycleInfo."""
        super().__init__()
        self.lc_object_ref: ARRef = None
        self.lc_state_ref: Optional[ARRef] = None
        self.period_begin: Optional[LifeCyclePeriod] = None
        self.period_end: Optional[LifeCyclePeriod] = None
        self.remark: Optional[DocumentationBlock] = None
        self.use_instead_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize LifeCycleInfo to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LifeCycleInfo, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize lc_object_ref
        if self.lc_object_ref is not None:
            serialized = SerializationHelper.serialize_item(self.lc_object_ref, "Referrable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LC-OBJECT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize lc_state_ref
        if self.lc_state_ref is not None:
            serialized = SerializationHelper.serialize_item(self.lc_state_ref, "LifeCycleState")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LC-STATE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize period_begin
        if self.period_begin is not None:
            serialized = SerializationHelper.serialize_item(self.period_begin, "LifeCyclePeriod")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PERIOD-BEGIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize period_end
        if self.period_end is not None:
            serialized = SerializationHelper.serialize_item(self.period_end, "LifeCyclePeriod")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PERIOD-END")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize remark
        if self.remark is not None:
            serialized = SerializationHelper.serialize_item(self.remark, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REMARK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize use_instead_refs (list to container "USE-INSTEAD-REFS")
        if self.use_instead_refs:
            wrapper = ET.Element("USE-INSTEAD-REFS")
            for item in self.use_instead_refs:
                serialized = SerializationHelper.serialize_item(item, "Referrable")
                if serialized is not None:
                    child_elem = ET.Element("USE-INSTEAD-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LifeCycleInfo":
        """Deserialize XML element to LifeCycleInfo object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LifeCycleInfo object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LifeCycleInfo, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "LC-OBJECT-REF":
                setattr(obj, "lc_object_ref", ARRef.deserialize(child))
            elif tag == "LC-STATE-REF":
                setattr(obj, "lc_state_ref", ARRef.deserialize(child))
            elif tag == "PERIOD-BEGIN":
                setattr(obj, "period_begin", SerializationHelper.deserialize_by_tag(child, "LifeCyclePeriod"))
            elif tag == "PERIOD-END":
                setattr(obj, "period_end", SerializationHelper.deserialize_by_tag(child, "LifeCyclePeriod"))
            elif tag == "REMARK":
                setattr(obj, "remark", SerializationHelper.deserialize_by_tag(child, "DocumentationBlock"))
            elif tag == "USE-INSTEAD-REFS":
                for item_elem in child:
                    obj.use_instead_refs.append(ARRef.deserialize(item_elem))

        return obj



class LifeCycleInfoBuilder(BuilderBase):
    """Builder for LifeCycleInfo with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: LifeCycleInfo = LifeCycleInfo()


    def with_lc_object(self, value: Referrable) -> "LifeCycleInfoBuilder":
        """Set lc_object attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.lc_object = value
        return self

    def with_lc_state(self, value: Optional[LifeCycleState]) -> "LifeCycleInfoBuilder":
        """Set lc_state attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.lc_state = value
        return self

    def with_period_begin(self, value: Optional[LifeCyclePeriod]) -> "LifeCycleInfoBuilder":
        """Set period_begin attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.period_begin = value
        return self

    def with_period_end(self, value: Optional[LifeCyclePeriod]) -> "LifeCycleInfoBuilder":
        """Set period_end attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.period_end = value
        return self

    def with_remark(self, value: Optional[DocumentationBlock]) -> "LifeCycleInfoBuilder":
        """Set remark attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.remark = value
        return self

    def with_use_insteads(self, items: list[Referrable]) -> "LifeCycleInfoBuilder":
        """Set use_insteads list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.use_insteads = list(items) if items else []
        return self


    def add_use_instead(self, item: Referrable) -> "LifeCycleInfoBuilder":
        """Add a single item to use_insteads list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.use_insteads.append(item)
        return self

    def clear_use_insteads(self) -> "LifeCycleInfoBuilder":
        """Clear all items from use_insteads list.

        Returns:
            self for method chaining
        """
        self._obj.use_insteads = []
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


    def build(self) -> LifeCycleInfo:
        """Build and return the LifeCycleInfo instance with validation."""
        self._validate_instance()
        pass
        return self._obj