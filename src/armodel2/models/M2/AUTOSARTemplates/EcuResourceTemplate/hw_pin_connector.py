"""HwPinConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 22)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import DescribableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin import (
    HwPin,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class HwPinConnector(Describable):
    """AUTOSAR HwPinConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "HW-PIN-CONNECTOR"


    hw_pin_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "HW-PIN-REFS": lambda obj, elem: [obj.hw_pin_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize HwPinConnector."""
        super().__init__()
        self.hw_pin_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize HwPinConnector to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(HwPinConnector, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize hw_pin_refs (list to container "HW-PIN-REFS")
        if self.hw_pin_refs:
            wrapper = ET.Element("HW-PIN-REFS")
            for item in self.hw_pin_refs:
                serialized = SerializationHelper.serialize_item(item, "HwPin")
                if serialized is not None:
                    child_elem = ET.Element("HW-PIN-REF")
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
    def deserialize(cls, element: ET.Element) -> "HwPinConnector":
        """Deserialize XML element to HwPinConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HwPinConnector object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(HwPinConnector, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "HW-PIN-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.hw_pin_refs.append(ARRef.deserialize(item_elem))

        return obj



class HwPinConnectorBuilder(DescribableBuilder):
    """Builder for HwPinConnector with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: HwPinConnector = HwPinConnector()


    def with_hw_pins(self, items: list[HwPin]) -> "HwPinConnectorBuilder":
        """Set hw_pins list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.hw_pins = list(items) if items else []
        return self


    def add_hw_pin(self, item: HwPin) -> "HwPinConnectorBuilder":
        """Add a single item to hw_pins list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.hw_pins.append(item)
        return self

    def clear_hw_pins(self) -> "HwPinConnectorBuilder":
        """Clear all items from hw_pins list.

        Returns:
            self for method chaining
        """
        self._obj.hw_pins = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "hwPin",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> HwPinConnector:
        """Build and return the HwPinConnector instance with validation."""
        self._validate_instance()
        return self._obj