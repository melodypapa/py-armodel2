"""GlobalTimeDomain AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 858)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 225)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.abstract_global_time_domain_props import (
    AbstractGlobalTimeDomainProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_gateway import (
    GlobalTimeGateway,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_master import (
    GlobalTimeMaster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_slave import (
    GlobalTimeSlave,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.network_segment_identification import (
    NetworkSegmentIdentification,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class GlobalTimeDomain(FibexElement):
    """AUTOSAR GlobalTimeDomain."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    debounce_time: Optional[TimeValue]
    domain_id: Optional[PositiveInteger]
    gateways: list[GlobalTimeGateway]
    global_time: Optional[AbstractGlobalTimeDomainProps]
    global_time_master: Optional[GlobalTimeMaster]
    global_time_subs: list[GlobalTimeDomain]
    network: Optional[NetworkSegmentIdentification]
    offset_time: Optional[GlobalTimeDomain]
    pdu_triggering_ref: Optional[ARRef]
    slaves: list[GlobalTimeSlave]
    sync_loss: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize GlobalTimeDomain."""
        super().__init__()
        self.debounce_time: Optional[TimeValue] = None
        self.domain_id: Optional[PositiveInteger] = None
        self.gateways: list[GlobalTimeGateway] = []
        self.global_time: Optional[AbstractGlobalTimeDomainProps] = None
        self.global_time_master: Optional[GlobalTimeMaster] = None
        self.global_time_subs: list[GlobalTimeDomain] = []
        self.network: Optional[NetworkSegmentIdentification] = None
        self.offset_time: Optional[GlobalTimeDomain] = None
        self.pdu_triggering_ref: Optional[ARRef] = None
        self.slaves: list[GlobalTimeSlave] = []
        self.sync_loss: Optional[TimeValue] = None


class GlobalTimeDomainBuilder:
    """Builder for GlobalTimeDomain."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeDomain = GlobalTimeDomain()

    def build(self) -> GlobalTimeDomain:
        """Build and return GlobalTimeDomain object.

        Returns:
            GlobalTimeDomain instance
        """
        # TODO: Add validation
        return self._obj
