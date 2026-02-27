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

    ecu_scope_refs: list[ARRef]
    resources: list[CpSoftwareCluster]
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
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse ecu_scope_refs (list from container "ECU-SCOPE-REFS")
        obj.ecu_scope_refs = []
        container = SerializationHelper.find_child_element(element, "ECU-SCOPE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ecu_scope_refs.append(child_value)

        # Parse resources (list from container "RESOURCES")
        obj.resources = []
        container = SerializationHelper.find_child_element(element, "RESOURCES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.resources.append(child_value)

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


    def build(self) -> CpSoftwareClusterResourcePool:
        """Build and return the CpSoftwareClusterResourcePool instance with validation."""
        self._validate_instance()
        pass
        return self._obj