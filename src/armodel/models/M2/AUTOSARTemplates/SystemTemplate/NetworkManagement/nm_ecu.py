"""NmEcu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 674)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_coordinator import (
    NmCoordinator,
)


class NmEcu(Identifiable):
    """AUTOSAR NmEcu."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "bus_dependent_nm_ecus": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BusspecificNmEcu,
        ),  # busDependentNmEcus
        "ecu_instance": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EcuInstance,
        ),  # ecuInstance
        "nm_bus_synchronization": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (BooleanEnabled),
        ),  # nmBusSynchronization
        "nm_com_control_enabled": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmComControlEnabled
        "nm_coordinator": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=NmCoordinator,
        ),  # nmCoordinator
        "nm_cycletime": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmCycletime
        "nm_pdu_rx_indication": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (BooleanEnabled),
        ),  # nmPduRxIndication
        "nm_remote_sleep_ind": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (BooleanEnabled),
        ),  # nmRemoteSleepInd
        "nm_state_change": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmStateChange
        "nm_user_data_enabled": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmUserDataEnabled
    }

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
