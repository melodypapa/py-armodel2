"""CryptoServiceCertificate AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 310)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 565)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    CryptoCertificateFormatEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CryptoServiceCertificate(ARElement):
    """AUTOSAR CryptoServiceCertificate."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CRYPTO-SERVICE-CERTIFICATE"


    algorithm_family: Optional[Any]
    format: Optional[CryptoCertificateFormatEnum]
    maximum: Optional[PositiveInteger]
    next_higher_ref: Optional[Any]
    server_name: Optional[String]
    _DESERIALIZE_DISPATCH = {
        "ALGORITHM-FAMILY": lambda obj, elem: setattr(obj, "algorithm_family", SerializationHelper.deserialize_by_tag(elem, "any (CryptoCertificate)")),
        "FORMAT": lambda obj, elem: setattr(obj, "format", CryptoCertificateFormatEnum.deserialize(elem)),
        "MAXIMUM": lambda obj, elem: setattr(obj, "maximum", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "NEXT-HIGHER-REF": lambda obj, elem: setattr(obj, "next_higher_ref", ARRef.deserialize(elem)),
        "SERVER-NAME": lambda obj, elem: setattr(obj, "server_name", SerializationHelper.deserialize_by_tag(elem, "String")),
    }


    def __init__(self) -> None:
        """Initialize CryptoServiceCertificate."""
        super().__init__()
        self.algorithm_family: Optional[Any] = None
        self.format: Optional[CryptoCertificateFormatEnum] = None
        self.maximum: Optional[PositiveInteger] = None
        self.next_higher_ref: Optional[Any] = None
        self.server_name: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize CryptoServiceCertificate to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CryptoServiceCertificate, self).serialize()

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
            serialized = SerializationHelper.serialize_item(self.algorithm_family, "Any")
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

        # Serialize format
        if self.format is not None:
            serialized = SerializationHelper.serialize_item(self.format, "CryptoCertificateFormatEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FORMAT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize maximum
        if self.maximum is not None:
            serialized = SerializationHelper.serialize_item(self.maximum, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAXIMUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize next_higher_ref
        if self.next_higher_ref is not None:
            serialized = SerializationHelper.serialize_item(self.next_higher_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NEXT-HIGHER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize server_name
        if self.server_name is not None:
            serialized = SerializationHelper.serialize_item(self.server_name, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVER-NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CryptoServiceCertificate":
        """Deserialize XML element to CryptoServiceCertificate object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CryptoServiceCertificate object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CryptoServiceCertificate, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ALGORITHM-FAMILY":
                setattr(obj, "algorithm_family", SerializationHelper.deserialize_by_tag(child, "any (CryptoCertificate)"))
            elif tag == "FORMAT":
                setattr(obj, "format", CryptoCertificateFormatEnum.deserialize(child))
            elif tag == "MAXIMUM":
                setattr(obj, "maximum", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "NEXT-HIGHER-REF":
                setattr(obj, "next_higher_ref", ARRef.deserialize(child))
            elif tag == "SERVER-NAME":
                setattr(obj, "server_name", SerializationHelper.deserialize_by_tag(child, "String"))

        return obj



class CryptoServiceCertificateBuilder(ARElementBuilder):
    """Builder for CryptoServiceCertificate with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CryptoServiceCertificate = CryptoServiceCertificate()


    def with_algorithm_family(self, value: Optional[any (CryptoCertificate)]) -> "CryptoServiceCertificateBuilder":
        """Set algorithm_family attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.algorithm_family = value
        return self

    def with_format(self, value: Optional[CryptoCertificateFormatEnum]) -> "CryptoServiceCertificateBuilder":
        """Set format attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.format = value
        return self

    def with_maximum(self, value: Optional[PositiveInteger]) -> "CryptoServiceCertificateBuilder":
        """Set maximum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.maximum = value
        return self

    def with_next_higher(self, value: Optional[any (CryptoService)]) -> "CryptoServiceCertificateBuilder":
        """Set next_higher attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.next_higher = value
        return self

    def with_server_name(self, value: Optional[String]) -> "CryptoServiceCertificateBuilder":
        """Set server_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.server_name = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "algorithmFamily",
        "format",
        "maximum",
        "nextHigher",
        "serverName",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CryptoServiceCertificate:
        """Build and return the CryptoServiceCertificate instance with validation."""
        self._validate_instance()
        return self._obj