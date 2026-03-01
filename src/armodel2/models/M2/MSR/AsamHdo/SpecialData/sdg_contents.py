"""SdgContents AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 90)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_SpecialData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import atp_mixed

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel2.models.M2.MSR.AsamHdo.SpecialData.sd import (
    Sd,
)
from armodel2.models.M2.MSR.AsamHdo.SpecialData.sdf import (
    Sdf,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.AsamHdo.SpecialData.sdg import (
        Sdg,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
@atp_mixed()

class SdgContents(ARObject):
    """AUTOSAR SdgContents."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SDG-CONTENTS"


    sd: Optional[Sd]
    sdf: Optional[Sdf]
    sdg: Optional[Sdg]
    sdx_ref: Optional[ARRef]
    sdxf_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "SD": lambda obj, elem: setattr(obj, "sd", SerializationHelper.deserialize_by_tag(elem, "Sd")),
        "SDF": lambda obj, elem: setattr(obj, "sdf", SerializationHelper.deserialize_by_tag(elem, "Sdf")),
        "SDG": lambda obj, elem: setattr(obj, "sdg", SerializationHelper.deserialize_by_tag(elem, "Sdg")),
        "SDX-REF": ("_POLYMORPHIC", "sdx_ref", ["ARPackage", "AclObjectSet", "AclOperation", "AclPermission", "AclRole", "AgeConstraint", "AggregationTailoring", "AliasNameSet", "AnalyzedExecutionTime", "AppOsTaskProxyToEcuTaskProxyMapping", "ApplicationArrayDataType", "ApplicationArrayElement", "ApplicationEndpoint", "ApplicationError", "ApplicationPartition", "ApplicationPartitionToEcuPartitionMapping", "ApplicationPrimitiveDataType", "ApplicationRecordDataType", "ApplicationRecordElement", "ApplicationSwComponentType", "ArbitraryEventTriggering", "ArgumentDataPrototype", "AssemblySwConnector", "AsynchronousServerCallPoint", "AsynchronousServerCallResultPoint", "AsynchronousServerCallReturnsEvent", "AtpDefinition", "AutosarOperationArgumentInstance", "AutosarVariableInstance", "BackgroundEvent", "BinaryManifestItem", "BinaryManifestItemDefinition", "BinaryManifestMetaDataField", "BinaryManifestProvideResource", "BinaryManifestRequireResource", "BinaryManifestResourceDefinition", "BlockState", "BlueprintMappingSet", "BswAsynchronousServerCallPoint", "BswAsynchronousServerCallResultPoint", "BswAsynchronousServerCallReturnsEvent", "BswBackgroundEvent", "BswCalledEntity", "BswCompositionTiming", "BswDataReceivedEvent", "BswDirectCallPoint", "BswDistinguishedPartition", "BswEntryRelationshipSet", "BswExternalTriggerOccurredEvent", "BswImplementation", "BswInternalBehavior", "BswInternalTriggerOccurredEvent", "BswInternalTriggeringPoint", "BswInterruptEntity", "BswInterruptEvent", "BswMgrNeeds", "BswModeManagerErrorEvent", "BswModeSwitchEvent", "BswModeSwitchedAckEvent", "BswModuleCallPoint", "BswModuleClientServerEntry", "BswModuleDependency", "BswModuleDescription", "BswModuleEntry", "BswModuleTiming", "BswOperationInvokedEvent", "BswOsTaskExecutionEvent", "BswSchedulableEntity", "BswSchedulerNamePrefix", "BswServiceDependencyIdent", "BswTimingEvent", "BswVariableAccess", "BuildAction", "BuildActionEnvironment", "BuildActionManifest", "BulkNvDataDescriptor", "BurstPatternEventTriggering", "BusMirrorChannelMappingCan", "BusMirrorChannelMappingFlexray", "BusMirrorChannelMappingIp", "CalibrationParameterValueSet", "CanCluster", "CanCommunicationConnector", "CanCommunicationController", "CanFrame", "CanFrameTriggering", "CanNmCluster", "CanNmNode", "CanPhysicalChannel", "CanTpAddress", "CanTpChannel", "CanTpConfig", "CanTpNode", "Caption", "Chapter", "ClassContentConditional", "ClientIdDefinition", "ClientIdDefinitionSet", "ClientServerInterface", "ClientServerInterfaceMapping", "ClientServerInterfaceToBswModuleEntryBlueprintMapping", "ClientServerOperation", "Code", "Collection", "ComManagementMapping", "ComMgrUserNeeds", "Compiler", "ComplexDeviceDriverSwComponentType", "CompositionSwComponentType", "CompuMethod", "ConcreteClassTailoring", "ConcretePatternEventTriggering", "ConsistencyNeeds", "ConsistencyNeedsBlueprintSet", "ConstantSpecification", "ConstantSpecificationMappingSet", "ConstraintTailoring", "ConsumedEventGroup", "ConsumedProvidedServiceInstanceGroup", "ConsumedServiceInstance", "ContainerIPdu", "CouplingElement", "CouplingElementSwitchDetails", "CouplingPort", "CouplingPortFifo", "CouplingPortScheduler", "CouplingPortShaper", "CouplingPortTrafficClassAssignment", "CpSoftwareCluster", "CpSoftwareClusterBinaryManifestDescriptor", "CpSoftwareClusterCommunicationResource", "CpSoftwareClusterMappingSet", "CpSoftwareClusterResourcePool", "CpSoftwareClusterResourceToApplicationPartitionMapping", "CpSoftwareClusterServiceResource", "CpSoftwareClusterToApplicationPartitionMapping", "CpSoftwareClusterToEcuInstanceMapping", "CpSoftwareClusterToResourceMapping", "CpSwClusterResourceToDiagDataElemMapping", "CpSwClusterResourceToDiagFunctionIdMapping", "CpSwClusterToDiagEventMapping", "CpSwClusterToDiagRoutineSubfunctionMapping", "CryptoEllipticCurveProps", "CryptoKeyManagementNeeds", "CryptoServiceCertificate", "CryptoServiceJobNeeds", "CryptoServiceKey", "CryptoServiceNeeds", "CryptoServicePrimitive", "CryptoServiceQueue", "CryptoSignatureScheme", "DataConstr", "DataExchangePoint", "DataPrototypeGroup", "DataReceiveErrorEvent", "DataReceivedEvent", "DataSendCompletedEvent", "DataTransformationSet", "DataTypeMappingSet", "DataWriteCompletedEvent", "DcmIPdu", "DdsCpConfig", "DdsCpConsumedServiceInstance", "DdsCpDomain", "DdsCpPartition", "DdsCpProvidedServiceInstance", "DdsCpQosProfile", "DdsCpTopic", "DefItem", "DelegationSwConnector", "DependencyOnArtifact", "DevelopmentError", "DiagEventDebounceCounterBased", "DiagEventDebounceMonitorInternal", "DiagnosticAccessPermission", "DiagnosticAging", "DiagnosticAuthRole", "DiagnosticAuthTransmitCertificate", "DiagnosticAuthTransmitCertificateEvaluation", "DiagnosticAuthTransmitCertificateMapping", "DiagnosticAuthenticationClass", "DiagnosticAuthenticationConfiguration", "DiagnosticClearDiagnosticInformation", "DiagnosticClearDiagnosticInformationClass", "DiagnosticClearResetEmissionRelatedInfo", "DiagnosticClearResetEmissionRelatedInfoClass", "DiagnosticComControl", "DiagnosticComControlClass", "DiagnosticCommunicationManagerNeeds", "DiagnosticComponentNeeds", "DiagnosticConnectedIndicator", "DiagnosticConnection", "DiagnosticContributionSet", "DiagnosticControlDTCSetting", "DiagnosticControlDTCSettingClass", "DiagnosticControlNeeds", "DiagnosticCustomServiceClass", "DiagnosticCustomServiceInstance", "DiagnosticDataElement", "DiagnosticDataIdentifier", "DiagnosticDataIdentifierSet", "DiagnosticDataTransfer", "DiagnosticDataTransferClass", "DiagnosticDeAuthentication", "DiagnosticDebounceAlgorithmProps", "DiagnosticDemProvidedDataMapping", "DiagnosticDynamicDataIdentifier", "DiagnosticDynamicallyDefineDataIdentifier", "DiagnosticDynamicallyDefineDataIdentifierClass", "DiagnosticEcuInstanceProps", "DiagnosticEcuReset", "DiagnosticEcuResetClass", "DiagnosticEnableCondition", "DiagnosticEnableConditionGroup", "DiagnosticEnableConditionNeeds", "DiagnosticEnableConditionPortMapping", "DiagnosticEnvBswModeElement", "DiagnosticEnvModeElement", "DiagnosticEnvSwcModeElement", "DiagnosticEnvironmentalCondition", "DiagnosticEvent", "DiagnosticEventInfoNeeds", "DiagnosticEventManagerNeeds", "DiagnosticEventNeeds", "DiagnosticEventPortMapping", "DiagnosticEventToDebounceAlgorithmMapping", "DiagnosticEventToEnableConditionGroupMapping", "DiagnosticEventToOperationCycleMapping", "DiagnosticEventToSecurityEventMapping", "DiagnosticEventToStorageConditionGroupMapping", "DiagnosticEventToTroubleCodeJ1939Mapping", "DiagnosticEventToTroubleCodeUdsMapping", "DiagnosticExtendedDataRecord", "DiagnosticFimAliasEvent", "DiagnosticFimAliasEventGroup", "DiagnosticFimAliasEventGroupMapping", "DiagnosticFimAliasEventMapping", "DiagnosticFimEventGroup", "DiagnosticFimFunctionMapping", "DiagnosticFreezeFrame", "DiagnosticFunctionIdentifier", "DiagnosticFunctionIdentifierInhibit", "DiagnosticFunctionInhibitSource", "DiagnosticIOControl", "DiagnosticIndicator", "DiagnosticInfoType", "DiagnosticInhibitSourceEventMapping", "DiagnosticIoControlClass", "DiagnosticIoControlNeeds", "DiagnosticIumpr", "DiagnosticIumprDenominatorGroup", "DiagnosticIumprGroup", "DiagnosticIumprToFunctionIdentifierMapping", "DiagnosticJ1939ExpandedFreezeFrame", "DiagnosticJ1939FreezeFrame", "DiagnosticJ1939Node", "DiagnosticJ1939Spn", "DiagnosticJ1939SpnMapping", "DiagnosticJ1939SwMapping", "DiagnosticMasterToSlaveEventMapping", "DiagnosticMeasurementIdentifier", "DiagnosticMemoryDestinationPrimary", "DiagnosticMemoryDestinationUserDefined", "DiagnosticMemoryIdentifier", "DiagnosticOperationCycle", "DiagnosticOperationCycleNeeds", "DiagnosticOperationCyclePortMapping", "DiagnosticParameterElement", "DiagnosticParameterIdent", "DiagnosticParameterIdentifier", "DiagnosticPowertrainFreezeFrame", "DiagnosticProofOfOwnership", "DiagnosticProtocol", "DiagnosticReadDTCInformation", "DiagnosticReadDTCInformationClass", "DiagnosticReadDataByIdentifier", "DiagnosticReadDataByIdentifierClass", "DiagnosticReadDataByPeriodicID", "DiagnosticReadDataByPeriodicIDClass", "DiagnosticReadMemoryByAddress", "DiagnosticReadMemoryByAddressClass", "DiagnosticReadScalingDataByIdentifier", "DiagnosticReadScalingDataByIdentifierClass", "DiagnosticRequestControlOfOnBoardDevice", "DiagnosticRequestControlOfOnBoardDeviceClass", "DiagnosticRequestCurrentPowertrainData", "DiagnosticRequestCurrentPowertrainDataClass", "DiagnosticRequestDownload", "DiagnosticRequestDownloadClass", "DiagnosticRequestEmissionRelatedDTC", "DiagnosticRequestEmissionRelatedDTCClass", "DiagnosticRequestEmissionRelatedDTCPermanentStatus", "DiagnosticRequestEmissionRelatedDTCPermanentStatusClass", "DiagnosticRequestFileTransfer", "DiagnosticRequestFileTransferClass", "DiagnosticRequestFileTransferNeeds", "DiagnosticRequestOnBoardMonitoringTestResults", "DiagnosticRequestOnBoardMonitoringTestResultsClass", "DiagnosticRequestPowertrainFreezeFrameData", "DiagnosticRequestPowertrainFreezeFrameDataClass", "DiagnosticRequestRoutineResults", "DiagnosticRequestUpload", "DiagnosticRequestUploadClass", "DiagnosticRequestVehicleInfo", "DiagnosticRequestVehicleInfoClass", "DiagnosticResponseOnEvent", "DiagnosticResponseOnEventClass", "DiagnosticRoutine", "DiagnosticRoutineControl", "DiagnosticRoutineControlClass", "DiagnosticRoutineNeeds", "DiagnosticSecureCodingMapping", "DiagnosticSecurityAccess", "DiagnosticSecurityAccessClass", "DiagnosticSecurityEventReportingModeMapping", "DiagnosticSecurityLevel", "DiagnosticServiceDataMapping", "DiagnosticServiceSwMapping", "DiagnosticServiceTable", "DiagnosticSession", "DiagnosticSessionControl", "DiagnosticSessionControlClass", "DiagnosticStartRoutine", "DiagnosticStopRoutine", "DiagnosticStorageCondition", "DiagnosticStorageConditionGroup", "DiagnosticStorageConditionNeeds", "DiagnosticStorageConditionPortMapping", "DiagnosticTestResult", "DiagnosticTestRoutineIdentifier", "DiagnosticTransferExit", "DiagnosticTransferExitClass", "DiagnosticTroubleCodeGroup", "DiagnosticTroubleCodeJ1939", "DiagnosticTroubleCodeObd", "DiagnosticTroubleCodeProps", "DiagnosticTroubleCodeUds", "DiagnosticTroubleCodeUdsToTroubleCodeObdMapping", "DiagnosticUploadDownloadNeeds", "DiagnosticValueNeeds", "DiagnosticVerifyCertificateBidirectional", "DiagnosticWriteDataByIdentifierClass", "DiagnosticWriteMemoryByAddressClass", "DiagnosticsCommunicationSecurityNeeds", "DltApplication", "DltArgument", "DltContext", "DltEcu", "DltLogChannel", "DltMessage", "DltUserNeeds", "DoIpActivationLineNeeds", "DoIpGidNeeds", "DoIpGidSynchronizationNeeds", "DoIpInterface", "DoIpLogicAddress", "DoIpLogicTargetAddressProps", "DoIpLogicTesterAddressProps", "DoIpPowerModeStatusNeeds", "DoIpRoutingActivation", "DoIpRoutingActivationAuthenticationNeeds", "DoIpRoutingActivationConfirmationNeeds", "DoIpTpConfig", "DocumentElementScope", "Documentation", "DocumentationContext", "DtcStatusChangeNotificationNeeds", "E2EProfileCompatibilityProps", "ECUMapping", "EOCEventRef", "EOCExecutableEntityRef", "EOCExecutableEntityRefGroup", "EcuAbstractionSwComponentType", "EcuInstance", "EcuPartition", "EcuStateMgrUserNeeds", "EcuTiming", "EcucAddInfoParamDef", "EcucBooleanParamDef", "EcucChoiceContainerDef", "EcucChoiceReferenceDef", "EcucContainerValue", "EcucDefinitionCollection", "EcucDestinationUriDef", "EcucDestinationUriDefSet", "EcucEnumerationLiteralDef", "EcucEnumerationParamDef", "EcucFloatParamDef", "EcucForeignReferenceDef", "EcucFunctionNameDef", "EcucInstanceReferenceDef", "EcucIntegerParamDef", "EcucLinkerSymbolDef", "EcucModuleConfigurationValues", "EcucModuleDef", "EcucMultilineStringParamDef", "EcucParamConfContainerDef", "EcucQuery", "EcucReferenceDef", "EcucStringParamDef", "EcucUriReferenceDef", "EcucValidationCondition", "EcucValueCollection", "EndToEndProtection", "EndToEndProtectionSet", "EnumerationMappingTable", "ErrorTracerNeeds", "EthIpProps", "EthTcpIpIcmpProps", "EthTcpIpProps", "EthTpConfig", "EthernetCluster", "EthernetCommunicationConnector", "EthernetCommunicationController", "EthernetFrameTriggering", "EthernetPhysicalChannel", "EthernetPriorityRegeneration", "EthernetWakeupSleepOnDatalineConfig", "EthernetWakeupSleepOnDatalineConfigSet", "EvaluatedVariantSet", "EventHandler", "ExclusiveArea", "ExclusiveAreaNestingOrder", "ExecutableEntityActivationReason", "ExecutionOrderConstraint", "ExecutionTimeConstraint", "ExternalTriggerOccurredEvent", "ExternalTriggeringPointIdent", "FMAttributeDef", "FMFeature", "FMFeatureMap", "FMFeatureMapAssertion", "FMFeatureMapCondition", "FMFeatureMapElement", "FMFeatureModel", "FMFeatureRelation", "FMFeatureRestriction", "FMFeatureSelection", "FMFeatureSelectionSet", "FirewallRule", "FlatInstanceDescriptor", "FlatMap", "FlexrayArTpConfig", "FlexrayArTpNode", "FlexrayCluster", "FlexrayCommunicationConnector", "FlexrayCommunicationController", "FlexrayFrame", "FlexrayFrameTriggering", "FlexrayNmCluster", "FlexrayNmNode", "FlexrayPhysicalChannel", "FlexrayTpConfig", "FlexrayTpConnectionControl", "FlexrayTpNode", "FlexrayTpPduPool", "FramePort", "FunctionInhibitionAvailabilityNeeds", "FunctionInhibitionNeeds", "Gateway", "GeneralPurposeConnection", "GeneralPurposeIPdu", "GeneralPurposePdu", "GenericEthernetFrame", "GlobalSupervisionNeeds", "GlobalTimeCanMaster", "GlobalTimeCanSlave", "GlobalTimeDomain", "GlobalTimeEthMaster", "GlobalTimeEthSlave", "GlobalTimeFrMaster", "GlobalTimeFrSlave", "GlobalTimeGateway", "HardwareTestNeeds", "HwAttributeDef", "HwAttributeLiteralDef", "HwCategory", "HwDescriptionEntity", "HwElement", "HwPin", "HwPinGroup", "HwType", "IEEE1722TpAafConnection", "IEEE1722TpAcfCan", "IEEE1722TpAcfCanPart", "IEEE1722TpAcfConnection", "IEEE1722TpAcfLin", "IEEE1722TpAcfLinPart", "IEEE1722TpConfig", "IEEE1722TpCrfConnection", "IEEE1722TpIidcConnection", "IPSecConfigProps", "IPSecRule", "IPduPort", "IPv6ExtHeaderFilterList", "IPv6ExtHeaderFilterSet", "ISignal", "ISignalGroup", "ISignalIPdu", "ISignalIPduGroup", "ISignalPort", "ISignalToIPduMapping", "ISignalTriggering", "IdsDesign", "IdsMgrCustomTimestampNeeds", "IdsMgrNeeds", "IdsmInstance", "IdsmProperties", "Ieee1722TpEthernetFrame", "ImplementationDataType", "ImplementationDataTypeElement", "ImplementationProps", "ImpositionTime", "IndicatorStatusNeeds", "InitEvent", "InternalTriggerOccurredEvent", "InternalTriggeringPoint", "InterpolationRoutineMappingSet", "J1939Cluster", "J1939ControllerApplication", "J1939DcmDm19Support", "J1939DcmIPdu", "J1939NmCluster", "J1939NmNode", "J1939RmIncomingRequestServiceNeeds", "J1939RmOutgoingRequestServiceNeeds", "J1939SharedAddressCluster", "J1939TpConfig", "J1939TpNode", "Keyword", "KeywordSet", "LatencyTimingConstraint", "LifeCycleInfoSet", "LifeCycleState", "LifeCycleStateDefinitionGroup", "LinCluster", "LinCommunicationConnector", "LinEventTriggeredFrame", "LinFrameTriggering", "LinMaster", "LinPhysicalChannel", "LinScheduleTable", "LinSlave", "LinSlaveConfigIdent", "LinSporadicFrame", "LinTpConfig", "LinTpNode", "LinUnconditionalFrame", "Linker", "LogAndTraceMessageCollectionSet", "MacMulticastGroup", "MacSecGlobalKayProps", "MacSecKayParticipant", "MacSecParticipantSet", "McDataInstance", "McFunction", "McGroup", "MeasuredExecutionTime", "MeasuredHeapUsage", "MeasuredStackUsage", "MemorySection", "ModeAccessPointIdent", "ModeDeclaration", "ModeDeclarationGroup", "ModeDeclarationGroupPrototype", "ModeDeclarationMapping", "ModeDeclarationMappingSet", "ModeInterfaceMapping", "ModeSwitchInterface", "ModeSwitchPoint", "ModeSwitchedAckEvent", "ModeTransition", "MultilanguageReferrable", "MultiplexedIPdu", "NPdu", "NetworkEndpoint", "NmConfig", "NmEcu", "NmPdu", "NvBlockDescriptor", "NvBlockNeeds", "NvBlockSwComponentType", "NvDataInterface", "ObdControlServiceNeeds", "ObdInfoServiceNeeds", "ObdMonitorServiceNeeds", "ObdPidServiceNeeds", "ObdRatioDenominatorNeeds", "ObdRatioServiceNeeds", "OffsetTimingConstraint", "OperationInvokedEvent", "OsTaskExecutionEvent", "OsTaskProxy", "PPortPrototype", "PRPortPrototype", "ParameterAccess", "ParameterDataPrototype", "ParameterInterface", "ParameterSwComponentType", "PassThroughSwConnector", "PduActivationRoutingGroup", "PduToFrameMapping", "PduTriggering", "PdurIPduGroup", "PerInstanceMemory", "PeriodicEventTriggering", "PhysicalDimension", "PhysicalDimensionMappingSet", "PncMappingIdent", "PortElementToCommunicationResourceMapping", "PortGroup", "PortInterfaceMappingSet", "PortPrototypeBlueprint", "PostBuildVariantCriterion", "PostBuildVariantCriterionValueSet", "PredefinedVariant", "PrimitiveAttributeTailoring", "ProvidedServiceInstance", "RPortPrototype", "RapidPrototypingScenario", "ReferenceTailoring", "ResourceConsumption", "RootSwCompositionPrototype", "RoughEstimateHeapUsage", "RoughEstimateOfExecutionTime", "RoughEstimateStackUsage", "RptComponent", "RptContainer", "RptExecutableEntity", "RptExecutableEntityEvent", "RptExecutionContext", "RptProfile", "RptServicePoint", "RteEventInCompositionSeparation", "RteEventInCompositionToOsTaskProxyMapping", "RteEventInSystemSeparation", "RteEventInSystemToOsTaskProxyMapping", "RunnableEntity", "RunnableEntityGroup", "RuntimeError", "SOMEIPTransformationProps", "Sdg", "SdgAggregationWithVariation", "SdgCaption", "SdgClass", "SdgDef", "SdgForeignReference", "SdgForeignReferenceWithVariation", "SdgPrimitiveAttribute", "SdgPrimitiveAttributeWithVariation", "SdgTailoring", "SecOcCryptoServiceMapping", "SectionNamePrefix", "SecureCommunicationAuthenticationProps", "SecureCommunicationFreshnessProps", "SecureCommunicationPropsSet", "SecureOnBoardCommunicationNeeds", "SecuredIPdu", "SecurityEventAggregationFilter", "SecurityEventContextMappingApplication", "SecurityEventContextMappingBswModule", "SecurityEventContextMappingCommConnector", "SecurityEventContextMappingFunctionalCluster", "SecurityEventContextProps", "SecurityEventDefinition", "SecurityEventFilterChain", "SecurityEventOneEveryNFilter", "SecurityEventStateFilter", "SenderReceiverInterface", "SensorActuatorSwComponentType", "ServiceInstanceCollectionSet", "ServiceProxySwComponentType", "ServiceSwComponentType", "SignalServiceTranslationElementProps", "SignalServiceTranslationEventProps", "SignalServiceTranslationProps", "SignalServiceTranslationPropsSet", "SingleLanguageReferrable", "SoAdRoutingGroup", "SoConIPduIdentifier", "SocketAddress", "SocketConnectionBundle", "SocketConnectionIpduIdentifierSet", "SomeipSdClientServiceInstanceConfig", "SomeipSdServerEventGroupTimingConfig", "SomeipSdServerServiceInstanceConfig", "SomeipTpChannel", "SomeipTpConfig", "SpecificationDocumentScope", "SporadicEventTriggering", "StaticSocketConnection", "Std", "StructuredReq", "SupervisedEntityCheckpointNeeds", "SupervisedEntityNeeds", "SwAddrMethod", "SwAxisType", "SwBaseType", "SwGenericAxisParamType", "SwRecordLayout", "SwServiceArg", "SwSystemconst", "SwSystemconstantValueSet", "SwcBswMapping", "SwcImplementation", "SwcInternalBehavior", "SwcModeManagerErrorEvent", "SwcModeSwitchEvent", "SwcServiceDependency", "SwcTiming", "SwcToApplicationPartitionMapping", "SwcToEcuMapping", "SwcToImplMapping", "SwitchAsynchronousTrafficShaperGroupEntry", "SwitchFlowMeteringEntry", "SwitchStreamFilterActionDestPortModification", "SwitchStreamFilterEntry", "SwitchStreamFilterRule", "SwitchStreamGateEntry", "SwitchStreamIdentification", "SymbolProps", "SyncTimeBaseMgrUserNeeds", "SynchronizationPointConstraint", "SynchronousServerCallPoint", "System", "SystemMapping", "SystemSignal", "SystemSignalGroup", "SystemSignalGroupToCommunicationResourceMapping", "SystemSignalToCommunicationResourceMapping", "SystemTiming", "TDCpSoftwareClusterMapping", "TDCpSoftwareClusterMappingSet", "TDCpSoftwareClusterResourceMapping", "TDEventBswInternalBehavior", "TDEventBswModeDeclaration", "TDEventBswModule", "TDEventComplex", "TDEventFrClusterCycleStart", "TDEventFrame", "TDEventFrameEthernet", "TDEventIPdu", "TDEventISignal", "TDEventModeDeclaration", "TDEventOperation", "TDEventSLLETPort", "TDEventSwcInternalBehavior", "TDEventSwcInternalBehaviorReference", "TDEventTTCanCycleStart", "TDEventTrigger", "TDEventVariableDataPrototype", "TDEventVfbReference", "TDLETZoneClock", "TcpOptionFilterList", "TcpOptionFilterSet", "TimeSyncServerConfiguration", "TimingClockSyncAccuracy", "TimingCondition", "TimingDescriptionEventChain", "TimingEvent", "TimingExtensionResource", "TimingModeInstance", "TlsCryptoCipherSuite", "TlsCryptoCipherSuiteProps", "TlsCryptoServiceMapping", "TlvDataIdDefinitionSet", "Topic1", "TpAddress", "TpConnectionIdent", "TraceableText", "TransformationPropsSet", "TransformationTechnology", "TransformerHardErrorEvent", "TransientFault", "Trigger", "TriggerInterface", "TriggerInterfaceMapping", "TtcanCluster", "TtcanCommunicationConnector", "TtcanCommunicationController", "TtcanPhysicalChannel", "UdpNmCluster", "UdpNmNode", "Unit", "UnitGroup", "UserDefinedCluster", "UserDefinedCommunicationConnector", "UserDefinedCommunicationController", "UserDefinedEthernetFrame", "UserDefinedGlobalTimeMaster", "UserDefinedGlobalTimeSlave", "UserDefinedIPdu", "UserDefinedPdu", "UserDefinedTransformationProps", "V2xDataManagerNeeds", "V2xFacUserNeeds", "V2xMUserNeeds", "VariableAccess", "VariableDataPrototype", "VariationPointProxy", "VendorSpecificServiceNeeds", "VfbTiming", "ViewMap", "ViewMapSet", "VlanConfig", "WaitPoint", "WorstCaseHeapUsage", "WorstCaseStackUsage", "Xdoc", "Xfile", "XrefTarget"]),
        "SDXF-REF": ("_POLYMORPHIC", "sdxf_ref", ["ARPackage", "AclObjectSet", "AclOperation", "AclPermission", "AclRole", "AgeConstraint", "AggregationTailoring", "AliasNameSet", "AnalyzedExecutionTime", "AppOsTaskProxyToEcuTaskProxyMapping", "ApplicationArrayDataType", "ApplicationArrayElement", "ApplicationEndpoint", "ApplicationError", "ApplicationPartition", "ApplicationPartitionToEcuPartitionMapping", "ApplicationPrimitiveDataType", "ApplicationRecordDataType", "ApplicationRecordElement", "ApplicationSwComponentType", "ArbitraryEventTriggering", "ArgumentDataPrototype", "AssemblySwConnector", "AsynchronousServerCallPoint", "AsynchronousServerCallResultPoint", "AsynchronousServerCallReturnsEvent", "AtpDefinition", "AutosarOperationArgumentInstance", "AutosarVariableInstance", "BackgroundEvent", "BinaryManifestItem", "BinaryManifestItemDefinition", "BinaryManifestMetaDataField", "BinaryManifestProvideResource", "BinaryManifestRequireResource", "BinaryManifestResourceDefinition", "BlockState", "BlueprintMappingSet", "BswAsynchronousServerCallPoint", "BswAsynchronousServerCallResultPoint", "BswAsynchronousServerCallReturnsEvent", "BswBackgroundEvent", "BswCalledEntity", "BswCompositionTiming", "BswDataReceivedEvent", "BswDirectCallPoint", "BswDistinguishedPartition", "BswEntryRelationshipSet", "BswExternalTriggerOccurredEvent", "BswImplementation", "BswInternalBehavior", "BswInternalTriggerOccurredEvent", "BswInternalTriggeringPoint", "BswInterruptEntity", "BswInterruptEvent", "BswMgrNeeds", "BswModeManagerErrorEvent", "BswModeSwitchEvent", "BswModeSwitchedAckEvent", "BswModuleCallPoint", "BswModuleClientServerEntry", "BswModuleDependency", "BswModuleDescription", "BswModuleEntry", "BswModuleTiming", "BswOperationInvokedEvent", "BswOsTaskExecutionEvent", "BswSchedulableEntity", "BswSchedulerNamePrefix", "BswServiceDependencyIdent", "BswTimingEvent", "BswVariableAccess", "BuildAction", "BuildActionEnvironment", "BuildActionManifest", "BulkNvDataDescriptor", "BurstPatternEventTriggering", "BusMirrorChannelMappingCan", "BusMirrorChannelMappingFlexray", "BusMirrorChannelMappingIp", "CalibrationParameterValueSet", "CanCluster", "CanCommunicationConnector", "CanCommunicationController", "CanFrame", "CanFrameTriggering", "CanNmCluster", "CanNmNode", "CanPhysicalChannel", "CanTpAddress", "CanTpChannel", "CanTpConfig", "CanTpNode", "Caption", "Chapter", "ClassContentConditional", "ClientIdDefinition", "ClientIdDefinitionSet", "ClientServerInterface", "ClientServerInterfaceMapping", "ClientServerInterfaceToBswModuleEntryBlueprintMapping", "ClientServerOperation", "Code", "Collection", "ComManagementMapping", "ComMgrUserNeeds", "Compiler", "ComplexDeviceDriverSwComponentType", "CompositionSwComponentType", "CompuMethod", "ConcreteClassTailoring", "ConcretePatternEventTriggering", "ConsistencyNeeds", "ConsistencyNeedsBlueprintSet", "ConstantSpecification", "ConstantSpecificationMappingSet", "ConstraintTailoring", "ConsumedEventGroup", "ConsumedProvidedServiceInstanceGroup", "ConsumedServiceInstance", "ContainerIPdu", "CouplingElement", "CouplingElementSwitchDetails", "CouplingPort", "CouplingPortFifo", "CouplingPortScheduler", "CouplingPortShaper", "CouplingPortTrafficClassAssignment", "CpSoftwareCluster", "CpSoftwareClusterBinaryManifestDescriptor", "CpSoftwareClusterCommunicationResource", "CpSoftwareClusterMappingSet", "CpSoftwareClusterResourcePool", "CpSoftwareClusterResourceToApplicationPartitionMapping", "CpSoftwareClusterServiceResource", "CpSoftwareClusterToApplicationPartitionMapping", "CpSoftwareClusterToEcuInstanceMapping", "CpSoftwareClusterToResourceMapping", "CpSwClusterResourceToDiagDataElemMapping", "CpSwClusterResourceToDiagFunctionIdMapping", "CpSwClusterToDiagEventMapping", "CpSwClusterToDiagRoutineSubfunctionMapping", "CryptoEllipticCurveProps", "CryptoKeyManagementNeeds", "CryptoServiceCertificate", "CryptoServiceJobNeeds", "CryptoServiceKey", "CryptoServiceNeeds", "CryptoServicePrimitive", "CryptoServiceQueue", "CryptoSignatureScheme", "DataConstr", "DataExchangePoint", "DataPrototypeGroup", "DataReceiveErrorEvent", "DataReceivedEvent", "DataSendCompletedEvent", "DataTransformationSet", "DataTypeMappingSet", "DataWriteCompletedEvent", "DcmIPdu", "DdsCpConfig", "DdsCpConsumedServiceInstance", "DdsCpDomain", "DdsCpPartition", "DdsCpProvidedServiceInstance", "DdsCpQosProfile", "DdsCpTopic", "DefItem", "DelegationSwConnector", "DependencyOnArtifact", "DevelopmentError", "DiagEventDebounceCounterBased", "DiagEventDebounceMonitorInternal", "DiagnosticAccessPermission", "DiagnosticAging", "DiagnosticAuthRole", "DiagnosticAuthTransmitCertificate", "DiagnosticAuthTransmitCertificateEvaluation", "DiagnosticAuthTransmitCertificateMapping", "DiagnosticAuthenticationClass", "DiagnosticAuthenticationConfiguration", "DiagnosticClearDiagnosticInformation", "DiagnosticClearDiagnosticInformationClass", "DiagnosticClearResetEmissionRelatedInfo", "DiagnosticClearResetEmissionRelatedInfoClass", "DiagnosticComControl", "DiagnosticComControlClass", "DiagnosticCommunicationManagerNeeds", "DiagnosticComponentNeeds", "DiagnosticConnectedIndicator", "DiagnosticConnection", "DiagnosticContributionSet", "DiagnosticControlDTCSetting", "DiagnosticControlDTCSettingClass", "DiagnosticControlNeeds", "DiagnosticCustomServiceClass", "DiagnosticCustomServiceInstance", "DiagnosticDataElement", "DiagnosticDataIdentifier", "DiagnosticDataIdentifierSet", "DiagnosticDataTransfer", "DiagnosticDataTransferClass", "DiagnosticDeAuthentication", "DiagnosticDebounceAlgorithmProps", "DiagnosticDemProvidedDataMapping", "DiagnosticDynamicDataIdentifier", "DiagnosticDynamicallyDefineDataIdentifier", "DiagnosticDynamicallyDefineDataIdentifierClass", "DiagnosticEcuInstanceProps", "DiagnosticEcuReset", "DiagnosticEcuResetClass", "DiagnosticEnableCondition", "DiagnosticEnableConditionGroup", "DiagnosticEnableConditionNeeds", "DiagnosticEnableConditionPortMapping", "DiagnosticEnvBswModeElement", "DiagnosticEnvModeElement", "DiagnosticEnvSwcModeElement", "DiagnosticEnvironmentalCondition", "DiagnosticEvent", "DiagnosticEventInfoNeeds", "DiagnosticEventManagerNeeds", "DiagnosticEventNeeds", "DiagnosticEventPortMapping", "DiagnosticEventToDebounceAlgorithmMapping", "DiagnosticEventToEnableConditionGroupMapping", "DiagnosticEventToOperationCycleMapping", "DiagnosticEventToSecurityEventMapping", "DiagnosticEventToStorageConditionGroupMapping", "DiagnosticEventToTroubleCodeJ1939Mapping", "DiagnosticEventToTroubleCodeUdsMapping", "DiagnosticExtendedDataRecord", "DiagnosticFimAliasEvent", "DiagnosticFimAliasEventGroup", "DiagnosticFimAliasEventGroupMapping", "DiagnosticFimAliasEventMapping", "DiagnosticFimEventGroup", "DiagnosticFimFunctionMapping", "DiagnosticFreezeFrame", "DiagnosticFunctionIdentifier", "DiagnosticFunctionIdentifierInhibit", "DiagnosticFunctionInhibitSource", "DiagnosticIOControl", "DiagnosticIndicator", "DiagnosticInfoType", "DiagnosticInhibitSourceEventMapping", "DiagnosticIoControlClass", "DiagnosticIoControlNeeds", "DiagnosticIumpr", "DiagnosticIumprDenominatorGroup", "DiagnosticIumprGroup", "DiagnosticIumprToFunctionIdentifierMapping", "DiagnosticJ1939ExpandedFreezeFrame", "DiagnosticJ1939FreezeFrame", "DiagnosticJ1939Node", "DiagnosticJ1939Spn", "DiagnosticJ1939SpnMapping", "DiagnosticJ1939SwMapping", "DiagnosticMasterToSlaveEventMapping", "DiagnosticMeasurementIdentifier", "DiagnosticMemoryDestinationPrimary", "DiagnosticMemoryDestinationUserDefined", "DiagnosticMemoryIdentifier", "DiagnosticOperationCycle", "DiagnosticOperationCycleNeeds", "DiagnosticOperationCyclePortMapping", "DiagnosticParameterElement", "DiagnosticParameterIdent", "DiagnosticParameterIdentifier", "DiagnosticPowertrainFreezeFrame", "DiagnosticProofOfOwnership", "DiagnosticProtocol", "DiagnosticReadDTCInformation", "DiagnosticReadDTCInformationClass", "DiagnosticReadDataByIdentifier", "DiagnosticReadDataByIdentifierClass", "DiagnosticReadDataByPeriodicID", "DiagnosticReadDataByPeriodicIDClass", "DiagnosticReadMemoryByAddress", "DiagnosticReadMemoryByAddressClass", "DiagnosticReadScalingDataByIdentifier", "DiagnosticReadScalingDataByIdentifierClass", "DiagnosticRequestControlOfOnBoardDevice", "DiagnosticRequestControlOfOnBoardDeviceClass", "DiagnosticRequestCurrentPowertrainData", "DiagnosticRequestCurrentPowertrainDataClass", "DiagnosticRequestDownload", "DiagnosticRequestDownloadClass", "DiagnosticRequestEmissionRelatedDTC", "DiagnosticRequestEmissionRelatedDTCClass", "DiagnosticRequestEmissionRelatedDTCPermanentStatus", "DiagnosticRequestEmissionRelatedDTCPermanentStatusClass", "DiagnosticRequestFileTransfer", "DiagnosticRequestFileTransferClass", "DiagnosticRequestFileTransferNeeds", "DiagnosticRequestOnBoardMonitoringTestResults", "DiagnosticRequestOnBoardMonitoringTestResultsClass", "DiagnosticRequestPowertrainFreezeFrameData", "DiagnosticRequestPowertrainFreezeFrameDataClass", "DiagnosticRequestRoutineResults", "DiagnosticRequestUpload", "DiagnosticRequestUploadClass", "DiagnosticRequestVehicleInfo", "DiagnosticRequestVehicleInfoClass", "DiagnosticResponseOnEvent", "DiagnosticResponseOnEventClass", "DiagnosticRoutine", "DiagnosticRoutineControl", "DiagnosticRoutineControlClass", "DiagnosticRoutineNeeds", "DiagnosticSecureCodingMapping", "DiagnosticSecurityAccess", "DiagnosticSecurityAccessClass", "DiagnosticSecurityEventReportingModeMapping", "DiagnosticSecurityLevel", "DiagnosticServiceDataMapping", "DiagnosticServiceSwMapping", "DiagnosticServiceTable", "DiagnosticSession", "DiagnosticSessionControl", "DiagnosticSessionControlClass", "DiagnosticStartRoutine", "DiagnosticStopRoutine", "DiagnosticStorageCondition", "DiagnosticStorageConditionGroup", "DiagnosticStorageConditionNeeds", "DiagnosticStorageConditionPortMapping", "DiagnosticTestResult", "DiagnosticTestRoutineIdentifier", "DiagnosticTransferExit", "DiagnosticTransferExitClass", "DiagnosticTroubleCodeGroup", "DiagnosticTroubleCodeJ1939", "DiagnosticTroubleCodeObd", "DiagnosticTroubleCodeProps", "DiagnosticTroubleCodeUds", "DiagnosticTroubleCodeUdsToTroubleCodeObdMapping", "DiagnosticUploadDownloadNeeds", "DiagnosticValueNeeds", "DiagnosticVerifyCertificateBidirectional", "DiagnosticWriteDataByIdentifierClass", "DiagnosticWriteMemoryByAddressClass", "DiagnosticsCommunicationSecurityNeeds", "DltApplication", "DltArgument", "DltContext", "DltEcu", "DltLogChannel", "DltMessage", "DltUserNeeds", "DoIpActivationLineNeeds", "DoIpGidNeeds", "DoIpGidSynchronizationNeeds", "DoIpInterface", "DoIpLogicAddress", "DoIpLogicTargetAddressProps", "DoIpLogicTesterAddressProps", "DoIpPowerModeStatusNeeds", "DoIpRoutingActivation", "DoIpRoutingActivationAuthenticationNeeds", "DoIpRoutingActivationConfirmationNeeds", "DoIpTpConfig", "DocumentElementScope", "Documentation", "DocumentationContext", "DtcStatusChangeNotificationNeeds", "E2EProfileCompatibilityProps", "ECUMapping", "EOCEventRef", "EOCExecutableEntityRef", "EOCExecutableEntityRefGroup", "EcuAbstractionSwComponentType", "EcuInstance", "EcuPartition", "EcuStateMgrUserNeeds", "EcuTiming", "EcucAddInfoParamDef", "EcucBooleanParamDef", "EcucChoiceContainerDef", "EcucChoiceReferenceDef", "EcucContainerValue", "EcucDefinitionCollection", "EcucDestinationUriDef", "EcucDestinationUriDefSet", "EcucEnumerationLiteralDef", "EcucEnumerationParamDef", "EcucFloatParamDef", "EcucForeignReferenceDef", "EcucFunctionNameDef", "EcucInstanceReferenceDef", "EcucIntegerParamDef", "EcucLinkerSymbolDef", "EcucModuleConfigurationValues", "EcucModuleDef", "EcucMultilineStringParamDef", "EcucParamConfContainerDef", "EcucQuery", "EcucReferenceDef", "EcucStringParamDef", "EcucUriReferenceDef", "EcucValidationCondition", "EcucValueCollection", "EndToEndProtection", "EndToEndProtectionSet", "EnumerationMappingTable", "ErrorTracerNeeds", "EthIpProps", "EthTcpIpIcmpProps", "EthTcpIpProps", "EthTpConfig", "EthernetCluster", "EthernetCommunicationConnector", "EthernetCommunicationController", "EthernetFrameTriggering", "EthernetPhysicalChannel", "EthernetPriorityRegeneration", "EthernetWakeupSleepOnDatalineConfig", "EthernetWakeupSleepOnDatalineConfigSet", "EvaluatedVariantSet", "EventHandler", "ExclusiveArea", "ExclusiveAreaNestingOrder", "ExecutableEntityActivationReason", "ExecutionOrderConstraint", "ExecutionTimeConstraint", "ExternalTriggerOccurredEvent", "ExternalTriggeringPointIdent", "FMAttributeDef", "FMFeature", "FMFeatureMap", "FMFeatureMapAssertion", "FMFeatureMapCondition", "FMFeatureMapElement", "FMFeatureModel", "FMFeatureRelation", "FMFeatureRestriction", "FMFeatureSelection", "FMFeatureSelectionSet", "FirewallRule", "FlatInstanceDescriptor", "FlatMap", "FlexrayArTpConfig", "FlexrayArTpNode", "FlexrayCluster", "FlexrayCommunicationConnector", "FlexrayCommunicationController", "FlexrayFrame", "FlexrayFrameTriggering", "FlexrayNmCluster", "FlexrayNmNode", "FlexrayPhysicalChannel", "FlexrayTpConfig", "FlexrayTpConnectionControl", "FlexrayTpNode", "FlexrayTpPduPool", "FramePort", "FunctionInhibitionAvailabilityNeeds", "FunctionInhibitionNeeds", "Gateway", "GeneralPurposeConnection", "GeneralPurposeIPdu", "GeneralPurposePdu", "GenericEthernetFrame", "GlobalSupervisionNeeds", "GlobalTimeCanMaster", "GlobalTimeCanSlave", "GlobalTimeDomain", "GlobalTimeEthMaster", "GlobalTimeEthSlave", "GlobalTimeFrMaster", "GlobalTimeFrSlave", "GlobalTimeGateway", "HardwareTestNeeds", "HwAttributeDef", "HwAttributeLiteralDef", "HwCategory", "HwDescriptionEntity", "HwElement", "HwPin", "HwPinGroup", "HwType", "IEEE1722TpAafConnection", "IEEE1722TpAcfCan", "IEEE1722TpAcfCanPart", "IEEE1722TpAcfConnection", "IEEE1722TpAcfLin", "IEEE1722TpAcfLinPart", "IEEE1722TpConfig", "IEEE1722TpCrfConnection", "IEEE1722TpIidcConnection", "IPSecConfigProps", "IPSecRule", "IPduPort", "IPv6ExtHeaderFilterList", "IPv6ExtHeaderFilterSet", "ISignal", "ISignalGroup", "ISignalIPdu", "ISignalIPduGroup", "ISignalPort", "ISignalToIPduMapping", "ISignalTriggering", "IdsDesign", "IdsMgrCustomTimestampNeeds", "IdsMgrNeeds", "IdsmInstance", "IdsmProperties", "Ieee1722TpEthernetFrame", "ImplementationDataType", "ImplementationDataTypeElement", "ImplementationProps", "ImpositionTime", "IndicatorStatusNeeds", "InitEvent", "InternalTriggerOccurredEvent", "InternalTriggeringPoint", "InterpolationRoutineMappingSet", "J1939Cluster", "J1939ControllerApplication", "J1939DcmDm19Support", "J1939DcmIPdu", "J1939NmCluster", "J1939NmNode", "J1939RmIncomingRequestServiceNeeds", "J1939RmOutgoingRequestServiceNeeds", "J1939SharedAddressCluster", "J1939TpConfig", "J1939TpNode", "Keyword", "KeywordSet", "LatencyTimingConstraint", "LifeCycleInfoSet", "LifeCycleState", "LifeCycleStateDefinitionGroup", "LinCluster", "LinCommunicationConnector", "LinEventTriggeredFrame", "LinFrameTriggering", "LinMaster", "LinPhysicalChannel", "LinScheduleTable", "LinSlave", "LinSlaveConfigIdent", "LinSporadicFrame", "LinTpConfig", "LinTpNode", "LinUnconditionalFrame", "Linker", "LogAndTraceMessageCollectionSet", "MacMulticastGroup", "MacSecGlobalKayProps", "MacSecKayParticipant", "MacSecParticipantSet", "McDataInstance", "McFunction", "McGroup", "MeasuredExecutionTime", "MeasuredHeapUsage", "MeasuredStackUsage", "MemorySection", "ModeAccessPointIdent", "ModeDeclaration", "ModeDeclarationGroup", "ModeDeclarationGroupPrototype", "ModeDeclarationMapping", "ModeDeclarationMappingSet", "ModeInterfaceMapping", "ModeSwitchInterface", "ModeSwitchPoint", "ModeSwitchedAckEvent", "ModeTransition", "MultilanguageReferrable", "MultiplexedIPdu", "NPdu", "NetworkEndpoint", "NmConfig", "NmEcu", "NmPdu", "NvBlockDescriptor", "NvBlockNeeds", "NvBlockSwComponentType", "NvDataInterface", "ObdControlServiceNeeds", "ObdInfoServiceNeeds", "ObdMonitorServiceNeeds", "ObdPidServiceNeeds", "ObdRatioDenominatorNeeds", "ObdRatioServiceNeeds", "OffsetTimingConstraint", "OperationInvokedEvent", "OsTaskExecutionEvent", "OsTaskProxy", "PPortPrototype", "PRPortPrototype", "ParameterAccess", "ParameterDataPrototype", "ParameterInterface", "ParameterSwComponentType", "PassThroughSwConnector", "PduActivationRoutingGroup", "PduToFrameMapping", "PduTriggering", "PdurIPduGroup", "PerInstanceMemory", "PeriodicEventTriggering", "PhysicalDimension", "PhysicalDimensionMappingSet", "PncMappingIdent", "PortElementToCommunicationResourceMapping", "PortGroup", "PortInterfaceMappingSet", "PortPrototypeBlueprint", "PostBuildVariantCriterion", "PostBuildVariantCriterionValueSet", "PredefinedVariant", "PrimitiveAttributeTailoring", "ProvidedServiceInstance", "RPortPrototype", "RapidPrototypingScenario", "ReferenceTailoring", "ResourceConsumption", "RootSwCompositionPrototype", "RoughEstimateHeapUsage", "RoughEstimateOfExecutionTime", "RoughEstimateStackUsage", "RptComponent", "RptContainer", "RptExecutableEntity", "RptExecutableEntityEvent", "RptExecutionContext", "RptProfile", "RptServicePoint", "RteEventInCompositionSeparation", "RteEventInCompositionToOsTaskProxyMapping", "RteEventInSystemSeparation", "RteEventInSystemToOsTaskProxyMapping", "RunnableEntity", "RunnableEntityGroup", "RuntimeError", "SOMEIPTransformationProps", "Sdg", "SdgAggregationWithVariation", "SdgCaption", "SdgClass", "SdgDef", "SdgForeignReference", "SdgForeignReferenceWithVariation", "SdgPrimitiveAttribute", "SdgPrimitiveAttributeWithVariation", "SdgTailoring", "SecOcCryptoServiceMapping", "SectionNamePrefix", "SecureCommunicationAuthenticationProps", "SecureCommunicationFreshnessProps", "SecureCommunicationPropsSet", "SecureOnBoardCommunicationNeeds", "SecuredIPdu", "SecurityEventAggregationFilter", "SecurityEventContextMappingApplication", "SecurityEventContextMappingBswModule", "SecurityEventContextMappingCommConnector", "SecurityEventContextMappingFunctionalCluster", "SecurityEventContextProps", "SecurityEventDefinition", "SecurityEventFilterChain", "SecurityEventOneEveryNFilter", "SecurityEventStateFilter", "SenderReceiverInterface", "SensorActuatorSwComponentType", "ServiceInstanceCollectionSet", "ServiceProxySwComponentType", "ServiceSwComponentType", "SignalServiceTranslationElementProps", "SignalServiceTranslationEventProps", "SignalServiceTranslationProps", "SignalServiceTranslationPropsSet", "SingleLanguageReferrable", "SoAdRoutingGroup", "SoConIPduIdentifier", "SocketAddress", "SocketConnectionBundle", "SocketConnectionIpduIdentifierSet", "SomeipSdClientServiceInstanceConfig", "SomeipSdServerEventGroupTimingConfig", "SomeipSdServerServiceInstanceConfig", "SomeipTpChannel", "SomeipTpConfig", "SpecificationDocumentScope", "SporadicEventTriggering", "StaticSocketConnection", "Std", "StructuredReq", "SupervisedEntityCheckpointNeeds", "SupervisedEntityNeeds", "SwAddrMethod", "SwAxisType", "SwBaseType", "SwGenericAxisParamType", "SwRecordLayout", "SwServiceArg", "SwSystemconst", "SwSystemconstantValueSet", "SwcBswMapping", "SwcImplementation", "SwcInternalBehavior", "SwcModeManagerErrorEvent", "SwcModeSwitchEvent", "SwcServiceDependency", "SwcTiming", "SwcToApplicationPartitionMapping", "SwcToEcuMapping", "SwcToImplMapping", "SwitchAsynchronousTrafficShaperGroupEntry", "SwitchFlowMeteringEntry", "SwitchStreamFilterActionDestPortModification", "SwitchStreamFilterEntry", "SwitchStreamFilterRule", "SwitchStreamGateEntry", "SwitchStreamIdentification", "SymbolProps", "SyncTimeBaseMgrUserNeeds", "SynchronizationPointConstraint", "SynchronousServerCallPoint", "System", "SystemMapping", "SystemSignal", "SystemSignalGroup", "SystemSignalGroupToCommunicationResourceMapping", "SystemSignalToCommunicationResourceMapping", "SystemTiming", "TDCpSoftwareClusterMapping", "TDCpSoftwareClusterMappingSet", "TDCpSoftwareClusterResourceMapping", "TDEventBswInternalBehavior", "TDEventBswModeDeclaration", "TDEventBswModule", "TDEventComplex", "TDEventFrClusterCycleStart", "TDEventFrame", "TDEventFrameEthernet", "TDEventIPdu", "TDEventISignal", "TDEventModeDeclaration", "TDEventOperation", "TDEventSLLETPort", "TDEventSwcInternalBehavior", "TDEventSwcInternalBehaviorReference", "TDEventTTCanCycleStart", "TDEventTrigger", "TDEventVariableDataPrototype", "TDEventVfbReference", "TDLETZoneClock", "TcpOptionFilterList", "TcpOptionFilterSet", "TimeSyncServerConfiguration", "TimingClockSyncAccuracy", "TimingCondition", "TimingDescriptionEventChain", "TimingEvent", "TimingExtensionResource", "TimingModeInstance", "TlsCryptoCipherSuite", "TlsCryptoCipherSuiteProps", "TlsCryptoServiceMapping", "TlvDataIdDefinitionSet", "Topic1", "TpAddress", "TpConnectionIdent", "TraceableText", "TransformationPropsSet", "TransformationTechnology", "TransformerHardErrorEvent", "TransientFault", "Trigger", "TriggerInterface", "TriggerInterfaceMapping", "TtcanCluster", "TtcanCommunicationConnector", "TtcanCommunicationController", "TtcanPhysicalChannel", "UdpNmCluster", "UdpNmNode", "Unit", "UnitGroup", "UserDefinedCluster", "UserDefinedCommunicationConnector", "UserDefinedCommunicationController", "UserDefinedEthernetFrame", "UserDefinedGlobalTimeMaster", "UserDefinedGlobalTimeSlave", "UserDefinedIPdu", "UserDefinedPdu", "UserDefinedTransformationProps", "V2xDataManagerNeeds", "V2xFacUserNeeds", "V2xMUserNeeds", "VariableAccess", "VariableDataPrototype", "VariationPointProxy", "VendorSpecificServiceNeeds", "VfbTiming", "ViewMap", "ViewMapSet", "VlanConfig", "WaitPoint", "WorstCaseHeapUsage", "WorstCaseStackUsage", "Xdoc", "Xfile", "XrefTarget"]),
    }


    def __init__(self) -> None:
        """Initialize SdgContents."""
        super().__init__()
        self.sd: Optional[Sd] = None
        self.sdf: Optional[Sdf] = None
        self.sdg: Optional[Sdg] = None
        self.sdx_ref: Optional[ARRef] = None
        self.sdxf_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SdgContents to XML element (atp_mixed - no wrapping).

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SdgContents, self).serialize()

        # Copy all attributes from parent element to current element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element to current element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element to current element
        for child in parent_elem:
            elem.append(child)

        # Serialize sd (complex type)
        if self.sd is not None:
            serialized = SerializationHelper.serialize_item(self.sd, "Sd")
            if serialized is not None:
                wrapped = ET.Element("SD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdf (complex type)
        if self.sdf is not None:
            serialized = SerializationHelper.serialize_item(self.sdf, "Sdf")
            if serialized is not None:
                wrapped = ET.Element("SDF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdg (complex type)
        if self.sdg is not None:
            serialized = SerializationHelper.serialize_item(self.sdg, "Sdg")
            if serialized is not None:
                wrapped = ET.Element("SDG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdx_ref (reference)
        if self.sdx_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sdx_ref, "Referrable")
            if serialized is not None:
                wrapped = ET.Element("SDX-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdxf_ref (reference)
        if self.sdxf_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sdxf_ref, "Referrable")
            if serialized is not None:
                wrapped = ET.Element("SDXF-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgContents":
        """Deserialize XML element to SdgContents object (atp_mixed - no unwrapping).

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SdgContents object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SdgContents, cls).deserialize(element)

        # Parse sd
        child = SerializationHelper.find_child_element(element, "SD")
        if child is not None:
            sd_value = SerializationHelper.deserialize_by_tag(child, "Sd")
            obj.sd = sd_value

        # Parse sdf
        child = SerializationHelper.find_child_element(element, "SDF")
        if child is not None:
            sdf_value = SerializationHelper.deserialize_by_tag(child, "Sdf")
            obj.sdf = sdf_value

        # Parse sdg
        child = SerializationHelper.find_child_element(element, "SDG")
        if child is not None:
            sdg_value = SerializationHelper.deserialize_by_tag(child, "Sdg")
            obj.sdg = sdg_value

        # Parse sdx_ref
        child = SerializationHelper.find_child_element(element, "SDX-REF")
        if child is not None:
            sdx_ref_value = SerializationHelper.deserialize_by_tag(child, "Referrable")
            obj.sdx_ref = sdx_ref_value

        # Parse sdxf_ref
        child = SerializationHelper.find_child_element(element, "SDXF-REF")
        if child is not None:
            sdxf_ref_value = SerializationHelper.deserialize_by_tag(child, "Referrable")
            obj.sdxf_ref = sdxf_ref_value

        return obj



class SdgContentsBuilder(BuilderBase):
    """Builder for SdgContents with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SdgContents = SdgContents()


    def with_sd(self, value: Optional[Sd]) -> "SdgContentsBuilder":
        """Set sd attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sd = value
        return self

    def with_sdf(self, value: Optional[Sdf]) -> "SdgContentsBuilder":
        """Set sdf attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sdf = value
        return self

    def with_sdg(self, value: Optional[Sdg]) -> "SdgContentsBuilder":
        """Set sdg attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sdg = value
        return self

    def with_sdx(self, value: Optional[Referrable]) -> "SdgContentsBuilder":
        """Set sdx attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sdx = value
        return self

    def with_sdxf(self, value: Optional[Referrable]) -> "SdgContentsBuilder":
        """Set sdxf attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sdxf = value
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


    def build(self) -> SdgContents:
        """Build and return the SdgContents instance with validation."""
        self._validate_instance()
        pass
        return self._obj