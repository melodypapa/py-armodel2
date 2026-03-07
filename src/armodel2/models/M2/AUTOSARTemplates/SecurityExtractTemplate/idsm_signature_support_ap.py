"""IdsmSignatureSupportAp AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 64)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.CryptoDeployment.crypto_key_slot import (
    CryptoKeySlot,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IdsmSignatureSupportAp(ARObject):
    """AUTOSAR IdsmSignatureSupportAp."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "IDSM-SIGNATURE-SUPPORT-AP"


    crypto_primitive: String
    key_slot_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "CRYPTO-PRIMITIVE": lambda obj, elem: setattr(obj, "crypto_primitive", SerializationHelper.deserialize_by_tag(elem, "String")),
        "KEY-SLOT-REF": lambda obj, elem: setattr(obj, "key_slot_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize IdsmSignatureSupportAp."""
        super().__init__()
        self.crypto_primitive: String = None
        self.key_slot_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize IdsmSignatureSupportAp to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IdsmSignatureSupportAp, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize crypto_primitive
        if self.crypto_primitive is not None:
            serialized = SerializationHelper.serialize_item(self.crypto_primitive, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRYPTO-PRIMITIVE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize key_slot_ref
        if self.key_slot_ref is not None:
            serialized = SerializationHelper.serialize_item(self.key_slot_ref, "CryptoKeySlot")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("KEY-SLOT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IdsmSignatureSupportAp":
        """Deserialize XML element to IdsmSignatureSupportAp object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IdsmSignatureSupportAp object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IdsmSignatureSupportAp, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CRYPTO-PRIMITIVE":
                setattr(obj, "crypto_primitive", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "KEY-SLOT-REF":
                setattr(obj, "key_slot_ref", ARRef.deserialize(child))

        return obj



class IdsmSignatureSupportApBuilder(BuilderBase):
    """Builder for IdsmSignatureSupportAp with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IdsmSignatureSupportAp = IdsmSignatureSupportAp()


    def with_crypto_primitive(self, value: String) -> "IdsmSignatureSupportApBuilder":
        """Set crypto_primitive attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'crypto_primitive' is required and cannot be None")
        self._obj.crypto_primitive = value
        return self

    def with_key_slot(self, value: Optional[CryptoKeySlot]) -> "IdsmSignatureSupportApBuilder":
        """Set key_slot attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'key_slot' is required and cannot be None")
        self._obj.key_slot = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "cryptoPrimitive",
    }
    _OPTIONAL_ATTRIBUTES = {
        "keySlot",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "cryptoPrimitive", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'cryptoPrimitive' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'cryptoPrimitive' is None", UserWarning)


    def build(self) -> IdsmSignatureSupportAp:
        """Build and return the IdsmSignatureSupportAp instance with validation."""
        self._validate_instance()
        return self._obj