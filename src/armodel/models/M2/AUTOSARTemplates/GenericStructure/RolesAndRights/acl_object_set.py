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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    acl_object_classe_refs: list[ARRef]
    acl_scope: AclScopeEnum
    collection_ref: Optional[ARRef]
    derived_froms: list[AtpBlueprint]
    engineerings: list[AutosarEngineeringObject]
    def __init__(self) -> None:
        """Initialize AclObjectSet."""
        super().__init__()
        self.acl_object_classe_refs: list[ARRef] = []
        self.acl_scope: AclScopeEnum = None
        self.collection_ref: Optional[ARRef] = None
        self.derived_froms: list[AtpBlueprint] = []
        self.engineerings: list[AutosarEngineeringObject] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AclObjectSet":
        """Deserialize XML element to AclObjectSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AclObjectSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse acl_object_classe_refs (list)
        obj.acl_object_classe_refs = []
        for child in ARObject._find_all_child_elements(element, "ACL-OBJECT-CLASSES"):
            acl_object_classe_refs_value = child.text
            obj.acl_object_classe_refs.append(acl_object_classe_refs_value)

        # Parse acl_scope
        child = ARObject._find_child_element(element, "ACL-SCOPE")
        if child is not None:
            acl_scope_value = child.text
            obj.acl_scope = acl_scope_value

        # Parse collection_ref
        child = ARObject._find_child_element(element, "COLLECTION")
        if child is not None:
            collection_ref_value = ARObject._deserialize_by_tag(child, "Collection")
            obj.collection_ref = collection_ref_value

        # Parse derived_froms (list)
        obj.derived_froms = []
        for child in ARObject._find_all_child_elements(element, "DERIVED-FROMS"):
            derived_froms_value = ARObject._deserialize_by_tag(child, "AtpBlueprint")
            obj.derived_froms.append(derived_froms_value)

        # Parse engineerings (list)
        obj.engineerings = []
        for child in ARObject._find_all_child_elements(element, "ENGINEERINGS"):
            engineerings_value = ARObject._deserialize_by_tag(child, "AutosarEngineeringObject")
            obj.engineerings.append(engineerings_value)

        return obj



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
