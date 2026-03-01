"""BswModeSenderPolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_mode_switch_ack_request import (
    BswModeSwitchAckRequest,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BswModeSenderPolicy(ARObject):
    """AUTOSAR BswModeSenderPolicy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BSW-MODE-SENDER-POLICY"


    ack_request_request: Optional[BswModeSwitchAckRequest]
    enhanced_mode: Optional[Boolean]
    provided_mode_ref: Optional[ARRef]
    queue_length: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "ACK-REQUEST-REQUEST": lambda obj, elem: setattr(obj, "ack_request_request", SerializationHelper.deserialize_by_tag(elem, "BswModeSwitchAckRequest")),
        "ENHANCED-MODE": lambda obj, elem: setattr(obj, "enhanced_mode", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "PROVIDED-MODE-REF": lambda obj, elem: setattr(obj, "provided_mode_ref", ARRef.deserialize(elem)),
        "QUEUE-LENGTH": lambda obj, elem: setattr(obj, "queue_length", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize BswModeSenderPolicy."""
        super().__init__()
        self.ack_request_request: Optional[BswModeSwitchAckRequest] = None
        self.enhanced_mode: Optional[Boolean] = None
        self.provided_mode_ref: Optional[ARRef] = None
        self.queue_length: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize BswModeSenderPolicy to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswModeSenderPolicy, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ack_request_request
        if self.ack_request_request is not None:
            serialized = SerializationHelper.serialize_item(self.ack_request_request, "BswModeSwitchAckRequest")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACK-REQUEST-REQUEST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize enhanced_mode
        if self.enhanced_mode is not None:
            serialized = SerializationHelper.serialize_item(self.enhanced_mode, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENHANCED-MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize provided_mode_ref
        if self.provided_mode_ref is not None:
            serialized = SerializationHelper.serialize_item(self.provided_mode_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROVIDED-MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize queue_length
        if self.queue_length is not None:
            serialized = SerializationHelper.serialize_item(self.queue_length, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("QUEUE-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModeSenderPolicy":
        """Deserialize XML element to BswModeSenderPolicy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswModeSenderPolicy object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswModeSenderPolicy, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ACK-REQUEST-REQUEST":
                setattr(obj, "ack_request_request", SerializationHelper.deserialize_by_tag(child, "BswModeSwitchAckRequest"))
            elif tag == "ENHANCED-MODE":
                setattr(obj, "enhanced_mode", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "PROVIDED-MODE-REF":
                setattr(obj, "provided_mode_ref", ARRef.deserialize(child))
            elif tag == "QUEUE-LENGTH":
                setattr(obj, "queue_length", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class BswModeSenderPolicyBuilder(BuilderBase):
    """Builder for BswModeSenderPolicy with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BswModeSenderPolicy = BswModeSenderPolicy()


    def with_ack_request_request(self, value: Optional[BswModeSwitchAckRequest]) -> "BswModeSenderPolicyBuilder":
        """Set ack_request_request attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ack_request_request = value
        return self

    def with_enhanced_mode(self, value: Optional[Boolean]) -> "BswModeSenderPolicyBuilder":
        """Set enhanced_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.enhanced_mode = value
        return self

    def with_provided_mode(self, value: Optional[ModeDeclarationGroup]) -> "BswModeSenderPolicyBuilder":
        """Set provided_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.provided_mode = value
        return self

    def with_queue_length(self, value: Optional[PositiveInteger]) -> "BswModeSenderPolicyBuilder":
        """Set queue_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.queue_length = value
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


    def build(self) -> BswModeSenderPolicy:
        """Build and return the BswModeSenderPolicy instance with validation."""
        self._validate_instance()
        pass
        return self._obj