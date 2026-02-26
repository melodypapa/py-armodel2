"""AppOsTaskProxyToEcuTaskProxyMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 209)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_RteEventToOsTaskMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping.os_task_proxy import (
    OsTaskProxy,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AppOsTaskProxyToEcuTaskProxyMapping(Identifiable):
    """AUTOSAR AppOsTaskProxyToEcuTaskProxyMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    app_task_proxy_ref: Optional[ARRef]
    ecu_task_proxy_ref: Optional[ARRef]
    offset: Optional[Integer]
    def __init__(self) -> None:
        """Initialize AppOsTaskProxyToEcuTaskProxyMapping."""
        super().__init__()
        self.app_task_proxy_ref: Optional[ARRef] = None
        self.ecu_task_proxy_ref: Optional[ARRef] = None
        self.offset: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize AppOsTaskProxyToEcuTaskProxyMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AppOsTaskProxyToEcuTaskProxyMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize app_task_proxy_ref
        if self.app_task_proxy_ref is not None:
            serialized = SerializationHelper.serialize_item(self.app_task_proxy_ref, "OsTaskProxy")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("APP-TASK-PROXY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ecu_task_proxy_ref
        if self.ecu_task_proxy_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ecu_task_proxy_ref, "OsTaskProxy")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-TASK-PROXY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize offset
        if self.offset is not None:
            serialized = SerializationHelper.serialize_item(self.offset, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AppOsTaskProxyToEcuTaskProxyMapping":
        """Deserialize XML element to AppOsTaskProxyToEcuTaskProxyMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AppOsTaskProxyToEcuTaskProxyMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AppOsTaskProxyToEcuTaskProxyMapping, cls).deserialize(element)

        # Parse app_task_proxy_ref
        child = SerializationHelper.find_child_element(element, "APP-TASK-PROXY-REF")
        if child is not None:
            app_task_proxy_ref_value = ARRef.deserialize(child)
            obj.app_task_proxy_ref = app_task_proxy_ref_value

        # Parse ecu_task_proxy_ref
        child = SerializationHelper.find_child_element(element, "ECU-TASK-PROXY-REF")
        if child is not None:
            ecu_task_proxy_ref_value = ARRef.deserialize(child)
            obj.ecu_task_proxy_ref = ecu_task_proxy_ref_value

        # Parse offset
        child = SerializationHelper.find_child_element(element, "OFFSET")
        if child is not None:
            offset_value = child.text
            obj.offset = offset_value

        return obj



class AppOsTaskProxyToEcuTaskProxyMappingBuilder(IdentifiableBuilder):
    """Builder for AppOsTaskProxyToEcuTaskProxyMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AppOsTaskProxyToEcuTaskProxyMapping = AppOsTaskProxyToEcuTaskProxyMapping()


    def with_app_task_proxy(self, value: Optional[OsTaskProxy]) -> "AppOsTaskProxyToEcuTaskProxyMappingBuilder":
        """Set app_task_proxy attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.app_task_proxy = value
        return self

    def with_ecu_task_proxy(self, value: Optional[OsTaskProxy]) -> "AppOsTaskProxyToEcuTaskProxyMappingBuilder":
        """Set ecu_task_proxy attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ecu_task_proxy = value
        return self

    def with_offset(self, value: Optional[Integer]) -> "AppOsTaskProxyToEcuTaskProxyMappingBuilder":
        """Set offset attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.offset = value
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


    def build(self) -> AppOsTaskProxyToEcuTaskProxyMapping:
        """Build and return the AppOsTaskProxyToEcuTaskProxyMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj