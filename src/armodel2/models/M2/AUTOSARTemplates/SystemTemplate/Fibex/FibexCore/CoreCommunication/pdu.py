"""Pdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 303)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 340)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import FibexElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    UnlimitedInteger,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Pdu(FibexElement, ABC):
    """AUTOSAR Pdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    has_dynamic_length: Optional[Boolean]
    length: Optional[UnlimitedInteger]
    _DESERIALIZE_DISPATCH = {
        "HAS-DYNAMIC-LENGTH": lambda obj, elem: setattr(obj, "has_dynamic_length", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "LENGTH": lambda obj, elem: setattr(obj, "length", SerializationHelper.deserialize_by_tag(elem, "UnlimitedInteger")),
    }


    def __init__(self) -> None:
        """Initialize Pdu."""
        super().__init__()
        self.has_dynamic_length: Optional[Boolean] = None
        self.length: Optional[UnlimitedInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize Pdu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Pdu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize has_dynamic_length
        if self.has_dynamic_length is not None:
            serialized = SerializationHelper.serialize_item(self.has_dynamic_length, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HAS-DYNAMIC-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize length
        if self.length is not None:
            serialized = SerializationHelper.serialize_item(self.length, "UnlimitedInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Pdu":
        """Deserialize XML element to Pdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Pdu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Pdu, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "HAS-DYNAMIC-LENGTH":
                setattr(obj, "has_dynamic_length", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "LENGTH":
                setattr(obj, "length", SerializationHelper.deserialize_by_tag(child, "UnlimitedInteger"))

        return obj



class PduBuilder(FibexElementBuilder):
    """Builder for Pdu with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Pdu = Pdu()


    def with_has_dynamic_length(self, value: Optional[Boolean]) -> "PduBuilder":
        """Set has_dynamic_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'has_dynamic_length' is required and cannot be None")
        self._obj.has_dynamic_length = value
        return self

    def with_length(self, value: Optional[UnlimitedInteger]) -> "PduBuilder":
        """Set length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'length' is required and cannot be None")
        self._obj.length = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "hasDynamicLength",
        "length",
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
    def build(self) -> Pdu:
        """Build and return the Pdu instance (abstract)."""
        raise NotImplementedError