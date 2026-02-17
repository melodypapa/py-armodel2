"""MappingConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 202)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)


class MappingConstraint(ARObject):
    """AUTOSAR MappingConstraint."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "introduction": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DocumentationBlock,
        ),  # introduction
    }

    def __init__(self) -> None:
        """Initialize MappingConstraint."""
        super().__init__()
        self.introduction: Optional[DocumentationBlock] = None


class MappingConstraintBuilder:
    """Builder for MappingConstraint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MappingConstraint = MappingConstraint()

    def build(self) -> MappingConstraint:
        """Build and return MappingConstraint object.

        Returns:
            MappingConstraint instance
        """
        # TODO: Add validation
        return self._obj
