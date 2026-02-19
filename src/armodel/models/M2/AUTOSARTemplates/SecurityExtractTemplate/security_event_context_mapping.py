"""SecurityEventContextMapping AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 32)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_mapping import (
    IdsMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.idsm_instance import (
    IdsmInstance,
)
from abc import ABC, abstractmethod


class SecurityEventContextMapping(IdsMapping, ABC):
    """AUTOSAR SecurityEventContextMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    filter_chain: Optional[Any]
    idsm_instance: Optional[IdsmInstance]
    mapped_securities: list[Any]
    def __init__(self) -> None:
        """Initialize SecurityEventContextMapping."""
        super().__init__()
        self.filter_chain: Optional[Any] = None
        self.idsm_instance: Optional[IdsmInstance] = None
        self.mapped_securities: list[Any] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecurityEventContextMapping":
        """Deserialize XML element to SecurityEventContextMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecurityEventContextMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecurityEventContextMapping, cls).deserialize(element)

        # Parse filter_chain
        child = ARObject._find_child_element(element, "FILTER-CHAIN")
        if child is not None:
            filter_chain_value = child.text
            obj.filter_chain = filter_chain_value

        # Parse idsm_instance
        child = ARObject._find_child_element(element, "IDSM-INSTANCE")
        if child is not None:
            idsm_instance_value = ARObject._deserialize_by_tag(child, "IdsmInstance")
            obj.idsm_instance = idsm_instance_value

        # Parse mapped_securities (list from container "MAPPED-SECURITIES")
        obj.mapped_securities = []
        container = ARObject._find_child_element(element, "MAPPED-SECURITIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mapped_securities.append(child_value)

        return obj



class SecurityEventContextMappingBuilder:
    """Builder for SecurityEventContextMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventContextMapping = SecurityEventContextMapping()

    def build(self) -> SecurityEventContextMapping:
        """Build and return SecurityEventContextMapping object.

        Returns:
            SecurityEventContextMapping instance
        """
        # TODO: Add validation
        return self._obj
