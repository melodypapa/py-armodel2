"""SignalPathConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2057)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SignalPaths.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from abc import ABC, abstractmethod


class SignalPathConstraint(ARObject, ABC):
    """AUTOSAR SignalPathConstraint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    introduction: DocumentationBlock
    def __init__(self) -> None:
        """Initialize SignalPathConstraint."""
        super().__init__()
        self.introduction: DocumentationBlock = None


class SignalPathConstraintBuilder:
    """Builder for SignalPathConstraint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SignalPathConstraint = SignalPathConstraint()

    def build(self) -> SignalPathConstraint:
        """Build and return SignalPathConstraint object.

        Returns:
            SignalPathConstraint instance
        """
        # TODO: Add validation
        return self._obj
