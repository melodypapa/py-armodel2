"""OperationInvokedEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 325)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 543)

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
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.p_operation_in_atomic_swc_instance_ref import (
    POperationInAtomicSwcInstanceRef,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class OperationInvokedEvent(RTEEvent):
    """AUTOSAR OperationInvokedEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _operation_iref: Optional[POperationInAtomicSwcInstanceRef]
    def __init__(self) -> None:
        """Initialize OperationInvokedEvent."""
        super().__init__()
        self._operation_iref: Optional[POperationInAtomicSwcInstanceRef] = None
    @property
    @instance_ref(flatten=True)
    def operation_iref(self) -> Optional[POperationInAtomicSwcInstanceRef]:
        """Get operation_iref instance reference."""
        return self._operation_iref

    @operation_iref.setter
    def operation_iref(self, value: Optional[POperationInAtomicSwcInstanceRef]) -> None:
        """Set operation_iref instance reference."""
        self._operation_iref = value


    def serialize(self) -> ET.Element:
        """Serialize OperationInvokedEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(OperationInvokedEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize operation_iref (instance reference with wrapper "OPERATION-IREF")
        if self.operation_iref is not None:
            serialized = SerializationHelper.serialize_item(self.operation_iref, "POperationInAtomicSwcInstanceRef")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("OPERATION-IREF")
                # Flatten: append children of serialized element directly to iref wrapper
                for child in serialized:
                    iref_wrapper.append(child)
                elem.append(iref_wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "OperationInvokedEvent":
        """Deserialize XML element to OperationInvokedEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized OperationInvokedEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(OperationInvokedEvent, cls).deserialize(element)

        # Parse operation_iref (instance reference from wrapper "OPERATION-IREF")
        wrapper = SerializationHelper.find_child_element(element, "OPERATION-IREF")
        if wrapper is not None:
            # Deserialize wrapper element directly as the type (flattened structure)
            operation_iref_value = SerializationHelper.deserialize_by_tag(wrapper, "POperationInAtomicSwcInstanceRef")
            obj.operation_iref = operation_iref_value

        return obj



class OperationInvokedEventBuilder(RTEEventBuilder):
    """Builder for OperationInvokedEvent with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: OperationInvokedEvent = OperationInvokedEvent()


    def with_operation(self, value: Optional[POperationInAtomicSwcInstanceRef]) -> "OperationInvokedEventBuilder":
        """Set operation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.operation = value
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


    def build(self) -> OperationInvokedEvent:
        """Build and return the OperationInvokedEvent instance with validation."""
        self._validate_instance()
        pass
        return self._obj