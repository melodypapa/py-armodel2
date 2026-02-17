"""AclObjectSet AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 383)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 158)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_RolesAndRights.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights import (
    AclScopeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ReferrableSubtypesEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.atp_blueprint import (
    AtpBlueprint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.autosar_engineering_object import (
    AutosarEngineeringObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection.collection import (
    Collection,
)


class AclObjectSet(ARElement):
    """AUTOSAR AclObjectSet."""

    def __init__(self) -> None:
        """Initialize AclObjectSet."""
        super().__init__()
        self.acl_object_classes: list[ReferrableSubtypesEnum] = []
        self.acl_scope: AclScopeEnum = None
        self.collection: Optional[Collection] = None
        self.derived_froms: list[AtpBlueprint] = []
        self.engineerings: list[AutosarEngineeringObject] = []


class AclObjectSetBuilder:
    """Builder for AclObjectSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AclObjectSet = AclObjectSet()

    def build(self) -> AclObjectSet:
        """Build and return AclObjectSet object.

        Returns:
            AclObjectSet instance
        """
        # TODO: Add validation
        return self._obj
