"""CommunicationConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 54)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 57)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    PncGatewayTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.comm_connector_port import (
    CommConnectorPort,
)
from abc import ABC, abstractmethod


class CommunicationConnector(Identifiable, ABC):
    """AUTOSAR CommunicationConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    comm_controller: Optional[Any]
    create_ecu: Optional[Boolean]
    dynamic_pnc_to: Optional[Boolean]
    ecu_comm_ports: list[CommConnectorPort]
    pnc_filter_arrays: list[PositiveInteger]
    pnc_gateway_type_enum: Optional[PncGatewayTypeEnum]
    def __init__(self) -> None:
        """Initialize CommunicationConnector."""
        super().__init__()
        self.comm_controller: Optional[Any] = None
        self.create_ecu: Optional[Boolean] = None
        self.dynamic_pnc_to: Optional[Boolean] = None
        self.ecu_comm_ports: list[CommConnectorPort] = []
        self.pnc_filter_arrays: list[PositiveInteger] = []
        self.pnc_gateway_type_enum: Optional[PncGatewayTypeEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CommunicationConnector":
        """Deserialize XML element to CommunicationConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CommunicationConnector object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse comm_controller
        child = ARObject._find_child_element(element, "COMM-CONTROLLER")
        if child is not None:
            comm_controller_value = child.text
            obj.comm_controller = comm_controller_value

        # Parse create_ecu
        child = ARObject._find_child_element(element, "CREATE-ECU")
        if child is not None:
            create_ecu_value = child.text
            obj.create_ecu = create_ecu_value

        # Parse dynamic_pnc_to
        child = ARObject._find_child_element(element, "DYNAMIC-PNC-TO")
        if child is not None:
            dynamic_pnc_to_value = child.text
            obj.dynamic_pnc_to = dynamic_pnc_to_value

        # Parse ecu_comm_ports (list)
        obj.ecu_comm_ports = []
        for child in ARObject._find_all_child_elements(element, "ECU-COMM-PORTS"):
            ecu_comm_ports_value = ARObject._deserialize_by_tag(child, "CommConnectorPort")
            obj.ecu_comm_ports.append(ecu_comm_ports_value)

        # Parse pnc_filter_arrays (list)
        obj.pnc_filter_arrays = []
        for child in ARObject._find_all_child_elements(element, "PNC-FILTER-ARRAYS"):
            pnc_filter_arrays_value = child.text
            obj.pnc_filter_arrays.append(pnc_filter_arrays_value)

        # Parse pnc_gateway_type_enum
        child = ARObject._find_child_element(element, "PNC-GATEWAY-TYPE-ENUM")
        if child is not None:
            pnc_gateway_type_enum_value = child.text
            obj.pnc_gateway_type_enum = pnc_gateway_type_enum_value

        return obj



class CommunicationConnectorBuilder:
    """Builder for CommunicationConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CommunicationConnector = CommunicationConnector()

    def build(self) -> CommunicationConnector:
        """Build and return CommunicationConnector object.

        Returns:
            CommunicationConnector instance
        """
        # TODO: Add validation
        return self._obj
