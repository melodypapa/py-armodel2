"""ApplicationAttributes module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.sender_receiver_annotation import (
        SenderReceiverAnnotation,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.sender_annotation import (
        SenderAnnotation,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.receiver_annotation import (
        ReceiverAnnotation,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.client_server_annotation import (
        ClientServerAnnotation,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.io_hw_abstraction_server_annotation import (
        IoHwAbstractionServerAnnotation,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.parameter_port_annotation import (
        ParameterPortAnnotation,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.mode_port_annotation import (
        ModePortAnnotation,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.trigger_port_annotation import (
        TriggerPortAnnotation,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.nv_data_port_annotation import (
        NvDataPortAnnotation,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.delegated_port_annotation import (
        DelegatedPortAnnotation,
    )

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.processing_kind_enum import (
    ProcessingKindEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.data_limit_kind_enum import (
    DataLimitKindEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.filter_debouncing_enum import (
    FilterDebouncingEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.pulse_test_enum import (
    PulseTestEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.signal_fan_enum import (
    SignalFanEnum,
)

__all__ = [
    "ClientServerAnnotation",
    "DataLimitKindEnum",
    "DelegatedPortAnnotation",
    "FilterDebouncingEnum",
    "IoHwAbstractionServerAnnotation",
    "ModePortAnnotation",
    "NvDataPortAnnotation",
    "ParameterPortAnnotation",
    "ProcessingKindEnum",
    "PulseTestEnum",
    "ReceiverAnnotation",
    "SenderAnnotation",
    "SenderReceiverAnnotation",
    "SignalFanEnum",
    "TriggerPortAnnotation",
]
