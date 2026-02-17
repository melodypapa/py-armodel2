"""GlobalTime module."""
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

__all__ = [
    "AbstractGlobalTimeDomainProps",
    "GlobalTimeCorrectionProps",
    "GlobalTimeDomain",
    "GlobalTimeGateway",
    "GlobalTimeMaster",
    "GlobalTimeSlave",
    "NetworkSegmentIdentification",
]
