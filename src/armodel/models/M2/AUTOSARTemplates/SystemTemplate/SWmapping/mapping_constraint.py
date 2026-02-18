"""MappingConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 202)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from abc import ABC, abstractmethod


class MappingConstraint(ARObject, ABC):
    """AUTOSAR MappingConstraint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    introduction: Optional[DocumentationBlock]
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
