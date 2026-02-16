"""ComponentSeparation AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.mapping_constraint import (
    MappingConstraint,
)


class ComponentSeparation(MappingConstraint):
    """AUTOSAR ComponentSeparation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "mapping_scope_enum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MappingScopeEnum,
        ),  # mappingScopeEnum
    }

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
