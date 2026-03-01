"""ApplicationPartitionToEcuPartitionMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 201)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

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
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.ecu_partition import (
    EcuPartition,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ApplicationPartitionToEcuPartitionMapping(Identifiable):
    """AUTOSAR ApplicationPartitionToEcuPartitionMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPING"


    application_refs: list[ARRef]
    ecu_partition_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "APPLICATIONS": lambda obj, elem: obj.application_refs.append(ARRef.deserialize(elem)),
        "ECU-PARTITION-REF": lambda obj, elem: setattr(obj, "ecu_partition_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ApplicationPartitionToEcuPartitionMapping."""
        super().__init__()
        self.application_refs: list[ARRef] = []
        self.ecu_partition_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ApplicationPartitionToEcuPartitionMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ApplicationPartitionToEcuPartitionMapping, self).serialize()

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

        # Serialize ecu_partition_ref
        if self.ecu_partition_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ecu_partition_ref, "EcuPartition")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-PARTITION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationPartitionToEcuPartitionMapping":
        """Deserialize XML element to ApplicationPartitionToEcuPartitionMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationPartitionToEcuPartitionMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ApplicationPartitionToEcuPartitionMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "APPLICATIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.application_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "ApplicationPartition"))
            elif tag == "ECU-PARTITION-REF":
                setattr(obj, "ecu_partition_ref", ARRef.deserialize(child))

        return obj



class ApplicationPartitionToEcuPartitionMappingBuilder(IdentifiableBuilder):
    """Builder for ApplicationPartitionToEcuPartitionMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ApplicationPartitionToEcuPartitionMapping = ApplicationPartitionToEcuPartitionMapping()


    def with_applications(self, items: list[ApplicationPartition]) -> "ApplicationPartitionToEcuPartitionMappingBuilder":
        """Set applications list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.applications = list(items) if items else []
        return self

    def with_ecu_partition(self, value: Optional[EcuPartition]) -> "ApplicationPartitionToEcuPartitionMappingBuilder":
        """Set ecu_partition attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ecu_partition = value
        return self


    def add_application(self, item: ApplicationPartition) -> "ApplicationPartitionToEcuPartitionMappingBuilder":
        """Add a single item to applications list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.applications.append(item)
        return self

    def clear_applications(self) -> "ApplicationPartitionToEcuPartitionMappingBuilder":
        """Clear all items from applications list.

        Returns:
            self for method chaining
        """
        self._obj.applications = []
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


    def build(self) -> ApplicationPartitionToEcuPartitionMapping:
        """Build and return the ApplicationPartitionToEcuPartitionMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj