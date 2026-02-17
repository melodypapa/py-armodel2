"""DocumentationContext AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 327)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_DocumentationOnM1.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.multilanguage_referrable import (
    MultilanguageReferrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class DocumentationContext(MultilanguageReferrable):
    """AUTOSAR DocumentationContext."""

    feature: Optional[AtpFeature]
    identifiable: Optional[Identifiable]
    def __init__(self) -> None:
        """Initialize DocumentationContext."""
        super().__init__()
        self.feature: Optional[AtpFeature] = None
        self.identifiable: Optional[Identifiable] = None


class DocumentationContextBuilder:
    """Builder for DocumentationContext."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DocumentationContext = DocumentationContext()

    def build(self) -> DocumentationContext:
        """Build and return DocumentationContext object.

        Returns:
            DocumentationContext instance
        """
        # TODO: Add validation
        return self._obj
