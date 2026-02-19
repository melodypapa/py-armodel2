"""EnumerationMappingTable AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 444)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling_AttributeValueVariationPoints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.packageable_element import (
    PackageableElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef


class EnumerationMappingTable(PackageableElement):
    """AUTOSAR EnumerationMappingTable."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    entrie_refs: list[Any]
    def __init__(self) -> None:
        """Initialize EnumerationMappingTable."""
        super().__init__()
        self.entrie_refs: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize EnumerationMappingTable to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EnumerationMappingTable, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize entrie_refs (list to container "ENTRIES")
        if self.entrie_refs:
            wrapper = ET.Element("ENTRIES")
            for item in self.entrie_refs:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EnumerationMappingTable":
        """Deserialize XML element to EnumerationMappingTable object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EnumerationMappingTable object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EnumerationMappingTable, cls).deserialize(element)

        # Parse entrie_refs (list from container "ENTRIES")
        obj.entrie_refs = []
        container = ARObject._find_child_element(element, "ENTRIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.entrie_refs.append(child_value)

        return obj



class EnumerationMappingTableBuilder:
    """Builder for EnumerationMappingTable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EnumerationMappingTable = EnumerationMappingTable()

    def build(self) -> EnumerationMappingTable:
        """Build and return EnumerationMappingTable object.

        Returns:
            EnumerationMappingTable instance
        """
        # TODO: Add validation
        return self._obj
