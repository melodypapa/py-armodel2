"""PduActivationRoutingGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 488)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    EventGroupControlTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.so_con_i_pdu_identifier import (
    SoConIPduIdentifier,
)


class PduActivationRoutingGroup(Identifiable):
    """AUTOSAR PduActivationRoutingGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    event_group_ref: Optional[ARRef]
    i_pdu_identifiers: list[SoConIPduIdentifier]
    def __init__(self) -> None:
        """Initialize PduActivationRoutingGroup."""
        super().__init__()
        self.event_group_ref: Optional[ARRef] = None
        self.i_pdu_identifiers: list[SoConIPduIdentifier] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "PduActivationRoutingGroup":
        """Deserialize XML element to PduActivationRoutingGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PduActivationRoutingGroup object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse event_group_ref
        child = ARObject._find_child_element(element, "EVENT-GROUP")
        if child is not None:
            event_group_ref_value = child.text
            obj.event_group_ref = event_group_ref_value

        # Parse i_pdu_identifiers (list)
        obj.i_pdu_identifiers = []
        for child in ARObject._find_all_child_elements(element, "I-PDU-IDENTIFIERS"):
            i_pdu_identifiers_value = ARObject._deserialize_by_tag(child, "SoConIPduIdentifier")
            obj.i_pdu_identifiers.append(i_pdu_identifiers_value)

        return obj



class PduActivationRoutingGroupBuilder:
    """Builder for PduActivationRoutingGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PduActivationRoutingGroup = PduActivationRoutingGroup()

    def build(self) -> PduActivationRoutingGroup:
        """Build and return PduActivationRoutingGroup object.

        Returns:
            PduActivationRoutingGroup instance
        """
        # TODO: Add validation
        return self._obj
