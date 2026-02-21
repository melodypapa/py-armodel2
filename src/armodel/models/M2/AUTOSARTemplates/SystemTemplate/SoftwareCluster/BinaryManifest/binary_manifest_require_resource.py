"""BinaryManifestRequireResource AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 916)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster_BinaryManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_resource import (
    BinaryManifestResource,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class BinaryManifestRequireResource(BinaryManifestResource):
    """AUTOSAR BinaryManifestRequireResource."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    connection_is: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize BinaryManifestRequireResource."""
        super().__init__()
        self.connection_is: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize BinaryManifestRequireResource to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BinaryManifestRequireResource, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize connection_is
        if self.connection_is is not None:
            serialized = ARObject._serialize_item(self.connection_is, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONNECTION-IS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestRequireResource":
        """Deserialize XML element to BinaryManifestRequireResource object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BinaryManifestRequireResource object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BinaryManifestRequireResource, cls).deserialize(element)

        # Parse connection_is
        child = ARObject._find_child_element(element, "CONNECTION-IS")
        if child is not None:
            connection_is_value = child.text
            obj.connection_is = connection_is_value

        return obj



class BinaryManifestRequireResourceBuilder:
    """Builder for BinaryManifestRequireResource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestRequireResource = BinaryManifestRequireResource()

    def build(self) -> BinaryManifestRequireResource:
        """Build and return BinaryManifestRequireResource object.

        Returns:
            BinaryManifestRequireResource instance
        """
        # TODO: Add validation
        return self._obj
