"""CAN module."""
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.CAN.global_time_can_master import (
    GlobalTimeCanMaster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.CAN.global_time_can_slave import (
    GlobalTimeCanSlave,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.CAN.can_global_time_domain_props import (
    CanGlobalTimeDomainProps,
)

__all__ = [
    "CanGlobalTimeDomainProps",
    "GlobalTimeCanMaster",
    "GlobalTimeCanSlave",
]
