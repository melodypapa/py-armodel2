"""CpSoftwareClusterServiceResource AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 904)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_resource import (
    CpSoftwareClusterResource,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_resource import CpSoftwareClusterResourceBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_container_value import (
    EcucContainerValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CpSoftwareClusterServiceResource(CpSoftwareClusterResource):
    """AUTOSAR CpSoftwareClusterServiceResource."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CP-SOFTWARE-CLUSTER-SERVICE-RESOURCE"


    resource_need_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "RESOURCE-NEEDS-REFS": lambda obj, elem: obj.resource_need_refs.append(ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize CpSoftwareClusterServiceResource."""
        super().__init__()
        self.resource_need_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize CpSoftwareClusterServiceResource to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CpSoftwareClusterServiceResource, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize resource_need_refs (list to container "RESOURCE-NEEDS-REFS")
        if self.resource_need_refs:
            wrapper = ET.Element("RESOURCE-NEEDS-REFS")
            for item in self.resource_need_refs:
                serialized = SerializationHelper.serialize_item(item, "EcucContainerValue")
                if serialized is not None:
                    child_elem = ET.Element("RESOURCE-NEED-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterServiceResource":
        """Deserialize XML element to CpSoftwareClusterServiceResource object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSoftwareClusterServiceResource object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CpSoftwareClusterServiceResource, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "RESOURCE-NEEDS-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.resource_need_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "EcucContainerValue"))

        return obj



class CpSoftwareClusterServiceResourceBuilder(CpSoftwareClusterResourceBuilder):
    """Builder for CpSoftwareClusterServiceResource with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CpSoftwareClusterServiceResource = CpSoftwareClusterServiceResource()


    def with_resource_needses(self, items: list[EcucContainerValue]) -> "CpSoftwareClusterServiceResourceBuilder":
        """Set resource_needses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.resource_needses = list(items) if items else []
        return self


    def add_resource_needs(self, item: EcucContainerValue) -> "CpSoftwareClusterServiceResourceBuilder":
        """Add a single item to resource_needses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.resource_needses.append(item)
        return self

    def clear_resource_needses(self) -> "CpSoftwareClusterServiceResourceBuilder":
        """Clear all items from resource_needses list.

        Returns:
            self for method chaining
        """
        self._obj.resource_needses = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> CpSoftwareClusterServiceResource:
        """Build and return the CpSoftwareClusterServiceResource instance with validation."""
        self._validate_instance()
        pass
        return self._obj