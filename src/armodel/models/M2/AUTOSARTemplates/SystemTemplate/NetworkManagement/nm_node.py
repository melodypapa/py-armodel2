"""NmNode AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 675)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import (
    NmCoordinatorRoleEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_ecu import (
    NmEcu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.nm_pdu import (
    NmPdu,
)


class NmNode(Identifiable):
    """AUTOSAR NmNode."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "controller": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (Communication),
        ),  # controller
        "nm_coord_cluster": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmCoordCluster
        "nm_coordinator_role": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=NmCoordinatorRoleEnum,
        ),  # nmCoordinatorRole
        "nm_if_ecu": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=NmEcu,
        ),  # nmIfEcu
        "nm_node_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmNodeId
        "nm_passive": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmPassive
        "rx_nm_pdus": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=NmPdu,
        ),  # rxNmPdus
        "tx_nm_pdus": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=NmPdu,
        ),  # txNmPdus
    }

    def __init__(self) -> None:
        """Initialize NmNode."""
        super().__init__()
        self.controller: Optional[Any] = None
        self.nm_coord_cluster: Optional[PositiveInteger] = None
        self.nm_coordinator_role: Optional[NmCoordinatorRoleEnum] = None
        self.nm_if_ecu: Optional[NmEcu] = None
        self.nm_node_id: Optional[Integer] = None
        self.nm_passive: Optional[Boolean] = None
        self.rx_nm_pdus: list[NmPdu] = []
        self.tx_nm_pdus: list[NmPdu] = []


class NmNodeBuilder:
    """Builder for NmNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NmNode = NmNode()

    def build(self) -> NmNode:
        """Build and return NmNode object.

        Returns:
            NmNode instance
        """
        # TODO: Add validation
        return self._obj
