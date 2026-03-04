"""ClientIdRange AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 52)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Limit,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ClientIdRange(ARObject):
    """AUTOSAR ClientIdRange."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CLIENT-ID-RANGE"


    lower_limit: Optional[Limit]
    upper_limit: Optional[Limit]
    _DESERIALIZE_DISPATCH = {
        "LOWER-LIMIT": lambda obj, elem: setattr(obj, "lower_limit", SerializationHelper.deserialize_by_tag(elem, "Limit")),
        "UPPER-LIMIT": lambda obj, elem: setattr(obj, "upper_limit", SerializationHelper.deserialize_by_tag(elem, "Limit")),
    }


    def __init__(self) -> None:
        """Initialize ClientIdRange."""
        super().__init__()
        self.lower_limit: Optional[Limit] = None
        self.upper_limit: Optional[Limit] = None

    def serialize(self) -> ET.Element:
        """Serialize ClientIdRange to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ClientIdRange, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize lower_limit
        if self.lower_limit is not None:
            serialized = SerializationHelper.serialize_item(self.lower_limit, "Limit")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOWER-LIMIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize upper_limit
        if self.upper_limit is not None:
            serialized = SerializationHelper.serialize_item(self.upper_limit, "Limit")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UPPER-LIMIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientIdRange":
        """Deserialize XML element to ClientIdRange object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientIdRange object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ClientIdRange, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "LOWER-LIMIT":
                setattr(obj, "lower_limit", SerializationHelper.deserialize_by_tag(child, "Limit"))
            elif tag == "UPPER-LIMIT":
                setattr(obj, "upper_limit", SerializationHelper.deserialize_by_tag(child, "Limit"))

        return obj



class ClientIdRangeBuilder(BuilderBase):
    """Builder for ClientIdRange with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ClientIdRange = ClientIdRange()


    def with_lower_limit(self, value: Optional[Limit]) -> "ClientIdRangeBuilder":
        """Set lower_limit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.lower_limit = value
        return self

    def with_upper_limit(self, value: Optional[Limit]) -> "ClientIdRangeBuilder":
        """Set upper_limit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.upper_limit = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "lowerLimit",
        "upperLimit",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ClientIdRange:
        """Build and return the ClientIdRange instance with validation."""
        self._validate_instance()
        return self._obj