"""AliasNameAssignment AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 175)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 968)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_FlatMap.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_instance_descriptor import (
    FlatInstanceDescriptor,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AliasNameAssignment(ARObject):
    """AUTOSAR AliasNameAssignment."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ALIAS-NAME-ASSIGNMENT"


    flat_instance_ref: Optional[ARRef]
    identifiable_ref: Optional[ARRef]
    label: Optional[MultilanguageLongName]
    short_label: Optional[String]
    _DESERIALIZE_DISPATCH = {
        "FLAT-INSTANCE-REF": lambda obj, elem: setattr(obj, "flat_instance_ref", ARRef.deserialize(elem)),
        "IDENTIFIABLE-REF": ("_POLYMORPHIC", "identifiable_ref", ["ARPackage", "AbstractDoIpLogicAddressProps", "AbstractEvent", "AbstractImplementationDataTypeElement", "AbstractSecurityEventFilter", "AbstractSecurityIdsmInstanceFilter", "AbstractServiceInstance", "AclObjectSet", "AclOperation", "AclPermission", "AclRole", "AgeConstraint", "AggregationTailoring", "AliasNameSet", "AnalyzedExecutionTime", "AppOsTaskProxyToEcuTaskProxyMapping", "ApplicationArrayDataType", "ApplicationArrayElement", "ApplicationEndpoint", "ApplicationError", "ApplicationPartition", "ApplicationPartitionToEcuPartitionMapping", "ApplicationPrimitiveDataType", "ApplicationRecordDataType", "ApplicationRecordElement", "ApplicationSwComponentType", "AppliedStandard", "ArbitraryEventTriggering", "ArgumentDataPrototype", "AssemblySwConnector", "AsynchronousServerCallPoint", "AsynchronousServerCallResultPoint", "AsynchronousServerCallReturnsEvent", "AtpBlueprint", "AtpBlueprintable", "AtpClassifier", "AtpFeature", "AutosarOperationArgumentInstance", "AutosarVariableInstance", "BackgroundEvent", "BinaryManifestAddressableObject", "BinaryManifestItem", "BinaryManifestItemDefinition", "BinaryManifestMetaDataField", "BinaryManifestProvideResource", "BinaryManifestRequireResource", "BinaryManifestResource", "BinaryManifestResourceDefinition", "BlockState", "BlueprintMappingSet", "BswAsynchronousServerCallReturnsEvent", "BswBackgroundEvent", "BswCalledEntity", "BswCompositionTiming", "BswDataReceivedEvent", "BswEntryRelationshipSet", "BswExternalTriggerOccurredEvent", "BswImplementation", "BswInternalBehavior", "BswInternalTriggerOccurredEvent", "BswInternalTriggeringPoint", "BswInterruptEntity", "BswInterruptEvent", "BswMgrNeeds", "BswModeManagerErrorEvent", "BswModeSwitchEvent", "BswModeSwitchedAckEvent", "BswModuleDependency", "BswModuleDescription", "BswModuleEntry", "BswModuleTiming", "BswOperationInvokedEvent", "BswOsTaskExecutionEvent", "BswSchedulableEntity", "BswServiceDependencyIdent", "BswTimingEvent", "BuildAction", "BuildActionEntity", "BuildActionEnvironment", "BuildActionManifest", "BulkNvDataDescriptor", "BurstPatternEventTriggering", "BusMirrorChannelMappingCan", "BusMirrorChannelMappingFlexray", "BusMirrorChannelMappingIp", "CalibrationParameterValueSet", "CanCluster", "CanCommunicationConnector", "CanCommunicationController", "CanFrame", "CanFrameTriggering", "CanNmCluster", "CanNmNode", "CanPhysicalChannel", "CanTpAddress", "CanTpChannel", "CanTpConfig", "CanTpNode", "Chapter", "ClassContentConditional", "ClientIdDefinition", "ClientIdDefinitionSet", "ClientServerInterface", "ClientServerInterfaceMapping", "ClientServerInterfaceToBswModuleEntryBlueprintMapping", "ClientServerOperation", "Code", "CollectableElement", "Collection", "ComManagementMapping", "ComMgrUserNeeds", "CommConnectorPort", "CommunicationConnector", "CommunicationController", "Compiler", "ComplexDeviceDriverSwComponentType", "CompositionSwComponentType", "CompuMethod", "ConcreteClassTailoring", "ConcretePatternEventTriggering", "ConsistencyNeeds", "ConsistencyNeedsBlueprintSet", "ConstantSpecification", "ConstantSpecificationMappingSet", "ConstraintTailoring", "ConsumedEventGroup", "ConsumedProvidedServiceInstanceGroup", "ConsumedServiceInstance", "ContainerIPdu", "CouplingElement", "CouplingElementAbstractDetails", "CouplingElementSwitchDetails", "CouplingPort", "CouplingPortAbstractShaper", "CouplingPortFifo", "CouplingPortScheduler", "CouplingPortShaper", "CouplingPortStructuralElement", "CpSoftwareCluster", "CpSoftwareClusterBinaryManifestDescriptor", "CpSoftwareClusterCommunicationResource", "CpSoftwareClusterMappingSet", "CpSoftwareClusterResource", "CpSoftwareClusterResourcePool", "CpSoftwareClusterResourceToApplicationPartitionMapping", "CpSoftwareClusterServiceResource", "CpSoftwareClusterToApplicationPartitionMapping", "CpSoftwareClusterToEcuInstanceMapping", "CpSoftwareClusterToResourceMapping", "CpSwClusterResourceToDiagDataElemMapping", "CpSwClusterResourceToDiagFunctionIdMapping", "CpSwClusterToDiagEventMapping", "CpSwClusterToDiagRoutineSubfunctionMapping", "CryptoEllipticCurveProps", "CryptoKeyManagementNeeds", "CryptoServiceCertificate", "CryptoServiceJobNeeds", "CryptoServiceKey", "CryptoServiceMapping", "CryptoServiceNeeds", "CryptoServicePrimitive", "CryptoServiceQueue", "CryptoSignatureScheme", "Data", "DataConstr", "DataExchangePoint", "DataPrototypeGroup", "DataReceiveErrorEvent", "DataReceivedEvent", "DataSendCompletedEvent", "DataTransformationSet", "DataTypeMappingSet", "DataWriteCompletedEvent", "DcmIPdu", "DdsCpConfig", "DdsCpConsumedServiceInstance", "DdsCpDomain", "DdsCpPartition", "DdsCpProvidedServiceInstance", "DdsCpQosProfile", "DdsCpTopic", "DelegationSwConnector", "DependencyOnArtifact", "DevelopmentError", "DiagEventDebounceAlgorithm", "DiagEventDebounceCounterBased", "DiagEventDebounceMonitorInternal", "DiagnosticAccessPermission", "DiagnosticAging", "DiagnosticAuthRole", "DiagnosticAuthTransmitCertificate", "DiagnosticAuthTransmitCertificateEvaluation", "DiagnosticAuthTransmitCertificateMapping", "DiagnosticAuthenticationClass", "DiagnosticAuthenticationConfiguration", "DiagnosticClearDiagnosticInformation", "DiagnosticClearDiagnosticInformationClass", "DiagnosticClearResetEmissionRelatedInfo", "DiagnosticClearResetEmissionRelatedInfoClass", "DiagnosticComControl", "DiagnosticComControlClass", "DiagnosticCommunicationManagerNeeds", "DiagnosticComponentNeeds", "DiagnosticConnectedIndicator", "DiagnosticConnection", "DiagnosticContributionSet", "DiagnosticControlDTCSetting", "DiagnosticControlDTCSettingClass", "DiagnosticControlNeeds", "DiagnosticCustomServiceClass", "DiagnosticCustomServiceInstance", "DiagnosticDataElement", "DiagnosticDataIdentifier", "DiagnosticDataIdentifierSet", "DiagnosticDataTransfer", "DiagnosticDataTransferClass", "DiagnosticDeAuthentication", "DiagnosticDebounceAlgorithmProps", "DiagnosticDemProvidedDataMapping", "DiagnosticDynamicDataIdentifier", "DiagnosticDynamicallyDefineDataIdentifier", "DiagnosticDynamicallyDefineDataIdentifierClass", "DiagnosticEcuInstanceProps", "DiagnosticEcuReset", "DiagnosticEcuResetClass", "DiagnosticEnableCondition", "DiagnosticEnableConditionGroup", "DiagnosticEnableConditionNeeds", "DiagnosticEnableConditionPortMapping", "DiagnosticEnvironmentalCondition", "DiagnosticEvent", "DiagnosticEventInfoNeeds", "DiagnosticEventManagerNeeds", "DiagnosticEventNeeds", "DiagnosticEventPortMapping", "DiagnosticEventToDebounceAlgorithmMapping", "DiagnosticEventToEnableConditionGroupMapping", "DiagnosticEventToOperationCycleMapping", "DiagnosticEventToSecurityEventMapping", "DiagnosticEventToStorageConditionGroupMapping", "DiagnosticEventToTroubleCodeJ1939Mapping", "DiagnosticEventToTroubleCodeUdsMapping", "DiagnosticExtendedDataRecord", "DiagnosticFimAliasEvent", "DiagnosticFimAliasEventGroup", "DiagnosticFimAliasEventGroupMapping", "DiagnosticFimAliasEventMapping", "DiagnosticFimEventGroup", "DiagnosticFimFunctionMapping", "DiagnosticFreezeFrame", "DiagnosticFunctionIdentifier", "DiagnosticFunctionIdentifierInhibit", "DiagnosticFunctionInhibitSource", "DiagnosticIOControl", "DiagnosticIndicator", "DiagnosticInfoType", "DiagnosticInhibitSourceEventMapping", "DiagnosticIoControlClass", "DiagnosticIoControlNeeds", "DiagnosticIumpr", "DiagnosticIumprDenominatorGroup", "DiagnosticIumprGroup", "DiagnosticIumprToFunctionIdentifierMapping", "DiagnosticJ1939ExpandedFreezeFrame", "DiagnosticJ1939FreezeFrame", "DiagnosticJ1939Node", "DiagnosticJ1939Spn", "DiagnosticJ1939SpnMapping", "DiagnosticJ1939SwMapping", "DiagnosticMasterToSlaveEventMapping", "DiagnosticMeasurementIdentifier", "DiagnosticMemoryDestinationPrimary", "DiagnosticMemoryDestinationUserDefined", "DiagnosticMemoryIdentifier", "DiagnosticOperationCycle", "DiagnosticOperationCycleNeeds", "DiagnosticOperationCyclePortMapping", "DiagnosticParameterElement", "DiagnosticParameterIdent", "DiagnosticParameterIdentifier", "DiagnosticPowertrainFreezeFrame", "DiagnosticProofOfOwnership", "DiagnosticProtocol", "DiagnosticReadDTCInformation", "DiagnosticReadDTCInformationClass", "DiagnosticReadDataByIdentifier", "DiagnosticReadDataByIdentifierClass", "DiagnosticReadDataByPeriodicID", "DiagnosticReadDataByPeriodicIDClass", "DiagnosticReadMemoryByAddress", "DiagnosticReadMemoryByAddressClass", "DiagnosticReadScalingDataByIdentifier", "DiagnosticReadScalingDataByIdentifierClass", "DiagnosticRequestControlOfOnBoardDevice", "DiagnosticRequestControlOfOnBoardDeviceClass", "DiagnosticRequestCurrentPowertrainData", "DiagnosticRequestCurrentPowertrainDataClass", "DiagnosticRequestDownload", "DiagnosticRequestDownloadClass", "DiagnosticRequestEmissionRelatedDTC", "DiagnosticRequestEmissionRelatedDTCClass", "DiagnosticRequestEmissionRelatedDTCPermanentStatus", "DiagnosticRequestEmissionRelatedDTCPermanentStatusClass", "DiagnosticRequestFileTransfer", "DiagnosticRequestFileTransferClass", "DiagnosticRequestFileTransferNeeds", "DiagnosticRequestOnBoardMonitoringTestResults", "DiagnosticRequestOnBoardMonitoringTestResultsClass", "DiagnosticRequestPowertrainFreezeFrameData", "DiagnosticRequestPowertrainFreezeFrameDataClass", "DiagnosticRequestRoutineResults", "DiagnosticRequestUpload", "DiagnosticRequestUploadClass", "DiagnosticRequestVehicleInfo", "DiagnosticRequestVehicleInfoClass", "DiagnosticResponseOnEvent", "DiagnosticResponseOnEventClass", "DiagnosticRoutine", "DiagnosticRoutineControl", "DiagnosticRoutineControlClass", "DiagnosticRoutineNeeds", "DiagnosticRoutineSubfunction", "DiagnosticSecureCodingMapping", "DiagnosticSecurityAccess", "DiagnosticSecurityAccessClass", "DiagnosticSecurityEventReportingModeMapping", "DiagnosticSecurityLevel", "DiagnosticServiceDataMapping", "DiagnosticServiceSwMapping", "DiagnosticServiceTable", "DiagnosticSession", "DiagnosticSessionControl", "DiagnosticSessionControlClass", "DiagnosticStartRoutine", "DiagnosticStopRoutine", "DiagnosticStorageCondition", "DiagnosticStorageConditionGroup", "DiagnosticStorageConditionNeeds", "DiagnosticStorageConditionPortMapping", "DiagnosticTestResult", "DiagnosticTestRoutineIdentifier", "DiagnosticTransferExit", "DiagnosticTransferExitClass", "DiagnosticTroubleCodeGroup", "DiagnosticTroubleCodeJ1939", "DiagnosticTroubleCodeObd", "DiagnosticTroubleCodeProps", "DiagnosticTroubleCodeUds", "DiagnosticTroubleCodeUdsToTroubleCodeObdMapping", "DiagnosticUploadDownloadNeeds", "DiagnosticValueNeeds", "DiagnosticVerifyCertificateBidirectional", "DiagnosticWriteDataByIdentifierClass", "DiagnosticWriteMemoryByAddressClass", "DiagnosticsCommunicationSecurityNeeds", "DltApplication", "DltArgument", "DltContext", "DltEcu", "DltLogChannel", "DltMessage", "DltUserNeeds", "DoIpActivationLineNeeds", "DoIpGidNeeds", "DoIpGidSynchronizationNeeds", "DoIpInterface", "DoIpLogicAddress", "DoIpLogicTargetAddressProps", "DoIpLogicTesterAddressProps", "DoIpPowerModeStatusNeeds", "DoIpRoutingActivation", "DoIpRoutingActivationAuthenticationNeeds", "DoIpRoutingActivationConfirmationNeeds", "DoIpTpConfig", "DocumentElementScope", "Documentation", "DtcStatusChangeNotificationNeeds", "E2EProfileCompatibilityProps", "ECUMapping", "EOCEventRef", "EOCExecutableEntityRef", "EOCExecutableEntityRefAbstract", "EOCExecutableEntityRefGroup", "EcuAbstractionSwComponentType", "EcuInstance", "EcuPartition", "EcuStateMgrUserNeeds", "EcuTiming", "EcucAddInfoParamDef", "EcucBooleanParamDef", "EcucChoiceContainerDef", "EcucChoiceReferenceDef", "EcucContainerValue", "EcucDefinitionCollection", "EcucDefinitionElement", "EcucDestinationUriDef", "EcucDestinationUriDefSet", "EcucEnumerationLiteralDef", "EcucEnumerationParamDef", "EcucFloatParamDef", "EcucForeignReferenceDef", "EcucFunctionNameDef", "EcucInstanceReferenceDef", "EcucIntegerParamDef", "EcucLinkerSymbolDef", "EcucModuleConfigurationValues", "EcucModuleDef", "EcucMultilineStringParamDef", "EcucParamConfContainerDef", "EcucQuery", "EcucReferenceDef", "EcucStringParamDef", "EcucUriReferenceDef", "EcucValidationCondition", "EcucValueCollection", "EndToEndProtection", "EndToEndProtectionSet", "EnumerationMappingTable", "ErrorTracerNeeds", "EthIpProps", "EthTcpIpIcmpProps", "EthTcpIpProps", "EthTpConfig", "EthernetCluster", "EthernetCommunicationConnector", "EthernetCommunicationController", "EthernetFrameTriggering", "EthernetPhysicalChannel", "EthernetWakeupSleepOnDatalineConfig", "EthernetWakeupSleepOnDatalineConfigSet", "EvaluatedVariantSet", "EventHandler", "ExclusiveArea", "ExecutableEntity", "ExecutionOrderConstraint", "ExecutionTime", "ExecutionTimeConstraint", "ExternalTriggerOccurredEvent", "ExternalTriggeringPointIdent", "FMAttributeDef", "FMFeature", "FMFeatureMap", "FMFeatureMapAssertion", "FMFeatureMapCondition", "FMFeatureMapElement", "FMFeatureModel", "FMFeatureRelation", "FMFeatureRestriction", "FMFeatureSelection", "FMFeatureSelectionSet", "FirewallRule", "FlatInstanceDescriptor", "FlatMap", "FlexrayArTpConfig", "FlexrayArTpNode", "FlexrayCluster", "FlexrayCommunicationConnector", "FlexrayCommunicationController", "FlexrayFrame", "FlexrayFrameTriggering", "FlexrayNmCluster", "FlexrayNmNode", "FlexrayPhysicalChannel", "FlexrayTpConfig", "FlexrayTpConnectionControl", "FlexrayTpNode", "FlexrayTpPduPool", "FramePort", "FrameTriggering", "FunctionInhibitionAvailabilityNeeds", "FunctionInhibitionNeeds", "Gateway", "GeneralParameter", "GeneralPurposeConnection", "GeneralPurposeIPdu", "GeneralPurposePdu", "GenericEthernetFrame", "GlobalSupervisionNeeds", "GlobalTimeCanMaster", "GlobalTimeCanSlave", "GlobalTimeDomain", "GlobalTimeEthMaster", "GlobalTimeEthSlave", "GlobalTimeFrMaster", "GlobalTimeFrSlave", "GlobalTimeGateway", "GlobalTimeMaster", "GlobalTimeSlave", "HardwareTestNeeds", "HeapUsage", "HwAttributeDef", "HwAttributeLiteralDef", "HwCategory", "HwElement", "HwPin", "HwPinGroup", "HwType", "IEEE1722TpAafConnection", "IEEE1722TpAcfBus", "IEEE1722TpAcfBusPart", "IEEE1722TpAcfCan", "IEEE1722TpAcfCanPart", "IEEE1722TpAcfConnection", "IEEE1722TpAcfLin", "IEEE1722TpAcfLinPart", "IEEE1722TpConfig", "IEEE1722TpCrfConnection", "IEEE1722TpIidcConnection", "IPSecConfigProps", "IPSecRule", "IPduPort", "IPv6ExtHeaderFilterList", "IPv6ExtHeaderFilterSet", "ISignal", "ISignalGroup", "ISignalIPdu", "ISignalIPduGroup", "ISignalPort", "ISignalToIPduMapping", "ISignalTriggering", "IdentCaption", "IdsDesign", "IdsMgrCustomTimestampNeeds", "IdsMgrNeeds", "IdsmInstance", "IdsmProperties", "Ieee1722TpEthernetFrame", "ImplementationDataType", "ImplementationDataTypeElement", "ImpositionTime", "IndicatorStatusNeeds", "InitEvent", "InternalTriggerOccurredEvent", "InternalTriggeringPoint", "InterpolationRoutineMappingSet", "J1939Cluster", "J1939ControllerApplication", "J1939DcmDm19Support", "J1939DcmIPdu", "J1939NmCluster", "J1939NmNode", "J1939RmIncomingRequestServiceNeeds", "J1939RmOutgoingRequestServiceNeeds", "J1939SharedAddressCluster", "J1939TpConfig", "J1939TpNode", "Keyword", "KeywordSet", "LatencyTimingConstraint", "LifeCycleInfoSet", "LifeCycleState", "LifeCycleStateDefinitionGroup", "LinCluster", "LinCommunicationConnector", "LinEventTriggeredFrame", "LinFrameTriggering", "LinMaster", "LinPhysicalChannel", "LinScheduleTable", "LinSlave", "LinSporadicFrame", "LinTpConfig", "LinTpNode", "LinUnconditionalFrame", "Linker", "LogAndTraceMessageCollectionSet", "MacMulticastGroup", "MacSecGlobalKayProps", "MacSecKayParticipant", "MacSecParticipantSet", "McDataInstance", "McFunction", "McGroup", "MeasuredExecutionTime", "MeasuredHeapUsage", "MeasuredStackUsage", "MemorySection", "ModeAccessPointIdent", "ModeDeclaration", "ModeDeclarationGroup", "ModeDeclarationGroupPrototype", "ModeDeclarationMapping", "ModeDeclarationMappingSet", "ModeInterfaceMapping", "ModeSwitchInterface", "ModeSwitchPoint", "ModeSwitchedAckEvent", "ModeTransition", "MultiplexedIPdu", "NPdu", "NetworkEndpoint", "NmCluster", "NmConfig", "NmEcu", "NmNode", "NmPdu", "NvBlockDescriptor", "NvBlockNeeds", "NvBlockSwComponentType", "NvDataInterface", "ObdControlServiceNeeds", "ObdInfoServiceNeeds", "ObdMonitorServiceNeeds", "ObdPidServiceNeeds", "ObdRatioDenominatorNeeds", "ObdRatioServiceNeeds", "OffsetTimingConstraint", "OperationInvokedEvent", "OsTaskExecutionEvent", "OsTaskProxy", "PPortPrototype", "PRPortPrototype", "PackageableElement", "ParameterAccess", "ParameterDataPrototype", "ParameterInterface", "ParameterSwComponentType", "PassThroughSwConnector", "PduActivationRoutingGroup", "PduToFrameMapping", "PduTriggering", "PdurIPduGroup", "PerInstanceMemory", "PeriodicEventTriggering", "PhysicalChannel", "PhysicalDimension", "PhysicalDimensionMappingSet", "PortElementToCommunicationResourceMapping", "PortGroup", "PortInterfaceMapping", "PortInterfaceMappingSet", "PortPrototypeBlueprint", "PossibleErrorReaction", "PostBuildVariantCriterion", "PostBuildVariantCriterionValueSet", "PredefinedVariant", "PrimitiveAttributeTailoring", "ProvidedServiceInstance", "RPortPrototype", "RapidPrototypingScenario", "ReferenceTailoring", "ResourceConsumption", "RootSwCompositionPrototype", "RoughEstimateHeapUsage", "RoughEstimateOfExecutionTime", "RoughEstimateStackUsage", "RptComponent", "RptContainer", "RptExecutableEntity", "RptExecutableEntityEvent", "RptExecutionContext", "RptProfile", "RptServicePoint", "RteEventInCompositionSeparation", "RteEventInCompositionToOsTaskProxyMapping", "RteEventInSystemSeparation", "RteEventInSystemToOsTaskProxyMapping", "RunnableEntity", "RunnableEntityGroup", "RuntimeError", "SOMEIPTransformationProps", "Sdg", "SdgAggregationWithVariation", "SdgAttribute", "SdgClass", "SdgDef", "SdgForeignReference", "SdgForeignReferenceWithVariation", "SdgPrimitiveAttribute", "SdgPrimitiveAttributeWithVariation", "SdgTailoring", "SecOcCryptoServiceMapping", "SecureCommunicationAuthenticationProps", "SecureCommunicationFreshnessProps", "SecureCommunicationPropsSet", "SecureOnBoardCommunicationNeeds", "SecuredIPdu", "SecurityEventAggregationFilter", "SecurityEventContextMappingApplication", "SecurityEventContextMappingBswModule", "SecurityEventContextMappingCommConnector", "SecurityEventContextMappingFunctionalCluster", "SecurityEventContextProps", "SecurityEventDefinition", "SecurityEventFilterChain", "SecurityEventOneEveryNFilter", "SecurityEventStateFilter", "SenderReceiverInterface", "SensorActuatorSwComponentType", "ServerCallPoint", "ServiceInstanceCollectionSet", "ServiceNeeds", "ServiceProxySwComponentType", "ServiceSwComponentType", "SignalServiceTranslationElementProps", "SignalServiceTranslationEventProps", "SignalServiceTranslationProps", "SignalServiceTranslationPropsSet", "SoAdRoutingGroup", "SocketAddress", "SocketConnectionIpduIdentifierSet", "SomeipSdClientServiceInstanceConfig", "SomeipSdServerEventGroupTimingConfig", "SomeipSdServerServiceInstanceConfig", "SomeipTpChannel", "SomeipTpConfig", "SpecElementReference", "SpecificationDocumentScope", "SporadicEventTriggering", "StackUsage", "StaticSocketConnection", "StructuredReq", "SupervisedEntityCheckpointNeeds", "SupervisedEntityNeeds", "SwAddrMethod", "SwAxisType", "SwBaseType", "SwGenericAxisParamType", "SwRecordLayout", "SwServiceArg", "SwSystemconst", "SwSystemconstantValueSet", "SwcBswMapping", "SwcImplementation", "SwcInternalBehavior", "SwcModeManagerErrorEvent", "SwcModeSwitchEvent", "SwcServiceDependency", "SwcTiming", "SwcToApplicationPartitionMapping", "SwcToEcuMapping", "SwcToImplMapping", "SwitchAsynchronousTrafficShaperGroupEntry", "SwitchFlowMeteringEntry", "SwitchStreamFilterActionDestPortModification", "SwitchStreamFilterEntry", "SwitchStreamFilterRule", "SwitchStreamGateEntry", "SwitchStreamIdentification", "SyncTimeBaseMgrUserNeeds", "SynchronizationPointConstraint", "SynchronousServerCallPoint", "System", "SystemMapping", "SystemSignal", "SystemSignalGroup", "SystemSignalGroupToCommunicationResourceMapping", "SystemSignalToCommunicationResourceMapping", "SystemTiming", "TDCpSoftwareClusterMapping", "TDCpSoftwareClusterMappingSet", "TDCpSoftwareClusterResourceMapping", "TDEventBswInternalBehavior", "TDEventBswModeDeclaration", "TDEventBswModule", "TDEventComplex", "TDEventFrClusterCycleStart", "TDEventFrame", "TDEventFrameEthernet", "TDEventIPdu", "TDEventISignal", "TDEventModeDeclaration", "TDEventOperation", "TDEventSLLETPort", "TDEventSwcInternalBehavior", "TDEventSwcInternalBehaviorReference", "TDEventTTCanCycleStart", "TDEventTrigger", "TDEventVariableDataPrototype", "TDEventVfbReference", "TDLETZoneClock", "TcpOptionFilterList", "TcpOptionFilterSet", "TimingClock", "TimingClockSyncAccuracy", "TimingCondition", "TimingConstraint", "TimingDescription", "TimingDescriptionEventChain", "TimingEvent", "TimingExtensionResource", "TimingModeInstance", "TlsCryptoCipherSuite", "TlsCryptoCipherSuiteProps", "TlsCryptoServiceMapping", "TlvDataIdDefinitionSet", "Topic1", "TpAddress", "TraceableTable", "TraceableText", "TracedFailure", "Transformation", "TransformationProps", "TransformationPropsSet", "TransformationTechnology", "TransformerHardErrorEvent", "TransientFault", "Trigger", "TriggerInterface", "TriggerInterfaceMapping", "TtcanCluster", "TtcanCommunicationConnector", "TtcanCommunicationController", "TtcanPhysicalChannel", "UdpNmCluster", "UdpNmNode", "Unit", "UnitGroup", "UserDefinedCluster", "UserDefinedCommunicationConnector", "UserDefinedCommunicationController", "UserDefinedEthernetFrame", "UserDefinedGlobalTimeMaster", "UserDefinedGlobalTimeSlave", "UserDefinedIPdu", "UserDefinedPdu", "UserDefinedTransformationProps", "V2xDataManagerNeeds", "V2xFacUserNeeds", "V2xMUserNeeds", "VariableAccess", "VariableDataPrototype", "VariationPointProxy", "VendorSpecificServiceNeeds", "VfbTiming", "ViewMap", "ViewMapSet", "VlanConfig", "WaitPoint", "WorstCaseHeapUsage", "WorstCaseStackUsage"]),
        "LABEL": lambda obj, elem: setattr(obj, "label", SerializationHelper.deserialize_by_tag(elem, "MultilanguageLongName")),
        "SHORT-LABEL": lambda obj, elem: setattr(obj, "short_label", SerializationHelper.deserialize_by_tag(elem, "String")),
    }


    def __init__(self) -> None:
        """Initialize AliasNameAssignment."""
        super().__init__()
        self.flat_instance_ref: Optional[ARRef] = None
        self.identifiable_ref: Optional[ARRef] = None
        self.label: Optional[MultilanguageLongName] = None
        self.short_label: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize AliasNameAssignment to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AliasNameAssignment, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize flat_instance_ref
        if self.flat_instance_ref is not None:
            serialized = SerializationHelper.serialize_item(self.flat_instance_ref, "FlatInstanceDescriptor")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FLAT-INSTANCE-REF")
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

        # Serialize label
        if self.label is not None:
            serialized = SerializationHelper.serialize_item(self.label, "MultilanguageLongName")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize short_label
        if self.short_label is not None:
            serialized = SerializationHelper.serialize_item(self.short_label, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHORT-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AliasNameAssignment":
        """Deserialize XML element to AliasNameAssignment object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AliasNameAssignment object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AliasNameAssignment, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "FLAT-INSTANCE-REF":
                setattr(obj, "flat_instance_ref", ARRef.deserialize(child))
            elif tag == "IDENTIFIABLE-REF":
                setattr(obj, "identifiable_ref", ARRef.deserialize(child))
            elif tag == "LABEL":
                setattr(obj, "label", SerializationHelper.deserialize_by_tag(child, "MultilanguageLongName"))
            elif tag == "SHORT-LABEL":
                setattr(obj, "short_label", SerializationHelper.deserialize_by_tag(child, "String"))

        return obj



class AliasNameAssignmentBuilder(BuilderBase):
    """Builder for AliasNameAssignment with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AliasNameAssignment = AliasNameAssignment()


    def with_flat_instance(self, value: Optional[FlatInstanceDescriptor]) -> "AliasNameAssignmentBuilder":
        """Set flat_instance attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.flat_instance = value
        return self

    def with_identifiable(self, value: Optional[Identifiable]) -> "AliasNameAssignmentBuilder":
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

    def with_label(self, value: Optional[MultilanguageLongName]) -> "AliasNameAssignmentBuilder":
        """Set label attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.label = value
        return self

    def with_short_label(self, value: Optional[String]) -> "AliasNameAssignmentBuilder":
        """Set short_label attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_label = value
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


    def build(self) -> AliasNameAssignment:
        """Build and return the AliasNameAssignment instance with validation."""
        self._validate_instance()
        pass
        return self._obj