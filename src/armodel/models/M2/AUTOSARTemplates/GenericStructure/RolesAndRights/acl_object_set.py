"""AclObjectSet AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 383)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 158)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_RolesAndRights.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "acl_object_classes": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
        ),  # aclObjectClasses
        "acl_scope": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=AclScopeEnum,
        ),  # aclScope
        "collection": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Collection,
        ),  # collection
        "derived_froms": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=AtpBlueprint,
        ),  # derivedFroms
        "engineerings": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=AutosarEngineeringObject,
        ),  # engineerings
    }

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
