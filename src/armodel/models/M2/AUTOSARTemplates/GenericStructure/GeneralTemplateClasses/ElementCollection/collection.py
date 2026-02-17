"""Collection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2009)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 398)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 175)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ElementCollection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import (
    AutoCollectEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    NameToken,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class Collection(ARElement):
    """AUTOSAR Collection."""

    auto_collect_enum: Optional[AutoCollectEnum]
    collecteds: list[AtpFeature]
    collection: Optional[NameToken]
    elements: list[Identifiable]
    element_role: Optional[Identifier]
    source_elements: list[Identifiable]
    source_instances: list[AtpFeature]
    def __init__(self) -> None:
        """Initialize Collection."""
        super().__init__()
        self.auto_collect_enum: Optional[AutoCollectEnum] = None
        self.collecteds: list[AtpFeature] = []
        self.collection: Optional[NameToken] = None
        self.elements: list[Identifiable] = []
        self.element_role: Optional[Identifier] = None
        self.source_elements: list[Identifiable] = []
        self.source_instances: list[AtpFeature] = []


class CollectionBuilder:
    """Builder for Collection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Collection = Collection()

    def build(self) -> Collection:
        """Build and return Collection object.

        Returns:
            Collection instance
        """
        # TODO: Add validation
        return self._obj
