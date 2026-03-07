"""CpSoftwareClusterResource AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 271)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 901)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.role_based_resource_dependency import (
    RoleBasedResourceDependency,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CpSoftwareClusterResource(Identifiable, ABC):
    """AUTOSAR CpSoftwareClusterResource."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    dependents: list[RoleBasedResourceDependency]
    global_resource: Optional[PositiveInteger]
    is_mandatory: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "DEPENDENTS": lambda obj, elem: obj.dependents.append(SerializationHelper.deserialize_by_tag(elem, "RoleBasedResourceDependency")),
        "GLOBAL-RESOURCE": lambda obj, elem: setattr(obj, "global_resource", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "IS-MANDATORY": lambda obj, elem: setattr(obj, "is_mandatory", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize CpSoftwareClusterResource."""
        super().__init__()
        self.dependents: list[RoleBasedResourceDependency] = []
        self.global_resource: Optional[PositiveInteger] = None
        self.is_mandatory: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize CpSoftwareClusterResource to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CpSoftwareClusterResource, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dependents (list to container "DEPENDENTS")
        if self.dependents:
            wrapper = ET.Element("DEPENDENTS")
            for item in self.dependents:
                serialized = SerializationHelper.serialize_item(item, "RoleBasedResourceDependency")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

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

        # Serialize is_mandatory
        if self.is_mandatory is not None:
            serialized = SerializationHelper.serialize_item(self.is_mandatory, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-MANDATORY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterResource":
        """Deserialize XML element to CpSoftwareClusterResource object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSoftwareClusterResource object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CpSoftwareClusterResource, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DEPENDENTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.dependents.append(SerializationHelper.deserialize_by_tag(item_elem, "RoleBasedResourceDependency"))
            elif tag == "GLOBAL-RESOURCE":
                setattr(obj, "global_resource", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "IS-MANDATORY":
                setattr(obj, "is_mandatory", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class CpSoftwareClusterResourceBuilder(IdentifiableBuilder):
    """Builder for CpSoftwareClusterResource with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CpSoftwareClusterResource = CpSoftwareClusterResource()


    def with_dependents(self, items: list[RoleBasedResourceDependency]) -> "CpSoftwareClusterResourceBuilder":
        """Set dependents list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.dependents = list(items) if items else []
        return self

    def with_global_resource(self, value: Optional[PositiveInteger]) -> "CpSoftwareClusterResourceBuilder":
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

    def with_is_mandatory(self, value: Optional[Boolean]) -> "CpSoftwareClusterResourceBuilder":
        """Set is_mandatory attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'is_mandatory' is required and cannot be None")
        self._obj.is_mandatory = value
        return self


    def add_dependent(self, item: RoleBasedResourceDependency) -> "CpSoftwareClusterResourceBuilder":
        """Add a single item to dependents list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.dependents.append(item)
        return self

    def clear_dependents(self) -> "CpSoftwareClusterResourceBuilder":
        """Clear all items from dependents list.

        Returns:
            self for method chaining
        """
        self._obj.dependents = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dependent",
        "globalResource",
        "isMandatory",
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
    def build(self) -> CpSoftwareClusterResource:
        """Build and return the CpSoftwareClusterResource instance (abstract)."""
        raise NotImplementedError