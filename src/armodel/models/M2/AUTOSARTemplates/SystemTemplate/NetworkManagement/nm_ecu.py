"""NmEcu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 674)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.busspecific_nm_ecu import (
    BusspecificNmEcu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_coordinator import (
        NmCoordinator,
    )



class NmEcu(Identifiable):
    """AUTOSAR NmEcu."""

    def __init__(self) -> None:
        """Initialize NmEcu."""
        super().__init__()
        self.bus_dependent_nm_ecus: list[BusspecificNmEcu] = []
        self.ecu_instance: Optional[EcuInstance] = None
        self.nm_bus_synchronization: Optional[Any] = None
        self.nm_com_control_enabled: Optional[Boolean] = None
        self.nm_coordinator: Optional[NmCoordinator] = None
        self.nm_cycletime: Optional[TimeValue] = None
        self.nm_pdu_rx_indication: Optional[Any] = None
        self.nm_remote_sleep_ind: Optional[Any] = None
        self.nm_state_change: Optional[Boolean] = None
        self.nm_user_data_enabled: Optional[Boolean] = None


class NmEcuBuilder:
    """Builder for NmEcu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NmEcu = NmEcu()

    def build(self) -> NmEcu:
        """Build and return NmEcu object.

        Returns:
            NmEcu instance
        """
        # TODO: Add validation
        return self._obj
