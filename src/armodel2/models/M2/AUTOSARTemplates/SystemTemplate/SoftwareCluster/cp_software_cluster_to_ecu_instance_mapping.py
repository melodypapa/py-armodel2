"""CpSoftwareClusterToEcuInstanceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 283)

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
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CpSoftwareClusterToEcuInstanceMapping(Identifiable):
    """AUTOSAR CpSoftwareClusterToEcuInstanceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CP-SOFTWARE-CLUSTER-TO-ECU-INSTANCE-MAPPING"


    ecu_instance_ref: Optional[ARRef]
    machine_id: Optional[PositiveInteger]
    sw_cluster_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "ECU-INSTANCE-REF": lambda obj, elem: setattr(obj, "ecu_instance_ref", ARRef.deserialize(elem)),
        "MACHINE-ID": lambda obj, elem: setattr(obj, "machine_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SW-CLUSTERS": lambda obj, elem: obj.sw_cluster_refs.append(ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize CpSoftwareClusterToEcuInstanceMapping."""
        super().__init__()
        self.ecu_instance_ref: Optional[ARRef] = None
        self.machine_id: Optional[PositiveInteger] = None
        self.sw_cluster_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize CpSoftwareClusterToEcuInstanceMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CpSoftwareClusterToEcuInstanceMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ecu_instance_ref
        if self.ecu_instance_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ecu_instance_ref, "EcuInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize machine_id
        if self.machine_id is not None:
            serialized = SerializationHelper.serialize_item(self.machine_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MACHINE-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_cluster_refs (list to container "SW-CLUSTER-REFS")
        if self.sw_cluster_refs:
            wrapper = ET.Element("SW-CLUSTER-REFS")
            for item in self.sw_cluster_refs:
                serialized = SerializationHelper.serialize_item(item, "CpSoftwareCluster")
                if serialized is not None:
                    child_elem = ET.Element("SW-CLUSTER-REF")
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
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterToEcuInstanceMapping":
        """Deserialize XML element to CpSoftwareClusterToEcuInstanceMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSoftwareClusterToEcuInstanceMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CpSoftwareClusterToEcuInstanceMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "ECU-INSTANCE-REF":
                setattr(obj, "ecu_instance_ref", ARRef.deserialize(child))
            elif tag == "MACHINE-ID":
                setattr(obj, "machine_id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SW-CLUSTERS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.sw_cluster_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "CpSoftwareCluster"))

        return obj



class CpSoftwareClusterToEcuInstanceMappingBuilder(IdentifiableBuilder):
    """Builder for CpSoftwareClusterToEcuInstanceMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CpSoftwareClusterToEcuInstanceMapping = CpSoftwareClusterToEcuInstanceMapping()


    def with_ecu_instance(self, value: Optional[EcuInstance]) -> "CpSoftwareClusterToEcuInstanceMappingBuilder":
        """Set ecu_instance attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ecu_instance = value
        return self

    def with_machine_id(self, value: Optional[PositiveInteger]) -> "CpSoftwareClusterToEcuInstanceMappingBuilder":
        """Set machine_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.machine_id = value
        return self

    def with_sw_clusters(self, items: list[CpSoftwareCluster]) -> "CpSoftwareClusterToEcuInstanceMappingBuilder":
        """Set sw_clusters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sw_clusters = list(items) if items else []
        return self


    def add_sw_cluster(self, item: CpSoftwareCluster) -> "CpSoftwareClusterToEcuInstanceMappingBuilder":
        """Add a single item to sw_clusters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sw_clusters.append(item)
        return self

    def clear_sw_clusters(self) -> "CpSoftwareClusterToEcuInstanceMappingBuilder":
        """Clear all items from sw_clusters list.

        Returns:
            self for method chaining
        """
        self._obj.sw_clusters = []
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


    def build(self) -> CpSoftwareClusterToEcuInstanceMapping:
        """Build and return the CpSoftwareClusterToEcuInstanceMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj