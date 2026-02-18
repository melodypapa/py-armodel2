"""BlueprintMappingSet AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 48)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 34)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_BlueprintMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.atp_blueprint_mapping import (
    AtpBlueprintMapping,
)


class BlueprintMappingSet(ARElement):
    """AUTOSAR BlueprintMappingSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    blueprint_map_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize BlueprintMappingSet."""
        super().__init__()
        self.blueprint_map_refs: list[ARRef] = []


class BlueprintMappingSetBuilder:
    """Builder for BlueprintMappingSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BlueprintMappingSet = BlueprintMappingSet()

    def build(self) -> BlueprintMappingSet:
        """Build and return BlueprintMappingSet object.

        Returns:
            BlueprintMappingSet instance
        """
        # TODO: Add validation
        return self._obj
