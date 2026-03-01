"""DiagnosticTroubleCodeObd AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 174)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code import (
    DiagnosticTroubleCode,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code import DiagnosticTroubleCodeBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.event_obd_readiness_group import (
    EventObdReadinessGroup,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticTroubleCodeObd(DiagnosticTroubleCode):
    """AUTOSAR DiagnosticTroubleCodeObd."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-TROUBLE-CODE-OBD"


    consider_pto: Optional[Boolean]
    dtc_props_props_ref: Optional[ARRef]
    event_readiness: Optional[EventObdReadinessGroup]
    obd_dtc_value: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "CONSIDER-PTO": lambda obj, elem: setattr(obj, "consider_pto", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "DTC-PROPS-PROPS-REF": ("_POLYMORPHIC", "dtc_props_props_ref", ["DiagnosticTroubleCodeJ1939", "DiagnosticTroubleCodeObd", "DiagnosticTroubleCodeUds"]),
        "EVENT-READINESS": lambda obj, elem: setattr(obj, "event_readiness", SerializationHelper.deserialize_by_tag(elem, "EventObdReadinessGroup")),
        "OBD-DTC-VALUE": lambda obj, elem: setattr(obj, "obd_dtc_value", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticTroubleCodeObd."""
        super().__init__()
        self.consider_pto: Optional[Boolean] = None
        self.dtc_props_props_ref: Optional[ARRef] = None
        self.event_readiness: Optional[EventObdReadinessGroup] = None
        self.obd_dtc_value: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticTroubleCodeObd to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticTroubleCodeObd, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize consider_pto
        if self.consider_pto is not None:
            serialized = SerializationHelper.serialize_item(self.consider_pto, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONSIDER-PTO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dtc_props_props_ref
        if self.dtc_props_props_ref is not None:
            serialized = SerializationHelper.serialize_item(self.dtc_props_props_ref, "DiagnosticTroubleCode")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DTC-PROPS-PROPS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize event_readiness
        if self.event_readiness is not None:
            serialized = SerializationHelper.serialize_item(self.event_readiness, "EventObdReadinessGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-READINESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize obd_dtc_value
        if self.obd_dtc_value is not None:
            serialized = SerializationHelper.serialize_item(self.obd_dtc_value, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OBD-DTC-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTroubleCodeObd":
        """Deserialize XML element to DiagnosticTroubleCodeObd object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticTroubleCodeObd object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticTroubleCodeObd, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONSIDER-PTO":
                setattr(obj, "consider_pto", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "DTC-PROPS-PROPS-REF":
                setattr(obj, "dtc_props_props_ref", ARRef.deserialize(child))
            elif tag == "EVENT-READINESS":
                setattr(obj, "event_readiness", SerializationHelper.deserialize_by_tag(child, "EventObdReadinessGroup"))
            elif tag == "OBD-DTC-VALUE":
                setattr(obj, "obd_dtc_value", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class DiagnosticTroubleCodeObdBuilder(DiagnosticTroubleCodeBuilder):
    """Builder for DiagnosticTroubleCodeObd with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticTroubleCodeObd = DiagnosticTroubleCodeObd()


    def with_consider_pto(self, value: Optional[Boolean]) -> "DiagnosticTroubleCodeObdBuilder":
        """Set consider_pto attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.consider_pto = value
        return self

    def with_dtc_props_props(self, value: Optional[DiagnosticTroubleCode]) -> "DiagnosticTroubleCodeObdBuilder":
        """Set dtc_props_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dtc_props_props = value
        return self

    def with_event_readiness(self, value: Optional[EventObdReadinessGroup]) -> "DiagnosticTroubleCodeObdBuilder":
        """Set event_readiness attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.event_readiness = value
        return self

    def with_obd_dtc_value(self, value: Optional[PositiveInteger]) -> "DiagnosticTroubleCodeObdBuilder":
        """Set obd_dtc_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.obd_dtc_value = value
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


    def build(self) -> DiagnosticTroubleCodeObd:
        """Build and return the DiagnosticTroubleCodeObd instance with validation."""
        self._validate_instance()
        pass
        return self._obj