"""DynamicPartAlternative AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 411)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_i_pdu import (
    ISignalIPdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class DynamicPartAlternative(ARObject):
    """AUTOSAR DynamicPartAlternative."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    initial_dynamic: Optional[Boolean]
    i_pdu_ref: Optional[ARRef]
    selector_field: Optional[Integer]
    def __init__(self) -> None:
        """Initialize DynamicPartAlternative."""
        super().__init__()
        self.initial_dynamic: Optional[Boolean] = None
        self.i_pdu_ref: Optional[ARRef] = None
        self.selector_field: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize DynamicPartAlternative to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DynamicPartAlternative, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize initial_dynamic
        if self.initial_dynamic is not None:
            serialized = SerializationHelper.serialize_item(self.initial_dynamic, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INITIAL-DYNAMIC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize i_pdu_ref
        if self.i_pdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.i_pdu_ref, "ISignalIPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("I-PDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize selector_field
        if self.selector_field is not None:
            serialized = SerializationHelper.serialize_item(self.selector_field, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SELECTOR-FIELD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DynamicPartAlternative":
        """Deserialize XML element to DynamicPartAlternative object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DynamicPartAlternative object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DynamicPartAlternative, cls).deserialize(element)

        # Parse initial_dynamic
        child = SerializationHelper.find_child_element(element, "INITIAL-DYNAMIC")
        if child is not None:
            initial_dynamic_value = child.text
            obj.initial_dynamic = initial_dynamic_value

        # Parse i_pdu_ref
        child = SerializationHelper.find_child_element(element, "I-PDU-REF")
        if child is not None:
            i_pdu_ref_value = ARRef.deserialize(child)
            obj.i_pdu_ref = i_pdu_ref_value

        # Parse selector_field
        child = SerializationHelper.find_child_element(element, "SELECTOR-FIELD")
        if child is not None:
            selector_field_value = child.text
            obj.selector_field = selector_field_value

        return obj



class DynamicPartAlternativeBuilder(BuilderBase):
    """Builder for DynamicPartAlternative with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DynamicPartAlternative = DynamicPartAlternative()


    def with_initial_dynamic(self, value: Optional[Boolean]) -> "DynamicPartAlternativeBuilder":
        """Set initial_dynamic attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.initial_dynamic = value
        return self

    def with_i_pdu(self, value: Optional[ISignalIPdu]) -> "DynamicPartAlternativeBuilder":
        """Set i_pdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.i_pdu = value
        return self

    def with_selector_field(self, value: Optional[Integer]) -> "DynamicPartAlternativeBuilder":
        """Set selector_field attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.selector_field = value
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


    def build(self) -> DynamicPartAlternative:
        """Build and return the DynamicPartAlternative instance with validation."""
        self._validate_instance()
        pass
        return self._obj