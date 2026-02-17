"""CompuScaleContents AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 388)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class CompuScaleContents(ARObject):
    """AUTOSAR CompuScaleContents."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize CompuScaleContents."""
        super().__init__()


class CompuScaleContentsBuilder:
    """Builder for CompuScaleContents."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuScaleContents = CompuScaleContents()

    def build(self) -> CompuScaleContents:
        """Build and return CompuScaleContents object.

        Returns:
            CompuScaleContents instance
        """
        # TODO: Add validation
        return self._obj
