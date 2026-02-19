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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

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

        # Serialize auto_collect_enum
        if self.auto_collect_enum is not None:
            serialized = ARObject._serialize_item(self.auto_collect_enum, "AutoCollectEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AUTO-COLLECT-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize collecteds (list to container "COLLECTEDS")
        if self.collecteds:
            wrapper = ET.Element("COLLECTEDS")
            for item in self.collecteds:
                serialized = ARObject._serialize_item(item, "AtpFeature")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize collection
        if self.collection is not None:
            serialized = ARObject._serialize_item(self.collection, "NameToken")
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

        # Serialize elements (list to container "ELEMENTS")
        if self.elements:
            wrapper = ET.Element("ELEMENTS")
            for item in self.elements:
                serialized = ARObject._serialize_item(item, "Identifiable")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

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

        # Serialize source_elements (list to container "SOURCE-ELEMENTS")
        if self.source_elements:
            wrapper = ET.Element("SOURCE-ELEMENTS")
            for item in self.source_elements:
                serialized = ARObject._serialize_item(item, "Identifiable")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize source_instances (list to container "SOURCE-INSTANCES")
        if self.source_instances:
            wrapper = ET.Element("SOURCE-INSTANCES")
            for item in self.source_instances:
                serialized = ARObject._serialize_item(item, "AtpFeature")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

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

        # Parse auto_collect_enum
        child = ARObject._find_child_element(element, "AUTO-COLLECT-ENUM")
        if child is not None:
            auto_collect_enum_value = AutoCollectEnum.deserialize(child)
            obj.auto_collect_enum = auto_collect_enum_value

        # Parse collecteds (list from container "COLLECTEDS")
        obj.collecteds = []
        container = ARObject._find_child_element(element, "COLLECTEDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.collecteds.append(child_value)

        # Parse collection
        child = ARObject._find_child_element(element, "COLLECTION")
        if child is not None:
            collection_value = child.text
            obj.collection = collection_value

        # Parse elements (list from container "ELEMENTS")
        obj.elements = []
        container = ARObject._find_child_element(element, "ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.elements.append(child_value)

        # Parse element_role
        child = ARObject._find_child_element(element, "ELEMENT-ROLE")
        if child is not None:
            element_role_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.element_role = element_role_value

        # Parse source_elements (list from container "SOURCE-ELEMENTS")
        obj.source_elements = []
        container = ARObject._find_child_element(element, "SOURCE-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.source_elements.append(child_value)

        # Parse source_instances (list from container "SOURCE-INSTANCES")
        obj.source_instances = []
        container = ARObject._find_child_element(element, "SOURCE-INSTANCES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.source_instances.append(child_value)

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
