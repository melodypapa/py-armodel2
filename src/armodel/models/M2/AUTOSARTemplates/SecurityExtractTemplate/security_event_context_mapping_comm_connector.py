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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecurityEventContextMappingCommConnector, cls).deserialize(element)

        # Parse comm_connectors (list from container "COMM-CONNECTORS")
        obj.comm_connectors = []
        container = ARObject._find_child_element(element, "COMM-CONNECTORS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.comm_connectors.append(child_value)

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
