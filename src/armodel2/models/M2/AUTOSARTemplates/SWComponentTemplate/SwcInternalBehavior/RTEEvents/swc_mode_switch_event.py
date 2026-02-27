"""SwcModeSwitchEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 544)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import instance_ref
from armodel2.serialization.decorators import ref_conditional

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import RTEEventBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import (
    ModeActivationKind,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.r_mode_in_atomic_swc_instance_ref import (
    RModeInAtomicSwcInstanceRef,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwcModeSwitchEvent(RTEEvent):
    """AUTOSAR SwcModeSwitchEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    activation: Optional[ModeActivationKind]
    _mode_iref: Optional[RModeInAtomicSwcInstanceRef]
    def __init__(self) -> None:
        """Initialize SwcModeSwitchEvent."""
        super().__init__()
        self.activation: Optional[ModeActivationKind] = None
        self._mode_iref: Optional[RModeInAtomicSwcInstanceRef] = None
    @property
    @instance_ref(flatten=True, list_type='multi')
    def mode_iref(self) -> Optional[RModeInAtomicSwcInstanceRef]:
        """Get mode_iref instance reference."""
        return self._mode_iref

    @mode_iref.setter
    def mode_iref(self, value: Optional[RModeInAtomicSwcInstanceRef]) -> None:
        """Set mode_iref instance reference."""
        self._mode_iref = value


    def serialize(self) -> ET.Element:
        """Serialize SwcModeSwitchEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwcModeSwitchEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize activation
        if self.activation is not None:
            serialized = SerializationHelper.serialize_item(self.activation, "ModeActivationKind")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACTIVATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mode_iref (instance reference with wrapper "MODE-IREF")
        if self.mode_iref is not None:
            serialized = SerializationHelper.serialize_item(self.mode_iref, "RModeInAtomicSwcInstanceRef")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("MODE-IREF")
                # Flatten: append children of serialized element directly to iref wrapper
                for child in serialized:
                    iref_wrapper.append(child)
                elem.append(iref_wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcModeSwitchEvent":
        """Deserialize XML element to SwcModeSwitchEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcModeSwitchEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwcModeSwitchEvent, cls).deserialize(element)

        # Parse activation
        child = SerializationHelper.find_child_element(element, "ACTIVATION")
        if child is not None:
            activation_value = ModeActivationKind.deserialize(child)
            obj.activation = activation_value

        # Parse mode_iref (instance reference from wrapper "MODE-IREF")
        wrapper = SerializationHelper.find_child_element(element, "MODE-IREF")
        if wrapper is not None:
            # Deserialize wrapper element directly as the type (flattened structure)
            mode_iref_value = SerializationHelper.deserialize_by_tag(wrapper, "RModeInAtomicSwcInstanceRef")
            obj.mode_iref = mode_iref_value

        return obj



class SwcModeSwitchEventBuilder(RTEEventBuilder):
    """Builder for SwcModeSwitchEvent with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwcModeSwitchEvent = SwcModeSwitchEvent()


    def with_activation(self, value: Optional[ModeActivationKind]) -> "SwcModeSwitchEventBuilder":
        """Set activation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.activation = value
        return self

    def with_mode(self, value: Optional[RModeInAtomicSwcInstanceRef]) -> "SwcModeSwitchEventBuilder":
        """Set mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mode = value
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


    def build(self) -> SwcModeSwitchEvent:
        """Build and return the SwcModeSwitchEvent instance with validation."""
        self._validate_instance()
        pass
        return self._obj