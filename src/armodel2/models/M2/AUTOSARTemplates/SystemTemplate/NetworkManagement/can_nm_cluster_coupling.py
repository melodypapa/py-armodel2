"""CanNmClusterCoupling AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 684)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster_coupling import (
    NmClusterCoupling,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster_coupling import NmClusterCouplingBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.can_nm_cluster import (
    CanNmCluster,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CanNmClusterCoupling(NmClusterCoupling):
    """AUTOSAR CanNmClusterCoupling."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CAN-NM-CLUSTER-COUPLING"


    coupled_cluster_refs: list[ARRef]
    nm_busload_reduction: Optional[Any]
    nm_immediate: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "COUPLED-CLUSTER-REFS": lambda obj, elem: obj.coupled_cluster_refs.append(ARRef.deserialize(elem)),
        "NM-BUSLOAD-REDUCTION": lambda obj, elem: setattr(obj, "nm_busload_reduction", SerializationHelper.deserialize_by_tag(elem, "any (BooleanEnabled)")),
        "NM-IMMEDIATE": lambda obj, elem: setattr(obj, "nm_immediate", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize CanNmClusterCoupling."""
        super().__init__()
        self.coupled_cluster_refs: list[ARRef] = []
        self.nm_busload_reduction: Optional[Any] = None
        self.nm_immediate: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize CanNmClusterCoupling to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CanNmClusterCoupling, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize coupled_cluster_refs (list to container "COUPLED-CLUSTER-REFS")
        if self.coupled_cluster_refs:
            wrapper = ET.Element("COUPLED-CLUSTER-REFS")
            for item in self.coupled_cluster_refs:
                serialized = SerializationHelper.serialize_item(item, "CanNmCluster")
                if serialized is not None:
                    child_elem = ET.Element("COUPLED-CLUSTER-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize nm_busload_reduction
        if self.nm_busload_reduction is not None:
            serialized = SerializationHelper.serialize_item(self.nm_busload_reduction, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-BUSLOAD-REDUCTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_immediate
        if self.nm_immediate is not None:
            serialized = SerializationHelper.serialize_item(self.nm_immediate, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-IMMEDIATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanNmClusterCoupling":
        """Deserialize XML element to CanNmClusterCoupling object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanNmClusterCoupling object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CanNmClusterCoupling, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "COUPLED-CLUSTER-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.coupled_cluster_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "CanNmCluster"))
            elif tag == "NM-BUSLOAD-REDUCTION":
                setattr(obj, "nm_busload_reduction", SerializationHelper.deserialize_by_tag(child, "any (BooleanEnabled)"))
            elif tag == "NM-IMMEDIATE":
                setattr(obj, "nm_immediate", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class CanNmClusterCouplingBuilder(NmClusterCouplingBuilder):
    """Builder for CanNmClusterCoupling with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CanNmClusterCoupling = CanNmClusterCoupling()


    def with_coupled_clusters(self, items: list[CanNmCluster]) -> "CanNmClusterCouplingBuilder":
        """Set coupled_clusters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.coupled_clusters = list(items) if items else []
        return self

    def with_nm_busload_reduction(self, value: Optional[any (BooleanEnabled)]) -> "CanNmClusterCouplingBuilder":
        """Set nm_busload_reduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_busload_reduction = value
        return self

    def with_nm_immediate(self, value: Optional[Boolean]) -> "CanNmClusterCouplingBuilder":
        """Set nm_immediate attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_immediate = value
        return self


    def add_coupled_cluster(self, item: CanNmCluster) -> "CanNmClusterCouplingBuilder":
        """Add a single item to coupled_clusters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.coupled_clusters.append(item)
        return self

    def clear_coupled_clusters(self) -> "CanNmClusterCouplingBuilder":
        """Clear all items from coupled_clusters list.

        Returns:
            self for method chaining
        """
        self._obj.coupled_clusters = []
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


    def build(self) -> CanNmClusterCoupling:
        """Build and return the CanNmClusterCoupling instance with validation."""
        self._validate_instance()
        pass
        return self._obj