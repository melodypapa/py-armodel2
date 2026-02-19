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
