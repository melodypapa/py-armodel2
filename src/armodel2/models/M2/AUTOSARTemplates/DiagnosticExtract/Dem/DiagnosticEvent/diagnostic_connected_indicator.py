"""DiagnosticConnectedIndicator AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 166)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticEvent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticIndicator.diagnostic_indicator import (
    DiagnosticIndicator,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticConnectedIndicator(Identifiable):
    """AUTOSAR DiagnosticConnectedIndicator."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-CONNECTED-INDICATOR"


    behavior_indicator_behavior_enum: Optional[Any]
    healing_cycle: Optional[PositiveInteger]
    indicator_ref: Optional[ARRef]
    indicator_failure: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "BEHAVIOR-INDICATOR-BEHAVIOR-ENUM": lambda obj, elem: setattr(obj, "behavior_indicator_behavior_enum", SerializationHelper.deserialize_by_tag(elem, "any (DiagnosticConnected)")),
        "HEALING-CYCLE": lambda obj, elem: setattr(obj, "healing_cycle", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "INDICATOR-REF": lambda obj, elem: setattr(obj, "indicator_ref", ARRef.deserialize(elem)),
        "INDICATOR-FAILURE": lambda obj, elem: setattr(obj, "indicator_failure", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticConnectedIndicator."""
        super().__init__()
        self.behavior_indicator_behavior_enum: Optional[Any] = None
        self.healing_cycle: Optional[PositiveInteger] = None
        self.indicator_ref: Optional[ARRef] = None
        self.indicator_failure: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticConnectedIndicator to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticConnectedIndicator, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize behavior_indicator_behavior_enum
        if self.behavior_indicator_behavior_enum is not None:
            serialized = SerializationHelper.serialize_item(self.behavior_indicator_behavior_enum, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BEHAVIOR-INDICATOR-BEHAVIOR-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize healing_cycle
        if self.healing_cycle is not None:
            serialized = SerializationHelper.serialize_item(self.healing_cycle, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HEALING-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize indicator_ref
        if self.indicator_ref is not None:
            serialized = SerializationHelper.serialize_item(self.indicator_ref, "DiagnosticIndicator")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INDICATOR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize indicator_failure
        if self.indicator_failure is not None:
            serialized = SerializationHelper.serialize_item(self.indicator_failure, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INDICATOR-FAILURE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticConnectedIndicator":
        """Deserialize XML element to DiagnosticConnectedIndicator object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticConnectedIndicator object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticConnectedIndicator, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BEHAVIOR-INDICATOR-BEHAVIOR-ENUM":
                setattr(obj, "behavior_indicator_behavior_enum", SerializationHelper.deserialize_by_tag(child, "any (DiagnosticConnected)"))
            elif tag == "HEALING-CYCLE":
                setattr(obj, "healing_cycle", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "INDICATOR-REF":
                setattr(obj, "indicator_ref", ARRef.deserialize(child))
            elif tag == "INDICATOR-FAILURE":
                setattr(obj, "indicator_failure", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class DiagnosticConnectedIndicatorBuilder(IdentifiableBuilder):
    """Builder for DiagnosticConnectedIndicator with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticConnectedIndicator = DiagnosticConnectedIndicator()


    def with_behavior_indicator_behavior_enum(self, value: Optional[any (DiagnosticConnected)]) -> "DiagnosticConnectedIndicatorBuilder":
        """Set behavior_indicator_behavior_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.behavior_indicator_behavior_enum = value
        return self

    def with_healing_cycle(self, value: Optional[PositiveInteger]) -> "DiagnosticConnectedIndicatorBuilder":
        """Set healing_cycle attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.healing_cycle = value
        return self

    def with_indicator(self, value: Optional[DiagnosticIndicator]) -> "DiagnosticConnectedIndicatorBuilder":
        """Set indicator attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.indicator = value
        return self

    def with_indicator_failure(self, value: Optional[PositiveInteger]) -> "DiagnosticConnectedIndicatorBuilder":
        """Set indicator_failure attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.indicator_failure = value
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


    def build(self) -> DiagnosticConnectedIndicator:
        """Build and return the DiagnosticConnectedIndicator instance with validation."""
        self._validate_instance()
        pass
        return self._obj