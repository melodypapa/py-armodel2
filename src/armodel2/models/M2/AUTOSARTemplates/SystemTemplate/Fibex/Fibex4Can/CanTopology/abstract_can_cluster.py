"""AbstractCanCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 62)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cluster import (
    CommunicationCluster,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveUnlimitedInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.can_cluster_bus_off_recovery import (
    CanClusterBusOffRecovery,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AbstractCanCluster(CommunicationCluster, ABC):
    """AUTOSAR AbstractCanCluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    bus_off_recovery: Optional[CanClusterBusOffRecovery]
    can_fd_baudrate: Optional[PositiveUnlimitedInteger]
    can_xl_baudrate: Optional[PositiveUnlimitedInteger]
    _DESERIALIZE_DISPATCH = {
        "BUS-OFF-RECOVERY": lambda obj, elem: setattr(obj, "bus_off_recovery", SerializationHelper.deserialize_by_tag(elem, "CanClusterBusOffRecovery")),
        "CAN-FD-BAUDRATE": lambda obj, elem: setattr(obj, "can_fd_baudrate", SerializationHelper.deserialize_by_tag(elem, "PositiveUnlimitedInteger")),
        "CAN-XL-BAUDRATE": lambda obj, elem: setattr(obj, "can_xl_baudrate", SerializationHelper.deserialize_by_tag(elem, "PositiveUnlimitedInteger")),
    }


    def __init__(self) -> None:
        """Initialize AbstractCanCluster."""
        super().__init__()
        self.bus_off_recovery: Optional[CanClusterBusOffRecovery] = None
        self.can_fd_baudrate: Optional[PositiveUnlimitedInteger] = None
        self.can_xl_baudrate: Optional[PositiveUnlimitedInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize AbstractCanCluster to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AbstractCanCluster, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bus_off_recovery
        if self.bus_off_recovery is not None:
            serialized = SerializationHelper.serialize_item(self.bus_off_recovery, "CanClusterBusOffRecovery")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BUS-OFF-RECOVERY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize can_fd_baudrate
        if self.can_fd_baudrate is not None:
            serialized = SerializationHelper.serialize_item(self.can_fd_baudrate, "PositiveUnlimitedInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAN-FD-BAUDRATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize can_xl_baudrate
        if self.can_xl_baudrate is not None:
            serialized = SerializationHelper.serialize_item(self.can_xl_baudrate, "PositiveUnlimitedInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAN-XL-BAUDRATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractCanCluster":
        """Deserialize XML element to AbstractCanCluster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractCanCluster object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AbstractCanCluster, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BUS-OFF-RECOVERY":
                setattr(obj, "bus_off_recovery", SerializationHelper.deserialize_by_tag(child, "CanClusterBusOffRecovery"))
            elif tag == "CAN-FD-BAUDRATE":
                setattr(obj, "can_fd_baudrate", SerializationHelper.deserialize_by_tag(child, "PositiveUnlimitedInteger"))
            elif tag == "CAN-XL-BAUDRATE":
                setattr(obj, "can_xl_baudrate", SerializationHelper.deserialize_by_tag(child, "PositiveUnlimitedInteger"))

        return obj



class AbstractCanClusterBuilder(BuilderBase, ABC):
    """Builder for AbstractCanCluster with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AbstractCanCluster = AbstractCanCluster()


    def with_bus_off_recovery(self, value: Optional[CanClusterBusOffRecovery]) -> "AbstractCanClusterBuilder":
        """Set bus_off_recovery attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bus_off_recovery = value
        return self

    def with_can_fd_baudrate(self, value: Optional[PositiveUnlimitedInteger]) -> "AbstractCanClusterBuilder":
        """Set can_fd_baudrate attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.can_fd_baudrate = value
        return self

    def with_can_xl_baudrate(self, value: Optional[PositiveUnlimitedInteger]) -> "AbstractCanClusterBuilder":
        """Set can_xl_baudrate attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.can_xl_baudrate = value
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


    @abstractmethod
    def build(self) -> AbstractCanCluster:
        """Build and return the AbstractCanCluster instance (abstract)."""
        raise NotImplementedError