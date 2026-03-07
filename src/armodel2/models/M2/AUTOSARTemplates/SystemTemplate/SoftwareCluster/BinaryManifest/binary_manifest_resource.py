"""BinaryManifestResource AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 915)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster_BinaryManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BinaryManifestResource(Identifiable, ABC):
    """AUTOSAR BinaryManifestResource."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    global_resource: Optional[PositiveInteger]
    resource_ref: Optional[Any]
    resource_guard: Optional[String]
    _DESERIALIZE_DISPATCH = {
        "GLOBAL-RESOURCE": lambda obj, elem: setattr(obj, "global_resource", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "RESOURCE-REF": lambda obj, elem: setattr(obj, "resource_ref", ARRef.deserialize(elem)),
        "RESOURCE-GUARD": lambda obj, elem: setattr(obj, "resource_guard", SerializationHelper.deserialize_by_tag(elem, "String")),
    }


    def __init__(self) -> None:
        """Initialize BinaryManifestResource."""
        super().__init__()
        self.global_resource: Optional[PositiveInteger] = None
        self.resource_ref: Optional[Any] = None
        self.resource_guard: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize BinaryManifestResource to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BinaryManifestResource, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize global_resource
        if self.global_resource is not None:
            serialized = SerializationHelper.serialize_item(self.global_resource, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("GLOBAL-RESOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize resource_ref
        if self.resource_ref is not None:
            serialized = SerializationHelper.serialize_item(self.resource_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESOURCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize resource_guard
        if self.resource_guard is not None:
            serialized = SerializationHelper.serialize_item(self.resource_guard, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESOURCE-GUARD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestResource":
        """Deserialize XML element to BinaryManifestResource object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BinaryManifestResource object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BinaryManifestResource, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "GLOBAL-RESOURCE":
                setattr(obj, "global_resource", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "RESOURCE-REF":
                setattr(obj, "resource_ref", ARRef.deserialize(child))
            elif tag == "RESOURCE-GUARD":
                setattr(obj, "resource_guard", SerializationHelper.deserialize_by_tag(child, "String"))

        return obj



class BinaryManifestResourceBuilder(IdentifiableBuilder):
    """Builder for BinaryManifestResource with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BinaryManifestResource = BinaryManifestResource()


    def with_global_resource(self, value: Optional[PositiveInteger]) -> "BinaryManifestResourceBuilder":
        """Set global_resource attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'global_resource' is required and cannot be None")
        self._obj.global_resource = value
        return self

    def with_resource(self, value: Optional[Any]) -> "BinaryManifestResourceBuilder":
        """Set resource attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'resource' is required and cannot be None")
        self._obj.resource = value
        return self

    def with_resource_guard(self, value: Optional[String]) -> "BinaryManifestResourceBuilder":
        """Set resource_guard attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'resource_guard' is required and cannot be None")
        self._obj.resource_guard = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "globalResource",
        "resource",
        "resourceGuard",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> BinaryManifestResource:
        """Build and return the BinaryManifestResource instance (abstract)."""
        raise NotImplementedError