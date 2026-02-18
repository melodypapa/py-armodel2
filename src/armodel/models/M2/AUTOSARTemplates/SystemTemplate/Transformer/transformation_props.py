"""TransformationProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 782)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from abc import ABC, abstractmethod


class TransformationProps(Identifiable, ABC):
    """AUTOSAR TransformationProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize TransformationProps."""
        super().__init__()


class TransformationPropsBuilder:
    """Builder for TransformationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransformationProps = TransformationProps()

    def build(self) -> TransformationProps:
        """Build and return TransformationProps object.

        Returns:
            TransformationProps instance
        """
        # TODO: Add validation
        return self._obj
