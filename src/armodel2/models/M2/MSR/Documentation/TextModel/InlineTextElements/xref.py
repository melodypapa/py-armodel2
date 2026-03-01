"""Xref AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 320)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.MSR.Documentation.TextModel.InlineAttributeEnums import (
    ResolutionPolicyEnum,
    ShowContentEnum,
    ShowResourceAliasNameEnum,
    ShowResourceLongNameEnum,
    ShowResourceNumberEnum,
    ShowResourcePageEnum,
    ShowResourceShortNameEnum,
    ShowResourceTypeEnum,
    ShowSeeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel2.models.M2.MSR.Documentation.TextModel.SingleLanguageData.single_language_long_name import (
    SingleLanguageLongName,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Xref(ARObject):
    """AUTOSAR Xref."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "XREF"


    label1: Optional[SingleLanguageLongName]
    referrable_ref: Optional[ARRef]
    resolution_policy_enum: Optional[ResolutionPolicyEnum]
    show_content_enum: Optional[ShowContentEnum]
    show_resource_alias: Optional[ShowResourceAliasNameEnum]
    show_resource: Optional[ShowResourceTypeEnum]
    show_resource_long: Optional[ShowResourceLongNameEnum]
    show_resource_number: Optional[ShowResourceNumberEnum]
    show_resource_page: Optional[ShowResourcePageEnum]
    show_resource_short: Optional[ShowResourceShortNameEnum]
    show_see: Optional[ShowSeeEnum]
    _DESERIALIZE_DISPATCH = {
        "LABEL1": lambda obj, elem: setattr(obj, "label1", SerializationHelper.deserialize_by_tag(elem, "SingleLanguageLongName")),
        "REFERRABLE-REF": ("_POLYMORPHIC", "referrable_ref", ["ARPackage", "AclObjectSet", "AclOperation", "AclPermission", "AclRole", "AgeConstraint", "AggregationTailoring", "AliasNameSet", "AnalyzedExecutionTime", "AppOsTaskProxyToEcuTaskProxyMapping", "ApplicationArrayDataType", "ApplicationArrayElement", "ApplicationEndpoint", "ApplicationError", "ApplicationPartition", "ApplicationPartitionToEcuPartitionMapping", "ApplicationPrimitiveDataType", "ApplicationRecordDataType", "ApplicationRecordElement", "ApplicationSwComponentType", "ArbitraryEventTriggering", "ArgumentDataPrototype", "AssemblySwConnector", "AsynchronousServerCallPoint", "AsynchronousServerCallResultPoint", "AsynchronousServerCallReturnsEvent", "AtpDefinition", "AutosarOperationArgumentInstance", "AutosarVariableInstance", "BackgroundEvent", "BinaryManifestItem", "BinaryManifestItemDefinition", "BinaryManifestMetaDataField", "BinaryManifestProvideResource", "BinaryManifestRequireResource", "BinaryManifestResourceDefinition", "BlockState", "BlueprintMappingSet", "BswAsynchronousServerCallPoint", "BswAsynchronousServerCallResultPoint", "BswAsynchronousServerCallReturnsEvent", "BswBackgroundEvent", "BswCalledEntity", "BswCompositionTiming", "BswDataReceivedEvent", "BswDirectCallPoint", "BswDistinguishedPartition", "BswEntryRelationshipSet", "BswExternalTriggerOccurredEvent", "BswImplementation", "BswInternalBehavior", "BswInternalTriggerOccurredEvent", "BswInternalTriggeringPoint", "BswInterruptEntity", "BswInterruptEvent", "BswMgrNeeds", "BswModeManagerErrorEvent", "BswModeSwitchEvent", "BswModeSwitchedAckEvent", "BswModuleCallPoint", "BswModuleClientServerEntry", "BswModuleDependency", "BswModuleDescription", "BswModuleEntry", "BswModuleTiming", "BswOperationInvokedEvent", "BswOsTaskExecutionEvent", "BswSchedulableEntity", "BswSchedulerNamePrefix", "BswServiceDependencyIdent", "BswTimingEvent", "BswVariableAccess", "BuildAction", "BuildActionEnvironment", "BuildActionManifest", "BulkNvDataDescriptor", "BurstPatternEventTriggering", "BusMirrorChannelMappingCan", "BusMirrorChannelMappingFlexray", "BusMirrorChannelMappingIp", "CalibrationParameterValueSet", "CanCluster", "CanCommunicationConnector", "CanCommunicationController", "CanFrame", "CanFrameTriggering", "CanNmCluster", "CanNmNode", "CanPhysicalChannel", "CanTpAddress", "CanTpChannel", "CanTpConfig", "CanTpNode", "Caption", "Chapter", "ClassContentConditional", "ClientIdDefinition", "ClientIdDefinitionSet", "ClientServerInterface", "ClientServerInterfaceMapping", "ClientServerInterfaceToBswModuleEntryBlueprintMapping", "ClientServerOperation", "Code", "Collection", "ComManagementMapping", "ComMgrUserNeeds", "Compiler", "ComplexDeviceDriverSwComponentType", "CompositionSwComponentType", "CompuMethod", "ConcreteClassTailoring", "ConcretePatternEventTriggering", "ConsistencyNeeds", "ConsistencyNeedsBlueprintSet", "ConstantSpecification", "ConstantSpecificationMappingSet", "ConstraintTailoring", "ConsumedEventGroup", "ConsumedProvidedServiceInstanceGroup", "ConsumedServiceInstance", "ContainerIPdu", "CouplingElement", "CouplingElementSwitchDetails", "CouplingPort", "CouplingPortFifo", "CouplingPortScheduler", "CouplingPortShaper", "CouplingPortTrafficClassAssignment", "CpSoftwareCluster", "CpSoftwareClusterBinaryManifestDescriptor", "CpSoftwareClusterCommunicationResource", "CpSoftwareClusterMappingSet", "CpSoftwareClusterResourcePool", "CpSoftwareClusterResourceToApplicationPartitionMapping", "CpSoftwareClusterServiceResource", "CpSoftwareClusterToApplicationPartitionMapping", "CpSoftwareClusterToEcuInstanceMapping", "CpSoftwareClusterToResourceMapping", "CpSwClusterResourceToDiagDataElemMapping", "CpSwClusterResourceToDiagFunctionIdMapping", "CpSwClusterToDiagEventMapping", "CpSwClusterToDiagRoutineSubfunctionMapping", "CryptoEllipticCurveProps", "CryptoKeyManagementNeeds", "CryptoServiceCertificate", "CryptoServiceJobNeeds", "CryptoServiceKey", "CryptoServiceNeeds", "CryptoServicePrimitive", "CryptoServiceQueue", "CryptoSignatureScheme", "DataConstr", "DataExchangePoint", "DataPrototypeGroup", "DataReceiveErrorEvent", "DataReceivedEvent", "DataSendCompletedEvent", "DataTransformationSet", "DataTypeMappingSet", "DataWriteCompletedEvent", "DcmIPdu", "DdsCpConfig", "DdsCpConsumedServiceInstance", "DdsCpDomain", "DdsCpPartition", "DdsCpProvidedServiceInstance", "DdsCpQosProfile", "DdsCpTopic", "DefItem", "DelegationSwConnector", "DependencyOnArtifact", "DevelopmentError", "DiagEventDebounceCounterBased", "DiagEventDebounceMonitorInternal", "DiagnosticAccessPermission", "DiagnosticAging", "DiagnosticAuthRole", "DiagnosticAuthTransmitCertificate", "DiagnosticAuthTransmitCertificateEvaluation", "DiagnosticAuthTransmitCertificateMapping", "DiagnosticAuthenticationClass", "DiagnosticAuthenticationConfiguration", "DiagnosticClearDiagnosticInformation", "DiagnosticClearDiagnosticInformationClass", "DiagnosticClearResetEmissionRelatedInfo", "DiagnosticClearResetEmissionRelatedInfoClass", "DiagnosticComControl", "DiagnosticComControlClass", "DiagnosticCommunicationManagerNeeds", "DiagnosticComponentNeeds", "DiagnosticConnectedIndicator", "DiagnosticConnection", "DiagnosticContributionSet", "DiagnosticControlDTCSetting", "DiagnosticControlDTCSettingClass", "DiagnosticControlNeeds", "DiagnosticCustomServiceClass", "DiagnosticCustomServiceInstance", "DiagnosticDataElement", "DiagnosticDataIdentifier", "DiagnosticDataIdentifierSet", "DiagnosticDataTransfer", "DiagnosticDataTransferClass", "DiagnosticDeAuthentication", "DiagnosticDebounceAlgorithmProps", "DiagnosticDemProvidedDataMapping", "DiagnosticDynamicDataIdentifier", "DiagnosticDynamicallyDefineDataIdentifier", "DiagnosticDynamicallyDefineDataIdentifierClass", "DiagnosticEcuInstanceProps", "DiagnosticEcuReset", "DiagnosticEcuResetClass", "DiagnosticEnableCondition", "DiagnosticEnableConditionGroup", "DiagnosticEnableConditionNeeds", "DiagnosticEnableConditionPortMapping", "DiagnosticEnvBswModeElement", "DiagnosticEnvModeElement", "DiagnosticEnvSwcModeElement", "DiagnosticEnvironmentalCondition", "DiagnosticEvent", "DiagnosticEventInfoNeeds", "DiagnosticEventManagerNeeds", "DiagnosticEventNeeds", "DiagnosticEventPortMapping", "DiagnosticEventToDebounceAlgorithmMapping", "DiagnosticEventToEnableConditionGroupMapping", "DiagnosticEventToOperationCycleMapping", "DiagnosticEventToSecurityEventMapping", "DiagnosticEventToStorageConditionGroupMapping", "DiagnosticEventToTroubleCodeJ1939Mapping", "DiagnosticEventToTroubleCodeUdsMapping", "DiagnosticExtendedDataRecord", "DiagnosticFimAliasEvent", "DiagnosticFimAliasEventGroup", "DiagnosticFimAliasEventGroupMapping", "DiagnosticFimAliasEventMapping", "DiagnosticFimEventGroup", "DiagnosticFimFunctionMapping", "DiagnosticFreezeFrame", "DiagnosticFunctionIdentifier", "DiagnosticFunctionIdentifierInhibit", "DiagnosticFunctionInhibitSource", "DiagnosticIOControl", "DiagnosticIndicator", "DiagnosticInfoType", "DiagnosticInhibitSourceEventMapping", "DiagnosticIoControlClass", "DiagnosticIoControlNeeds", "DiagnosticIumpr", "DiagnosticIumprDenominatorGroup", "DiagnosticIumprGroup", "DiagnosticIumprToFunctionIdentifierMapping", "DiagnosticJ1939ExpandedFreezeFrame", "DiagnosticJ1939FreezeFrame", "DiagnosticJ1939Node", "DiagnosticJ1939Spn", "DiagnosticJ1939SpnMapping", "DiagnosticJ1939SwMapping", "DiagnosticMasterToSlaveEventMapping", "DiagnosticMeasurementIdentifier", "DiagnosticMemoryDestinationPrimary", "DiagnosticMemoryDestinationUserDefined", "DiagnosticMemoryIdentifier", "DiagnosticOperationCycle", "DiagnosticOperationCycleNeeds", "DiagnosticOperationCyclePortMapping", "DiagnosticParameterElement", "DiagnosticParameterIdent", "DiagnosticParameterIdentifier", "DiagnosticPowertrainFreezeFrame", "DiagnosticProofOfOwnership", "DiagnosticProtocol", "DiagnosticReadDTCInformation", "DiagnosticReadDTCInformationClass", "DiagnosticReadDataByIdentifier", "DiagnosticReadDataByIdentifierClass", "DiagnosticReadDataByPeriodicID", "DiagnosticReadDataByPeriodicIDClass", "DiagnosticReadMemoryByAddress", "DiagnosticReadMemoryByAddressClass", "DiagnosticReadScalingDataByIdentifier", "DiagnosticReadScalingDataByIdentifierClass", "DiagnosticRequestControlOfOnBoardDevice", "DiagnosticRequestControlOfOnBoardDeviceClass", "DiagnosticRequestCurrentPowertrainData", "DiagnosticRequestCurrentPowertrainDataClass", "DiagnosticRequestDownload", "DiagnosticRequestDownloadClass", "DiagnosticRequestEmissionRelatedDTC", "DiagnosticRequestEmissionRelatedDTCClass", "DiagnosticRequestEmissionRelatedDTCPermanentStatus", "DiagnosticRequestEmissionRelatedDTCPermanentStatusClass", "DiagnosticRequestFileTransfer", "DiagnosticRequestFileTransferClass", "DiagnosticRequestFileTransferNeeds", "DiagnosticRequestOnBoardMonitoringTestResults", "DiagnosticRequestOnBoardMonitoringTestResultsClass", "DiagnosticRequestPowertrainFreezeFrameData", "DiagnosticRequestPowertrainFreezeFrameDataClass", "DiagnosticRequestRoutineResults", "DiagnosticRequestUpload", "DiagnosticRequestUploadClass", "DiagnosticRequestVehicleInfo", "DiagnosticRequestVehicleInfoClass", "DiagnosticResponseOnEvent", "DiagnosticResponseOnEventClass", "DiagnosticRoutine", "DiagnosticRoutineControl", "DiagnosticRoutineControlClass", "DiagnosticRoutineNeeds", "DiagnosticSecureCodingMapping", "DiagnosticSecurityAccess", "DiagnosticSecurityAccessClass", "DiagnosticSecurityEventReportingModeMapping", "DiagnosticSecurityLevel", "DiagnosticServiceDataMapping", "DiagnosticServiceSwMapping", "DiagnosticServiceTable", "DiagnosticSession", "DiagnosticSessionControl", "DiagnosticSessionControlClass", "DiagnosticStartRoutine", "DiagnosticStopRoutine", "DiagnosticStorageCondition", "DiagnosticStorageConditionGroup", "DiagnosticStorageConditionNeeds", "DiagnosticStorageConditionPortMapping", "DiagnosticTestResult", "DiagnosticTestRoutineIdentifier", "DiagnosticTransferExit", "DiagnosticTransferExitClass", "DiagnosticTroubleCodeGroup", "DiagnosticTroubleCodeJ1939", "DiagnosticTroubleCodeObd", "DiagnosticTroubleCodeProps", "DiagnosticTroubleCodeUds", "DiagnosticTroubleCodeUdsToTroubleCodeObdMapping", "DiagnosticUploadDownloadNeeds", "DiagnosticValueNeeds", "DiagnosticVerifyCertificateBidirectional", "DiagnosticWriteDataByIdentifierClass", "DiagnosticWriteMemoryByAddressClass", "DiagnosticsCommunicationSecurityNeeds", "DltApplication", "DltArgument", "DltContext", "DltEcu", "DltLogChannel", "DltMessage", "DltUserNeeds", "DoIpActivationLineNeeds", "DoIpGidNeeds", "DoIpGidSynchronizationNeeds", "DoIpInterface", "DoIpLogicAddress", "DoIpLogicTargetAddressProps", "DoIpLogicTesterAddressProps", "DoIpPowerModeStatusNeeds", "DoIpRoutingActivation", "DoIpRoutingActivationAuthenticationNeeds", "DoIpRoutingActivationConfirmationNeeds", "DoIpTpConfig", "DocumentElementScope", "Documentation", "DocumentationContext", "DtcStatusChangeNotificationNeeds", "E2EProfileCompatibilityProps", "ECUMapping", "EOCEventRef", "EOCExecutableEntityRef", "EOCExecutableEntityRefGroup", "EcuAbstractionSwComponentType", "EcuInstance", "EcuPartition", "EcuStateMgrUserNeeds", "EcuTiming", "EcucAddInfoParamDef", "EcucBooleanParamDef", "EcucChoiceContainerDef", "EcucChoiceReferenceDef", "EcucContainerValue", "EcucDefinitionCollection", "EcucDestinationUriDef", "EcucDestinationUriDefSet", "EcucEnumerationLiteralDef", "EcucEnumerationParamDef", "EcucFloatParamDef", "EcucForeignReferenceDef", "EcucFunctionNameDef", "EcucInstanceReferenceDef", "EcucIntegerParamDef", "EcucLinkerSymbolDef", "EcucModuleConfigurationValues", "EcucModuleDef", "EcucMultilineStringParamDef", "EcucParamConfContainerDef", "EcucQuery", "EcucReferenceDef", "EcucStringParamDef", "EcucUriReferenceDef", "EcucValidationCondition", "EcucValueCollection", "EndToEndProtection", "EndToEndProtectionSet", "EnumerationMappingTable", "ErrorTracerNeeds", "EthIpProps", "EthTcpIpIcmpProps", "EthTcpIpProps", "EthTpConfig", "EthernetCluster", "EthernetCommunicationConnector", "EthernetCommunicationController", "EthernetFrameTriggering", "EthernetPhysicalChannel", "EthernetPriorityRegeneration", "EthernetWakeupSleepOnDatalineConfig", "EthernetWakeupSleepOnDatalineConfigSet", "EvaluatedVariantSet", "EventHandler", "ExclusiveArea", "ExclusiveAreaNestingOrder", "ExecutableEntityActivationReason", "ExecutionOrderConstraint", "ExecutionTimeConstraint", "ExternalTriggerOccurredEvent", "ExternalTriggeringPointIdent", "FMAttributeDef", "FMFeature", "FMFeatureMap", "FMFeatureMapAssertion", "FMFeatureMapCondition", "FMFeatureMapElement", "FMFeatureModel", "FMFeatureRelation", "FMFeatureRestriction", "FMFeatureSelection", "FMFeatureSelectionSet", "FirewallRule", "FlatInstanceDescriptor", "FlatMap", "FlexrayArTpConfig", "FlexrayArTpNode", "FlexrayCluster", "FlexrayCommunicationConnector", "FlexrayCommunicationController", "FlexrayFrame", "FlexrayFrameTriggering", "FlexrayNmCluster", "FlexrayNmNode", "FlexrayPhysicalChannel", "FlexrayTpConfig", "FlexrayTpConnectionControl", "FlexrayTpNode", "FlexrayTpPduPool", "FramePort", "FunctionInhibitionAvailabilityNeeds", "FunctionInhibitionNeeds", "Gateway", "GeneralPurposeConnection", "GeneralPurposeIPdu", "GeneralPurposePdu", "GenericEthernetFrame", "GlobalSupervisionNeeds", "GlobalTimeCanMaster", "GlobalTimeCanSlave", "GlobalTimeDomain", "GlobalTimeEthMaster", "GlobalTimeEthSlave", "GlobalTimeFrMaster", "GlobalTimeFrSlave", "GlobalTimeGateway", "HardwareTestNeeds", "HwAttributeDef", "HwAttributeLiteralDef", "HwCategory", "HwDescriptionEntity", "HwElement", "HwPin", "HwPinGroup", "HwType", "IEEE1722TpAafConnection", "IEEE1722TpAcfCan", "IEEE1722TpAcfCanPart", "IEEE1722TpAcfConnection", "IEEE1722TpAcfLin", "IEEE1722TpAcfLinPart", "IEEE1722TpConfig", "IEEE1722TpCrfConnection", "IEEE1722TpIidcConnection", "IPSecConfigProps", "IPSecRule", "IPduPort", "IPv6ExtHeaderFilterList", "IPv6ExtHeaderFilterSet", "ISignal", "ISignalGroup", "ISignalIPdu", "ISignalIPduGroup", "ISignalPort", "ISignalToIPduMapping", "ISignalTriggering", "IdsDesign", "IdsMgrCustomTimestampNeeds", "IdsMgrNeeds", "IdsmInstance", "IdsmProperties", "Ieee1722TpEthernetFrame", "ImplementationDataType", "ImplementationDataTypeElement", "ImplementationProps", "ImpositionTime", "IndicatorStatusNeeds", "InitEvent", "InternalTriggerOccurredEvent", "InternalTriggeringPoint", "InterpolationRoutineMappingSet", "J1939Cluster", "J1939ControllerApplication", "J1939DcmDm19Support", "J1939DcmIPdu", "J1939NmCluster", "J1939NmNode", "J1939RmIncomingRequestServiceNeeds", "J1939RmOutgoingRequestServiceNeeds", "J1939SharedAddressCluster", "J1939TpConfig", "J1939TpNode", "Keyword", "KeywordSet", "LatencyTimingConstraint", "LifeCycleInfoSet", "LifeCycleState", "LifeCycleStateDefinitionGroup", "LinCluster", "LinCommunicationConnector", "LinEventTriggeredFrame", "LinFrameTriggering", "LinMaster", "LinPhysicalChannel", "LinScheduleTable", "LinSlave", "LinSlaveConfigIdent", "LinSporadicFrame", "LinTpConfig", "LinTpNode", "LinUnconditionalFrame", "Linker", "LogAndTraceMessageCollectionSet", "MacMulticastGroup", "MacSecGlobalKayProps", "MacSecKayParticipant", "MacSecParticipantSet", "McDataInstance", "McFunction", "McGroup", "MeasuredExecutionTime", "MeasuredHeapUsage", "MeasuredStackUsage", "MemorySection", "ModeAccessPointIdent", "ModeDeclaration", "ModeDeclarationGroup", "ModeDeclarationGroupPrototype", "ModeDeclarationMapping", "ModeDeclarationMappingSet", "ModeInterfaceMapping", "ModeSwitchInterface", "ModeSwitchPoint", "ModeSwitchedAckEvent", "ModeTransition", "MultilanguageReferrable", "MultiplexedIPdu", "NPdu", "NetworkEndpoint", "NmConfig", "NmEcu", "NmPdu", "NvBlockDescriptor", "NvBlockNeeds", "NvBlockSwComponentType", "NvDataInterface", "ObdControlServiceNeeds", "ObdInfoServiceNeeds", "ObdMonitorServiceNeeds", "ObdPidServiceNeeds", "ObdRatioDenominatorNeeds", "ObdRatioServiceNeeds", "OffsetTimingConstraint", "OperationInvokedEvent", "OsTaskExecutionEvent", "OsTaskProxy", "PPortPrototype", "PRPortPrototype", "ParameterAccess", "ParameterDataPrototype", "ParameterInterface", "ParameterSwComponentType", "PassThroughSwConnector", "PduActivationRoutingGroup", "PduToFrameMapping", "PduTriggering", "PdurIPduGroup", "PerInstanceMemory", "PeriodicEventTriggering", "PhysicalDimension", "PhysicalDimensionMappingSet", "PncMappingIdent", "PortElementToCommunicationResourceMapping", "PortGroup", "PortInterfaceMappingSet", "PortPrototypeBlueprint", "PostBuildVariantCriterion", "PostBuildVariantCriterionValueSet", "PredefinedVariant", "PrimitiveAttributeTailoring", "ProvidedServiceInstance", "RPortPrototype", "RapidPrototypingScenario", "ReferenceTailoring", "ResourceConsumption", "RootSwCompositionPrototype", "RoughEstimateHeapUsage", "RoughEstimateOfExecutionTime", "RoughEstimateStackUsage", "RptComponent", "RptContainer", "RptExecutableEntity", "RptExecutableEntityEvent", "RptExecutionContext", "RptProfile", "RptServicePoint", "RteEventInCompositionSeparation", "RteEventInCompositionToOsTaskProxyMapping", "RteEventInSystemSeparation", "RteEventInSystemToOsTaskProxyMapping", "RunnableEntity", "RunnableEntityGroup", "RuntimeError", "SOMEIPTransformationProps", "Sdg", "SdgAggregationWithVariation", "SdgCaption", "SdgClass", "SdgDef", "SdgForeignReference", "SdgForeignReferenceWithVariation", "SdgPrimitiveAttribute", "SdgPrimitiveAttributeWithVariation", "SdgTailoring", "SecOcCryptoServiceMapping", "SectionNamePrefix", "SecureCommunicationAuthenticationProps", "SecureCommunicationFreshnessProps", "SecureCommunicationPropsSet", "SecureOnBoardCommunicationNeeds", "SecuredIPdu", "SecurityEventAggregationFilter", "SecurityEventContextMappingApplication", "SecurityEventContextMappingBswModule", "SecurityEventContextMappingCommConnector", "SecurityEventContextMappingFunctionalCluster", "SecurityEventContextProps", "SecurityEventDefinition", "SecurityEventFilterChain", "SecurityEventOneEveryNFilter", "SecurityEventStateFilter", "SenderReceiverInterface", "SensorActuatorSwComponentType", "ServiceInstanceCollectionSet", "ServiceProxySwComponentType", "ServiceSwComponentType", "SignalServiceTranslationElementProps", "SignalServiceTranslationEventProps", "SignalServiceTranslationProps", "SignalServiceTranslationPropsSet", "SingleLanguageReferrable", "SoAdRoutingGroup", "SoConIPduIdentifier", "SocketAddress", "SocketConnectionBundle", "SocketConnectionIpduIdentifierSet", "SomeipSdClientServiceInstanceConfig", "SomeipSdServerEventGroupTimingConfig", "SomeipSdServerServiceInstanceConfig", "SomeipTpChannel", "SomeipTpConfig", "SpecificationDocumentScope", "SporadicEventTriggering", "StaticSocketConnection", "Std", "StructuredReq", "SupervisedEntityCheckpointNeeds", "SupervisedEntityNeeds", "SwAddrMethod", "SwAxisType", "SwBaseType", "SwGenericAxisParamType", "SwRecordLayout", "SwServiceArg", "SwSystemconst", "SwSystemconstantValueSet", "SwcBswMapping", "SwcImplementation", "SwcInternalBehavior", "SwcModeManagerErrorEvent", "SwcModeSwitchEvent", "SwcServiceDependency", "SwcTiming", "SwcToApplicationPartitionMapping", "SwcToEcuMapping", "SwcToImplMapping", "SwitchAsynchronousTrafficShaperGroupEntry", "SwitchFlowMeteringEntry", "SwitchStreamFilterActionDestPortModification", "SwitchStreamFilterEntry", "SwitchStreamFilterRule", "SwitchStreamGateEntry", "SwitchStreamIdentification", "SymbolProps", "SyncTimeBaseMgrUserNeeds", "SynchronizationPointConstraint", "SynchronousServerCallPoint", "System", "SystemMapping", "SystemSignal", "SystemSignalGroup", "SystemSignalGroupToCommunicationResourceMapping", "SystemSignalToCommunicationResourceMapping", "SystemTiming", "TDCpSoftwareClusterMapping", "TDCpSoftwareClusterMappingSet", "TDCpSoftwareClusterResourceMapping", "TDEventBswInternalBehavior", "TDEventBswModeDeclaration", "TDEventBswModule", "TDEventComplex", "TDEventFrClusterCycleStart", "TDEventFrame", "TDEventFrameEthernet", "TDEventIPdu", "TDEventISignal", "TDEventModeDeclaration", "TDEventOperation", "TDEventSLLETPort", "TDEventSwcInternalBehavior", "TDEventSwcInternalBehaviorReference", "TDEventTTCanCycleStart", "TDEventTrigger", "TDEventVariableDataPrototype", "TDEventVfbReference", "TDLETZoneClock", "TcpOptionFilterList", "TcpOptionFilterSet", "TimeSyncServerConfiguration", "TimingClockSyncAccuracy", "TimingCondition", "TimingDescriptionEventChain", "TimingEvent", "TimingExtensionResource", "TimingModeInstance", "TlsCryptoCipherSuite", "TlsCryptoCipherSuiteProps", "TlsCryptoServiceMapping", "TlvDataIdDefinitionSet", "Topic1", "TpAddress", "TpConnectionIdent", "TraceableText", "TransformationPropsSet", "TransformationTechnology", "TransformerHardErrorEvent", "TransientFault", "Trigger", "TriggerInterface", "TriggerInterfaceMapping", "TtcanCluster", "TtcanCommunicationConnector", "TtcanCommunicationController", "TtcanPhysicalChannel", "UdpNmCluster", "UdpNmNode", "Unit", "UnitGroup", "UserDefinedCluster", "UserDefinedCommunicationConnector", "UserDefinedCommunicationController", "UserDefinedEthernetFrame", "UserDefinedGlobalTimeMaster", "UserDefinedGlobalTimeSlave", "UserDefinedIPdu", "UserDefinedPdu", "UserDefinedTransformationProps", "V2xDataManagerNeeds", "V2xFacUserNeeds", "V2xMUserNeeds", "VariableAccess", "VariableDataPrototype", "VariationPointProxy", "VendorSpecificServiceNeeds", "VfbTiming", "ViewMap", "ViewMapSet", "VlanConfig", "WaitPoint", "WorstCaseHeapUsage", "WorstCaseStackUsage", "Xdoc", "Xfile", "XrefTarget"]),
        "RESOLUTION-POLICY-ENUM": lambda obj, elem: setattr(obj, "resolution_policy_enum", ResolutionPolicyEnum.deserialize(elem)),
        "SHOW-CONTENT-ENUM": lambda obj, elem: setattr(obj, "show_content_enum", ShowContentEnum.deserialize(elem)),
        "SHOW-RESOURCE-ALIAS": lambda obj, elem: setattr(obj, "show_resource_alias", ShowResourceAliasNameEnum.deserialize(elem)),
        "SHOW-RESOURCE": lambda obj, elem: setattr(obj, "show_resource", ShowResourceTypeEnum.deserialize(elem)),
        "SHOW-RESOURCE-LONG": lambda obj, elem: setattr(obj, "show_resource_long", ShowResourceLongNameEnum.deserialize(elem)),
        "SHOW-RESOURCE-NUMBER": lambda obj, elem: setattr(obj, "show_resource_number", ShowResourceNumberEnum.deserialize(elem)),
        "SHOW-RESOURCE-PAGE": lambda obj, elem: setattr(obj, "show_resource_page", ShowResourcePageEnum.deserialize(elem)),
        "SHOW-RESOURCE-SHORT": lambda obj, elem: setattr(obj, "show_resource_short", ShowResourceShortNameEnum.deserialize(elem)),
        "SHOW-SEE": lambda obj, elem: setattr(obj, "show_see", ShowSeeEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize Xref."""
        super().__init__()
        self.label1: Optional[SingleLanguageLongName] = None
        self.referrable_ref: Optional[ARRef] = None
        self.resolution_policy_enum: Optional[ResolutionPolicyEnum] = None
        self.show_content_enum: Optional[ShowContentEnum] = None
        self.show_resource_alias: Optional[ShowResourceAliasNameEnum] = None
        self.show_resource: Optional[ShowResourceTypeEnum] = None
        self.show_resource_long: Optional[ShowResourceLongNameEnum] = None
        self.show_resource_number: Optional[ShowResourceNumberEnum] = None
        self.show_resource_page: Optional[ShowResourcePageEnum] = None
        self.show_resource_short: Optional[ShowResourceShortNameEnum] = None
        self.show_see: Optional[ShowSeeEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize Xref to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Xref, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize label1
        if self.label1 is not None:
            serialized = SerializationHelper.serialize_item(self.label1, "SingleLanguageLongName")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LABEL1")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize referrable_ref
        if self.referrable_ref is not None:
            serialized = SerializationHelper.serialize_item(self.referrable_ref, "Referrable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REFERRABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize resolution_policy_enum
        if self.resolution_policy_enum is not None:
            serialized = SerializationHelper.serialize_item(self.resolution_policy_enum, "ResolutionPolicyEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESOLUTION-POLICY-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_content_enum
        if self.show_content_enum is not None:
            serialized = SerializationHelper.serialize_item(self.show_content_enum, "ShowContentEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-CONTENT-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_resource_alias
        if self.show_resource_alias is not None:
            serialized = SerializationHelper.serialize_item(self.show_resource_alias, "ShowResourceAliasNameEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-RESOURCE-ALIAS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_resource
        if self.show_resource is not None:
            serialized = SerializationHelper.serialize_item(self.show_resource, "ShowResourceTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-RESOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_resource_long
        if self.show_resource_long is not None:
            serialized = SerializationHelper.serialize_item(self.show_resource_long, "ShowResourceLongNameEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-RESOURCE-LONG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_resource_number
        if self.show_resource_number is not None:
            serialized = SerializationHelper.serialize_item(self.show_resource_number, "ShowResourceNumberEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-RESOURCE-NUMBER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_resource_page
        if self.show_resource_page is not None:
            serialized = SerializationHelper.serialize_item(self.show_resource_page, "ShowResourcePageEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-RESOURCE-PAGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_resource_short
        if self.show_resource_short is not None:
            serialized = SerializationHelper.serialize_item(self.show_resource_short, "ShowResourceShortNameEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-RESOURCE-SHORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_see
        if self.show_see is not None:
            serialized = SerializationHelper.serialize_item(self.show_see, "ShowSeeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-SEE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Xref":
        """Deserialize XML element to Xref object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Xref object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Xref, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "LABEL1":
                setattr(obj, "label1", SerializationHelper.deserialize_by_tag(child, "SingleLanguageLongName"))
            elif tag == "REFERRABLE-REF":
                setattr(obj, "referrable_ref", ARRef.deserialize(child))
            elif tag == "RESOLUTION-POLICY-ENUM":
                setattr(obj, "resolution_policy_enum", ResolutionPolicyEnum.deserialize(child))
            elif tag == "SHOW-CONTENT-ENUM":
                setattr(obj, "show_content_enum", ShowContentEnum.deserialize(child))
            elif tag == "SHOW-RESOURCE-ALIAS":
                setattr(obj, "show_resource_alias", ShowResourceAliasNameEnum.deserialize(child))
            elif tag == "SHOW-RESOURCE":
                setattr(obj, "show_resource", ShowResourceTypeEnum.deserialize(child))
            elif tag == "SHOW-RESOURCE-LONG":
                setattr(obj, "show_resource_long", ShowResourceLongNameEnum.deserialize(child))
            elif tag == "SHOW-RESOURCE-NUMBER":
                setattr(obj, "show_resource_number", ShowResourceNumberEnum.deserialize(child))
            elif tag == "SHOW-RESOURCE-PAGE":
                setattr(obj, "show_resource_page", ShowResourcePageEnum.deserialize(child))
            elif tag == "SHOW-RESOURCE-SHORT":
                setattr(obj, "show_resource_short", ShowResourceShortNameEnum.deserialize(child))
            elif tag == "SHOW-SEE":
                setattr(obj, "show_see", ShowSeeEnum.deserialize(child))

        return obj



class XrefBuilder(BuilderBase):
    """Builder for Xref with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Xref = Xref()


    def with_label1(self, value: Optional[SingleLanguageLongName]) -> "XrefBuilder":
        """Set label1 attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.label1 = value
        return self

    def with_referrable(self, value: Optional[Referrable]) -> "XrefBuilder":
        """Set referrable attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.referrable = value
        return self

    def with_resolution_policy_enum(self, value: Optional[ResolutionPolicyEnum]) -> "XrefBuilder":
        """Set resolution_policy_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.resolution_policy_enum = value
        return self

    def with_show_content_enum(self, value: Optional[ShowContentEnum]) -> "XrefBuilder":
        """Set show_content_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.show_content_enum = value
        return self

    def with_show_resource_alias(self, value: Optional[ShowResourceAliasNameEnum]) -> "XrefBuilder":
        """Set show_resource_alias attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.show_resource_alias = value
        return self

    def with_show_resource(self, value: Optional[ShowResourceTypeEnum]) -> "XrefBuilder":
        """Set show_resource attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.show_resource = value
        return self

    def with_show_resource_long(self, value: Optional[ShowResourceLongNameEnum]) -> "XrefBuilder":
        """Set show_resource_long attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.show_resource_long = value
        return self

    def with_show_resource_number(self, value: Optional[ShowResourceNumberEnum]) -> "XrefBuilder":
        """Set show_resource_number attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.show_resource_number = value
        return self

    def with_show_resource_page(self, value: Optional[ShowResourcePageEnum]) -> "XrefBuilder":
        """Set show_resource_page attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.show_resource_page = value
        return self

    def with_show_resource_short(self, value: Optional[ShowResourceShortNameEnum]) -> "XrefBuilder":
        """Set show_resource_short attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.show_resource_short = value
        return self

    def with_show_see(self, value: Optional[ShowSeeEnum]) -> "XrefBuilder":
        """Set show_see attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.show_see = value
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


    def build(self) -> Xref:
        """Build and return the Xref instance with validation."""
        self._validate_instance()
        pass
        return self._obj