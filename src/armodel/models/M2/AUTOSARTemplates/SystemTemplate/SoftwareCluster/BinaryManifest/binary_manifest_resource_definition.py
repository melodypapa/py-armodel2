"""BinaryManifestResourceDefinition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 917)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster_BinaryManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_item import (
    BinaryManifestItem,
)


class BinaryManifestResourceDefinition(Identifiable):
    """AUTOSAR BinaryManifestResourceDefinition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    item_definitions: list[BinaryManifestItem]
    def __init__(self) -> None:
        """Initialize BinaryManifestResourceDefinition."""
        super().__init__()
        self.item_definitions: list[BinaryManifestItem] = []

    def serialize(self) -> ET.Element:
        """Serialize BinaryManifestResourceDefinition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BinaryManifestResourceDefinition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize item_definitions (list to container "ITEM-DEFINITIONS")
        if self.item_definitions:
            wrapper = ET.Element("ITEM-DEFINITIONS")
            for item in self.item_definitions:
                serialized = SerializationHelper.serialize_item(item, "BinaryManifestItem")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestResourceDefinition":
        """Deserialize XML element to BinaryManifestResourceDefinition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BinaryManifestResourceDefinition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BinaryManifestResourceDefinition, cls).deserialize(element)

        # Parse item_definitions (list from container "ITEM-DEFINITIONS")
        obj.item_definitions = []
        container = SerializationHelper.find_child_element(element, "ITEM-DEFINITIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.item_definitions.append(child_value)

        return obj



class BinaryManifestResourceDefinitionBuilder:
    """Builder for BinaryManifestResourceDefinition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestResourceDefinition = BinaryManifestResourceDefinition()

    def build(self) -> BinaryManifestResourceDefinition:
        """Build and return BinaryManifestResourceDefinition object.

        Returns:
            BinaryManifestResourceDefinition instance
        """
        # TODO: Add validation
        return self._obj
