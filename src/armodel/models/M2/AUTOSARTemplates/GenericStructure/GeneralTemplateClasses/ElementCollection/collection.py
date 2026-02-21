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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import (
    AutoCollectEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    NameToken,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef.any_instance_ref import (
    AnyInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class Collection(ARElement):
    """AUTOSAR Collection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    auto_collect: Optional[AutoCollectEnum]
    collected_instance_irefs: list[AnyInstanceRef]
    collection_semantics: Optional[NameToken]
    element_role: Optional[Identifier]
    element_refs: list[ARRef]
    source_element_refs: list[ARRef]
    source_instance_irefs: list[AnyInstanceRef]
    def __init__(self) -> None:
        """Initialize Collection."""
        super().__init__()
        self.auto_collect: Optional[AutoCollectEnum] = None
        self.collected_instance_irefs: list[AnyInstanceRef] = []
        self.collection_semantics: Optional[NameToken] = None
        self.element_role: Optional[Identifier] = None
        self.element_refs: list[ARRef] = []
        self.source_element_refs: list[ARRef] = []
        self.source_instance_irefs: list[AnyInstanceRef] = []

    def serialize(self) -> ET.Element:
        """Serialize Collection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Collection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize auto_collect
        if self.auto_collect is not None:
            serialized = ARObject._serialize_item(self.auto_collect, "AutoCollectEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AUTO-COLLECT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

            serialized = ARObject._serialize_item(self.collected_instance_irefs, "AnyInstanceRef")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("COLLECTED-INSTANCE-IREF")
                # Append the serialized element as a child (don't flatten it)
                iref_wrapper.append(serialized)
                elem.append(iref_wrapper)

        # Serialize collection_semantics
        if self.collection_semantics is not None:
            serialized = ARObject._serialize_item(self.collection_semantics, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COLLECTION-SEMANTICS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize element_role
        if self.element_role is not None:
            serialized = ARObject._serialize_item(self.element_role, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ELEMENT-ROLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize element_refs (list to container "ELEMENT-REFS")
        if self.element_refs:
            wrapper = ET.Element("ELEMENT-REFS")
            for item in self.element_refs:
                serialized = ARObject._serialize_item(item, "Identifiable")
                if serialized is not None:
                    child_elem = ET.Element("ELEMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize source_element_refs (list to container "SOURCE-ELEMENT-REFS")
        if self.source_element_refs:
            wrapper = ET.Element("SOURCE-ELEMENT-REFS")
            for item in self.source_element_refs:
                serialized = ARObject._serialize_item(item, "Identifiable")
                if serialized is not None:
                    child_elem = ET.Element("SOURCE-ELEMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

            serialized = ARObject._serialize_item(self.source_instance_irefs, "AnyInstanceRef")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("SOURCE-INSTANCES-IREF")
                # Append the serialized element as a child (don't flatten it)
                iref_wrapper.append(serialized)
                elem.append(iref_wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Collection":
        """Deserialize XML element to Collection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Collection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Collection, cls).deserialize(element)

        # Parse auto_collect
        child = ARObject._find_child_element(element, "AUTO-COLLECT")
        if child is not None:
            auto_collect_value = AutoCollectEnum.deserialize(child)
            obj.auto_collect = auto_collect_value

        # Parse collected_instance_irefs (instance reference from wrapper "COLLECTED-INSTANCE-IREF")
        wrapper = ARObject._find_child_element(element, "COLLECTED-INSTANCE-IREF")
        if wrapper is not None:
            # Get the first child element (the actual reference)
            children = list(wrapper)
            if children:
                inner_elem = children[0]
                collected_instance_irefs_value = ARObject._deserialize_by_tag(inner_elem)
                obj.collected_instance_irefs = collected_instance_irefs_value

        # Parse collection_semantics
        child = ARObject._find_child_element(element, "COLLECTION-SEMANTICS")
        if child is not None:
            collection_semantics_value = child.text
            obj.collection_semantics = collection_semantics_value

        # Parse element_role
        child = ARObject._find_child_element(element, "ELEMENT-ROLE")
        if child is not None:
            element_role_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.element_role = element_role_value

        # Parse element_refs (list from container "ELEMENT-REFS")
        obj.element_refs = []
        container = ARObject._find_child_element(element, "ELEMENT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.element_refs.append(child_value)

        # Parse source_element_refs (list from container "SOURCE-ELEMENT-REFS")
        obj.source_element_refs = []
        container = ARObject._find_child_element(element, "SOURCE-ELEMENT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.source_element_refs.append(child_value)

        # Parse source_instance_irefs (instance reference from wrapper "SOURCE-INSTANCES-IREF")
        wrapper = ARObject._find_child_element(element, "SOURCE-INSTANCES-IREF")
        if wrapper is not None:
            # Get the first child element (the actual reference)
            children = list(wrapper)
            if children:
                inner_elem = children[0]
                source_instance_irefs_value = ARObject._deserialize_by_tag(inner_elem)
                obj.source_instance_irefs = source_instance_irefs_value

        return obj



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
