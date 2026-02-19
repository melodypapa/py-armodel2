"""BinaryManifestItemDefinition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 920)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster_BinaryManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_item import (
    BinaryManifestItem,
)


class BinaryManifestItemDefinition(Identifiable):
    """AUTOSAR BinaryManifestItemDefinition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    auxiliary_fields: list[BinaryManifestItem]
    is_optional: Optional[Boolean]
    size: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize BinaryManifestItemDefinition."""
        super().__init__()
        self.auxiliary_fields: list[BinaryManifestItem] = []
        self.is_optional: Optional[Boolean] = None
        self.size: Optional[PositiveInteger] = None
    def serialize(self) -> ET.Element:
        """Serialize BinaryManifestItemDefinition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BinaryManifestItemDefinition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize auxiliary_fields (list to container "AUXILIARY-FIELDS")
        if self.auxiliary_fields:
            wrapper = ET.Element("AUXILIARY-FIELDS")
            for item in self.auxiliary_fields:
                serialized = ARObject._serialize_item(item, "BinaryManifestItem")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize is_optional
        if self.is_optional is not None:
            serialized = ARObject._serialize_item(self.is_optional, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-OPTIONAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize size
        if self.size is not None:
            serialized = ARObject._serialize_item(self.size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestItemDefinition":
        """Deserialize XML element to BinaryManifestItemDefinition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BinaryManifestItemDefinition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BinaryManifestItemDefinition, cls).deserialize(element)

        # Parse auxiliary_fields (list from container "AUXILIARY-FIELDS")
        obj.auxiliary_fields = []
        container = ARObject._find_child_element(element, "AUXILIARY-FIELDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.auxiliary_fields.append(child_value)

        # Parse is_optional
        child = ARObject._find_child_element(element, "IS-OPTIONAL")
        if child is not None:
            is_optional_value = child.text
            obj.is_optional = is_optional_value

        # Parse size
        child = ARObject._find_child_element(element, "SIZE")
        if child is not None:
            size_value = child.text
            obj.size = size_value

        return obj



class BinaryManifestItemDefinitionBuilder:
    """Builder for BinaryManifestItemDefinition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestItemDefinition = BinaryManifestItemDefinition()

    def build(self) -> BinaryManifestItemDefinition:
        """Build and return BinaryManifestItemDefinition object.

        Returns:
            BinaryManifestItemDefinition instance
        """
        # TODO: Add validation
        return self._obj
