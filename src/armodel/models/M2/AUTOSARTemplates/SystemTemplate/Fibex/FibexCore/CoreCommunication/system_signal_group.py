"""SystemSignalGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 324)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class SystemSignalGroup(ARElement):
    """AUTOSAR SystemSignalGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    system_signal_refs: list[ARRef]
    transforming_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SystemSignalGroup."""
        super().__init__()
        self.system_signal_refs: list[ARRef] = []
        self.transforming_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SystemSignalGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SystemSignalGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize system_signal_refs (list to container "SYSTEM-SIGNAL-REFS")
        if self.system_signal_refs:
            wrapper = ET.Element("SYSTEM-SIGNAL-REFS")
            for item in self.system_signal_refs:
                serialized = SerializationHelper.serialize_item(item, "SystemSignal")
                if serialized is not None:
                    child_elem = ET.Element("SYSTEM-SIGNAL-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize transforming_ref
        if self.transforming_ref is not None:
            serialized = SerializationHelper.serialize_item(self.transforming_ref, "SystemSignal")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSFORMING-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SystemSignalGroup":
        """Deserialize XML element to SystemSignalGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SystemSignalGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SystemSignalGroup, cls).deserialize(element)

        # Parse system_signal_refs (list from container "SYSTEM-SIGNAL-REFS")
        obj.system_signal_refs = []
        container = SerializationHelper.find_child_element(element, "SYSTEM-SIGNAL-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.system_signal_refs.append(child_value)

        # Parse transforming_ref
        child = SerializationHelper.find_child_element(element, "TRANSFORMING-REF")
        if child is not None:
            transforming_ref_value = ARRef.deserialize(child)
            obj.transforming_ref = transforming_ref_value

        return obj



class SystemSignalGroupBuilder(ARElementBuilder):
    """Builder for SystemSignalGroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SystemSignalGroup = SystemSignalGroup()


    def with_system_signals(self, items: list[SystemSignal]) -> "SystemSignalGroupBuilder":
        """Set system_signals list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.system_signals = list(items) if items else []
        return self

    def with_transforming(self, value: Optional[SystemSignal]) -> "SystemSignalGroupBuilder":
        """Set transforming attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.transforming = value
        return self


    def add_system_signal(self, item: SystemSignal) -> "SystemSignalGroupBuilder":
        """Add a single item to system_signals list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.system_signals.append(item)
        return self

    def clear_system_signals(self) -> "SystemSignalGroupBuilder":
        """Clear all items from system_signals list.

        Returns:
            self for method chaining
        """
        self._obj.system_signals = []
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


    def build(self) -> SystemSignalGroup:
        """Build and return the SystemSignalGroup instance with validation."""
        self._validate_instance()
        pass
        return self._obj