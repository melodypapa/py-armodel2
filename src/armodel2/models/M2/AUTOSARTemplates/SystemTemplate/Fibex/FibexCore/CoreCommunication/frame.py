"""Frame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 295)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 418)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 224)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import FibexElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_to_frame_mapping import (
    PduToFrameMapping,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Frame(FibexElement, ABC):
    """AUTOSAR Frame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    frame_length: Optional[Integer]
    pdu_to_frame_mappings: list[PduToFrameMapping]
    _DESERIALIZE_DISPATCH = {
        "FRAME-LENGTH": lambda obj, elem: setattr(obj, "frame_length", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "PDU-TO-FRAME-MAPPINGS": lambda obj, elem: obj.pdu_to_frame_mappings.append(SerializationHelper.deserialize_by_tag(elem, "PduToFrameMapping")),
    }


    def __init__(self) -> None:
        """Initialize Frame."""
        super().__init__()
        self.frame_length: Optional[Integer] = None
        self.pdu_to_frame_mappings: list[PduToFrameMapping] = []

    def serialize(self) -> ET.Element:
        """Serialize Frame to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Frame, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize frame_length
        if self.frame_length is not None:
            serialized = SerializationHelper.serialize_item(self.frame_length, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FRAME-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pdu_to_frame_mappings (list to container "PDU-TO-FRAME-MAPPINGS")
        if self.pdu_to_frame_mappings:
            wrapper = ET.Element("PDU-TO-FRAME-MAPPINGS")
            for item in self.pdu_to_frame_mappings:
                serialized = SerializationHelper.serialize_item(item, "PduToFrameMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Frame":
        """Deserialize XML element to Frame object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Frame object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Frame, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "FRAME-LENGTH":
                setattr(obj, "frame_length", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "PDU-TO-FRAME-MAPPINGS":
                obj.pdu_to_frame_mappings.append(SerializationHelper.deserialize_by_tag(child, "PduToFrameMapping"))

        return obj



class FrameBuilder(FibexElementBuilder):
    """Builder for Frame with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Frame = Frame()


    def with_frame_length(self, value: Optional[Integer]) -> "FrameBuilder":
        """Set frame_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.frame_length = value
        return self

    def with_pdu_to_frame_mappings(self, items: list[PduToFrameMapping]) -> "FrameBuilder":
        """Set pdu_to_frame_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.pdu_to_frame_mappings = list(items) if items else []
        return self


    def add_pdu_to_frame_mapping(self, item: PduToFrameMapping) -> "FrameBuilder":
        """Add a single item to pdu_to_frame_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.pdu_to_frame_mappings.append(item)
        return self

    def clear_pdu_to_frame_mappings(self) -> "FrameBuilder":
        """Clear all items from pdu_to_frame_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.pdu_to_frame_mappings = []
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


    @abstractmethod
    def build(self) -> Frame:
        """Build and return the Frame instance (abstract)."""
        raise NotImplementedError