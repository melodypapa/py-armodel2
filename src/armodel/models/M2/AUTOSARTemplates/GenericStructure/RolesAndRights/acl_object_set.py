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
    def serialize(self) -> ET.Element:
        """Serialize AclObjectSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AclObjectSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize acl_object_classe_refs (list to container "ACL-OBJECT-CLASSES")
        if self.acl_object_classe_refs:
            wrapper = ET.Element("ACL-OBJECT-CLASSES")
            for item in self.acl_object_classe_refs:
                serialized = ARObject._serialize_item(item, "ReferrableSubtypesEnum")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize acl_scope
        if self.acl_scope is not None:
            serialized = ARObject._serialize_item(self.acl_scope, "AclScopeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACL-SCOPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize collection_ref
        if self.collection_ref is not None:
            serialized = ARObject._serialize_item(self.collection_ref, "Collection")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COLLECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize derived_froms (list to container "DERIVED-FROMS")
        if self.derived_froms:
            wrapper = ET.Element("DERIVED-FROMS")
            for item in self.derived_froms:
                serialized = ARObject._serialize_item(item, "AtpBlueprint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize engineerings (list to container "ENGINEERINGS")
        if self.engineerings:
            wrapper = ET.Element("ENGINEERINGS")
            for item in self.engineerings:
                serialized = ARObject._serialize_item(item, "AutosarEngineeringObject")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AclObjectSet":
        """Deserialize XML element to AclObjectSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AclObjectSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AclObjectSet, cls).deserialize(element)

        # Parse acl_object_classe_refs (list from container "ACL-OBJECT-CLASSES")
        obj.acl_object_classe_refs = []
        container = ARObject._find_child_element(element, "ACL-OBJECT-CLASSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.acl_object_classe_refs.append(child_value)

        # Parse acl_scope
        child = ARObject._find_child_element(element, "ACL-SCOPE")
        if child is not None:
            acl_scope_value = AclScopeEnum.deserialize(child)
            obj.acl_scope = acl_scope_value

        # Parse collection_ref
        child = ARObject._find_child_element(element, "COLLECTION")
        if child is not None:
            collection_ref_value = ARObject._deserialize_by_tag(child, "Collection")
            obj.collection_ref = collection_ref_value

        # Parse derived_froms (list from container "DERIVED-FROMS")
        obj.derived_froms = []
        container = ARObject._find_child_element(element, "DERIVED-FROMS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.derived_froms.append(child_value)

        # Parse engineerings (list from container "ENGINEERINGS")
        obj.engineerings = []
        container = ARObject._find_child_element(element, "ENGINEERINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.engineerings.append(child_value)

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
