"""ContainerIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 353)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ContainerIPduHeaderTypeEnum,
    ContainerIPduTriggerEnum,
    RxAcceptContainedIPduEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.contained_i_pdu_props import (
    ContainedIPduProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class ContainerIPdu(IPdu):
    """AUTOSAR ContainerIPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    contained_i_pdu_propses: list[ContainedIPduProps]
    contained_pdus: list[PduTriggering]
    container: Optional[TimeValue]
    container_trigger: Optional[ContainerIPduTriggerEnum]
    header_type: Optional[ContainerIPduHeaderTypeEnum]
    minimum_rx: Optional[PositiveInteger]
    minimum_tx: Optional[PositiveInteger]
    rx_accept: Optional[RxAcceptContainedIPduEnum]
    threshold_size: Optional[PositiveInteger]
    unused_bit: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize ContainerIPdu."""
        super().__init__()
        self.contained_i_pdu_propses: list[ContainedIPduProps] = []
        self.contained_pdus: list[PduTriggering] = []
        self.container: Optional[TimeValue] = None
        self.container_trigger: Optional[ContainerIPduTriggerEnum] = None
        self.header_type: Optional[ContainerIPduHeaderTypeEnum] = None
        self.minimum_rx: Optional[PositiveInteger] = None
        self.minimum_tx: Optional[PositiveInteger] = None
        self.rx_accept: Optional[RxAcceptContainedIPduEnum] = None
        self.threshold_size: Optional[PositiveInteger] = None
        self.unused_bit: Optional[PositiveInteger] = None


class ContainerIPduBuilder:
    """Builder for ContainerIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ContainerIPdu = ContainerIPdu()

    def build(self) -> ContainerIPdu:
        """Build and return ContainerIPdu object.

        Returns:
            ContainerIPdu instance
        """
        # TODO: Add validation
        return self._obj
