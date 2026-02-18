"""ComponentClustering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 203)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.mapping_constraint import (
    MappingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import (
    MappingScopeEnum,
)


class ComponentClustering(MappingConstraint):
    """AUTOSAR ComponentClustering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    clustereds: list[Any]
    mapping_scope_enum: Optional[MappingScopeEnum]
    def __init__(self) -> None:
        """Initialize ComponentClustering."""
        super().__init__()
        self.clustereds: list[Any] = []
        self.mapping_scope_enum: Optional[MappingScopeEnum] = None


class ComponentClusteringBuilder:
    """Builder for ComponentClustering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ComponentClustering = ComponentClustering()

    def build(self) -> ComponentClustering:
        """Build and return ComponentClustering object.

        Returns:
            ComponentClustering instance
        """
        # TODO: Add validation
        return self._obj
