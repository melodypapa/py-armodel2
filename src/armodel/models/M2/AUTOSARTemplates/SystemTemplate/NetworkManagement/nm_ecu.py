"""NmEcu AUTOSAR element."""

from typing import Optional, cast
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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_coordinator import (
    NmCoordinator,
)


class NmEcu(Identifiable):
    """AUTOSAR NmEcu."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("bus_dependent_nm_ecus", None, False, True, BusspecificNmEcu),  # busDependentNmEcus
        ("ecu_instance", None, False, False, EcuInstance),  # ecuInstance
        ("nm_bus_synchronization", None, False, False, any (BooleanEnabled)),  # nmBusSynchronization
        ("nm_com_control_enabled", None, True, False, None),  # nmComControlEnabled
        ("nm_coordinator", None, False, False, NmCoordinator),  # nmCoordinator
        ("nm_cycletime", None, True, False, None),  # nmCycletime
        ("nm_pdu_rx_indication", None, False, False, any (BooleanEnabled)),  # nmPduRxIndication
        ("nm_remote_sleep_ind", None, False, False, any (BooleanEnabled)),  # nmRemoteSleepInd
        ("nm_state_change", None, True, False, None),  # nmStateChange
        ("nm_user_data_enabled", None, True, False, None),  # nmUserDataEnabled
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert NmEcu to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NmEcu":
        """Create NmEcu from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            NmEcu instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to NmEcu since parent returns ARObject
        return cast("NmEcu", obj)


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
