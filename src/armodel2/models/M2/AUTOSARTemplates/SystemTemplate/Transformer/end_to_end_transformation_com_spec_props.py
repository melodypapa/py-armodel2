"""EndToEndTransformationComSpecProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 200)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2023)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.transformation_com_spec_props import (
    TransformationComSpecProps,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.transformation_com_spec_props import TransformationComSpecPropsBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.e2_e_profile_compatibility_props import (
    E2EProfileCompatibilityProps,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EndToEndTransformationComSpecProps(TransformationComSpecProps):
    """AUTOSAR EndToEndTransformationComSpecProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "END-TO-END-TRANSFORMATION-COM-SPEC-PROPS"


    clear_from_valid: Optional[Boolean]
    disable_end_to: Optional[Boolean]
    e2e_profile_ref: Optional[ARRef]
    max_delta: Optional[PositiveInteger]
    max_error_state: Optional[PositiveInteger]
    max_no_new_or: Optional[PositiveInteger]
    min_ok_state_init: Optional[PositiveInteger]
    min_ok_state: Optional[PositiveInteger]
    sync_counter_init: Optional[PositiveInteger]
    window_size_init: Optional[PositiveInteger]
    window_size: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "CLEAR-FROM-VALID": lambda obj, elem: setattr(obj, "clear_from_valid", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "DISABLE-END-TO": lambda obj, elem: setattr(obj, "disable_end_to", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "E2E-PROFILE-REF": lambda obj, elem: setattr(obj, "e2e_profile_ref", ARRef.deserialize(elem)),
        "MAX-DELTA": lambda obj, elem: setattr(obj, "max_delta", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MAX-ERROR-STATE": lambda obj, elem: setattr(obj, "max_error_state", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MAX-NO-NEW-OR": lambda obj, elem: setattr(obj, "max_no_new_or", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MIN-OK-STATE-INIT": lambda obj, elem: setattr(obj, "min_ok_state_init", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MIN-OK-STATE": lambda obj, elem: setattr(obj, "min_ok_state", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SYNC-COUNTER-INIT": lambda obj, elem: setattr(obj, "sync_counter_init", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "WINDOW-SIZE-INIT": lambda obj, elem: setattr(obj, "window_size_init", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "WINDOW-SIZE": lambda obj, elem: setattr(obj, "window_size", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize EndToEndTransformationComSpecProps."""
        super().__init__()
        self.clear_from_valid: Optional[Boolean] = None
        self.disable_end_to: Optional[Boolean] = None
        self.e2e_profile_ref: Optional[ARRef] = None
        self.max_delta: Optional[PositiveInteger] = None
        self.max_error_state: Optional[PositiveInteger] = None
        self.max_no_new_or: Optional[PositiveInteger] = None
        self.min_ok_state_init: Optional[PositiveInteger] = None
        self.min_ok_state: Optional[PositiveInteger] = None
        self.sync_counter_init: Optional[PositiveInteger] = None
        self.window_size_init: Optional[PositiveInteger] = None
        self.window_size: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize EndToEndTransformationComSpecProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EndToEndTransformationComSpecProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize clear_from_valid
        if self.clear_from_valid is not None:
            serialized = SerializationHelper.serialize_item(self.clear_from_valid, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CLEAR-FROM-VALID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize disable_end_to
        if self.disable_end_to is not None:
            serialized = SerializationHelper.serialize_item(self.disable_end_to, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DISABLE-END-TO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize e2e_profile_ref
        if self.e2e_profile_ref is not None:
            serialized = SerializationHelper.serialize_item(self.e2e_profile_ref, "E2EProfileCompatibilityProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("E2E-PROFILE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_delta
        if self.max_delta is not None:
            serialized = SerializationHelper.serialize_item(self.max_delta, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-DELTA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_error_state
        if self.max_error_state is not None:
            serialized = SerializationHelper.serialize_item(self.max_error_state, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-ERROR-STATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_no_new_or
        if self.max_no_new_or is not None:
            serialized = SerializationHelper.serialize_item(self.max_no_new_or, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-NO-NEW-OR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_ok_state_init
        if self.min_ok_state_init is not None:
            serialized = SerializationHelper.serialize_item(self.min_ok_state_init, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-OK-STATE-INIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_ok_state
        if self.min_ok_state is not None:
            serialized = SerializationHelper.serialize_item(self.min_ok_state, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-OK-STATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sync_counter_init
        if self.sync_counter_init is not None:
            serialized = SerializationHelper.serialize_item(self.sync_counter_init, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYNC-COUNTER-INIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize window_size_init
        if self.window_size_init is not None:
            serialized = SerializationHelper.serialize_item(self.window_size_init, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WINDOW-SIZE-INIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize window_size
        if self.window_size is not None:
            serialized = SerializationHelper.serialize_item(self.window_size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WINDOW-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EndToEndTransformationComSpecProps":
        """Deserialize XML element to EndToEndTransformationComSpecProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EndToEndTransformationComSpecProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EndToEndTransformationComSpecProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CLEAR-FROM-VALID":
                setattr(obj, "clear_from_valid", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "DISABLE-END-TO":
                setattr(obj, "disable_end_to", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "E2E-PROFILE-REF":
                setattr(obj, "e2e_profile_ref", ARRef.deserialize(child))
            elif tag == "MAX-DELTA":
                setattr(obj, "max_delta", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "MAX-ERROR-STATE":
                setattr(obj, "max_error_state", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "MAX-NO-NEW-OR":
                setattr(obj, "max_no_new_or", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "MIN-OK-STATE-INIT":
                setattr(obj, "min_ok_state_init", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "MIN-OK-STATE":
                setattr(obj, "min_ok_state", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SYNC-COUNTER-INIT":
                setattr(obj, "sync_counter_init", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "WINDOW-SIZE-INIT":
                setattr(obj, "window_size_init", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "WINDOW-SIZE":
                setattr(obj, "window_size", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class EndToEndTransformationComSpecPropsBuilder(TransformationComSpecPropsBuilder):
    """Builder for EndToEndTransformationComSpecProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EndToEndTransformationComSpecProps = EndToEndTransformationComSpecProps()


    def with_clear_from_valid(self, value: Optional[Boolean]) -> "EndToEndTransformationComSpecPropsBuilder":
        """Set clear_from_valid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'clear_from_valid' is required and cannot be None")
        self._obj.clear_from_valid = value
        return self

    def with_disable_end_to(self, value: Optional[Boolean]) -> "EndToEndTransformationComSpecPropsBuilder":
        """Set disable_end_to attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'disable_end_to' is required and cannot be None")
        self._obj.disable_end_to = value
        return self

    def with_e2e_profile(self, value: Optional[E2EProfileCompatibilityProps]) -> "EndToEndTransformationComSpecPropsBuilder":
        """Set e2e_profile attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'e2e_profile' is required and cannot be None")
        self._obj.e2e_profile = value
        return self

    def with_max_delta(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationComSpecPropsBuilder":
        """Set max_delta attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'max_delta' is required and cannot be None")
        self._obj.max_delta = value
        return self

    def with_max_error_state(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationComSpecPropsBuilder":
        """Set max_error_state attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'max_error_state' is required and cannot be None")
        self._obj.max_error_state = value
        return self

    def with_max_no_new_or(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationComSpecPropsBuilder":
        """Set max_no_new_or attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'max_no_new_or' is required and cannot be None")
        self._obj.max_no_new_or = value
        return self

    def with_min_ok_state_init(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationComSpecPropsBuilder":
        """Set min_ok_state_init attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'min_ok_state_init' is required and cannot be None")
        self._obj.min_ok_state_init = value
        return self

    def with_min_ok_state(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationComSpecPropsBuilder":
        """Set min_ok_state attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'min_ok_state' is required and cannot be None")
        self._obj.min_ok_state = value
        return self

    def with_sync_counter_init(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationComSpecPropsBuilder":
        """Set sync_counter_init attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sync_counter_init' is required and cannot be None")
        self._obj.sync_counter_init = value
        return self

    def with_window_size_init(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationComSpecPropsBuilder":
        """Set window_size_init attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'window_size_init' is required and cannot be None")
        self._obj.window_size_init = value
        return self

    def with_window_size(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationComSpecPropsBuilder":
        """Set window_size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'window_size' is required and cannot be None")
        self._obj.window_size = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "clearFromValid",
        "disableEndTo",
        "e2eProfile",
        "maxDelta",
        "maxErrorState",
        "maxNoNewOr",
        "minOkState",
        "minOkStateInit",
        "syncCounterInit",
        "windowSize",
        "windowSizeInit",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> EndToEndTransformationComSpecProps:
        """Build and return the EndToEndTransformationComSpecProps instance with validation."""
        self._validate_instance()
        return self._obj