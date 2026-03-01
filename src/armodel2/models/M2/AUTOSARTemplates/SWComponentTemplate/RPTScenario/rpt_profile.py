"""RptProfile AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 853)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_RPTScenario.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport import (
    RptEnablerImplTypeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class RptProfile(Identifiable):
    """AUTOSAR RptProfile."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "RPT-PROFILE"


    max_service: Optional[PositiveInteger]
    min_service_point: Optional[PositiveInteger]
    service_point: Optional[CIdentifier]
    stim_enabler: Optional[RptEnablerImplTypeEnum]
    _DESERIALIZE_DISPATCH = {
        "MAX-SERVICE": lambda obj, elem: setattr(obj, "max_service", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MIN-SERVICE-POINT": lambda obj, elem: setattr(obj, "min_service_point", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SERVICE-POINT": lambda obj, elem: setattr(obj, "service_point", SerializationHelper.deserialize_by_tag(elem, "CIdentifier")),
        "STIM-ENABLER": lambda obj, elem: setattr(obj, "stim_enabler", RptEnablerImplTypeEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize RptProfile."""
        super().__init__()
        self.max_service: Optional[PositiveInteger] = None
        self.min_service_point: Optional[PositiveInteger] = None
        self.service_point: Optional[CIdentifier] = None
        self.stim_enabler: Optional[RptEnablerImplTypeEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize RptProfile to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RptProfile, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize max_service
        if self.max_service is not None:
            serialized = SerializationHelper.serialize_item(self.max_service, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-SERVICE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_service_point
        if self.min_service_point is not None:
            serialized = SerializationHelper.serialize_item(self.min_service_point, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-SERVICE-POINT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize service_point
        if self.service_point is not None:
            serialized = SerializationHelper.serialize_item(self.service_point, "CIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-POINT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize stim_enabler
        if self.stim_enabler is not None:
            serialized = SerializationHelper.serialize_item(self.stim_enabler, "RptEnablerImplTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STIM-ENABLER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptProfile":
        """Deserialize XML element to RptProfile object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RptProfile object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RptProfile, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "MAX-SERVICE":
                setattr(obj, "max_service", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "MIN-SERVICE-POINT":
                setattr(obj, "min_service_point", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SERVICE-POINT":
                setattr(obj, "service_point", SerializationHelper.deserialize_by_tag(child, "CIdentifier"))
            elif tag == "STIM-ENABLER":
                setattr(obj, "stim_enabler", RptEnablerImplTypeEnum.deserialize(child))

        return obj



class RptProfileBuilder(IdentifiableBuilder):
    """Builder for RptProfile with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RptProfile = RptProfile()


    def with_max_service(self, value: Optional[PositiveInteger]) -> "RptProfileBuilder":
        """Set max_service attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_service = value
        return self

    def with_min_service_point(self, value: Optional[PositiveInteger]) -> "RptProfileBuilder":
        """Set min_service_point attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.min_service_point = value
        return self

    def with_service_point(self, value: Optional[CIdentifier]) -> "RptProfileBuilder":
        """Set service_point attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.service_point = value
        return self

    def with_stim_enabler(self, value: Optional[RptEnablerImplTypeEnum]) -> "RptProfileBuilder":
        """Set stim_enabler attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.stim_enabler = value
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


    def build(self) -> RptProfile:
        """Build and return the RptProfile instance with validation."""
        self._validate_instance()
        pass
        return self._obj