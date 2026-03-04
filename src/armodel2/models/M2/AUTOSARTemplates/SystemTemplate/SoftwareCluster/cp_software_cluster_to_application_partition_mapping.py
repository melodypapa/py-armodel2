"""CpSoftwareClusterToApplicationPartitionMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 287)

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
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.application_partition import (
    ApplicationPartition,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CpSoftwareClusterToApplicationPartitionMapping(Identifiable):
    """AUTOSAR CpSoftwareClusterToApplicationPartitionMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CP-SOFTWARE-CLUSTER-TO-APPLICATION-PARTITION-MAPPING"


    application_refs: list[ARRef]
    software_cluster_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "APPLICATION-REFS": lambda obj, elem: [obj.application_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "SOFTWARE-CLUSTER-REF": lambda obj, elem: setattr(obj, "software_cluster_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize CpSoftwareClusterToApplicationPartitionMapping."""
        super().__init__()
        self.application_refs: list[ARRef] = []
        self.software_cluster_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize CpSoftwareClusterToApplicationPartitionMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CpSoftwareClusterToApplicationPartitionMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize application_refs (list to container "APPLICATION-REFS")
        if self.application_refs:
            wrapper = ET.Element("APPLICATION-REFS")
            for item in self.application_refs:
                serialized = SerializationHelper.serialize_item(item, "ApplicationPartition")
                if serialized is not None:
                    child_elem = ET.Element("APPLICATION-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize software_cluster_ref
        if self.software_cluster_ref is not None:
            serialized = SerializationHelper.serialize_item(self.software_cluster_ref, "CpSoftwareCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOFTWARE-CLUSTER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterToApplicationPartitionMapping":
        """Deserialize XML element to CpSoftwareClusterToApplicationPartitionMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSoftwareClusterToApplicationPartitionMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CpSoftwareClusterToApplicationPartitionMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "APPLICATION-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.application_refs.append(ARRef.deserialize(item_elem))
            elif tag == "SOFTWARE-CLUSTER-REF":
                setattr(obj, "software_cluster_ref", ARRef.deserialize(child))

        return obj



class CpSoftwareClusterToApplicationPartitionMappingBuilder(IdentifiableBuilder):
    """Builder for CpSoftwareClusterToApplicationPartitionMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CpSoftwareClusterToApplicationPartitionMapping = CpSoftwareClusterToApplicationPartitionMapping()


    def with_applications(self, items: list[ApplicationPartition]) -> "CpSoftwareClusterToApplicationPartitionMappingBuilder":
        """Set applications list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.applications = list(items) if items else []
        return self

    def with_software_cluster(self, value: Optional[CpSoftwareCluster]) -> "CpSoftwareClusterToApplicationPartitionMappingBuilder":
        """Set software_cluster attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.software_cluster = value
        return self


    def add_application(self, item: ApplicationPartition) -> "CpSoftwareClusterToApplicationPartitionMappingBuilder":
        """Add a single item to applications list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.applications.append(item)
        return self

    def clear_applications(self) -> "CpSoftwareClusterToApplicationPartitionMappingBuilder":
        """Clear all items from applications list.

        Returns:
            self for method chaining
        """
        self._obj.applications = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "application",
        "softwareCluster",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CpSoftwareClusterToApplicationPartitionMapping:
        """Build and return the CpSoftwareClusterToApplicationPartitionMapping instance with validation."""
        self._validate_instance()
        return self._obj