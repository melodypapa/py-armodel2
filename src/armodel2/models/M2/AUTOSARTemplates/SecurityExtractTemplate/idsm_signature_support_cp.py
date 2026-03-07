"""IdsmSignatureSupportCp AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 64)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_key import (
    CryptoServiceKey,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_primitive import (
    CryptoServicePrimitive,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IdsmSignatureSupportCp(ARObject):
    """AUTOSAR IdsmSignatureSupportCp."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "IDSM-SIGNATURE-SUPPORT-CP"


    authentication_ref: Optional[ARRef]
    crypto_service_key_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "AUTHENTICATION-REF": lambda obj, elem: setattr(obj, "authentication_ref", ARRef.deserialize(elem)),
        "CRYPTO-SERVICE-KEY-REF": lambda obj, elem: setattr(obj, "crypto_service_key_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize IdsmSignatureSupportCp."""
        super().__init__()
        self.authentication_ref: Optional[ARRef] = None
        self.crypto_service_key_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize IdsmSignatureSupportCp to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IdsmSignatureSupportCp, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize authentication_ref
        if self.authentication_ref is not None:
            serialized = SerializationHelper.serialize_item(self.authentication_ref, "CryptoServicePrimitive")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AUTHENTICATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crypto_service_key_ref
        if self.crypto_service_key_ref is not None:
            serialized = SerializationHelper.serialize_item(self.crypto_service_key_ref, "CryptoServiceKey")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRYPTO-SERVICE-KEY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IdsmSignatureSupportCp":
        """Deserialize XML element to IdsmSignatureSupportCp object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IdsmSignatureSupportCp object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IdsmSignatureSupportCp, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "AUTHENTICATION-REF":
                setattr(obj, "authentication_ref", ARRef.deserialize(child))
            elif tag == "CRYPTO-SERVICE-KEY-REF":
                setattr(obj, "crypto_service_key_ref", ARRef.deserialize(child))

        return obj



class IdsmSignatureSupportCpBuilder(BuilderBase):
    """Builder for IdsmSignatureSupportCp with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IdsmSignatureSupportCp = IdsmSignatureSupportCp()


    def with_authentication(self, value: Optional[CryptoServicePrimitive]) -> "IdsmSignatureSupportCpBuilder":
        """Set authentication attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'authentication' is required and cannot be None")
        self._obj.authentication = value
        return self

    def with_crypto_service_key(self, value: Optional[CryptoServiceKey]) -> "IdsmSignatureSupportCpBuilder":
        """Set crypto_service_key attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'crypto_service_key' is required and cannot be None")
        self._obj.crypto_service_key = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "authentication",
        "cryptoServiceKey",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> IdsmSignatureSupportCp:
        """Build and return the IdsmSignatureSupportCp instance with validation."""
        self._validate_instance()
        return self._obj