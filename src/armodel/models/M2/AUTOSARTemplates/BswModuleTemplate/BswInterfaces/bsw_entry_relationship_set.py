"""BswEntryRelationshipSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 51)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 51)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswInterfaces.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_entry_relationship import (
    BswEntryRelationship,
)


class BswEntryRelationshipSet(ARElement):
    """AUTOSAR BswEntryRelationshipSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bsw_entry_relationships: list[BswEntryRelationship]
    def __init__(self) -> None:
        """Initialize BswEntryRelationshipSet."""
        super().__init__()
        self.bsw_entry_relationships: list[BswEntryRelationship] = []

    def serialize(self) -> ET.Element:
        """Serialize BswEntryRelationshipSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswEntryRelationshipSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bsw_entry_relationships (list to container "BSW-ENTRY-RELATIONSHIPS")
        if self.bsw_entry_relationships:
            wrapper = ET.Element("BSW-ENTRY-RELATIONSHIPS")
            for item in self.bsw_entry_relationships:
                serialized = SerializationHelper.serialize_item(item, "BswEntryRelationship")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswEntryRelationshipSet":
        """Deserialize XML element to BswEntryRelationshipSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswEntryRelationshipSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswEntryRelationshipSet, cls).deserialize(element)

        # Parse bsw_entry_relationships (list from container "BSW-ENTRY-RELATIONSHIPS")
        obj.bsw_entry_relationships = []
        container = SerializationHelper.find_child_element(element, "BSW-ENTRY-RELATIONSHIPS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.bsw_entry_relationships.append(child_value)

        return obj



class BswEntryRelationshipSetBuilder:
    """Builder for BswEntryRelationshipSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswEntryRelationshipSet = BswEntryRelationshipSet()

    def build(self) -> BswEntryRelationshipSet:
        """Build and return BswEntryRelationshipSet object.

        Returns:
            BswEntryRelationshipSet instance
        """
        # TODO: Add validation
        return self._obj
