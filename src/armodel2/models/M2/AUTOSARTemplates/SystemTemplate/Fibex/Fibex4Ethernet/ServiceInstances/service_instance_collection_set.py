"""ServiceInstanceCollectionSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 476)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import FibexElementBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.abstract_service_instance import (
    AbstractServiceInstance,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ServiceInstanceCollectionSet(FibexElement):
    """AUTOSAR ServiceInstanceCollectionSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SERVICE-INSTANCE-COLLECTION-SET"


    service_instances: list[AbstractServiceInstance]
    _DESERIALIZE_DISPATCH = {
        "SERVICE-INSTANCES": ("_POLYMORPHIC_LIST", "service_instances", ["ConsumedServiceInstance", "DdsCpConsumedServiceInstance", "DdsCpProvidedServiceInstance", "DdsCpServiceInstance", "ProvidedServiceInstance"]),
    }


    def __init__(self) -> None:
        """Initialize ServiceInstanceCollectionSet."""
        super().__init__()
        self.service_instances: list[AbstractServiceInstance] = []

    def serialize(self) -> ET.Element:
        """Serialize ServiceInstanceCollectionSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ServiceInstanceCollectionSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize service_instances (list to container "SERVICE-INSTANCES")
        if self.service_instances:
            wrapper = ET.Element("SERVICE-INSTANCES")
            for item in self.service_instances:
                serialized = SerializationHelper.serialize_item(item, "AbstractServiceInstance")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ServiceInstanceCollectionSet":
        """Deserialize XML element to ServiceInstanceCollectionSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ServiceInstanceCollectionSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ServiceInstanceCollectionSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SERVICE-INSTANCES":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "CONSUMED-SERVICE-INSTANCE":
                        obj.service_instances.append(SerializationHelper.deserialize_by_tag(item_elem, "ConsumedServiceInstance"))
                    elif concrete_tag == "DDS-CP-CONSUMED-SERVICE-INSTANCE":
                        obj.service_instances.append(SerializationHelper.deserialize_by_tag(item_elem, "DdsCpConsumedServiceInstance"))
                    elif concrete_tag == "DDS-CP-PROVIDED-SERVICE-INSTANCE":
                        obj.service_instances.append(SerializationHelper.deserialize_by_tag(item_elem, "DdsCpProvidedServiceInstance"))
                    elif concrete_tag == "DDS-CP-SERVICE-INSTANCE":
                        obj.service_instances.append(SerializationHelper.deserialize_by_tag(item_elem, "DdsCpServiceInstance"))
                    elif concrete_tag == "PROVIDED-SERVICE-INSTANCE":
                        obj.service_instances.append(SerializationHelper.deserialize_by_tag(item_elem, "ProvidedServiceInstance"))

        return obj



class ServiceInstanceCollectionSetBuilder(FibexElementBuilder):
    """Builder for ServiceInstanceCollectionSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ServiceInstanceCollectionSet = ServiceInstanceCollectionSet()


    def with_service_instances(self, items: list[AbstractServiceInstance]) -> "ServiceInstanceCollectionSetBuilder":
        """Set service_instances list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.service_instances = list(items) if items else []
        return self


    def add_service_instance(self, item: AbstractServiceInstance) -> "ServiceInstanceCollectionSetBuilder":
        """Add a single item to service_instances list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.service_instances.append(item)
        return self

    def clear_service_instances(self) -> "ServiceInstanceCollectionSetBuilder":
        """Clear all items from service_instances list.

        Returns:
            self for method chaining
        """
        self._obj.service_instances = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "serviceInstance",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ServiceInstanceCollectionSet:
        """Build and return the ServiceInstanceCollectionSet instance with validation."""
        self._validate_instance()
        return self._obj