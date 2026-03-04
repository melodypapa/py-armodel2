"""CpSoftwareClusterToResourceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 907)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CpSoftwareClusterToResourceMapping(Identifiable):
    """AUTOSAR CpSoftwareClusterToResourceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CP-SOFTWARE-CLUSTER-TO-RESOURCE-MAPPING"


    provider_ref: Optional[ARRef]
    requester_refs: list[ARRef]
    service_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "PROVIDER-REF": lambda obj, elem: setattr(obj, "provider_ref", ARRef.deserialize(elem)),
        "REQUESTER-REFS": lambda obj, elem: [obj.requester_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "SERVICE-REF": lambda obj, elem: setattr(obj, "service_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize CpSoftwareClusterToResourceMapping."""
        super().__init__()
        self.provider_ref: Optional[ARRef] = None
        self.requester_refs: list[ARRef] = []
        self.service_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize CpSoftwareClusterToResourceMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CpSoftwareClusterToResourceMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize provider_ref
        if self.provider_ref is not None:
            serialized = SerializationHelper.serialize_item(self.provider_ref, "CpSoftwareCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROVIDER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize requester_refs (list to container "REQUESTER-REFS")
        if self.requester_refs:
            wrapper = ET.Element("REQUESTER-REFS")
            for item in self.requester_refs:
                serialized = SerializationHelper.serialize_item(item, "CpSoftwareCluster")
                if serialized is not None:
                    child_elem = ET.Element("REQUESTER-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize service_ref
        if self.service_ref is not None:
            serialized = SerializationHelper.serialize_item(self.service_ref, "CpSoftwareCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterToResourceMapping":
        """Deserialize XML element to CpSoftwareClusterToResourceMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSoftwareClusterToResourceMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CpSoftwareClusterToResourceMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "PROVIDER-REF":
                setattr(obj, "provider_ref", ARRef.deserialize(child))
            elif tag == "REQUESTER-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.requester_refs.append(ARRef.deserialize(item_elem))
            elif tag == "SERVICE-REF":
                setattr(obj, "service_ref", ARRef.deserialize(child))

        return obj



class CpSoftwareClusterToResourceMappingBuilder(IdentifiableBuilder):
    """Builder for CpSoftwareClusterToResourceMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CpSoftwareClusterToResourceMapping = CpSoftwareClusterToResourceMapping()


    def with_provider(self, value: Optional[CpSoftwareCluster]) -> "CpSoftwareClusterToResourceMappingBuilder":
        """Set provider attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.provider = value
        return self

    def with_requesters(self, items: list[CpSoftwareCluster]) -> "CpSoftwareClusterToResourceMappingBuilder":
        """Set requesters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.requesters = list(items) if items else []
        return self

    def with_service(self, value: Optional[CpSoftwareCluster]) -> "CpSoftwareClusterToResourceMappingBuilder":
        """Set service attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.service = value
        return self


    def add_requester(self, item: CpSoftwareCluster) -> "CpSoftwareClusterToResourceMappingBuilder":
        """Add a single item to requesters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.requesters.append(item)
        return self

    def clear_requesters(self) -> "CpSoftwareClusterToResourceMappingBuilder":
        """Clear all items from requesters list.

        Returns:
            self for method chaining
        """
        self._obj.requesters = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "provider",
        "requester",
        "service",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CpSoftwareClusterToResourceMapping:
        """Build and return the CpSoftwareClusterToResourceMapping instance with validation."""
        self._validate_instance()
        return self._obj