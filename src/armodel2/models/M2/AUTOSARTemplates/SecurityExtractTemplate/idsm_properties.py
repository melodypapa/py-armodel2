"""IdsmProperties AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 63)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import (
    IdsCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import IdsCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.idsm_rate_limitation import (
    IdsmRateLimitation,
)
from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.idsm_traffic_limitation import (
    IdsmTrafficLimitation,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IdsmProperties(IdsCommonElement):
    """AUTOSAR IdsmProperties."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "IDSM-PROPERTIES"


    rate_limitations: list[IdsmRateLimitation]
    traffic_limitations: list[IdsmTrafficLimitation]
    _DESERIALIZE_DISPATCH = {
        "RATE-LIMITATIONS": lambda obj, elem: obj.rate_limitations.append(SerializationHelper.deserialize_by_tag(elem, "IdsmRateLimitation")),
        "TRAFFIC-LIMITATIONS": lambda obj, elem: obj.traffic_limitations.append(SerializationHelper.deserialize_by_tag(elem, "IdsmTrafficLimitation")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "RATE-LIMITATIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.rate_limitations.append(SerializationHelper.deserialize_by_tag(item_elem, "IdsmRateLimitation"))
            elif tag == "TRAFFIC-LIMITATIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.traffic_limitations.append(SerializationHelper.deserialize_by_tag(item_elem, "IdsmTrafficLimitation"))

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


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "rateLimitation",
        "trafficLimitation",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> IdsmProperties:
        """Build and return the IdsmProperties instance with validation."""
        self._validate_instance()
        return self._obj