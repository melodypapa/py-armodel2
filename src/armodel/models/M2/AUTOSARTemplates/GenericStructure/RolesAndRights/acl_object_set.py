"""AclObjectSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("acl_object_classes", None, False, True, None),  # aclObjectClasses
        ("acl_scope", None, False, False, AclScopeEnum),  # aclScope
        ("collection", None, False, False, Collection),  # collection
        ("derived_froms", None, False, True, AtpBlueprint),  # derivedFroms
        ("engineerings", None, False, True, AutosarEngineeringObject),  # engineerings
    ]

    def __init__(self) -> None:
        """Initialize AclObjectSet."""
        super().__init__()
        self.acl_object_classes: list[ReferrableSubtypesEnum] = []
        self.acl_scope: AclScopeEnum = None
        self.collection: Optional[Collection] = None
        self.derived_froms: list[AtpBlueprint] = []
        self.engineerings: list[AutosarEngineeringObject] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AclObjectSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AclObjectSet":
        """Create AclObjectSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AclObjectSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AclObjectSet since parent returns ARObject
        return cast("AclObjectSet", obj)


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
