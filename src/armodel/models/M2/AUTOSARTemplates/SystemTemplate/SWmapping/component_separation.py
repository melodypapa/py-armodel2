"""ComponentSeparation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 205)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.mapping_constraint import (
    MappingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import (
    MappingScopeEnum,
)


class ComponentSeparation(MappingConstraint):
    """AUTOSAR ComponentSeparation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mapping_scope_enum: Optional[MappingScopeEnum]
    def __init__(self) -> None:
        """Initialize ComponentSeparation."""
        super().__init__()
        self.mapping_scope_enum: Optional[MappingScopeEnum] = None


class ComponentSeparationBuilder:
    """Builder for ComponentSeparation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ComponentSeparation = ComponentSeparation()

    def build(self) -> ComponentSeparation:
        """Build and return ComponentSeparation object.

        Returns:
            ComponentSeparation instance
        """
        # TODO: Add validation
        return self._obj
