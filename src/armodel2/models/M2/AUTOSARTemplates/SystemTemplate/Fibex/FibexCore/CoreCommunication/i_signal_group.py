"""ISignalGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 993)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 323)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import FibexElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_transformation import (
    DataTransformation,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal import (
    ISignal,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal_group import (
    SystemSignalGroup,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ISignalGroup(FibexElement):
    """AUTOSAR ISignalGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "I-SIGNAL-GROUP"


    com_based_ref: Optional[ARRef]
    i_signal_refs: list[ARRef]
    system_signal_group_ref: Optional[ARRef]
    transformation_i_signals: list[Any]
    _DESERIALIZE_DISPATCH = {
        "COM-BASED-REF": lambda obj, elem: setattr(obj, "com_based_ref", ARRef.deserialize(elem)),
        "I-SIGNAL-REFS": lambda obj, elem: obj.i_signal_refs.append(ARRef.deserialize(elem)),
        "SYSTEM-SIGNAL-GROUP-REF": lambda obj, elem: setattr(obj, "system_signal_group_ref", ARRef.deserialize(elem)),
        "TRANSFORMATION-I-SIGNALS": lambda obj, elem: obj.transformation_i_signals.append(SerializationHelper.deserialize_by_tag(elem, "any (TransformationISignal)")),
    }


    def __init__(self) -> None:
        """Initialize ISignalGroup."""
        super().__init__()
        self.com_based_ref: Optional[ARRef] = None
        self.i_signal_refs: list[ARRef] = []
        self.system_signal_group_ref: Optional[ARRef] = None
        self.transformation_i_signals: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize ISignalGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ISignalGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize com_based_ref
        if self.com_based_ref is not None:
            serialized = SerializationHelper.serialize_item(self.com_based_ref, "DataTransformation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COM-BASED-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize i_signal_refs (list to container "I-SIGNAL-REFS")
        if self.i_signal_refs:
            wrapper = ET.Element("I-SIGNAL-REFS")
            for item in self.i_signal_refs:
                serialized = SerializationHelper.serialize_item(item, "ISignal")
                if serialized is not None:
                    child_elem = ET.Element("I-SIGNAL-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize system_signal_group_ref
        if self.system_signal_group_ref is not None:
            serialized = SerializationHelper.serialize_item(self.system_signal_group_ref, "SystemSignalGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYSTEM-SIGNAL-GROUP-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transformation_i_signals (list to container "TRANSFORMATION-I-SIGNALS")
        if self.transformation_i_signals:
            wrapper = ET.Element("TRANSFORMATION-I-SIGNALS")
            for item in self.transformation_i_signals:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ISignalGroup":
        """Deserialize XML element to ISignalGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ISignalGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ISignalGroup, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "COM-BASED-REF":
                setattr(obj, "com_based_ref", ARRef.deserialize(child))
            elif tag == "I-SIGNAL-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.i_signal_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "ISignal"))
            elif tag == "SYSTEM-SIGNAL-GROUP-REF":
                setattr(obj, "system_signal_group_ref", ARRef.deserialize(child))
            elif tag == "TRANSFORMATION-I-SIGNALS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.transformation_i_signals.append(SerializationHelper.deserialize_by_tag(item_elem, "any (TransformationISignal)"))

        return obj



class ISignalGroupBuilder(FibexElementBuilder):
    """Builder for ISignalGroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ISignalGroup = ISignalGroup()


    def with_com_based(self, value: Optional[DataTransformation]) -> "ISignalGroupBuilder":
        """Set com_based attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.com_based = value
        return self

    def with_i_signals(self, items: list[ISignal]) -> "ISignalGroupBuilder":
        """Set i_signals list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.i_signals = list(items) if items else []
        return self

    def with_system_signal_group(self, value: Optional[SystemSignalGroup]) -> "ISignalGroupBuilder":
        """Set system_signal_group attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.system_signal_group = value
        return self

    def with_transformation_i_signals(self, items: list[any (TransformationISignal)]) -> "ISignalGroupBuilder":
        """Set transformation_i_signals list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.transformation_i_signals = list(items) if items else []
        return self


    def add_i_signal(self, item: ISignal) -> "ISignalGroupBuilder":
        """Add a single item to i_signals list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.i_signals.append(item)
        return self

    def clear_i_signals(self) -> "ISignalGroupBuilder":
        """Clear all items from i_signals list.

        Returns:
            self for method chaining
        """
        self._obj.i_signals = []
        return self

    def add_transformation_i_signal(self, item: any (TransformationISignal)) -> "ISignalGroupBuilder":
        """Add a single item to transformation_i_signals list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.transformation_i_signals.append(item)
        return self

    def clear_transformation_i_signals(self) -> "ISignalGroupBuilder":
        """Clear all items from transformation_i_signals list.

        Returns:
            self for method chaining
        """
        self._obj.transformation_i_signals = []
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


    def build(self) -> ISignalGroup:
        """Build and return the ISignalGroup instance with validation."""
        self._validate_instance()
        pass
        return self._obj