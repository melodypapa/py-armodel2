"""AtpInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 301)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 971)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2000)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 206)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 174)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_AbstractStructure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_classifier import (
    AtpClassifier,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_prototype import (
    AtpPrototype,
)


class AtpInstanceRef(ARObject):
    """AUTOSAR AtpInstanceRef."""
    """Abstract base class - do not instantiate directly."""

    atp_base: AtpClassifier
    atp_contexts: list[AtpPrototype]
    atp_target: AtpFeature
    def __init__(self) -> None:
        """Initialize AtpInstanceRef."""
        super().__init__()
        self.atp_base: AtpClassifier = None
        self.atp_contexts: list[AtpPrototype] = []
        self.atp_target: AtpFeature = None


class AtpInstanceRefBuilder:
    """Builder for AtpInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AtpInstanceRef = AtpInstanceRef()

    def build(self) -> AtpInstanceRef:
        """Build and return AtpInstanceRef object.

        Returns:
            AtpInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
