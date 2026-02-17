"""TimingDescription module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb import (
        TDEventVfb,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb_reference import (
        TDEventVfbReference,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb_port import (
        TDEventVfbPort,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_variable_data_prototype import (
        TDEventVariableDataPrototype,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_operation import (
        TDEventOperation,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_mode_declaration import (
        TDEventModeDeclaration,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_trigger import (
        TDEventTrigger,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_swc import (
        TDEventSwc,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_swc_internal_behavior import (
        TDEventSwcInternalBehavior,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_swc_internal_behavior_reference import (
        TDEventSwcInternalBehaviorReference,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_com import (
        TDEventCom,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_i_signal import (
        TDEventISignal,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_i_pdu import (
        TDEventIPdu,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_frame import (
        TDEventFrame,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_frame_ethernet import (
        TDEventFrameEthernet,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_header_id_range import (
        TDHeaderIdRange,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_cycle_start import (
        TDEventCycleStart,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_fr_cluster_cycle_start import (
        TDEventFrClusterCycleStart,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_tt_can_cycle_start import (
        TDEventTTCanCycleStart,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_bsw_internal_behavior import (
        TDEventBswInternalBehavior,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_bsw_module import (
        TDEventBswModule,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_bsw_mode_declaration import (
        TDEventBswModeDeclaration,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_complex import (
        TDEventComplex,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_sllet_port import (
        TDEventSLLETPort,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_occurrence_expression import (
        TDEventOccurrenceExpression,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_occurrence_expression_formula import (
        TDEventOccurrenceExpressionFormula,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.autosar_variable_instance import (
        AutosarVariableInstance,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.autosar_operation_argument_instance import (
        AutosarOperationArgumentInstance,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_bsw import (
        TDEventBsw,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_sllet import (
        TDEventSLLET,
    )

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_variable_data_prototype_type_enum import (
    TDEventVariableDataPrototypeTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_operation_type_enum import (
    TDEventOperationTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_mode_declaration_type_enum import (
    TDEventModeDeclarationTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_trigger_type_enum import (
    TDEventTriggerTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_swc_internal_behavior_type_enum import (
    TDEventSwcInternalBehaviorTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_i_signal_type_enum import (
    TDEventISignalTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_i_pdu_type_enum import (
    TDEventIPduTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_frame_type_enum import (
    TDEventFrameTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_frame_ethernet_type_enum import (
    TDEventFrameEthernetTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_bsw_internal_behavior_type_enum import (
    TDEventBswInternalBehaviorTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_bsw_module_type_enum import (
    TDEventBswModuleTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_bsw_mode_declaration_type_enum import (
    TDEventBswModeDeclarationTypeEnum,
)

__all__ = [
    "AutosarOperationArgumentInstance",
    "AutosarVariableInstance",
    "TDEventBsw",
    "TDEventBswInternalBehavior",
    "TDEventBswInternalBehaviorTypeEnum",
    "TDEventBswModeDeclaration",
    "TDEventBswModeDeclarationTypeEnum",
    "TDEventBswModule",
    "TDEventBswModuleTypeEnum",
    "TDEventCom",
    "TDEventComplex",
    "TDEventCycleStart",
    "TDEventFrClusterCycleStart",
    "TDEventFrame",
    "TDEventFrameEthernet",
    "TDEventFrameEthernetTypeEnum",
    "TDEventFrameTypeEnum",
    "TDEventIPdu",
    "TDEventIPduTypeEnum",
    "TDEventISignal",
    "TDEventISignalTypeEnum",
    "TDEventModeDeclaration",
    "TDEventModeDeclarationTypeEnum",
    "TDEventOccurrenceExpression",
    "TDEventOccurrenceExpressionFormula",
    "TDEventOperation",
    "TDEventOperationTypeEnum",
    "TDEventSLLET",
    "TDEventSLLETPort",
    "TDEventSwc",
    "TDEventSwcInternalBehavior",
    "TDEventSwcInternalBehaviorReference",
    "TDEventSwcInternalBehaviorTypeEnum",
    "TDEventTTCanCycleStart",
    "TDEventTrigger",
    "TDEventTriggerTypeEnum",
    "TDEventVariableDataPrototype",
    "TDEventVariableDataPrototypeTypeEnum",
    "TDEventVfb",
    "TDEventVfbPort",
    "TDEventVfbReference",
    "TDHeaderIdRange",
]
