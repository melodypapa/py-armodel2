"""McGroupDataRefSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 191)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2035)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_McGroups.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import xml_element_name
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_instance_descriptor import (
    FlatInstanceDescriptor,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_data_instance import (
    McDataInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


@atp_variant()

class McGroupDataRefSet(ARObject):
    """AUTOSAR McGroupDataRefSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _flat_map_entrie_refs: list[ARRef]
    mc_data_instance_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize McGroupDataRefSet."""
        super().__init__()
        self._flat_map_entrie_refs: list[ARRef] = []
        self.mc_data_instance_refs: list[ARRef] = []
    @property
    @xml_element_name("FLAT-MAP-ENTRYS")
    def flat_map_entrie_refs(self) -> list[ARRef]:
        """Get flat_map_entrie_refs with custom XML element name."""
        return self._flat_map_entrie_refs

    @flat_map_entrie_refs.setter
    def flat_map_entrie_refs(self, value: list[ARRef]) -> None:
        """Set flat_map_entrie_refs with custom XML element name."""
        self._flat_map_entrie_refs = value


    def serialize(self) -> ET.Element:
        """Serialize McGroupDataRefSet to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(McGroupDataRefSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Serialize flat_map_entrie_refs (list from container "FLAT-MAP-ENTRIE-REFS")
        if self.flat_map_entrie_refs:
            container = ET.Element("FLAT-MAP-ENTRIE-REFS")
            for item in self.flat_map_entrie_refs:
                # For reference lists, serialize as reference
                if hasattr(item, "serialize"):
                    container.append(item.serialize())
            inner_elem.append(container)

        # Serialize mc_data_instance_refs (list from container "MC-DATA-INSTANCE-REFS")
        if self.mc_data_instance_refs:
            container = ET.Element("MC-DATA-INSTANCE-REFS")
            for item in self.mc_data_instance_refs:
                # For reference lists, serialize as reference
                if hasattr(item, "serialize"):
                    container.append(item.serialize())
            inner_elem.append(container)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "McGroupDataRefSet")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "McGroupDataRefSet":
        """Deserialize XML element to McGroupDataRefSet object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized McGroupDataRefSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(McGroupDataRefSet, cls).deserialize(element)

        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "McGroupDataRefSet")
        if inner_elem is None:
            # No wrapper structure found, return object with default values
            return obj

        # Parse flat_map_entrie_refs (list from container "FLAT-MAP-ENTRYS")
        obj.flat_map_entrie_refs = []
        container = SerializationHelper.find_child_element(inner_elem, "FLAT-MAP-ENTRYS")
        if container is not None:
            for child in container:
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    child_value = ARRef.deserialize(child)
                else:
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.flat_map_entrie_refs.append(child_value)

        # Parse mc_data_instance_refs (list from container "MC-DATA-INSTANCE-REFS")
        obj.mc_data_instance_refs = []
        container = SerializationHelper.find_child_element(inner_elem, "MC-DATA-INSTANCE-REFS")
        if container is not None:
            for child in container:
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    child_value = ARRef.deserialize(child)
                else:
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mc_data_instance_refs.append(child_value)

        return obj



class McGroupDataRefSetBuilder(BuilderBase):
    """Builder for McGroupDataRefSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: McGroupDataRefSet = McGroupDataRefSet()


    def with_flat_map_entries(self, items: list[FlatInstanceDescriptor]) -> "McGroupDataRefSetBuilder":
        """Set flat_map_entries list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.flat_map_entries = list(items) if items else []
        return self

    def with_mc_data_instances(self, items: list[McDataInstance]) -> "McGroupDataRefSetBuilder":
        """Set mc_data_instances list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mc_data_instances = list(items) if items else []
        return self


    def add_flat_map_entrie(self, item: FlatInstanceDescriptor) -> "McGroupDataRefSetBuilder":
        """Add a single item to flat_map_entries list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.flat_map_entries.append(item)
        return self

    def clear_flat_map_entries(self) -> "McGroupDataRefSetBuilder":
        """Clear all items from flat_map_entries list.

        Returns:
            self for method chaining
        """
        self._obj.flat_map_entries = []
        return self

    def add_mc_data_instance(self, item: McDataInstance) -> "McGroupDataRefSetBuilder":
        """Add a single item to mc_data_instances list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mc_data_instances.append(item)
        return self

    def clear_mc_data_instances(self) -> "McGroupDataRefSetBuilder":
        """Clear all items from mc_data_instances list.

        Returns:
            self for method chaining
        """
        self._obj.mc_data_instances = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> McGroupDataRefSet:
        """Build and return the McGroupDataRefSet instance with validation."""
        self._validate_instance()
        pass
        return self._obj