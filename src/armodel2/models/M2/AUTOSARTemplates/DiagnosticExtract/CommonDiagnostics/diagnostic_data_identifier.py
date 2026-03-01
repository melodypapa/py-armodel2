"""DiagnosticDataIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 33)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_abstract_data_identifier import (
    DiagnosticAbstractDataIdentifier,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_abstract_data_identifier import DiagnosticAbstractDataIdentifierBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_support_info_byte import (
    DiagnosticSupportInfoByte,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticDataIdentifier(DiagnosticAbstractDataIdentifier):
    """AUTOSAR DiagnosticDataIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-DATA-IDENTIFIER"


    data_elements: list[DiagnosticParameter]
    did_size: Optional[PositiveInteger]
    represents_vin: Optional[Boolean]
    support_info_byte: Optional[DiagnosticSupportInfoByte]
    _DESERIALIZE_DISPATCH = {
        "DATA-ELEMENTS": lambda obj, elem: obj.data_elements.append(SerializationHelper.deserialize_by_tag(elem, "DiagnosticParameter")),
        "DID-SIZE": lambda obj, elem: setattr(obj, "did_size", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "REPRESENTS-VIN": lambda obj, elem: setattr(obj, "represents_vin", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "SUPPORT-INFO-BYTE": lambda obj, elem: setattr(obj, "support_info_byte", SerializationHelper.deserialize_by_tag(elem, "DiagnosticSupportInfoByte")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticDataIdentifier."""
        super().__init__()
        self.data_elements: list[DiagnosticParameter] = []
        self.did_size: Optional[PositiveInteger] = None
        self.represents_vin: Optional[Boolean] = None
        self.support_info_byte: Optional[DiagnosticSupportInfoByte] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticDataIdentifier to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticDataIdentifier, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_elements (list to container "DATA-ELEMENTS")
        if self.data_elements:
            wrapper = ET.Element("DATA-ELEMENTS")
            for item in self.data_elements:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticParameter")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize did_size
        if self.did_size is not None:
            serialized = SerializationHelper.serialize_item(self.did_size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DID-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize represents_vin
        if self.represents_vin is not None:
            serialized = SerializationHelper.serialize_item(self.represents_vin, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REPRESENTS-VIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize support_info_byte
        if self.support_info_byte is not None:
            serialized = SerializationHelper.serialize_item(self.support_info_byte, "DiagnosticSupportInfoByte")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUPPORT-INFO-BYTE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticDataIdentifier":
        """Deserialize XML element to DiagnosticDataIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticDataIdentifier object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticDataIdentifier, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "DATA-ELEMENTS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.data_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticParameter"))
            elif tag == "DID-SIZE":
                setattr(obj, "did_size", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "REPRESENTS-VIN":
                setattr(obj, "represents_vin", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "SUPPORT-INFO-BYTE":
                setattr(obj, "support_info_byte", SerializationHelper.deserialize_by_tag(child, "DiagnosticSupportInfoByte"))

        return obj



class DiagnosticDataIdentifierBuilder(DiagnosticAbstractDataIdentifierBuilder):
    """Builder for DiagnosticDataIdentifier with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticDataIdentifier = DiagnosticDataIdentifier()


    def with_data_elements(self, items: list[DiagnosticParameter]) -> "DiagnosticDataIdentifierBuilder":
        """Set data_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_elements = list(items) if items else []
        return self

    def with_did_size(self, value: Optional[PositiveInteger]) -> "DiagnosticDataIdentifierBuilder":
        """Set did_size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.did_size = value
        return self

    def with_represents_vin(self, value: Optional[Boolean]) -> "DiagnosticDataIdentifierBuilder":
        """Set represents_vin attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.represents_vin = value
        return self

    def with_support_info_byte(self, value: Optional[DiagnosticSupportInfoByte]) -> "DiagnosticDataIdentifierBuilder":
        """Set support_info_byte attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.support_info_byte = value
        return self


    def add_data_element(self, item: DiagnosticParameter) -> "DiagnosticDataIdentifierBuilder":
        """Add a single item to data_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_elements.append(item)
        return self

    def clear_data_elements(self) -> "DiagnosticDataIdentifierBuilder":
        """Clear all items from data_elements list.

        Returns:
            self for method chaining
        """
        self._obj.data_elements = []
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


    def build(self) -> DiagnosticDataIdentifier:
        """Build and return the DiagnosticDataIdentifier instance with validation."""
        self._validate_instance()
        pass
        return self._obj