"""ServiceNeeds module."""
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_dependency import (
    ServiceDependency,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.role_based_data_assignment import (
    RoleBasedDataAssignment,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.nv_block_needs import (
    NvBlockNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.supervised_entity_needs import (
    SupervisedEntityNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.com_mgr_user_needs import (
    ComMgrUserNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.ecu_state_mgr_user_needs import (
    EcuStateMgrUserNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.crypto_service_needs import (
    CryptoServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.dlt_user_needs import (
    DltUserNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.sync_time_base_mgr_user_needs import (
    SyncTimeBaseMgrUserNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.function_inhibition_needs import (
    FunctionInhibitionNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.do_ip_service_needs import (
    DoIpServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_value_needs import (
    DiagnosticValueNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_routine_needs import (
    DiagnosticRoutineNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_io_control_needs import (
    DiagnosticIoControlNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostics_communication_security_needs import (
    DiagnosticsCommunicationSecurityNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_communication_manager_needs import (
    DiagnosticCommunicationManagerNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_upload_download_needs import (
    DiagnosticUploadDownloadNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.supervised_entity_checkpoint_needs import (
    SupervisedEntityCheckpointNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_event_needs import (
    DiagnosticEventNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diag_event_debounce_algorithm import (
    DiagEventDebounceAlgorithm,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diag_event_debounce_counter_based import (
    DiagEventDebounceCounterBased,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diag_event_debounce_time_based import (
    DiagEventDebounceTimeBased,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diag_event_debounce_monitor_internal import (
    DiagEventDebounceMonitorInternal,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.error_tracer_needs import (
    ErrorTracerNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.traced_failure import (
    TracedFailure,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.development_error import (
    DevelopmentError,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.runtime_error import (
    RuntimeError,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.hardware_test_needs import (
    HardwareTestNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_component_needs import (
    DiagnosticComponentNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_event_info_needs import (
    DiagnosticEventInfoNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.function_inhibition_availability_needs import (
    FunctionInhibitionAvailabilityNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.global_supervision_needs import (
    GlobalSupervisionNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.obd_info_service_needs import (
    ObdInfoServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.obd_pid_service_needs import (
    ObdPidServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.obd_control_service_needs import (
    ObdControlServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.obd_monitor_service_needs import (
    ObdMonitorServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.vendor_specific_service_needs import (
    VendorSpecificServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.symbolic_name_props import (
    SymbolicNameProps,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.bsw_mgr_needs import (
    BswMgrNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.crypto_service_job_needs import (
    CryptoServiceJobNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.crypto_key_management_needs import (
    CryptoKeyManagementNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_event_manager_needs import (
    DiagnosticEventManagerNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_operation_cycle_needs import (
    DiagnosticOperationCycleNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_enable_condition_needs import (
    DiagnosticEnableConditionNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_storage_condition_needs import (
    DiagnosticStorageConditionNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.indicator_status_needs import (
    IndicatorStatusNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.dtc_status_change_notification_needs import (
    DtcStatusChangeNotificationNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_request_file_transfer_needs import (
    DiagnosticRequestFileTransferNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.obd_ratio_service_needs import (
    ObdRatioServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.obd_ratio_denominator_needs import (
    ObdRatioDenominatorNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.do_ip_gid_needs import (
    DoIpGidNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.do_ip_gid_synchronization_needs import (
    DoIpGidSynchronizationNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.do_ip_power_mode_status_needs import (
    DoIpPowerModeStatusNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.do_ip_routing_activation_authentication_needs import (
    DoIpRoutingActivationAuthenticationNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.do_ip_routing_activation_confirmation_needs import (
    DoIpRoutingActivationConfirmationNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.do_ip_activation_line_needs import (
    DoIpActivationLineNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.warning_indicator_requested_bit_needs import (
    WarningIndicatorRequestedBitNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.further_action_byte_needs import (
    FurtherActionByteNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_control_needs import (
    DiagnosticControlNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.secure_on_board_communication_needs import (
    SecureOnBoardCommunicationNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.j1939_rm_outgoing_request_service_needs import (
    J1939RmOutgoingRequestServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.j1939_rm_incoming_request_service_needs import (
    J1939RmIncomingRequestServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.j1939_dcm_dm19_support import (
    J1939DcmDm19Support,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.v2x_fac_user_needs import (
    V2xFacUserNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.v2x_m_user_needs import (
    V2xMUserNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.v2x_data_manager_needs import (
    V2xDataManagerNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.ids_mgr_needs import (
    IdsMgrNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.ids_mgr_custom_timestamp_needs import (
    IdsMgrCustomTimestampNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.transient_fault import (
    TransientFault,
)

__all__ = [
    "BswMgrNeeds",
    "ComMgrUserNeeds",
    "CryptoKeyManagementNeeds",
    "CryptoServiceJobNeeds",
    "CryptoServiceNeeds",
    "DevelopmentError",
    "DiagEventDebounceAlgorithm",
    "DiagEventDebounceCounterBased",
    "DiagEventDebounceMonitorInternal",
    "DiagEventDebounceTimeBased",
    "DiagnosticCapabilityElement",
    "DiagnosticCommunicationManagerNeeds",
    "DiagnosticComponentNeeds",
    "DiagnosticControlNeeds",
    "DiagnosticEnableConditionNeeds",
    "DiagnosticEventInfoNeeds",
    "DiagnosticEventManagerNeeds",
    "DiagnosticEventNeeds",
    "DiagnosticIoControlNeeds",
    "DiagnosticOperationCycleNeeds",
    "DiagnosticRequestFileTransferNeeds",
    "DiagnosticRoutineNeeds",
    "DiagnosticStorageConditionNeeds",
    "DiagnosticUploadDownloadNeeds",
    "DiagnosticValueNeeds",
    "DiagnosticsCommunicationSecurityNeeds",
    "DltUserNeeds",
    "DoIpActivationLineNeeds",
    "DoIpGidNeeds",
    "DoIpGidSynchronizationNeeds",
    "DoIpPowerModeStatusNeeds",
    "DoIpRoutingActivationAuthenticationNeeds",
    "DoIpRoutingActivationConfirmationNeeds",
    "DoIpServiceNeeds",
    "DtcStatusChangeNotificationNeeds",
    "EcuStateMgrUserNeeds",
    "ErrorTracerNeeds",
    "FunctionInhibitionAvailabilityNeeds",
    "FunctionInhibitionNeeds",
    "FurtherActionByteNeeds",
    "GlobalSupervisionNeeds",
    "HardwareTestNeeds",
    "IdsMgrCustomTimestampNeeds",
    "IdsMgrNeeds",
    "IndicatorStatusNeeds",
    "J1939DcmDm19Support",
    "J1939RmIncomingRequestServiceNeeds",
    "J1939RmOutgoingRequestServiceNeeds",
    "NvBlockNeeds",
    "ObdControlServiceNeeds",
    "ObdInfoServiceNeeds",
    "ObdMonitorServiceNeeds",
    "ObdPidServiceNeeds",
    "ObdRatioDenominatorNeeds",
    "ObdRatioServiceNeeds",
    "RoleBasedDataAssignment",
    "RuntimeError",
    "SecureOnBoardCommunicationNeeds",
    "ServiceDependency",
    "ServiceNeeds",
    "SupervisedEntityCheckpointNeeds",
    "SupervisedEntityNeeds",
    "SymbolicNameProps",
    "SyncTimeBaseMgrUserNeeds",
    "TracedFailure",
    "TransientFault",
    "V2xDataManagerNeeds",
    "V2xFacUserNeeds",
    "V2xMUserNeeds",
    "VendorSpecificServiceNeeds",
    "WarningIndicatorRequestedBitNeeds",
]
