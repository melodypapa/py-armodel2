"""GenericTp AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 459)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.transport_protocol_configuration import (
    TransportProtocolConfiguration,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.transport_protocol_configuration import TransportProtocolConfigurationBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class GenericTp(TransportProtocolConfiguration):
    """AUTOSAR GenericTp."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "GENERIC-TP"


    tp_address: Optional[String]
    tp_technology: Optional[String]
    _DESERIALIZE_DISPATCH = {
        "TP-ADDRESS": lambda obj, elem: setattr(obj, "tp_address", SerializationHelper.deserialize_by_tag(elem, "String")),
        "TP-TECHNOLOGY": lambda obj, elem: setattr(obj, "tp_technology", SerializationHelper.deserialize_by_tag(elem, "String")),
    }


    def __init__(self) -> None:
        """Initialize GenericTp."""
        super().__init__()
        self.tp_address: Optional[String] = None
        self.tp_technology: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize GenericTp to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(GenericTp, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tp_address
        if self.tp_address is not None:
            serialized = SerializationHelper.serialize_item(self.tp_address, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TP-ADDRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tp_technology
        if self.tp_technology is not None:
            serialized = SerializationHelper.serialize_item(self.tp_technology, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TP-TECHNOLOGY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GenericTp":
        """Deserialize XML element to GenericTp object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GenericTp object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(GenericTp, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TP-ADDRESS":
                setattr(obj, "tp_address", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "TP-TECHNOLOGY":
                setattr(obj, "tp_technology", SerializationHelper.deserialize_by_tag(child, "String"))

        return obj



class GenericTpBuilder(TransportProtocolConfigurationBuilder):
    """Builder for GenericTp with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: GenericTp = GenericTp()


    def with_tp_address(self, value: Optional[String]) -> "GenericTpBuilder":
        """Set tp_address attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tp_address = value
        return self

    def with_tp_technology(self, value: Optional[String]) -> "GenericTpBuilder":
        """Set tp_technology attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tp_technology = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "tpAddress",
        "tpTechnology",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> GenericTp:
        """Build and return the GenericTp instance with validation."""
        self._validate_instance()
        return self._obj