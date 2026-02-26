"""Communication module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
        PPortComSpec,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
        RPortComSpec,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.receiver_com_spec import (
        ReceiverComSpec,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.nonqueued_receiver_com_spec import (
        NonqueuedReceiverComSpec,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.queued_receiver_com_spec import (
        QueuedReceiverComSpec,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.reception_com_spec_props import (
        ReceptionComSpecProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.sender_com_spec import (
        SenderComSpec,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.queued_sender_com_spec import (
        QueuedSenderComSpec,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.nonqueued_sender_com_spec import (
        NonqueuedSenderComSpec,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.transmission_com_spec_props import (
        TransmissionComSpecProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.transmission_acknowledgement_request import (
        TransmissionAcknowledgementRequest,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.composite_network_representation import (
        CompositeNetworkRepresentation,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.client_com_spec import (
        ClientComSpec,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.server_com_spec import (
        ServerComSpec,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.mode_switch_sender_com_spec import (
        ModeSwitchSenderComSpec,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.mode_switched_ack_request import (
        ModeSwitchedAckRequest,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.mode_switch_receiver_com_spec import (
        ModeSwitchReceiverComSpec,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.parameter_provide_com_spec import (
        ParameterProvideComSpec,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.parameter_require_com_spec import (
        ParameterRequireComSpec,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.nv_require_com_spec import (
        NvRequireComSpec,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.nv_provide_com_spec import (
        NvProvideComSpec,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.transformation_com_spec_props import (
        TransformationComSpecProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.user_defined_transformation_com_spec_props import (
        UserDefinedTransformationComSpecProps,
    )

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.handle_invalid_enum import (
    HandleInvalidEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.handle_out_of_range_status_enum import (
    HandleOutOfRangeStatusEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.handle_timeout_enum import (
    HandleTimeoutEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.handle_out_of_range_enum import (
    HandleOutOfRangeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.transmission_mode_definition_enum import (
    TransmissionModeDefinitionEnum,
)

__all__ = [
    "ClientComSpec",
    "CompositeNetworkRepresentation",
    "HandleInvalidEnum",
    "HandleOutOfRangeEnum",
    "HandleOutOfRangeStatusEnum",
    "HandleTimeoutEnum",
    "ModeSwitchReceiverComSpec",
    "ModeSwitchSenderComSpec",
    "ModeSwitchedAckRequest",
    "NonqueuedReceiverComSpec",
    "NonqueuedSenderComSpec",
    "NvProvideComSpec",
    "NvRequireComSpec",
    "PPortComSpec",
    "ParameterProvideComSpec",
    "ParameterRequireComSpec",
    "QueuedReceiverComSpec",
    "QueuedSenderComSpec",
    "RPortComSpec",
    "ReceiverComSpec",
    "ReceptionComSpecProps",
    "SenderComSpec",
    "ServerComSpec",
    "TransformationComSpecProps",
    "TransmissionAcknowledgementRequest",
    "TransmissionComSpecProps",
    "TransmissionModeDefinitionEnum",
    "UserDefinedTransformationComSpecProps",
]
