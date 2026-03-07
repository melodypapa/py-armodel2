"""CryptoServicePrimitive AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 376)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 59)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CryptoServicePrimitive(ARElement):
    """AUTOSAR CryptoServicePrimitive."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CRYPTO-SERVICE-PRIMITIVE"


    algorithm_family: Optional[String]
    algorithm_mode: Optional[String]
    algorithm: Optional[String]
    _DESERIALIZE_DISPATCH = {
        "ALGORITHM-FAMILY": lambda obj, elem: setattr(obj, "algorithm_family", SerializationHelper.deserialize_by_tag(elem, "String")),
        "ALGORITHM-MODE": lambda obj, elem: setattr(obj, "algorithm_mode", SerializationHelper.deserialize_by_tag(elem, "String")),
        "ALGORITHM": lambda obj, elem: setattr(obj, "algorithm", SerializationHelper.deserialize_by_tag(elem, "String")),
    }


    def __init__(self) -> None:
        """Initialize CryptoServicePrimitive."""
        super().__init__()
        self.algorithm_family: Optional[String] = None
        self.algorithm_mode: Optional[String] = None
        self.algorithm: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize CryptoServicePrimitive to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CryptoServicePrimitive, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize algorithm_family
        if self.algorithm_family is not None:
            serialized = SerializationHelper.serialize_item(self.algorithm_family, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALGORITHM-FAMILY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize algorithm_mode
        if self.algorithm_mode is not None:
            serialized = SerializationHelper.serialize_item(self.algorithm_mode, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALGORITHM-MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize algorithm
        if self.algorithm is not None:
            serialized = SerializationHelper.serialize_item(self.algorithm, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALGORITHM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CryptoServicePrimitive":
        """Deserialize XML element to CryptoServicePrimitive object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CryptoServicePrimitive object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CryptoServicePrimitive, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ALGORITHM-FAMILY":
                setattr(obj, "algorithm_family", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "ALGORITHM-MODE":
                setattr(obj, "algorithm_mode", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "ALGORITHM":
                setattr(obj, "algorithm", SerializationHelper.deserialize_by_tag(child, "String"))

        return obj



class CryptoServicePrimitiveBuilder(ARElementBuilder):
    """Builder for CryptoServicePrimitive with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CryptoServicePrimitive = CryptoServicePrimitive()


    def with_algorithm_family(self, value: Optional[String]) -> "CryptoServicePrimitiveBuilder":
        """Set algorithm_family attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'algorithm_family' is required and cannot be None")
        self._obj.algorithm_family = value
        return self

    def with_algorithm_mode(self, value: Optional[String]) -> "CryptoServicePrimitiveBuilder":
        """Set algorithm_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'algorithm_mode' is required and cannot be None")
        self._obj.algorithm_mode = value
        return self

    def with_algorithm(self, value: Optional[String]) -> "CryptoServicePrimitiveBuilder":
        """Set algorithm attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'algorithm' is required and cannot be None")
        self._obj.algorithm = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "algorithm",
        "algorithmFamily",
        "algorithmMode",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CryptoServicePrimitive:
        """Build and return the CryptoServicePrimitive instance with validation."""
        self._validate_instance()
        return self._obj