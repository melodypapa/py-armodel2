"""InfrastructureServices AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 469)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.do_ip_entity import (
    DoIpEntity,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.time_synchronization import (
    TimeSynchronization,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class InfrastructureServices(ARObject):
    """AUTOSAR InfrastructureServices."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "INFRASTRUCTURE-SERVICES"


    do_ip_entity: Optional[DoIpEntity]
    time: Optional[TimeSynchronization]
    _DESERIALIZE_DISPATCH = {
        "DO-IP-ENTITY": lambda obj, elem: setattr(obj, "do_ip_entity", DoIpEntity.deserialize(elem)),
        "TIME": lambda obj, elem: setattr(obj, "time", TimeSynchronization.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize InfrastructureServices."""
        super().__init__()
        self.do_ip_entity: Optional[DoIpEntity] = None
        self.time: Optional[TimeSynchronization] = None

    def serialize(self) -> ET.Element:
        """Serialize InfrastructureServices to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(InfrastructureServices, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize do_ip_entity
        if self.do_ip_entity is not None:
            serialized = SerializationHelper.serialize_item(self.do_ip_entity, "DoIpEntity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DO-IP-ENTITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time
        if self.time is not None:
            serialized = SerializationHelper.serialize_item(self.time, "TimeSynchronization")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InfrastructureServices":
        """Deserialize XML element to InfrastructureServices object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InfrastructureServices object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(InfrastructureServices, cls).deserialize(element)

        # Parse do_ip_entity
        child = SerializationHelper.find_child_element(element, "DO-IP-ENTITY")
        if child is not None:
            do_ip_entity_value = SerializationHelper.deserialize_by_tag(child, "DoIpEntity")
            obj.do_ip_entity = do_ip_entity_value

        # Parse time
        child = SerializationHelper.find_child_element(element, "TIME")
        if child is not None:
            time_value = SerializationHelper.deserialize_by_tag(child, "TimeSynchronization")
            obj.time = time_value

        return obj



class InfrastructureServicesBuilder(BuilderBase):
    """Builder for InfrastructureServices with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: InfrastructureServices = InfrastructureServices()


    def with_do_ip_entity(self, value: Optional[DoIpEntity]) -> "InfrastructureServicesBuilder":
        """Set do_ip_entity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.do_ip_entity = value
        return self

    def with_time(self, value: Optional[TimeSynchronization]) -> "InfrastructureServicesBuilder":
        """Set time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.time = value
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


    def build(self) -> InfrastructureServices:
        """Build and return the InfrastructureServices instance with validation."""
        self._validate_instance()
        pass
        return self._obj