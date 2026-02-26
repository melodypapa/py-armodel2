"""CoreCommunication module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal import (
        ISignal,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_i_pdu_group import (
        ISignalIPduGroup,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.j1939_dcm_i_pdu import (
        J1939DcmIPdu,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
        SystemSignal,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame import (
        Frame,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import (
        FrameTriggering,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.n_pdu import (
        NPdu,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.nm_pdu import (
        NmPdu,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu import (
        Pdu,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
        PduTriggering,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.user_defined_pdu import (
        UserDefinedPdu,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_group import (
        ISignalGroup,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_i_pdu import (
        ISignalIPdu,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_port import (
        FramePort,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu_port import (
        IPduPort,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_port import (
        ISignalPort,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_props import (
        ISignalProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal_group import (
        SystemSignalGroup,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_to_i_pdu_mapping import (
        ISignalToIPduMapping,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_triggering import (
        ISignalTriggering,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
        IPdu,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.dcm_i_pdu import (
        DcmIPdu,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.general_purpose_pdu import (
        GeneralPurposePdu,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.general_purpose_i_pdu import (
        GeneralPurposeIPdu,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.user_defined_i_pdu import (
        UserDefinedIPdu,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_to_frame_mapping import (
        PduToFrameMapping,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu_timing import (
        IPduTiming,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdur_i_pdu_group import (
        PdurIPduGroup,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.container_i_pdu import (
        ContainerIPdu,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.contained_i_pdu_props import (
        ContainedIPduProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.secured_i_pdu import (
        SecuredIPdu,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.secure_communication_props import (
        SecureCommunicationProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.secure_communication_props_set import (
        SecureCommunicationPropsSet,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.secure_communication_freshness_props import (
        SecureCommunicationFreshnessProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.secure_communication_authentication_props import (
        SecureCommunicationAuthenticationProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.multiplexed_i_pdu import (
        MultiplexedIPdu,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.static_part import (
        StaticPart,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.dynamic_part import (
        DynamicPart,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.dynamic_part_alternative import (
        DynamicPartAlternative,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.multiplexed_part import (
        MultiplexedPart,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.segment_position import (
        SegmentPosition,
    )

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu_signal_processing_enum import (
    IPduSignalProcessingEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_type_enum import (
    ISignalTypeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.transfer_property_enum import (
    TransferPropertyEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.diag_pdu_type import (
    DiagPduType,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.communication_direction_type import (
    CommunicationDirectionType,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.container_i_pdu_trigger_enum import (
    ContainerIPduTriggerEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.container_i_pdu_header_type_enum import (
    ContainerIPduHeaderTypeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.rx_accept_contained_i_pdu_enum import (
    RxAcceptContainedIPduEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.contained_i_pdu_collection_semantics_enum import (
    ContainedIPduCollectionSemanticsEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.secured_pdu_header_enum import (
    SecuredPduHeaderEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.trigger_mode import (
    TriggerMode,
)

__all__ = [
    "CommunicationDirectionType",
    "ContainedIPduCollectionSemanticsEnum",
    "ContainedIPduProps",
    "ContainerIPdu",
    "ContainerIPduHeaderTypeEnum",
    "ContainerIPduTriggerEnum",
    "DcmIPdu",
    "DiagPduType",
    "DynamicPart",
    "DynamicPartAlternative",
    "Frame",
    "FramePort",
    "FrameTriggering",
    "GeneralPurposeIPdu",
    "GeneralPurposePdu",
    "IPdu",
    "IPduPort",
    "IPduSignalProcessingEnum",
    "IPduTiming",
    "ISignal",
    "ISignalGroup",
    "ISignalIPdu",
    "ISignalIPduGroup",
    "ISignalPort",
    "ISignalProps",
    "ISignalToIPduMapping",
    "ISignalTriggering",
    "ISignalTypeEnum",
    "J1939DcmIPdu",
    "MultiplexedIPdu",
    "MultiplexedPart",
    "NPdu",
    "NmPdu",
    "Pdu",
    "PduToFrameMapping",
    "PduTriggering",
    "PdurIPduGroup",
    "RxAcceptContainedIPduEnum",
    "SecureCommunicationAuthenticationProps",
    "SecureCommunicationFreshnessProps",
    "SecureCommunicationProps",
    "SecureCommunicationPropsSet",
    "SecuredIPdu",
    "SecuredPduHeaderEnum",
    "SegmentPosition",
    "StaticPart",
    "SystemSignal",
    "SystemSignalGroup",
    "TransferPropertyEnum",
    "TriggerMode",
    "UserDefinedIPdu",
    "UserDefinedPdu",
]
