"""TriggerPortAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 160)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class TriggerPortAnnotation(GeneralAnnotation):
    """AUTOSAR TriggerPortAnnotation."""

    def __init__(self) -> None:
        """Initialize TriggerPortAnnotation."""
        super().__init__()
        self.trigger: Optional[Trigger] = None


class TriggerPortAnnotationBuilder:
    """Builder for TriggerPortAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TriggerPortAnnotation = TriggerPortAnnotation()

    def build(self) -> TriggerPortAnnotation:
        """Build and return TriggerPortAnnotation object.

        Returns:
            TriggerPortAnnotation instance
        """
        # TODO: Add validation
        return self._obj
