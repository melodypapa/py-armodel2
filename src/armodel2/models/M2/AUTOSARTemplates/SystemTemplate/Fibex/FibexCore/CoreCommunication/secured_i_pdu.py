"""SecuredIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 367)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import IPduBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    SecuredPduHeaderEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SecuredIPdu(IPdu):
    """AUTOSAR SecuredIPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SECURED-I-PDU"


    authentication_ref: Optional[Any]
    dynamic: Optional[Boolean]
    freshness_props_ref: Optional[Any]
    payload_ref: Optional[ARRef]
    secure: Optional[Any]
    use_as: Optional[Boolean]
    use_secured_pdu: Optional[SecuredPduHeaderEnum]
    _DESERIALIZE_DISPATCH = {
        "AUTHENTICATION-REF": lambda obj, elem: setattr(obj, "authentication_ref", ARRef.deserialize(elem)),
        "DYNAMIC": lambda obj, elem: setattr(obj, "dynamic", elem.text),
        "FRESHNESS-PROPS-REF": lambda obj, elem: setattr(obj, "freshness_props_ref", ARRef.deserialize(elem)),
        "PAYLOAD-REF": lambda obj, elem: setattr(obj, "payload_ref", ARRef.deserialize(elem)),
        "SECURE": lambda obj, elem: setattr(obj, "secure", any (SecureCommunication).deserialize(elem)),
        "USE-AS": lambda obj, elem: setattr(obj, "use_as", elem.text),
        "USE-SECURED-PDU": lambda obj, elem: setattr(obj, "use_secured_pdu", SecuredPduHeaderEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize SecuredIPdu."""
        super().__init__()
        self.authentication_ref: Optional[Any] = None
        self.dynamic: Optional[Boolean] = None
        self.freshness_props_ref: Optional[Any] = None
        self.payload_ref: Optional[ARRef] = None
        self.secure: Optional[Any] = None
        self.use_as: Optional[Boolean] = None
        self.use_secured_pdu: Optional[SecuredPduHeaderEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize SecuredIPdu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecuredIPdu, self).serialize()

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
            serialized = SerializationHelper.serialize_item(self.authentication_ref, "Any")
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

        # Serialize dynamic
        if self.dynamic is not None:
            serialized = SerializationHelper.serialize_item(self.dynamic, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DYNAMIC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize freshness_props_ref
        if self.freshness_props_ref is not None:
            serialized = SerializationHelper.serialize_item(self.freshness_props_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FRESHNESS-PROPS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize payload_ref
        if self.payload_ref is not None:
            serialized = SerializationHelper.serialize_item(self.payload_ref, "PduTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PAYLOAD-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize secure
        if self.secure is not None:
            serialized = SerializationHelper.serialize_item(self.secure, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECURE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize use_as
        if self.use_as is not None:
            serialized = SerializationHelper.serialize_item(self.use_as, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USE-AS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize use_secured_pdu
        if self.use_secured_pdu is not None:
            serialized = SerializationHelper.serialize_item(self.use_secured_pdu, "SecuredPduHeaderEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USE-SECURED-PDU")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecuredIPdu":
        """Deserialize XML element to SecuredIPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecuredIPdu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecuredIPdu, cls).deserialize(element)

        # Parse authentication_ref
        child = SerializationHelper.find_child_element(element, "AUTHENTICATION-REF")
        if child is not None:
            authentication_ref_value = ARRef.deserialize(child)
            obj.authentication_ref = authentication_ref_value

        # Parse dynamic
        child = SerializationHelper.find_child_element(element, "DYNAMIC")
        if child is not None:
            dynamic_value = child.text
            obj.dynamic = dynamic_value

        # Parse freshness_props_ref
        child = SerializationHelper.find_child_element(element, "FRESHNESS-PROPS-REF")
        if child is not None:
            freshness_props_ref_value = ARRef.deserialize(child)
            obj.freshness_props_ref = freshness_props_ref_value

        # Parse payload_ref
        child = SerializationHelper.find_child_element(element, "PAYLOAD-REF")
        if child is not None:
            payload_ref_value = ARRef.deserialize(child)
            obj.payload_ref = payload_ref_value

        # Parse secure
        child = SerializationHelper.find_child_element(element, "SECURE")
        if child is not None:
            secure_value = child.text
            obj.secure = secure_value

        # Parse use_as
        child = SerializationHelper.find_child_element(element, "USE-AS")
        if child is not None:
            use_as_value = child.text
            obj.use_as = use_as_value

        # Parse use_secured_pdu
        child = SerializationHelper.find_child_element(element, "USE-SECURED-PDU")
        if child is not None:
            use_secured_pdu_value = SecuredPduHeaderEnum.deserialize(child)
            obj.use_secured_pdu = use_secured_pdu_value

        return obj



class SecuredIPduBuilder(IPduBuilder):
    """Builder for SecuredIPdu with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SecuredIPdu = SecuredIPdu()


    def with_authentication(self, value: Optional[any (SecureCommunication)]) -> "SecuredIPduBuilder":
        """Set authentication attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.authentication = value
        return self

    def with_dynamic(self, value: Optional[Boolean]) -> "SecuredIPduBuilder":
        """Set dynamic attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dynamic = value
        return self

    def with_freshness_props(self, value: Optional[any (SecureCommunication)]) -> "SecuredIPduBuilder":
        """Set freshness_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.freshness_props = value
        return self

    def with_payload(self, value: Optional[PduTriggering]) -> "SecuredIPduBuilder":
        """Set payload attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.payload = value
        return self

    def with_secure(self, value: Optional[any (SecureCommunication)]) -> "SecuredIPduBuilder":
        """Set secure attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.secure = value
        return self

    def with_use_as(self, value: Optional[Boolean]) -> "SecuredIPduBuilder":
        """Set use_as attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.use_as = value
        return self

    def with_use_secured_pdu(self, value: Optional[SecuredPduHeaderEnum]) -> "SecuredIPduBuilder":
        """Set use_secured_pdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.use_secured_pdu = value
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


    def build(self) -> SecuredIPdu:
        """Build and return the SecuredIPdu instance with validation."""
        self._validate_instance()
        pass
        return self._obj