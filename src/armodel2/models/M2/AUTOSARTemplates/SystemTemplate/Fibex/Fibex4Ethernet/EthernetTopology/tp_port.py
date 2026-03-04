"""TpPort AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 461)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TpPort(ARObject):
    """AUTOSAR TpPort."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TP-PORT"


    dynamically: Optional[Boolean]
    port_number: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "DYNAMICALLY": lambda obj, elem: setattr(obj, "dynamically", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "PORT-NUMBER": lambda obj, elem: setattr(obj, "port_number", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize TpPort."""
        super().__init__()
        self.dynamically: Optional[Boolean] = None
        self.port_number: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize TpPort to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TpPort, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dynamically
        if self.dynamically is not None:
            serialized = SerializationHelper.serialize_item(self.dynamically, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DYNAMICALLY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize port_number
        if self.port_number is not None:
            serialized = SerializationHelper.serialize_item(self.port_number, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PORT-NUMBER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TpPort":
        """Deserialize XML element to TpPort object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TpPort object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TpPort, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DYNAMICALLY":
                setattr(obj, "dynamically", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "PORT-NUMBER":
                setattr(obj, "port_number", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class TpPortBuilder(BuilderBase):
    """Builder for TpPort with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TpPort = TpPort()


    def with_dynamically(self, value: Optional[Boolean]) -> "TpPortBuilder":
        """Set dynamically attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dynamically = value
        return self

    def with_port_number(self, value: Optional[PositiveInteger]) -> "TpPortBuilder":
        """Set port_number attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.port_number = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dynamically",
        "portNumber",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TpPort:
        """Build and return the TpPort instance with validation."""
        self._validate_instance()
        return self._obj