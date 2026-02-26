"""DiagnosticTroubleCodeUds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 173)

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
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode import (
    DiagnosticUdsSeverityEnum,
    DiagnosticWwhObdDtcClassEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.event_obd_readiness_group import (
    EventObdReadinessGroup,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticTroubleCodeUds(DiagnosticTroubleCode):
    """AUTOSAR DiagnosticTroubleCodeUds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    consider_pto: Optional[Boolean]
    dtc_props_props_ref: Optional[ARRef]
    event_readiness: Optional[EventObdReadinessGroup]
    functional_unit: Optional[PositiveInteger]
    obd_dtc: Optional[PositiveInteger]
    severity: Optional[DiagnosticUdsSeverityEnum]
    uds_dtc_value: Optional[PositiveInteger]
    wwh_obd_dtc: Optional[DiagnosticWwhObdDtcClassEnum]
    def __init__(self) -> None:
        """Initialize DiagnosticTroubleCodeUds."""
        super().__init__()
        self.consider_pto: Optional[Boolean] = None
        self.dtc_props_props_ref: Optional[ARRef] = None
        self.event_readiness: Optional[EventObdReadinessGroup] = None
        self.functional_unit: Optional[PositiveInteger] = None
        self.obd_dtc: Optional[PositiveInteger] = None
        self.severity: Optional[DiagnosticUdsSeverityEnum] = None
        self.uds_dtc_value: Optional[PositiveInteger] = None
        self.wwh_obd_dtc: Optional[DiagnosticWwhObdDtcClassEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticTroubleCodeUds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticTroubleCodeUds, self).serialize()

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

        # Serialize functional_unit
        if self.functional_unit is not None:
            serialized = SerializationHelper.serialize_item(self.functional_unit, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FUNCTIONAL-UNIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize obd_dtc
        if self.obd_dtc is not None:
            serialized = SerializationHelper.serialize_item(self.obd_dtc, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OBD-DTC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize severity
        if self.severity is not None:
            serialized = SerializationHelper.serialize_item(self.severity, "DiagnosticUdsSeverityEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SEVERITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize uds_dtc_value
        if self.uds_dtc_value is not None:
            serialized = SerializationHelper.serialize_item(self.uds_dtc_value, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UDS-DTC-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize wwh_obd_dtc
        if self.wwh_obd_dtc is not None:
            serialized = SerializationHelper.serialize_item(self.wwh_obd_dtc, "DiagnosticWwhObdDtcClassEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WWH-OBD-DTC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTroubleCodeUds":
        """Deserialize XML element to DiagnosticTroubleCodeUds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticTroubleCodeUds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticTroubleCodeUds, cls).deserialize(element)

        # Parse consider_pto
        child = SerializationHelper.find_child_element(element, "CONSIDER-PTO")
        if child is not None:
            consider_pto_value = child.text
            obj.consider_pto = consider_pto_value

        # Parse dtc_props_props_ref
        child = SerializationHelper.find_child_element(element, "DTC-PROPS-PROPS-REF")
        if child is not None:
            dtc_props_props_ref_value = ARRef.deserialize(child)
            obj.dtc_props_props_ref = dtc_props_props_ref_value

        # Parse event_readiness
        child = SerializationHelper.find_child_element(element, "EVENT-READINESS")
        if child is not None:
            event_readiness_value = SerializationHelper.deserialize_by_tag(child, "EventObdReadinessGroup")
            obj.event_readiness = event_readiness_value

        # Parse functional_unit
        child = SerializationHelper.find_child_element(element, "FUNCTIONAL-UNIT")
        if child is not None:
            functional_unit_value = child.text
            obj.functional_unit = functional_unit_value

        # Parse obd_dtc
        child = SerializationHelper.find_child_element(element, "OBD-DTC")
        if child is not None:
            obd_dtc_value = child.text
            obj.obd_dtc = obd_dtc_value

        # Parse severity
        child = SerializationHelper.find_child_element(element, "SEVERITY")
        if child is not None:
            severity_value = DiagnosticUdsSeverityEnum.deserialize(child)
            obj.severity = severity_value

        # Parse uds_dtc_value
        child = SerializationHelper.find_child_element(element, "UDS-DTC-VALUE")
        if child is not None:
            uds_dtc_value_value = child.text
            obj.uds_dtc_value = uds_dtc_value_value

        # Parse wwh_obd_dtc
        child = SerializationHelper.find_child_element(element, "WWH-OBD-DTC")
        if child is not None:
            wwh_obd_dtc_value = DiagnosticWwhObdDtcClassEnum.deserialize(child)
            obj.wwh_obd_dtc = wwh_obd_dtc_value

        return obj



class DiagnosticTroubleCodeUdsBuilder(DiagnosticTroubleCodeBuilder):
    """Builder for DiagnosticTroubleCodeUds with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticTroubleCodeUds = DiagnosticTroubleCodeUds()


    def with_consider_pto(self, value: Optional[Boolean]) -> "DiagnosticTroubleCodeUdsBuilder":
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

    def with_dtc_props_props(self, value: Optional[DiagnosticTroubleCode]) -> "DiagnosticTroubleCodeUdsBuilder":
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

    def with_event_readiness(self, value: Optional[EventObdReadinessGroup]) -> "DiagnosticTroubleCodeUdsBuilder":
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

    def with_functional_unit(self, value: Optional[PositiveInteger]) -> "DiagnosticTroubleCodeUdsBuilder":
        """Set functional_unit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.functional_unit = value
        return self

    def with_obd_dtc(self, value: Optional[PositiveInteger]) -> "DiagnosticTroubleCodeUdsBuilder":
        """Set obd_dtc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.obd_dtc = value
        return self

    def with_severity(self, value: Optional[DiagnosticUdsSeverityEnum]) -> "DiagnosticTroubleCodeUdsBuilder":
        """Set severity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.severity = value
        return self

    def with_uds_dtc_value(self, value: Optional[PositiveInteger]) -> "DiagnosticTroubleCodeUdsBuilder":
        """Set uds_dtc_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uds_dtc_value = value
        return self

    def with_wwh_obd_dtc(self, value: Optional[DiagnosticWwhObdDtcClassEnum]) -> "DiagnosticTroubleCodeUdsBuilder":
        """Set wwh_obd_dtc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.wwh_obd_dtc = value
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


    def build(self) -> DiagnosticTroubleCodeUds:
        """Build and return the DiagnosticTroubleCodeUds instance with validation."""
        self._validate_instance()
        pass
        return self._obj