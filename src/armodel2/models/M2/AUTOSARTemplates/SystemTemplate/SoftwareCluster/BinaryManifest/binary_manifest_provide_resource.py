"""BinaryManifestProvideResource AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 914)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster_BinaryManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_resource import (
    BinaryManifestResource,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_resource import BinaryManifestResourceBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BinaryManifestProvideResource(BinaryManifestResource):
    """AUTOSAR BinaryManifestProvideResource."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BINARY-MANIFEST-PROVIDE-RESOURCE"


    number_of: Optional[PositiveInteger]
    supports: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "NUMBER-OF": lambda obj, elem: setattr(obj, "number_of", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SUPPORTS": lambda obj, elem: setattr(obj, "supports", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BinaryManifestProvideResource, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize number_of
        if self.number_of is not None:
            serialized = SerializationHelper.serialize_item(self.number_of, "PositiveInteger")
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
            serialized = SerializationHelper.serialize_item(self.supports, "Boolean")
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "NUMBER-OF":
                setattr(obj, "number_of", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SUPPORTS":
                setattr(obj, "supports", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class BinaryManifestProvideResourceBuilder(BinaryManifestResourceBuilder):
    """Builder for BinaryManifestProvideResource with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BinaryManifestProvideResource = BinaryManifestProvideResource()


    def with_number_of(self, value: Optional[PositiveInteger]) -> "BinaryManifestProvideResourceBuilder":
        """Set number_of attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'number_of' is required and cannot be None")
        self._obj.number_of = value
        return self

    def with_supports(self, value: Optional[Boolean]) -> "BinaryManifestProvideResourceBuilder":
        """Set supports attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'supports' is required and cannot be None")
        self._obj.supports = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "numberOf",
        "supports",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> BinaryManifestProvideResource:
        """Build and return the BinaryManifestProvideResource instance with validation."""
        self._validate_instance()
        return self._obj