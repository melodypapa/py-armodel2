"""CanCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 62)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.abstract_can_cluster import (
    AbstractCanCluster,
)
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


@atp_variant()

class CanCluster(AbstractCanCluster):
    """AUTOSAR CanCluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize CanCluster."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize CanCluster to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CanCluster, self).serialize()

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

        # Serialize bus_off_recovery
        if self.bus_off_recovery is not None:
            serialized = SerializationHelper.serialize_item(self.bus_off_recovery, "CanClusterBusOffRecovery")
            if serialized is not None:
                wrapped = ET.Element("BUS-OFF-RECOVERY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize can_fd_baudrate
        if self.can_fd_baudrate is not None:
            serialized = SerializationHelper.serialize_item(self.can_fd_baudrate, "PositiveUnlimitedInteger")
            if serialized is not None:
                wrapped = ET.Element("CAN-FD-BAUDRATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize can_xl_baudrate
        if self.can_xl_baudrate is not None:
            serialized = SerializationHelper.serialize_item(self.can_xl_baudrate, "PositiveUnlimitedInteger")
            if serialized is not None:
                wrapped = ET.Element("CAN-XL-BAUDRATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

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

        # Serialize speed
        if self.speed is not None:
            serialized = SerializationHelper.serialize_item(self.speed, "Integer")
            if serialized is not None:
                wrapped = ET.Element("SPEED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "CanCluster")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanCluster":
        """Deserialize XML element to CanCluster object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanCluster object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CanCluster, cls).deserialize(element)

        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "CanCluster")
        if inner_elem is None:
            # No wrapper structure found, return object with default values
            return obj

        # Parse bus_off_recovery
        child = SerializationHelper.find_child_element(inner_elem, "BUS-OFF-RECOVERY")
        if child is not None:
            bus_off_recovery_value = SerializationHelper.deserialize_by_tag(child, "CanClusterBusOffRecovery")
            obj.bus_off_recovery = bus_off_recovery_value

        # Parse can_fd_baudrate
        child = SerializationHelper.find_child_element(inner_elem, "CAN-FD-BAUDRATE")
        if child is not None:
            can_fd_baudrate_value = child.text
            obj.can_fd_baudrate = can_fd_baudrate_value

        # Parse can_xl_baudrate
        child = SerializationHelper.find_child_element(inner_elem, "CAN-XL-BAUDRATE")
        if child is not None:
            can_xl_baudrate_value = child.text
            obj.can_xl_baudrate = can_xl_baudrate_value

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

        # Parse speed
        child = SerializationHelper.find_child_element(inner_elem, "SPEED")
        if child is not None:
            speed_value = child.text
            obj.speed = speed_value

        return obj



class CanClusterBuilder(BuilderBase):
    """Builder for CanCluster with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CanCluster = CanCluster()





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


    def build(self) -> CanCluster:
        """Build and return the CanCluster instance with validation."""
        self._validate_instance()
        pass
        return self._obj