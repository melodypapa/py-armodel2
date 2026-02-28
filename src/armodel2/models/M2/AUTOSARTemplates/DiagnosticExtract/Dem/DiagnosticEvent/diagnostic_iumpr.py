"""DiagnosticIumpr AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 210)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticEvent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import DiagnosticCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent import (
    DiagnosticIumprKindEnum,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticIumpr(DiagnosticCommonElement):
    """AUTOSAR DiagnosticIumpr."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-IUMPR"


    event_ref: Optional[ARRef]
    ratio_kind: Optional[DiagnosticIumprKindEnum]
    _DESERIALIZE_DISPATCH = {
        "EVENT-REF": lambda obj, elem: setattr(obj, "event_ref", ARRef.deserialize(elem)),
        "RATIO-KIND": lambda obj, elem: setattr(obj, "ratio_kind", DiagnosticIumprKindEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticIumpr."""
        super().__init__()
        self.event_ref: Optional[ARRef] = None
        self.ratio_kind: Optional[DiagnosticIumprKindEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticIumpr to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticIumpr, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize event_ref
        if self.event_ref is not None:
            serialized = SerializationHelper.serialize_item(self.event_ref, "DiagnosticEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ratio_kind
        if self.ratio_kind is not None:
            serialized = SerializationHelper.serialize_item(self.ratio_kind, "DiagnosticIumprKindEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RATIO-KIND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticIumpr":
        """Deserialize XML element to DiagnosticIumpr object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticIumpr object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticIumpr, cls).deserialize(element)

        # Parse event_ref
        child = SerializationHelper.find_child_element(element, "EVENT-REF")
        if child is not None:
            event_ref_value = ARRef.deserialize(child)
            obj.event_ref = event_ref_value

        # Parse ratio_kind
        child = SerializationHelper.find_child_element(element, "RATIO-KIND")
        if child is not None:
            ratio_kind_value = DiagnosticIumprKindEnum.deserialize(child)
            obj.ratio_kind = ratio_kind_value

        return obj



class DiagnosticIumprBuilder(DiagnosticCommonElementBuilder):
    """Builder for DiagnosticIumpr with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticIumpr = DiagnosticIumpr()


    def with_event(self, value: Optional[DiagnosticEvent]) -> "DiagnosticIumprBuilder":
        """Set event attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.event = value
        return self

    def with_ratio_kind(self, value: Optional[DiagnosticIumprKindEnum]) -> "DiagnosticIumprBuilder":
        """Set ratio_kind attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ratio_kind = value
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


    def build(self) -> DiagnosticIumpr:
        """Build and return the DiagnosticIumpr instance with validation."""
        self._validate_instance()
        pass
        return self._obj