"""DelegatedPortAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 162)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import (
    SignalFanEnum,
)


class DelegatedPortAnnotation(GeneralAnnotation):
    """AUTOSAR DelegatedPortAnnotation."""

    signal_fan: Optional[SignalFanEnum]
    def __init__(self) -> None:
        """Initialize DelegatedPortAnnotation."""
        super().__init__()
        self.signal_fan: Optional[SignalFanEnum] = None


class DelegatedPortAnnotationBuilder:
    """Builder for DelegatedPortAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DelegatedPortAnnotation = DelegatedPortAnnotation()

    def build(self) -> DelegatedPortAnnotation:
        """Build and return DelegatedPortAnnotation object.

        Returns:
            DelegatedPortAnnotation instance
        """
        # TODO: Add validation
        return self._obj
