"""DiagnosticAuthTransmitCertificateMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 242)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import DiagnosticMappingBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticAuthTransmitCertificateMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticAuthTransmitCertificateMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE-MAPPING"


    crypto_service_refs: list[Any]
    service_instance_ref: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "CRYPTO-SERVICES": lambda obj, elem: obj.crypto_service_refs.append(ARRef.deserialize(elem)),
        "SERVICE-INSTANCE-REF": lambda obj, elem: setattr(obj, "service_instance_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticAuthTransmitCertificateMapping."""
        super().__init__()
        self.crypto_service_refs: list[Any] = []
        self.service_instance_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticAuthTransmitCertificateMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticAuthTransmitCertificateMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize crypto_service_refs (list to container "CRYPTO-SERVICE-REFS")
        if self.crypto_service_refs:
            wrapper = ET.Element("CRYPTO-SERVICE-REFS")
            for item in self.crypto_service_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("CRYPTO-SERVICE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize service_instance_ref
        if self.service_instance_ref is not None:
            serialized = SerializationHelper.serialize_item(self.service_instance_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAuthTransmitCertificateMapping":
        """Deserialize XML element to DiagnosticAuthTransmitCertificateMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticAuthTransmitCertificateMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticAuthTransmitCertificateMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "CRYPTO-SERVICES":
                obj.crypto_service_refs.append(ARRef.deserialize(child))
            elif tag == "SERVICE-INSTANCE-REF":
                setattr(obj, "service_instance_ref", ARRef.deserialize(child))

        return obj



class DiagnosticAuthTransmitCertificateMappingBuilder(DiagnosticMappingBuilder):
    """Builder for DiagnosticAuthTransmitCertificateMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticAuthTransmitCertificateMapping = DiagnosticAuthTransmitCertificateMapping()


    def with_crypto_services(self, items: list[any (CryptoService)]) -> "DiagnosticAuthTransmitCertificateMappingBuilder":
        """Set crypto_services list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.crypto_services = list(items) if items else []
        return self

    def with_service_instance(self, value: Optional[any (DiagnosticAuthTransmit)]) -> "DiagnosticAuthTransmitCertificateMappingBuilder":
        """Set service_instance attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.service_instance = value
        return self


    def add_crypto_service(self, item: any (CryptoService)) -> "DiagnosticAuthTransmitCertificateMappingBuilder":
        """Add a single item to crypto_services list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.crypto_services.append(item)
        return self

    def clear_crypto_services(self) -> "DiagnosticAuthTransmitCertificateMappingBuilder":
        """Clear all items from crypto_services list.

        Returns:
            self for method chaining
        """
        self._obj.crypto_services = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> DiagnosticAuthTransmitCertificateMapping:
        """Build and return the DiagnosticAuthTransmitCertificateMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj