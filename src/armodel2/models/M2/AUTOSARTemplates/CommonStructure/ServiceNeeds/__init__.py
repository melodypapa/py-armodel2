"""ServiceNeeds module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_dependency import (
        ServiceDependency,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.role_based_data_assignment import (
        RoleBasedDataAssignment,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
        ServiceNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.nv_block_needs import (
        NvBlockNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.supervised_entity_needs import (
        SupervisedEntityNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.com_mgr_user_needs import (
        ComMgrUserNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.ecu_state_mgr_user_needs import (
        EcuStateMgrUserNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.crypto_service_needs import (
        CryptoServiceNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.dlt_user_needs import (
        DltUserNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.sync_time_base_mgr_user_needs import (
        SyncTimeBaseMgrUserNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
        DiagnosticCapabilityElement,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.function_inhibition_needs import (
        FunctionInhibitionNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.do_ip_service_needs import (
        DoIpServiceNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_value_needs import (
        DiagnosticValueNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_routine_needs import (
        DiagnosticRoutineNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_io_control_needs import (
        DiagnosticIoControlNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostics_communication_security_needs import (
        DiagnosticsCommunicationSecurityNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_communication_manager_needs import (
        DiagnosticCommunicationManagerNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_upload_download_needs import (
        DiagnosticUploadDownloadNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.supervised_entity_checkpoint_needs import (
        SupervisedEntityCheckpointNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_event_needs import (
        DiagnosticEventNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diag_event_debounce_algorithm import (
        DiagEventDebounceAlgorithm,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diag_event_debounce_counter_based import (
        DiagEventDebounceCounterBased,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diag_event_debounce_time_based import (
        DiagEventDebounceTimeBased,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diag_event_debounce_monitor_internal import (
        DiagEventDebounceMonitorInternal,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.error_tracer_needs import (
        ErrorTracerNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.traced_failure import (
        TracedFailure,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.development_error import (
        DevelopmentError,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.runtime_error import (
        RuntimeError,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.hardware_test_needs import (
        HardwareTestNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_component_needs import (
        DiagnosticComponentNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_event_info_needs import (
        DiagnosticEventInfoNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.function_inhibition_availability_needs import (
        FunctionInhibitionAvailabilityNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.global_supervision_needs import (
        GlobalSupervisionNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.obd_info_service_needs import (
        ObdInfoServiceNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.obd_pid_service_needs import (
        ObdPidServiceNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.obd_control_service_needs import (
        ObdControlServiceNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.obd_monitor_service_needs import (
        ObdMonitorServiceNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.vendor_specific_service_needs import (
        VendorSpecificServiceNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.symbolic_name_props import (
        SymbolicNameProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.bsw_mgr_needs import (
        BswMgrNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.crypto_service_job_needs import (
        CryptoServiceJobNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.crypto_key_management_needs import (
        CryptoKeyManagementNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_event_manager_needs import (
        DiagnosticEventManagerNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_operation_cycle_needs import (
        DiagnosticOperationCycleNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_enable_condition_needs import (
        DiagnosticEnableConditionNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_storage_condition_needs import (
        DiagnosticStorageConditionNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.indicator_status_needs import (
        IndicatorStatusNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.dtc_status_change_notification_needs import (
        DtcStatusChangeNotificationNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_request_file_transfer_needs import (
        DiagnosticRequestFileTransferNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.obd_ratio_service_needs import (
        ObdRatioServiceNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.obd_ratio_denominator_needs import (
        ObdRatioDenominatorNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.do_ip_gid_needs import (
        DoIpGidNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.do_ip_gid_synchronization_needs import (
        DoIpGidSynchronizationNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.do_ip_power_mode_status_needs import (
        DoIpPowerModeStatusNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.do_ip_routing_activation_authentication_needs import (
        DoIpRoutingActivationAuthenticationNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.do_ip_routing_activation_confirmation_needs import (
        DoIpRoutingActivationConfirmationNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.do_ip_activation_line_needs import (
        DoIpActivationLineNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.warning_indicator_requested_bit_needs import (
        WarningIndicatorRequestedBitNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.further_action_byte_needs import (
        FurtherActionByteNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_control_needs import (
        DiagnosticControlNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.secure_on_board_communication_needs import (
        SecureOnBoardCommunicationNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.j1939_rm_outgoing_request_service_needs import (
        J1939RmOutgoingRequestServiceNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.j1939_rm_incoming_request_service_needs import (
        J1939RmIncomingRequestServiceNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.j1939_dcm_dm19_support import (
        J1939DcmDm19Support,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.v2x_fac_user_needs import (
        V2xFacUserNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.v2x_m_user_needs import (
        V2xMUserNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.v2x_data_manager_needs import (
        V2xDataManagerNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.ids_mgr_needs import (
        IdsMgrNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.ids_mgr_custom_timestamp_needs import (
        IdsMgrCustomTimestampNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.transient_fault import (
        TransientFault,
    )

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.nv_block_needs_reliability_enum import (
    NvBlockNeedsReliabilityEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.nv_block_needs_writing_priority_enum import (
    NvBlockNeedsWritingPriorityEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.max_comm_mode_enum import (
    MaxCommModeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_value_access_enum import (
    DiagnosticValueAccessEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_processing_style_enum import (
    DiagnosticProcessingStyleEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_routine_type_enum import (
    DiagnosticRoutineTypeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_provider_enum import (
    ServiceProviderEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_diagnostic_relevance_enum import (
    ServiceDiagnosticRelevanceEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_audience_enum import (
    DiagnosticAudienceEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.operation_cycle_type_enum import (
    OperationCycleTypeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.event_acceptance_status_enum import (
    EventAcceptanceStatusEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.storage_condition_status_enum import (
    StorageConditionStatusEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_clear_dtc_notification_enum import (
    DiagnosticClearDtcNotificationEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_service_request_callback_type_enum import (
    DiagnosticServiceRequestCallbackTypeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.obd_ratio_connection_kind_enum import (
    ObdRatioConnectionKindEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_monitor_update_kind_enum import (
    DiagnosticMonitorUpdateKindEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_denominator_condition_enum import (
    DiagnosticDenominatorConditionEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.verification_status_indication_mode_enum import (
    VerificationStatusIndicationModeEnum,
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
    "DiagnosticAudienceEnum",
    "DiagnosticCapabilityElement",
    "DiagnosticClearDtcNotificationEnum",
    "DiagnosticCommunicationManagerNeeds",
    "DiagnosticComponentNeeds",
    "DiagnosticControlNeeds",
    "DiagnosticDenominatorConditionEnum",
    "DiagnosticEnableConditionNeeds",
    "DiagnosticEventInfoNeeds",
    "DiagnosticEventManagerNeeds",
    "DiagnosticEventNeeds",
    "DiagnosticIoControlNeeds",
    "DiagnosticMonitorUpdateKindEnum",
    "DiagnosticOperationCycleNeeds",
    "DiagnosticProcessingStyleEnum",
    "DiagnosticRequestFileTransferNeeds",
    "DiagnosticRoutineNeeds",
    "DiagnosticRoutineTypeEnum",
    "DiagnosticServiceRequestCallbackTypeEnum",
    "DiagnosticStorageConditionNeeds",
    "DiagnosticUploadDownloadNeeds",
    "DiagnosticValueAccessEnum",
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
    "EventAcceptanceStatusEnum",
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
    "MaxCommModeEnum",
    "NvBlockNeeds",
    "NvBlockNeedsReliabilityEnum",
    "NvBlockNeedsWritingPriorityEnum",
    "ObdControlServiceNeeds",
    "ObdInfoServiceNeeds",
    "ObdMonitorServiceNeeds",
    "ObdPidServiceNeeds",
    "ObdRatioConnectionKindEnum",
    "ObdRatioDenominatorNeeds",
    "ObdRatioServiceNeeds",
    "OperationCycleTypeEnum",
    "RoleBasedDataAssignment",
    "RuntimeError",
    "SecureOnBoardCommunicationNeeds",
    "ServiceDependency",
    "ServiceDiagnosticRelevanceEnum",
    "ServiceNeeds",
    "ServiceProviderEnum",
    "StorageConditionStatusEnum",
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
    "VerificationStatusIndicationModeEnum",
    "WarningIndicatorRequestedBitNeeds",
]
