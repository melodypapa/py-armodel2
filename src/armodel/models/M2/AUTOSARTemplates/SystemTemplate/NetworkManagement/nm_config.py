"""NmConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 672)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster import (
    NmCluster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster_coupling import (
    NmClusterCoupling,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_ecu import (
    NmEcu,
)


class NmConfig(FibexElement):
    """AUTOSAR NmConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    nm_clusters: list[NmCluster]
    nm_cluster_couplings: list[NmClusterCoupling]
    nm_if_ecus: list[NmEcu]
    def __init__(self) -> None:
        """Initialize NmConfig."""
        super().__init__()
        self.nm_clusters: list[NmCluster] = []
        self.nm_cluster_couplings: list[NmClusterCoupling] = []
        self.nm_if_ecus: list[NmEcu] = []

    def serialize(self) -> ET.Element:
        """Serialize NmConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NmConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize nm_clusters (list to container "NM-CLUSTERS")
        if self.nm_clusters:
            wrapper = ET.Element("NM-CLUSTERS")
            for item in self.nm_clusters:
                serialized = SerializationHelper.serialize_item(item, "NmCluster")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize nm_cluster_couplings (list to container "NM-CLUSTER-COUPLINGS")
        if self.nm_cluster_couplings:
            wrapper = ET.Element("NM-CLUSTER-COUPLINGS")
            for item in self.nm_cluster_couplings:
                serialized = SerializationHelper.serialize_item(item, "NmClusterCoupling")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize nm_if_ecus (list to container "NM-IF-ECUS")
        if self.nm_if_ecus:
            wrapper = ET.Element("NM-IF-ECUS")
            for item in self.nm_if_ecus:
                serialized = SerializationHelper.serialize_item(item, "NmEcu")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NmConfig":
        """Deserialize XML element to NmConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NmConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NmConfig, cls).deserialize(element)

        # Parse nm_clusters (list from container "NM-CLUSTERS")
        obj.nm_clusters = []
        container = SerializationHelper.find_child_element(element, "NM-CLUSTERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.nm_clusters.append(child_value)

        # Parse nm_cluster_couplings (list from container "NM-CLUSTER-COUPLINGS")
        obj.nm_cluster_couplings = []
        container = SerializationHelper.find_child_element(element, "NM-CLUSTER-COUPLINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.nm_cluster_couplings.append(child_value)

        # Parse nm_if_ecus (list from container "NM-IF-ECUS")
        obj.nm_if_ecus = []
        container = SerializationHelper.find_child_element(element, "NM-IF-ECUS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.nm_if_ecus.append(child_value)

        return obj



class NmConfigBuilder:
    """Builder for NmConfig with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: NmConfig = NmConfig()


    def with_short_name(self, value: Identifier) -> "NmConfigBuilder":
        """Set short_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_name = value
        return self

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "NmConfigBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "NmConfigBuilder":
        """Set long_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.long_name = value
        return self

    def with_admin_data(self, value: Optional[AdminData]) -> "NmConfigBuilder":
        """Set admin_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.admin_data = value
        return self

    def with_annotations(self, items: list[Annotation]) -> "NmConfigBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "NmConfigBuilder":
        """Set desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_category(self, value: Optional[CategoryString]) -> "NmConfigBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "NmConfigBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.introduction = value
        return self

    def with_uuid(self, value: Optional[String]) -> "NmConfigBuilder":
        """Set uuid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uuid = value
        return self

    def with_nm_clusters(self, items: list[NmCluster]) -> "NmConfigBuilder":
        """Set nm_clusters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.nm_clusters = list(items) if items else []
        return self

    def with_nm_cluster_couplings(self, items: list[NmClusterCoupling]) -> "NmConfigBuilder":
        """Set nm_cluster_couplings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.nm_cluster_couplings = list(items) if items else []
        return self

    def with_nm_if_ecus(self, items: list[NmEcu]) -> "NmConfigBuilder":
        """Set nm_if_ecus list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.nm_if_ecus = list(items) if items else []
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "NmConfigBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "NmConfigBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "NmConfigBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "NmConfigBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_nm_cluster(self, item: NmCluster) -> "NmConfigBuilder":
        """Add a single item to nm_clusters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.nm_clusters.append(item)
        return self

    def clear_nm_clusters(self) -> "NmConfigBuilder":
        """Clear all items from nm_clusters list.

        Returns:
            self for method chaining
        """
        self._obj.nm_clusters = []
        return self

    def add_nm_cluster_coupling(self, item: NmClusterCoupling) -> "NmConfigBuilder":
        """Add a single item to nm_cluster_couplings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.nm_cluster_couplings.append(item)
        return self

    def clear_nm_cluster_couplings(self) -> "NmConfigBuilder":
        """Clear all items from nm_cluster_couplings list.

        Returns:
            self for method chaining
        """
        self._obj.nm_cluster_couplings = []
        return self

    def add_nm_if_ecu(self, item: NmEcu) -> "NmConfigBuilder":
        """Add a single item to nm_if_ecus list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.nm_if_ecus.append(item)
        return self

    def clear_nm_if_ecus(self) -> "NmConfigBuilder":
        """Clear all items from nm_if_ecus list.

        Returns:
            self for method chaining
        """
        self._obj.nm_if_ecus = []
        return self


    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")


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


    def build(self) -> NmConfig:
        """Build and return the NmConfig instance with validation."""
        self._validate_instance()
        pass
        return self._obj