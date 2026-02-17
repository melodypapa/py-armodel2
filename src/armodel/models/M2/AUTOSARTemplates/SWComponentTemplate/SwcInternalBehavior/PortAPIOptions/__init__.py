"""PortAPIOptions module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.port_defined_argument_value import (
        PortDefinedArgumentValue,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.port_api_option import (
        PortAPIOption,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.swc_supported_feature import (
        SwcSupportedFeature,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.communication_buffer_locking import (
        CommunicationBufferLocking,
    )

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.data_transformation_error_handling_enum import (
    DataTransformationErrorHandlingEnum,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.data_transformation_status_forwarding_enum import (
    DataTransformationStatusForwardingEnum,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.support_buffer_locking_enum import (
    SupportBufferLockingEnum,
)

__all__ = [
    "CommunicationBufferLocking",
    "DataTransformationErrorHandlingEnum",
    "DataTransformationStatusForwardingEnum",
    "PortAPIOption",
    "PortDefinedArgumentValue",
    "SupportBufferLockingEnum",
    "SwcSupportedFeature",
]
