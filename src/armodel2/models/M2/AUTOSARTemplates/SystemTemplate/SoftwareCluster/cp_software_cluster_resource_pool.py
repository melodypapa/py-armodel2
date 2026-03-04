"""CpSoftwareClusterResourcePool AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 901)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CpSoftwareClusterResourcePool(ARElement):
    """AUTOSAR CpSoftwareClusterResourcePool."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CP-SOFTWARE-CLUSTER-RESOURCE-POOL"


    ecu_scope_refs: list[ARRef]
    resources: list[CpSoftwareCluster]
    _DESERIALIZE_DISPATCH = {
        "ECU-SCOPE-REFS": lambda obj, elem: [obj.ecu_scope_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "RESOURCES": lambda obj, elem: obj.resources.append(SerializationHelper.deserialize_by_tag(elem, "CpSoftwareCluster")),
    }


    def __init__(self) -> None:
        """Initialize CpSoftwareClusterResourcePool."""
        super().__init__()
        self.ecu_scope_refs: list[ARRef] = []
        self.resources: list[CpSoftwareCluster] = []

    def serialize(self) -> ET.Element:
        """Serialize CpSoftwareClusterResourcePool to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CpSoftwareClusterResourcePool, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ecu_scope_refs (list to container "ECU-SCOPE-REFS")
        if self.ecu_scope_refs:
            wrapper = ET.Element("ECU-SCOPE-REFS")
            for item in self.ecu_scope_refs:
                serialized = SerializationHelper.serialize_item(item, "EcuInstance")
                if serialized is not None:
                    child_elem = ET.Element("ECU-SCOPE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize resources (list to container "RESOURCES")
        if self.resources:
            wrapper = ET.Element("RESOURCES")
            for item in self.resources:
                serialized = SerializationHelper.serialize_item(item, "CpSoftwareCluster")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterResourcePool":
        """Deserialize XML element to CpSoftwareClusterResourcePool object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSoftwareClusterResourcePool object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CpSoftwareClusterResourcePool, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ECU-SCOPE-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.ecu_scope_refs.append(ARRef.deserialize(item_elem))
            elif tag == "RESOURCES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.resources.append(SerializationHelper.deserialize_by_tag(item_elem, "CpSoftwareCluster"))

        return obj



class CpSoftwareClusterResourcePoolBuilder(ARElementBuilder):
    """Builder for CpSoftwareClusterResourcePool with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CpSoftwareClusterResourcePool = CpSoftwareClusterResourcePool()


    def with_ecu_scopes(self, items: list[EcuInstance]) -> "CpSoftwareClusterResourcePoolBuilder":
        """Set ecu_scopes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.ecu_scopes = list(items) if items else []
        return self

    def with_resources(self, items: list[CpSoftwareCluster]) -> "CpSoftwareClusterResourcePoolBuilder":
        """Set resources list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.resources = list(items) if items else []
        return self


    def add_ecu_scope(self, item: EcuInstance) -> "CpSoftwareClusterResourcePoolBuilder":
        """Add a single item to ecu_scopes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.ecu_scopes.append(item)
        return self

    def clear_ecu_scopes(self) -> "CpSoftwareClusterResourcePoolBuilder":
        """Clear all items from ecu_scopes list.

        Returns:
            self for method chaining
        """
        self._obj.ecu_scopes = []
        return self

    def add_resource(self, item: CpSoftwareCluster) -> "CpSoftwareClusterResourcePoolBuilder":
        """Add a single item to resources list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.resources.append(item)
        return self

    def clear_resources(self) -> "CpSoftwareClusterResourcePoolBuilder":
        """Clear all items from resources list.

        Returns:
            self for method chaining
        """
        self._obj.resources = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "ecuScope",
        "resource",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CpSoftwareClusterResourcePool:
        """Build and return the CpSoftwareClusterResourcePool instance with validation."""
        self._validate_instance()
        return self._obj