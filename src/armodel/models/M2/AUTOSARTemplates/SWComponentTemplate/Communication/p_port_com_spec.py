"""PPortComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 166)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 199)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class PPortComSpec(ARObject):
    """AUTOSAR PPortComSpec."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize PPortComSpec."""
        super().__init__()


class PPortComSpecBuilder:
    """Builder for PPortComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PPortComSpec = PPortComSpec()

    def build(self) -> PPortComSpec:
        """Build and return PPortComSpec object.

        Returns:
            PPortComSpec instance
        """
        # TODO: Add validation
        return self._obj
