"""BswBehavior module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_internal_behavior import (
        BswInternalBehavior,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import (
        BswModuleEntity,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_called_entity import (
        BswCalledEntity,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedulable_entity import (
        BswSchedulableEntity,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_interrupt_entity import (
        BswInterruptEntity,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_call_point import (
        BswModuleCallPoint,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_direct_call_point import (
        BswDirectCallPoint,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_synchronous_server_call_point import (
        BswSynchronousServerCallPoint,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_asynchronous_server_call_point import (
        BswAsynchronousServerCallPoint,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_asynchronous_server_call_result_point import (
        BswAsynchronousServerCallResultPoint,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_variable_access import (
        BswVariableAccess,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_exclusive_area_policy import (
        BswExclusiveAreaPolicy,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_scheduler_name_prefix import (
        BswSchedulerNamePrefix,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_event import (
        BswEvent,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import (
        BswScheduleEvent,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_interrupt_event import (
        BswInterruptEvent,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_timing_event import (
        BswTimingEvent,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_background_event import (
        BswBackgroundEvent,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_os_task_execution_event import (
        BswOsTaskExecutionEvent,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_internal_triggering_point import (
        BswInternalTriggeringPoint,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_internal_trigger_occurred_event import (
        BswInternalTriggerOccurredEvent,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_external_trigger_occurred_event import (
        BswExternalTriggerOccurredEvent,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_mode_switch_event import (
        BswModeSwitchEvent,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_mode_switched_ack_event import (
        BswModeSwitchedAckEvent,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_mode_manager_error_event import (
        BswModeManagerErrorEvent,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_operation_invoked_event import (
        BswOperationInvokedEvent,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_asynchronous_server_call_returns_event import (
        BswAsynchronousServerCallReturnsEvent,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_data_received_event import (
        BswDataReceivedEvent,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_trigger_direct_implementation import (
        BswTriggerDirectImplementation,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_mode_sender_policy import (
        BswModeSenderPolicy,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_mode_switch_ack_request import (
        BswModeSwitchAckRequest,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_mode_receiver_policy import (
        BswModeReceiverPolicy,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_data_reception_policy import (
        BswDataReceptionPolicy,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_queued_data_reception_policy import (
        BswQueuedDataReceptionPolicy,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_distinguished_partition import (
        BswDistinguishedPartition,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_service_dependency import (
        BswServiceDependency,
    )
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.role_based_bsw_module_entry_assignment import (
        RoleBasedBswModuleEntryAssignment,
    )

from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_interrupt_category import (
    BswInterruptCategory,
)

__all__ = [
    "BswAsynchronousServerCallPoint",
    "BswAsynchronousServerCallResultPoint",
    "BswAsynchronousServerCallReturnsEvent",
    "BswBackgroundEvent",
    "BswCalledEntity",
    "BswDataReceivedEvent",
    "BswDataReceptionPolicy",
    "BswDirectCallPoint",
    "BswDistinguishedPartition",
    "BswEvent",
    "BswExclusiveAreaPolicy",
    "BswExternalTriggerOccurredEvent",
    "BswInternalBehavior",
    "BswInternalTriggerOccurredEvent",
    "BswInternalTriggeringPoint",
    "BswInterruptCategory",
    "BswInterruptEntity",
    "BswInterruptEvent",
    "BswModeManagerErrorEvent",
    "BswModeReceiverPolicy",
    "BswModeSenderPolicy",
    "BswModeSwitchAckRequest",
    "BswModeSwitchEvent",
    "BswModeSwitchedAckEvent",
    "BswModuleCallPoint",
    "BswModuleEntity",
    "BswOperationInvokedEvent",
    "BswOsTaskExecutionEvent",
    "BswQueuedDataReceptionPolicy",
    "BswSchedulableEntity",
    "BswScheduleEvent",
    "BswSchedulerNamePrefix",
    "BswServiceDependency",
    "BswSynchronousServerCallPoint",
    "BswTimingEvent",
    "BswTriggerDirectImplementation",
    "BswVariableAccess",
    "RoleBasedBswModuleEntryAssignment",
]
