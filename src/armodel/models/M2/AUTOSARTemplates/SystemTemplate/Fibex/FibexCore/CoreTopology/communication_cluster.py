"""CommunicationCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 107)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 57)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveUnlimitedInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from abc import ABC, abstractmethod
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class CommunicationCluster(ARElement, ABC):
    """AUTOSAR CommunicationCluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    baudrate: Optional[PositiveUnlimitedInteger]
    physical_channels: list[PhysicalChannel]
    protocol_name: Optional[String]
    protocol_version: Optional[String]
    def __init__(self) -> None:
        """Initialize CommunicationCluster."""
        super().__init__()
        self.baudrate: Optional[PositiveUnlimitedInteger] = None
        self.physical_channels: list[PhysicalChannel] = []
        self.protocol_name: Optional[String] = None
        self.protocol_version: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize CommunicationCluster to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CommunicationCluster, self).serialize()

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

        # Serialize baudrate
        if self.baudrate is not None:
            serialized = SerializationHelper.serialize_item(self.baudrate, "PositiveUnlimitedInteger")
            if serialized is not None:
                wrapped = ET.Element("BAUDRATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize physical_channels (list from container "PHYSICAL-CHANNELS")
        if self.physical_channels:
            container = ET.Element("PHYSICAL-CHANNELS")
            for item in self.physical_channels:
                # Complex object type
                if hasattr(item, "serialize"):
                    container.append(item.serialize())
            inner_elem.append(container)

        # Serialize protocol_name
        if self.protocol_name is not None:
            serialized = SerializationHelper.serialize_item(self.protocol_name, "String")
            if serialized is not None:
                wrapped = ET.Element("PROTOCOL-NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize protocol_version
        if self.protocol_version is not None:
            serialized = SerializationHelper.serialize_item(self.protocol_version, "String")
            if serialized is not None:
                wrapped = ET.Element("PROTOCOL-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "CommunicationCluster")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CommunicationCluster":
        """Deserialize XML element to CommunicationCluster object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CommunicationCluster object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CommunicationCluster, cls).deserialize(element)

        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "CommunicationCluster")
        if inner_elem is None:
            # No wrapper structure found, return object with default values
            return obj

        # Parse baudrate
        child = SerializationHelper.find_child_element(inner_elem, "BAUDRATE")
        if child is not None:
            baudrate_value = child.text
            obj.baudrate = baudrate_value

        # Parse physical_channels (list from container "PHYSICAL-CHANNELS")
        obj.physical_channels = []
        container = SerializationHelper.find_child_element(inner_elem, "PHYSICAL-CHANNELS")
        if container is not None:
            for child in container:
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.physical_channels.append(child_value)

        # Parse protocol_name
        child = SerializationHelper.find_child_element(inner_elem, "PROTOCOL-NAME")
        if child is not None:
            protocol_name_value = child.text
            obj.protocol_name = protocol_name_value

        # Parse protocol_version
        child = SerializationHelper.find_child_element(inner_elem, "PROTOCOL-VERSION")
        if child is not None:
            protocol_version_value = child.text
            obj.protocol_version = protocol_version_value

        return obj



class CommunicationClusterBuilder(BuilderBase, ABC):
    """Builder for CommunicationCluster with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CommunicationCluster = CommunicationCluster()


    def with_baudrate(self, value: Optional[PositiveUnlimitedInteger]) -> "CommunicationClusterBuilder":
        """Set baudrate attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.baudrate = value
        return self

    def with_physical_channels(self, items: list[PhysicalChannel]) -> "CommunicationClusterBuilder":
        """Set physical_channels list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.physical_channels = list(items) if items else []
        return self

    def with_protocol_name(self, value: Optional[String]) -> "CommunicationClusterBuilder":
        """Set protocol_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.protocol_name = value
        return self

    def with_protocol_version(self, value: Optional[String]) -> "CommunicationClusterBuilder":
        """Set protocol_version attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.protocol_version = value
        return self


    def add_physical_channel(self, item: PhysicalChannel) -> "CommunicationClusterBuilder":
        """Add a single item to physical_channels list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.physical_channels.append(item)
        return self

    def clear_physical_channels(self) -> "CommunicationClusterBuilder":
        """Clear all items from physical_channels list.

        Returns:
            self for method chaining
        """
        self._obj.physical_channels = []
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


    @abstractmethod
    def build(self) -> CommunicationCluster:
        """Build and return the CommunicationCluster instance (abstract)."""
        raise NotImplementedError