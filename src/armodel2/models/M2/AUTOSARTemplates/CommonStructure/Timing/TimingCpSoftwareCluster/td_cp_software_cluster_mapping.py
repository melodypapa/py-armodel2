"""TDCpSoftwareClusterMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 157)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingCpSoftwareCluster.classes.json"""

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
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description import (
    TimingDescription,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TDCpSoftwareClusterMapping(Identifiable):
    """AUTOSAR TDCpSoftwareClusterMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "T-D-CP-SOFTWARE-CLUSTER-MAPPING"


    provider_ref: Optional[ARRef]
    requestor_refs: list[ARRef]
    timing_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "PROVIDER-REF": lambda obj, elem: setattr(obj, "provider_ref", ARRef.deserialize(elem)),
        "REQUESTORS": lambda obj, elem: obj.requestor_refs.append(ARRef.deserialize(elem)),
        "TIMING-REF": lambda obj, elem: setattr(obj, "timing_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize TDCpSoftwareClusterMapping."""
        super().__init__()
        self.provider_ref: Optional[ARRef] = None
        self.requestor_refs: list[ARRef] = []
        self.timing_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize TDCpSoftwareClusterMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDCpSoftwareClusterMapping, self).serialize()

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

        # Serialize requestor_refs (list to container "REQUESTOR-REFS")
        if self.requestor_refs:
            wrapper = ET.Element("REQUESTOR-REFS")
            for item in self.requestor_refs:
                serialized = SerializationHelper.serialize_item(item, "CpSoftwareCluster")
                if serialized is not None:
                    child_elem = ET.Element("REQUESTOR-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize timing_ref
        if self.timing_ref is not None:
            serialized = SerializationHelper.serialize_item(self.timing_ref, "TimingDescription")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMING-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDCpSoftwareClusterMapping":
        """Deserialize XML element to TDCpSoftwareClusterMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDCpSoftwareClusterMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDCpSoftwareClusterMapping, cls).deserialize(element)

        # Parse provider_ref
        child = SerializationHelper.find_child_element(element, "PROVIDER-REF")
        if child is not None:
            provider_ref_value = ARRef.deserialize(child)
            obj.provider_ref = provider_ref_value

        # Parse requestor_refs (list from container "REQUESTOR-REFS")
        obj.requestor_refs = []
        container = SerializationHelper.find_child_element(element, "REQUESTOR-REFS")
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
                    obj.requestor_refs.append(child_value)

        # Parse timing_ref
        child = SerializationHelper.find_child_element(element, "TIMING-REF")
        if child is not None:
            timing_ref_value = ARRef.deserialize(child)
            obj.timing_ref = timing_ref_value

        return obj



class TDCpSoftwareClusterMappingBuilder(IdentifiableBuilder):
    """Builder for TDCpSoftwareClusterMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TDCpSoftwareClusterMapping = TDCpSoftwareClusterMapping()


    def with_provider(self, value: Optional[CpSoftwareCluster]) -> "TDCpSoftwareClusterMappingBuilder":
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

    def with_requestors(self, items: list[CpSoftwareCluster]) -> "TDCpSoftwareClusterMappingBuilder":
        """Set requestors list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.requestors = list(items) if items else []
        return self

    def with_timing(self, value: Optional[TimingDescription]) -> "TDCpSoftwareClusterMappingBuilder":
        """Set timing attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timing = value
        return self


    def add_requestor(self, item: CpSoftwareCluster) -> "TDCpSoftwareClusterMappingBuilder":
        """Add a single item to requestors list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.requestors.append(item)
        return self

    def clear_requestors(self) -> "TDCpSoftwareClusterMappingBuilder":
        """Clear all items from requestors list.

        Returns:
            self for method chaining
        """
        self._obj.requestors = []
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


    def build(self) -> TDCpSoftwareClusterMapping:
        """Build and return the TDCpSoftwareClusterMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj