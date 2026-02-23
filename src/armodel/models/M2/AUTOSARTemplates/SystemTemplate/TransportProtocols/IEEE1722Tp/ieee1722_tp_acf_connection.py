"""IEEE1722TpAcfConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 656)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_connection import (
    IEEE1722TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_connection import IEEE1722TpConnectionBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus import (
    IEEE1722TpAcfBus,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class IEEE1722TpAcfConnection(IEEE1722TpConnection):
    """AUTOSAR IEEE1722TpAcfConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    acf_transporteds: list[IEEE1722TpAcfBus]
    collection: Optional[TimeValue]
    mixed_bus_type: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfConnection."""
        super().__init__()
        self.acf_transporteds: list[IEEE1722TpAcfBus] = []
        self.collection: Optional[TimeValue] = None
        self.mixed_bus_type: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize IEEE1722TpAcfConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IEEE1722TpAcfConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize acf_transporteds (list to container "ACF-TRANSPORTEDS")
        if self.acf_transporteds:
            wrapper = ET.Element("ACF-TRANSPORTEDS")
            for item in self.acf_transporteds:
                serialized = SerializationHelper.serialize_item(item, "IEEE1722TpAcfBus")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize collection
        if self.collection is not None:
            serialized = SerializationHelper.serialize_item(self.collection, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COLLECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mixed_bus_type
        if self.mixed_bus_type is not None:
            serialized = SerializationHelper.serialize_item(self.mixed_bus_type, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIXED-BUS-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAcfConnection":
        """Deserialize XML element to IEEE1722TpAcfConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpAcfConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IEEE1722TpAcfConnection, cls).deserialize(element)

        # Parse acf_transporteds (list from container "ACF-TRANSPORTEDS")
        obj.acf_transporteds = []
        container = SerializationHelper.find_child_element(element, "ACF-TRANSPORTEDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.acf_transporteds.append(child_value)

        # Parse collection
        child = SerializationHelper.find_child_element(element, "COLLECTION")
        if child is not None:
            collection_value = child.text
            obj.collection = collection_value

        # Parse mixed_bus_type
        child = SerializationHelper.find_child_element(element, "MIXED-BUS-TYPE")
        if child is not None:
            mixed_bus_type_value = child.text
            obj.mixed_bus_type = mixed_bus_type_value

        return obj



class IEEE1722TpAcfConnectionBuilder(IEEE1722TpConnectionBuilder):
    """Builder for IEEE1722TpAcfConnection with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IEEE1722TpAcfConnection = IEEE1722TpAcfConnection()


    def with_acf_transporteds(self, items: list[IEEE1722TpAcfBus]) -> "IEEE1722TpAcfConnectionBuilder":
        """Set acf_transporteds list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.acf_transporteds = list(items) if items else []
        return self

    def with_collection(self, value: Optional[TimeValue]) -> "IEEE1722TpAcfConnectionBuilder":
        """Set collection attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.collection = value
        return self

    def with_mixed_bus_type(self, value: Optional[Boolean]) -> "IEEE1722TpAcfConnectionBuilder":
        """Set mixed_bus_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mixed_bus_type = value
        return self


    def add_acf_transported(self, item: IEEE1722TpAcfBus) -> "IEEE1722TpAcfConnectionBuilder":
        """Add a single item to acf_transporteds list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.acf_transporteds.append(item)
        return self

    def clear_acf_transporteds(self) -> "IEEE1722TpAcfConnectionBuilder":
        """Clear all items from acf_transporteds list.

        Returns:
            self for method chaining
        """
        self._obj.acf_transporteds = []
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


    def build(self) -> IEEE1722TpAcfConnection:
        """Build and return the IEEE1722TpAcfConnection instance with validation."""
        self._validate_instance()
        pass
        return self._obj