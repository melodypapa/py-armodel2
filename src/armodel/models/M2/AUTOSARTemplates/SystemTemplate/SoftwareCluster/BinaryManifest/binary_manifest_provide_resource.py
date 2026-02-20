"""BinaryManifestProvideResource AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 914)

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
    PositiveInteger,
)


class BinaryManifestProvideResource(BinaryManifestResource):
    """AUTOSAR BinaryManifestProvideResource."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    number_of: Optional[PositiveInteger]
    supports: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize BinaryManifestProvideResource."""
        super().__init__()
        self.number_of: Optional[PositiveInteger] = None
        self.supports: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize BinaryManifestProvideResource to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BinaryManifestProvideResource, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize number_of
        if self.number_of is not None:
            serialized = ARObject._serialize_item(self.number_of, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NUMBER-OF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize supports
        if self.supports is not None:
            serialized = ARObject._serialize_item(self.supports, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUPPORTS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestProvideResource":
        """Deserialize XML element to BinaryManifestProvideResource object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BinaryManifestProvideResource object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BinaryManifestProvideResource, cls).deserialize(element)

        # Parse number_of
        child = ARObject._find_child_element(element, "NUMBER-OF")
        if child is not None:
            number_of_value = child.text
            obj.number_of = number_of_value

        # Parse supports
        child = ARObject._find_child_element(element, "SUPPORTS")
        if child is not None:
            supports_value = child.text
            obj.supports = supports_value

        return obj



class BinaryManifestProvideResourceBuilder:
    """Builder for BinaryManifestProvideResource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestProvideResource = BinaryManifestProvideResource()

    def build(self) -> BinaryManifestProvideResource:
        """Build and return BinaryManifestProvideResource object.

        Returns:
            BinaryManifestProvideResource instance
        """
        # TODO: Add validation
        return self._obj
