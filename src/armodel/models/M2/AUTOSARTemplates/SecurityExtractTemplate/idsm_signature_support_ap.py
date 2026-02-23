"""IdsmSignatureSupportAp AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 64)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.CryptoDeployment.crypto_key_slot import (
    CryptoKeySlot,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class IdsmSignatureSupportAp(ARObject):
    """AUTOSAR IdsmSignatureSupportAp."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    crypto_primitive: String
    key_slot_ref: Optional[ARRef]
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
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse crypto_primitive
        child = SerializationHelper.find_child_element(element, "CRYPTO-PRIMITIVE")
        if child is not None:
            crypto_primitive_value = child.text
            obj.crypto_primitive = crypto_primitive_value

        # Parse key_slot_ref
        child = SerializationHelper.find_child_element(element, "KEY-SLOT-REF")
        if child is not None:
            key_slot_ref_value = ARRef.deserialize(child)
            obj.key_slot_ref = key_slot_ref_value

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
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
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
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.key_slot = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> IdsmSignatureSupportAp:
        """Build and return the IdsmSignatureSupportAp instance with validation."""
        self._validate_instance()
        pass
        return self._obj