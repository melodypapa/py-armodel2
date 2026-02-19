"""SecurityEventContextMappingCommConnector AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 40)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_context_mapping import (
    SecurityEventContextMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)


class SecurityEventContextMappingCommConnector(SecurityEventContextMapping):
    """AUTOSAR SecurityEventContextMappingCommConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    comm_connectors: list[CommunicationConnector]
    def __init__(self) -> None:
        """Initialize SecurityEventContextMappingCommConnector."""
        super().__init__()
        self.comm_connectors: list[CommunicationConnector] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecurityEventContextMappingCommConnector":
        """Deserialize XML element to SecurityEventContextMappingCommConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecurityEventContextMappingCommConnector object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse comm_connectors (list)
        obj.comm_connectors = []
        for child in ARObject._find_all_child_elements(element, "COMM-CONNECTORS"):
            comm_connectors_value = ARObject._deserialize_by_tag(child, "CommunicationConnector")
            obj.comm_connectors.append(comm_connectors_value)

        return obj



class SecurityEventContextMappingCommConnectorBuilder:
    """Builder for SecurityEventContextMappingCommConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventContextMappingCommConnector = SecurityEventContextMappingCommConnector()

    def build(self) -> SecurityEventContextMappingCommConnector:
        """Build and return SecurityEventContextMappingCommConnector object.

        Returns:
            SecurityEventContextMappingCommConnector instance
        """
        # TODO: Add validation
        return self._obj
