"""SwCalprmRefProxy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 370)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_DatadictionaryProxies.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_parameter_ref import (
    AutosarParameterRef,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_data_instance import (
    McDataInstance,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwCalprmRefProxy(ARObject):
    """AUTOSAR SwCalprmRefProxy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ar_parameter_ref: Optional[ARRef]
    mc_data_instance_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SwCalprmRefProxy."""
        super().__init__()
        self.ar_parameter_ref: Optional[ARRef] = None
        self.mc_data_instance_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SwCalprmRefProxy to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwCalprmRefProxy, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ar_parameter_ref
        if self.ar_parameter_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ar_parameter_ref, "AutosarParameterRef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AR-PARAMETER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mc_data_instance_ref
        if self.mc_data_instance_ref is not None:
            serialized = SerializationHelper.serialize_item(self.mc_data_instance_ref, "McDataInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MC-DATA-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwCalprmRefProxy":
        """Deserialize XML element to SwCalprmRefProxy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwCalprmRefProxy object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwCalprmRefProxy, cls).deserialize(element)

        # Parse ar_parameter_ref
        child = SerializationHelper.find_child_element(element, "AR-PARAMETER-REF")
        if child is not None:
            ar_parameter_ref_value = ARRef.deserialize(child)
            obj.ar_parameter_ref = ar_parameter_ref_value

        # Parse mc_data_instance_ref
        child = SerializationHelper.find_child_element(element, "MC-DATA-INSTANCE-REF")
        if child is not None:
            mc_data_instance_ref_value = ARRef.deserialize(child)
            obj.mc_data_instance_ref = mc_data_instance_ref_value

        return obj



class SwCalprmRefProxyBuilder(BuilderBase):
    """Builder for SwCalprmRefProxy with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwCalprmRefProxy = SwCalprmRefProxy()


    def with_ar_parameter(self, value: Optional[AutosarParameterRef]) -> "SwCalprmRefProxyBuilder":
        """Set ar_parameter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ar_parameter = value
        return self

    def with_mc_data_instance(self, value: Optional[McDataInstance]) -> "SwCalprmRefProxyBuilder":
        """Set mc_data_instance attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mc_data_instance = value
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


    def build(self) -> SwCalprmRefProxy:
        """Build and return the SwCalprmRefProxy instance with validation."""
        self._validate_instance()
        pass
        return self._obj