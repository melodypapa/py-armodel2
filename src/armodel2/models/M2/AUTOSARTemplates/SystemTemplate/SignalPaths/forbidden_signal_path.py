"""ForbiddenSignalPath AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 255)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SignalPaths.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.signal_path_constraint import (
    SignalPathConstraint,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.signal_path_constraint import SignalPathConstraintBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.swc_to_swc_signal import (
    SwcToSwcSignal,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ForbiddenSignalPath(SignalPathConstraint):
    """AUTOSAR ForbiddenSignalPath."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "FORBIDDEN-SIGNAL-PATH"


    operations: list[Any]
    physical_channel_refs: list[ARRef]
    signals: list[SwcToSwcSignal]
    _DESERIALIZE_DISPATCH = {
        "OPERATIONS": lambda obj, elem: obj.operations.append(SerializationHelper.deserialize_by_tag(elem, "any (SwcToSwcOperation)")),
        "PHYSICAL-CHANNEL-REFS": ("_POLYMORPHIC_LIST", "physical_channel_refs", ["AbstractCanPhysicalChannel", "CanPhysicalChannel", "EthernetPhysicalChannel", "FlexrayPhysicalChannel", "LinPhysicalChannel", "TtcanPhysicalChannel"]),
        "SIGNALS": lambda obj, elem: obj.signals.append(SerializationHelper.deserialize_by_tag(elem, "SwcToSwcSignal")),
    }


    def __init__(self) -> None:
        """Initialize ForbiddenSignalPath."""
        super().__init__()
        self.operations: list[Any] = []
        self.physical_channel_refs: list[ARRef] = []
        self.signals: list[SwcToSwcSignal] = []

    def serialize(self) -> ET.Element:
        """Serialize ForbiddenSignalPath to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ForbiddenSignalPath, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize operations (list to container "OPERATIONS")
        if self.operations:
            wrapper = ET.Element("OPERATIONS")
            for item in self.operations:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize physical_channel_refs (list to container "PHYSICAL-CHANNEL-REFS")
        if self.physical_channel_refs:
            wrapper = ET.Element("PHYSICAL-CHANNEL-REFS")
            for item in self.physical_channel_refs:
                serialized = SerializationHelper.serialize_item(item, "PhysicalChannel")
                if serialized is not None:
                    child_elem = ET.Element("PHYSICAL-CHANNEL-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize signals (list to container "SIGNALS")
        if self.signals:
            wrapper = ET.Element("SIGNALS")
            for item in self.signals:
                serialized = SerializationHelper.serialize_item(item, "SwcToSwcSignal")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ForbiddenSignalPath":
        """Deserialize XML element to ForbiddenSignalPath object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ForbiddenSignalPath object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ForbiddenSignalPath, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "OPERATIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.operations.append(SerializationHelper.deserialize_by_tag(item_elem, "any (SwcToSwcOperation)"))
            elif tag == "PHYSICAL-CHANNEL-REFS":
                for item_elem in child:
                    obj.physical_channel_refs.append(ARRef.deserialize(item_elem))
            elif tag == "SIGNALS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.signals.append(SerializationHelper.deserialize_by_tag(item_elem, "SwcToSwcSignal"))

        return obj



class ForbiddenSignalPathBuilder(SignalPathConstraintBuilder):
    """Builder for ForbiddenSignalPath with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ForbiddenSignalPath = ForbiddenSignalPath()


    def with_operations(self, items: list[any (SwcToSwcOperation)]) -> "ForbiddenSignalPathBuilder":
        """Set operations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.operations = list(items) if items else []
        return self

    def with_physical_channels(self, items: list[PhysicalChannel]) -> "ForbiddenSignalPathBuilder":
        """Set physical_channels list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.physical_channels = list(items) if items else []
        return self

    def with_signals(self, items: list[SwcToSwcSignal]) -> "ForbiddenSignalPathBuilder":
        """Set signals list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.signals = list(items) if items else []
        return self


    def add_operation(self, item: any (SwcToSwcOperation)) -> "ForbiddenSignalPathBuilder":
        """Add a single item to operations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.operations.append(item)
        return self

    def clear_operations(self) -> "ForbiddenSignalPathBuilder":
        """Clear all items from operations list.

        Returns:
            self for method chaining
        """
        self._obj.operations = []
        return self

    def add_physical_channel(self, item: PhysicalChannel) -> "ForbiddenSignalPathBuilder":
        """Add a single item to physical_channels list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.physical_channels.append(item)
        return self

    def clear_physical_channels(self) -> "ForbiddenSignalPathBuilder":
        """Clear all items from physical_channels list.

        Returns:
            self for method chaining
        """
        self._obj.physical_channels = []
        return self

    def add_signal(self, item: SwcToSwcSignal) -> "ForbiddenSignalPathBuilder":
        """Add a single item to signals list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.signals.append(item)
        return self

    def clear_signals(self) -> "ForbiddenSignalPathBuilder":
        """Clear all items from signals list.

        Returns:
            self for method chaining
        """
        self._obj.signals = []
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


    def build(self) -> ForbiddenSignalPath:
        """Build and return the ForbiddenSignalPath instance with validation."""
        self._validate_instance()
        pass
        return self._obj