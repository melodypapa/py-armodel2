"""Communication module."""
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
    PPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.receiver_com_spec import (
    ReceiverComSpec,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.nonqueued_receiver_com_spec import (
    NonqueuedReceiverComSpec,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.queued_receiver_com_spec import (
    QueuedReceiverComSpec,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.reception_com_spec_props import (
    ReceptionComSpecProps,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.sender_com_spec import (
    SenderComSpec,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.queued_sender_com_spec import (
    QueuedSenderComSpec,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.nonqueued_sender_com_spec import (
    NonqueuedSenderComSpec,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.transmission_com_spec_props import (
    TransmissionComSpecProps,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.transmission_acknowledgement_request import (
    TransmissionAcknowledgementRequest,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.composite_network_representation import (
    CompositeNetworkRepresentation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.client_com_spec import (
    ClientComSpec,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.server_com_spec import (
    ServerComSpec,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.mode_switch_sender_com_spec import (
    ModeSwitchSenderComSpec,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.mode_switched_ack_request import (
    ModeSwitchedAckRequest,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.mode_switch_receiver_com_spec import (
    ModeSwitchReceiverComSpec,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.parameter_provide_com_spec import (
    ParameterProvideComSpec,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.parameter_require_com_spec import (
    ParameterRequireComSpec,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.nv_require_com_spec import (
    NvRequireComSpec,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.nv_provide_com_spec import (
    NvProvideComSpec,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.transformation_com_spec_props import (
    TransformationComSpecProps,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.user_defined_transformation_com_spec_props import (
    UserDefinedTransformationComSpecProps,
)

__all__ = [
    "ClientComSpec",
    "CompositeNetworkRepresentation",
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
    "UserDefinedTransformationComSpecProps",
]
