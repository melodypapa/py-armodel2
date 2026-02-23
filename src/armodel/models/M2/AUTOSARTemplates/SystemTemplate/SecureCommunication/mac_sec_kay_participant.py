"""MacSecKayParticipant AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 175)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_key import (
    CryptoServiceKey,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.mac_sec_crypto_algo_config import (
    MacSecCryptoAlgoConfig,
)


class MacSecKayParticipant(Identifiable):
    """AUTOSAR MacSecKayParticipant."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ckn_ref: Optional[ARRef]
    crypto_algo: Optional[MacSecCryptoAlgoConfig]
    sak_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize MacSecKayParticipant."""
        super().__init__()
        self.ckn_ref: Optional[ARRef] = None
        self.crypto_algo: Optional[MacSecCryptoAlgoConfig] = None
        self.sak_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize MacSecKayParticipant to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MacSecKayParticipant, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ckn_ref
        if self.ckn_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ckn_ref, "CryptoServiceKey")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CKN-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crypto_algo
        if self.crypto_algo is not None:
            serialized = SerializationHelper.serialize_item(self.crypto_algo, "MacSecCryptoAlgoConfig")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRYPTO-ALGO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sak_ref
        if self.sak_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sak_ref, "CryptoServiceKey")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SAK-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MacSecKayParticipant":
        """Deserialize XML element to MacSecKayParticipant object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MacSecKayParticipant object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MacSecKayParticipant, cls).deserialize(element)

        # Parse ckn_ref
        child = SerializationHelper.find_child_element(element, "CKN-REF")
        if child is not None:
            ckn_ref_value = ARRef.deserialize(child)
            obj.ckn_ref = ckn_ref_value

        # Parse crypto_algo
        child = SerializationHelper.find_child_element(element, "CRYPTO-ALGO")
        if child is not None:
            crypto_algo_value = SerializationHelper.deserialize_by_tag(child, "MacSecCryptoAlgoConfig")
            obj.crypto_algo = crypto_algo_value

        # Parse sak_ref
        child = SerializationHelper.find_child_element(element, "SAK-REF")
        if child is not None:
            sak_ref_value = ARRef.deserialize(child)
            obj.sak_ref = sak_ref_value

        return obj



class MacSecKayParticipantBuilder(IdentifiableBuilder):
    """Builder for MacSecKayParticipant with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MacSecKayParticipant = MacSecKayParticipant()


    def with_ckn(self, value: Optional[CryptoServiceKey]) -> "MacSecKayParticipantBuilder":
        """Set ckn attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ckn = value
        return self

    def with_crypto_algo(self, value: Optional[MacSecCryptoAlgoConfig]) -> "MacSecKayParticipantBuilder":
        """Set crypto_algo attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.crypto_algo = value
        return self

    def with_sak(self, value: Optional[CryptoServiceKey]) -> "MacSecKayParticipantBuilder":
        """Set sak attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sak = value
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


    def build(self) -> MacSecKayParticipant:
        """Build and return the MacSecKayParticipant instance with validation."""
        self._validate_instance()
        pass
        return self._obj