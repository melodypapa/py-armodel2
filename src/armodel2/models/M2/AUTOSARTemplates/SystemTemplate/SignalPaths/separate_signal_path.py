"""SeparateSignalPath AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 257)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SignalPaths.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.signal_path_constraint import (
    SignalPathConstraint,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.signal_path_constraint import SignalPathConstraintBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.swc_to_swc_signal import (
    SwcToSwcSignal,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SeparateSignalPath(SignalPathConstraint):
    """AUTOSAR SeparateSignalPath."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SEPARATE-SIGNAL-PATH"


    operations: list[Any]
    signals: list[SwcToSwcSignal]
    _DESERIALIZE_DISPATCH = {
        "OPERATIONS": lambda obj, elem: obj.operations.append(SerializationHelper.deserialize_by_tag(elem, "any (SwcToSwcOperation)")),
        "SIGNALS": lambda obj, elem: obj.signals.append(SerializationHelper.deserialize_by_tag(elem, "SwcToSwcSignal")),
    }


    def __init__(self) -> None:
        """Initialize SeparateSignalPath."""
        super().__init__()
        self.operations: list[Any] = []
        self.signals: list[SwcToSwcSignal] = []

    def serialize(self) -> ET.Element:
        """Serialize SeparateSignalPath to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SeparateSignalPath, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "SeparateSignalPath":
        """Deserialize XML element to SeparateSignalPath object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SeparateSignalPath object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SeparateSignalPath, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "OPERATIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.operations.append(SerializationHelper.deserialize_by_tag(item_elem, "any (SwcToSwcOperation)"))
            elif tag == "SIGNALS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.signals.append(SerializationHelper.deserialize_by_tag(item_elem, "SwcToSwcSignal"))

        return obj



class SeparateSignalPathBuilder(SignalPathConstraintBuilder):
    """Builder for SeparateSignalPath with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SeparateSignalPath = SeparateSignalPath()


    def with_operations(self, items: list[any (SwcToSwcOperation)]) -> "SeparateSignalPathBuilder":
        """Set operations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.operations = list(items) if items else []
        return self

    def with_signals(self, items: list[SwcToSwcSignal]) -> "SeparateSignalPathBuilder":
        """Set signals list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.signals = list(items) if items else []
        return self


    def add_operation(self, item: any (SwcToSwcOperation)) -> "SeparateSignalPathBuilder":
        """Add a single item to operations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.operations.append(item)
        return self

    def clear_operations(self) -> "SeparateSignalPathBuilder":
        """Clear all items from operations list.

        Returns:
            self for method chaining
        """
        self._obj.operations = []
        return self

    def add_signal(self, item: SwcToSwcSignal) -> "SeparateSignalPathBuilder":
        """Add a single item to signals list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.signals.append(item)
        return self

    def clear_signals(self) -> "SeparateSignalPathBuilder":
        """Clear all items from signals list.

        Returns:
            self for method chaining
        """
        self._obj.signals = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "operation",
        "signal",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SeparateSignalPath:
        """Build and return the SeparateSignalPath instance with validation."""
        self._validate_instance()
        return self._obj