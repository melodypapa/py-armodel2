"""IEEE1722TpAcfBus AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 657)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAcf.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus_part import (
    IEEE1722TpAcfBusPart,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IEEE1722TpAcfBus(Identifiable, ABC):
    """AUTOSAR IEEE1722TpAcfBus."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    acf_parts: list[IEEE1722TpAcfBusPart]
    bus_id: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "ACF-PARTS": ("_POLYMORPHIC_LIST", "acf_parts", ["IEEE1722TpAcfCanPart", "IEEE1722TpAcfLinPart"]),
        "BUS-ID": lambda obj, elem: setattr(obj, "bus_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfBus."""
        super().__init__()
        self.acf_parts: list[IEEE1722TpAcfBusPart] = []
        self.bus_id: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize IEEE1722TpAcfBus to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IEEE1722TpAcfBus, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize acf_parts (list to container "ACF-PARTS")
        if self.acf_parts:
            wrapper = ET.Element("ACF-PARTS")
            for item in self.acf_parts:
                serialized = SerializationHelper.serialize_item(item, "IEEE1722TpAcfBusPart")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize bus_id
        if self.bus_id is not None:
            serialized = SerializationHelper.serialize_item(self.bus_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BUS-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAcfBus":
        """Deserialize XML element to IEEE1722TpAcfBus object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpAcfBus object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IEEE1722TpAcfBus, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ACF-PARTS":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "I-E-E-E1722-TP-ACF-CAN-PART":
                        obj.acf_parts.append(SerializationHelper.deserialize_by_tag(item_elem, "IEEE1722TpAcfCanPart"))
                    elif concrete_tag == "I-E-E-E1722-TP-ACF-LIN-PART":
                        obj.acf_parts.append(SerializationHelper.deserialize_by_tag(item_elem, "IEEE1722TpAcfLinPart"))
            elif tag == "BUS-ID":
                setattr(obj, "bus_id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class IEEE1722TpAcfBusBuilder(IdentifiableBuilder):
    """Builder for IEEE1722TpAcfBus with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IEEE1722TpAcfBus = IEEE1722TpAcfBus()


    def with_acf_parts(self, items: list[IEEE1722TpAcfBusPart]) -> "IEEE1722TpAcfBusBuilder":
        """Set acf_parts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.acf_parts = list(items) if items else []
        return self

    def with_bus_id(self, value: Optional[PositiveInteger]) -> "IEEE1722TpAcfBusBuilder":
        """Set bus_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'bus_id' is required and cannot be None")
        self._obj.bus_id = value
        return self


    def add_acf_part(self, item: IEEE1722TpAcfBusPart) -> "IEEE1722TpAcfBusBuilder":
        """Add a single item to acf_parts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.acf_parts.append(item)
        return self

    def clear_acf_parts(self) -> "IEEE1722TpAcfBusBuilder":
        """Clear all items from acf_parts list.

        Returns:
            self for method chaining
        """
        self._obj.acf_parts = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "acfPart",
        "busId",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> IEEE1722TpAcfBus:
        """Build and return the IEEE1722TpAcfBus instance (abstract)."""
        raise NotImplementedError