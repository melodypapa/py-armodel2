"""GlobalTime module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_domain import (
        GlobalTimeDomain,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.abstract_global_time_domain_props import (
        AbstractGlobalTimeDomainProps,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.network_segment_identification import (
        NetworkSegmentIdentification,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_master import (
        GlobalTimeMaster,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_slave import (
        GlobalTimeSlave,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_gateway import (
        GlobalTimeGateway,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_correction_props import (
        GlobalTimeCorrectionProps,
    )

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_crc_support_enum import (
    GlobalTimeCrcSupportEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_crc_validation_enum import (
    GlobalTimeCrcValidationEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_icv_support_enum import (
    GlobalTimeIcvSupportEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_icv_verification_enum import (
    GlobalTimeIcvVerificationEnum,
)

__all__ = [
    "AbstractGlobalTimeDomainProps",
    "GlobalTimeCorrectionProps",
    "GlobalTimeCrcSupportEnum",
    "GlobalTimeCrcValidationEnum",
    "GlobalTimeDomain",
    "GlobalTimeGateway",
    "GlobalTimeIcvSupportEnum",
    "GlobalTimeIcvVerificationEnum",
    "GlobalTimeMaster",
    "GlobalTimeSlave",
    "NetworkSegmentIdentification",
]
