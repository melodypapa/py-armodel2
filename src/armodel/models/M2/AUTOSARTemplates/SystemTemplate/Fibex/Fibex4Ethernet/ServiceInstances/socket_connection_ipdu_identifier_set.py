"""SocketConnectionIpduIdentifierSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 490)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.so_con_i_pdu_identifier import (
    SoConIPduIdentifier,
)


class SocketConnectionIpduIdentifierSet(FibexElement):
    """AUTOSAR SocketConnectionIpduIdentifierSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    i_pdu_identifiers: list[SoConIPduIdentifier]
    def __init__(self) -> None:
        """Initialize SocketConnectionIpduIdentifierSet."""
        super().__init__()
        self.i_pdu_identifiers: list[SoConIPduIdentifier] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SocketConnectionIpduIdentifierSet":
        """Deserialize XML element to SocketConnectionIpduIdentifierSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SocketConnectionIpduIdentifierSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SocketConnectionIpduIdentifierSet, cls).deserialize(element)

        # Parse i_pdu_identifiers (list from container "I-PDU-IDENTIFIERS")
        obj.i_pdu_identifiers = []
        container = ARObject._find_child_element(element, "I-PDU-IDENTIFIERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.i_pdu_identifiers.append(child_value)

        return obj



class SocketConnectionIpduIdentifierSetBuilder:
    """Builder for SocketConnectionIpduIdentifierSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SocketConnectionIpduIdentifierSet = SocketConnectionIpduIdentifierSet()

    def build(self) -> SocketConnectionIpduIdentifierSet:
        """Build and return SocketConnectionIpduIdentifierSet object.

        Returns:
            SocketConnectionIpduIdentifierSet instance
        """
        # TODO: Add validation
        return self._obj
