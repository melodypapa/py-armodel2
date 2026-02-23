"""MacSecProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 173)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.mac_sec_local_kay_props import (
    MacSecLocalKayProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class MacSecProps(ARObject):
    """AUTOSAR MacSecProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    auto_start: Optional[Boolean]
    mac_sec_kay: Optional[MacSecLocalKayProps]
    on_fail: Optional[TimeValue]
    sak_rekey_time: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize MacSecProps."""
        super().__init__()
        self.auto_start: Optional[Boolean] = None
        self.mac_sec_kay: Optional[MacSecLocalKayProps] = None
        self.on_fail: Optional[TimeValue] = None
        self.sak_rekey_time: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize MacSecProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MacSecProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize auto_start
        if self.auto_start is not None:
            serialized = SerializationHelper.serialize_item(self.auto_start, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AUTO-START")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mac_sec_kay
        if self.mac_sec_kay is not None:
            serialized = SerializationHelper.serialize_item(self.mac_sec_kay, "MacSecLocalKayProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAC-SEC-KAY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize on_fail
        if self.on_fail is not None:
            serialized = SerializationHelper.serialize_item(self.on_fail, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ON-FAIL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sak_rekey_time
        if self.sak_rekey_time is not None:
            serialized = SerializationHelper.serialize_item(self.sak_rekey_time, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SAK-REKEY-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MacSecProps":
        """Deserialize XML element to MacSecProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MacSecProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MacSecProps, cls).deserialize(element)

        # Parse auto_start
        child = SerializationHelper.find_child_element(element, "AUTO-START")
        if child is not None:
            auto_start_value = child.text
            obj.auto_start = auto_start_value

        # Parse mac_sec_kay
        child = SerializationHelper.find_child_element(element, "MAC-SEC-KAY")
        if child is not None:
            mac_sec_kay_value = SerializationHelper.deserialize_by_tag(child, "MacSecLocalKayProps")
            obj.mac_sec_kay = mac_sec_kay_value

        # Parse on_fail
        child = SerializationHelper.find_child_element(element, "ON-FAIL")
        if child is not None:
            on_fail_value = child.text
            obj.on_fail = on_fail_value

        # Parse sak_rekey_time
        child = SerializationHelper.find_child_element(element, "SAK-REKEY-TIME")
        if child is not None:
            sak_rekey_time_value = child.text
            obj.sak_rekey_time = sak_rekey_time_value

        return obj



class MacSecPropsBuilder(BuilderBase):
    """Builder for MacSecProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MacSecProps = MacSecProps()


    def with_auto_start(self, value: Optional[Boolean]) -> "MacSecPropsBuilder":
        """Set auto_start attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.auto_start = value
        return self

    def with_mac_sec_kay(self, value: Optional[MacSecLocalKayProps]) -> "MacSecPropsBuilder":
        """Set mac_sec_kay attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mac_sec_kay = value
        return self

    def with_on_fail(self, value: Optional[TimeValue]) -> "MacSecPropsBuilder":
        """Set on_fail attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.on_fail = value
        return self

    def with_sak_rekey_time(self, value: Optional[TimeValue]) -> "MacSecPropsBuilder":
        """Set sak_rekey_time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sak_rekey_time = value
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


    def build(self) -> MacSecProps:
        """Build and return the MacSecProps instance with validation."""
        self._validate_instance()
        pass
        return self._obj