"""WhitespaceControlled AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 292)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_LanguageDataModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class WhitespaceControlled(ARObject, ABC):
    """AUTOSAR WhitespaceControlled."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    xml_space: Any
    def __init__(self) -> None:
        """Initialize WhitespaceControlled."""
        super().__init__()
        self.xml_space: Any = None


class WhitespaceControlledBuilder:
    """Builder for WhitespaceControlled."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: WhitespaceControlled = WhitespaceControlled()

    def build(self) -> WhitespaceControlled:
        """Build and return WhitespaceControlled object.

        Returns:
            WhitespaceControlled instance
        """
        # TODO: Add validation
        return self._obj
