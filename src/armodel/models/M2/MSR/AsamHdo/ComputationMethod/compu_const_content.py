"""CompuConstContent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 390)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class CompuConstContent(ARObject, ABC):
    """AUTOSAR CompuConstContent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize CompuConstContent."""
        super().__init__()


class CompuConstContentBuilder:
    """Builder for CompuConstContent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuConstContent = CompuConstContent()

    def build(self) -> CompuConstContent:
        """Build and return CompuConstContent object.

        Returns:
            CompuConstContent instance
        """
        # TODO: Add validation
        return self._obj
