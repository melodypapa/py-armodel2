"""SecurityEventStateFilter AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 22)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.abstract_security_event_filter import (
    AbstractSecurityEventFilter,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.block_state import (
    BlockState,
)


class SecurityEventStateFilter(AbstractSecurityEventFilter):
    """AUTOSAR SecurityEventStateFilter."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    block_if_states: list[BlockState]
    def __init__(self) -> None:
        """Initialize SecurityEventStateFilter."""
        super().__init__()
        self.block_if_states: list[BlockState] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecurityEventStateFilter":
        """Deserialize XML element to SecurityEventStateFilter object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecurityEventStateFilter object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecurityEventStateFilter, cls).deserialize(element)

        # Parse block_if_states (list from container "BLOCK-IF-STATES")
        obj.block_if_states = []
        container = ARObject._find_child_element(element, "BLOCK-IF-STATES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.block_if_states.append(child_value)

        return obj



class SecurityEventStateFilterBuilder:
    """Builder for SecurityEventStateFilter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventStateFilter = SecurityEventStateFilter()

    def build(self) -> SecurityEventStateFilter:
        """Build and return SecurityEventStateFilter object.

        Returns:
            SecurityEventStateFilter instance
        """
        # TODO: Add validation
        return self._obj
