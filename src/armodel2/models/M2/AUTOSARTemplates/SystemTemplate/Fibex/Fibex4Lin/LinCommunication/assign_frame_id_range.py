"""AssignFrameIdRange AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 437)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import (
    LinConfigurationEntry,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import LinConfigurationEntryBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.frame_pid import (
    FramePid,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AssignFrameIdRange(LinConfigurationEntry):
    """AUTOSAR AssignFrameIdRange."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ASSIGN-FRAME-ID-RANGE"


    frame_pid: FramePid
    start_index: Optional[Integer]
    _DESERIALIZE_DISPATCH = {
        "FRAME-PID": lambda obj, elem: setattr(obj, "frame_pid", FramePid.deserialize(elem)),
        "START-INDEX": lambda obj, elem: setattr(obj, "start_index", elem.text),
    }


    def __init__(self) -> None:
        """Initialize AssignFrameIdRange."""
        super().__init__()
        self.frame_pid: FramePid = None
        self.start_index: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize AssignFrameIdRange to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AssignFrameIdRange, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize frame_pid
        if self.frame_pid is not None:
            serialized = SerializationHelper.serialize_item(self.frame_pid, "FramePid")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FRAME-PID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize start_index
        if self.start_index is not None:
            serialized = SerializationHelper.serialize_item(self.start_index, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("START-INDEX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AssignFrameIdRange":
        """Deserialize XML element to AssignFrameIdRange object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AssignFrameIdRange object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AssignFrameIdRange, cls).deserialize(element)

        # Parse frame_pid
        child = SerializationHelper.find_child_element(element, "FRAME-PID")
        if child is not None:
            frame_pid_value = SerializationHelper.deserialize_by_tag(child, "FramePid")
            obj.frame_pid = frame_pid_value

        # Parse start_index
        child = SerializationHelper.find_child_element(element, "START-INDEX")
        if child is not None:
            start_index_value = child.text
            obj.start_index = start_index_value

        return obj



class AssignFrameIdRangeBuilder(LinConfigurationEntryBuilder):
    """Builder for AssignFrameIdRange with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AssignFrameIdRange = AssignFrameIdRange()


    def with_frame_pid(self, value: FramePid) -> "AssignFrameIdRangeBuilder":
        """Set frame_pid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.frame_pid = value
        return self

    def with_start_index(self, value: Optional[Integer]) -> "AssignFrameIdRangeBuilder":
        """Set start_index attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.start_index = value
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


    def build(self) -> AssignFrameIdRange:
        """Build and return the AssignFrameIdRange instance with validation."""
        self._validate_instance()
        pass
        return self._obj