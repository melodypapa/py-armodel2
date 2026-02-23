"""IdsmProperties AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 63)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import (
    IdsCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import IdsCommonElementBuilder
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.idsm_rate_limitation import (
    IdsmRateLimitation,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.idsm_traffic_limitation import (
    IdsmTrafficLimitation,
)


class IdsmProperties(IdsCommonElement):
    """AUTOSAR IdsmProperties."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    rate_limitations: list[IdsmRateLimitation]
    traffic_limitations: list[IdsmTrafficLimitation]
    def __init__(self) -> None:
        """Initialize IdsmProperties."""
        super().__init__()
        self.rate_limitations: list[IdsmRateLimitation] = []
        self.traffic_limitations: list[IdsmTrafficLimitation] = []

    def serialize(self) -> ET.Element:
        """Serialize IdsmProperties to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IdsmProperties, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize rate_limitations (list to container "RATE-LIMITATIONS")
        if self.rate_limitations:
            wrapper = ET.Element("RATE-LIMITATIONS")
            for item in self.rate_limitations:
                serialized = SerializationHelper.serialize_item(item, "IdsmRateLimitation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize traffic_limitations (list to container "TRAFFIC-LIMITATIONS")
        if self.traffic_limitations:
            wrapper = ET.Element("TRAFFIC-LIMITATIONS")
            for item in self.traffic_limitations:
                serialized = SerializationHelper.serialize_item(item, "IdsmTrafficLimitation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IdsmProperties":
        """Deserialize XML element to IdsmProperties object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IdsmProperties object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IdsmProperties, cls).deserialize(element)

        # Parse rate_limitations (list from container "RATE-LIMITATIONS")
        obj.rate_limitations = []
        container = SerializationHelper.find_child_element(element, "RATE-LIMITATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rate_limitations.append(child_value)

        # Parse traffic_limitations (list from container "TRAFFIC-LIMITATIONS")
        obj.traffic_limitations = []
        container = SerializationHelper.find_child_element(element, "TRAFFIC-LIMITATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.traffic_limitations.append(child_value)

        return obj



class IdsmPropertiesBuilder(IdsCommonElementBuilder):
    """Builder for IdsmProperties with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IdsmProperties = IdsmProperties()


    def with_rate_limitations(self, items: list[IdsmRateLimitation]) -> "IdsmPropertiesBuilder":
        """Set rate_limitations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.rate_limitations = list(items) if items else []
        return self

    def with_traffic_limitations(self, items: list[IdsmTrafficLimitation]) -> "IdsmPropertiesBuilder":
        """Set traffic_limitations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.traffic_limitations = list(items) if items else []
        return self


    def add_rate_limitation(self, item: IdsmRateLimitation) -> "IdsmPropertiesBuilder":
        """Add a single item to rate_limitations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.rate_limitations.append(item)
        return self

    def clear_rate_limitations(self) -> "IdsmPropertiesBuilder":
        """Clear all items from rate_limitations list.

        Returns:
            self for method chaining
        """
        self._obj.rate_limitations = []
        return self

    def add_traffic_limitation(self, item: IdsmTrafficLimitation) -> "IdsmPropertiesBuilder":
        """Add a single item to traffic_limitations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.traffic_limitations.append(item)
        return self

    def clear_traffic_limitations(self) -> "IdsmPropertiesBuilder":
        """Clear all items from traffic_limitations list.

        Returns:
            self for method chaining
        """
        self._obj.traffic_limitations = []
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


    def build(self) -> IdsmProperties:
        """Build and return the IdsmProperties instance with validation."""
        self._validate_instance()
        pass
        return self._obj