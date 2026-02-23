"""EndToEndTransformationDescription AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 987)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 806)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_description import (
    TransformationDescription,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_description import TransformationDescriptionBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    DataIdModeEnum,
    EndToEndProfileBehaviorEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    NameToken,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.e2_e_profile_compatibility_props import (
    E2EProfileCompatibilityProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class EndToEndTransformationDescription(TransformationDescription):
    """AUTOSAR EndToEndTransformationDescription."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    clear_from_valid: Optional[Boolean]
    counter_offset: Optional[PositiveInteger]
    crc_offset: Optional[PositiveInteger]
    data_id_mode: Optional[DataIdModeEnum]
    data_id_nibble: Optional[PositiveInteger]
    e2e_profile_ref: Optional[ARRef]
    max_delta: Optional[PositiveInteger]
    max_error_state: Optional[PositiveInteger]
    max_no_new_or: Optional[PositiveInteger]
    min_ok_state_init: Optional[PositiveInteger]
    min_ok_state: Optional[PositiveInteger]
    offset: Optional[PositiveInteger]
    profile_behavior_behavior_enum: Optional[EndToEndProfileBehaviorEnum]
    profile_name: Optional[NameToken]
    sync_counter_init: Optional[PositiveInteger]
    upper_header: Optional[PositiveInteger]
    window_size_init: Optional[PositiveInteger]
    window_size: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize EndToEndTransformationDescription."""
        super().__init__()
        self.clear_from_valid: Optional[Boolean] = None
        self.counter_offset: Optional[PositiveInteger] = None
        self.crc_offset: Optional[PositiveInteger] = None
        self.data_id_mode: Optional[DataIdModeEnum] = None
        self.data_id_nibble: Optional[PositiveInteger] = None
        self.e2e_profile_ref: Optional[ARRef] = None
        self.max_delta: Optional[PositiveInteger] = None
        self.max_error_state: Optional[PositiveInteger] = None
        self.max_no_new_or: Optional[PositiveInteger] = None
        self.min_ok_state_init: Optional[PositiveInteger] = None
        self.min_ok_state: Optional[PositiveInteger] = None
        self.offset: Optional[PositiveInteger] = None
        self.profile_behavior_behavior_enum: Optional[EndToEndProfileBehaviorEnum] = None
        self.profile_name: Optional[NameToken] = None
        self.sync_counter_init: Optional[PositiveInteger] = None
        self.upper_header: Optional[PositiveInteger] = None
        self.window_size_init: Optional[PositiveInteger] = None
        self.window_size: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize EndToEndTransformationDescription to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EndToEndTransformationDescription, self).serialize()

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

        # Serialize counter_offset
        if self.counter_offset is not None:
            serialized = SerializationHelper.serialize_item(self.counter_offset, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COUNTER-OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crc_offset
        if self.crc_offset is not None:
            serialized = SerializationHelper.serialize_item(self.crc_offset, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRC-OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize data_id_mode
        if self.data_id_mode is not None:
            serialized = SerializationHelper.serialize_item(self.data_id_mode, "DataIdModeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-ID-MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize data_id_nibble
        if self.data_id_nibble is not None:
            serialized = SerializationHelper.serialize_item(self.data_id_nibble, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-ID-NIBBLE")
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

        # Serialize offset
        if self.offset is not None:
            serialized = SerializationHelper.serialize_item(self.offset, "PositiveInteger")
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

        # Serialize profile_behavior_behavior_enum
        if self.profile_behavior_behavior_enum is not None:
            serialized = SerializationHelper.serialize_item(self.profile_behavior_behavior_enum, "EndToEndProfileBehaviorEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROFILE-BEHAVIOR-BEHAVIOR-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize profile_name
        if self.profile_name is not None:
            serialized = SerializationHelper.serialize_item(self.profile_name, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROFILE-NAME")
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

        # Serialize upper_header
        if self.upper_header is not None:
            serialized = SerializationHelper.serialize_item(self.upper_header, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UPPER-HEADER")
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
    def deserialize(cls, element: ET.Element) -> "EndToEndTransformationDescription":
        """Deserialize XML element to EndToEndTransformationDescription object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EndToEndTransformationDescription object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EndToEndTransformationDescription, cls).deserialize(element)

        # Parse clear_from_valid
        child = SerializationHelper.find_child_element(element, "CLEAR-FROM-VALID")
        if child is not None:
            clear_from_valid_value = child.text
            obj.clear_from_valid = clear_from_valid_value

        # Parse counter_offset
        child = SerializationHelper.find_child_element(element, "COUNTER-OFFSET")
        if child is not None:
            counter_offset_value = child.text
            obj.counter_offset = counter_offset_value

        # Parse crc_offset
        child = SerializationHelper.find_child_element(element, "CRC-OFFSET")
        if child is not None:
            crc_offset_value = child.text
            obj.crc_offset = crc_offset_value

        # Parse data_id_mode
        child = SerializationHelper.find_child_element(element, "DATA-ID-MODE")
        if child is not None:
            data_id_mode_value = DataIdModeEnum.deserialize(child)
            obj.data_id_mode = data_id_mode_value

        # Parse data_id_nibble
        child = SerializationHelper.find_child_element(element, "DATA-ID-NIBBLE")
        if child is not None:
            data_id_nibble_value = child.text
            obj.data_id_nibble = data_id_nibble_value

        # Parse e2e_profile_ref
        child = SerializationHelper.find_child_element(element, "E2E-PROFILE-REF")
        if child is not None:
            e2e_profile_ref_value = ARRef.deserialize(child)
            obj.e2e_profile_ref = e2e_profile_ref_value

        # Parse max_delta
        child = SerializationHelper.find_child_element(element, "MAX-DELTA")
        if child is not None:
            max_delta_value = child.text
            obj.max_delta = max_delta_value

        # Parse max_error_state
        child = SerializationHelper.find_child_element(element, "MAX-ERROR-STATE")
        if child is not None:
            max_error_state_value = child.text
            obj.max_error_state = max_error_state_value

        # Parse max_no_new_or
        child = SerializationHelper.find_child_element(element, "MAX-NO-NEW-OR")
        if child is not None:
            max_no_new_or_value = child.text
            obj.max_no_new_or = max_no_new_or_value

        # Parse min_ok_state_init
        child = SerializationHelper.find_child_element(element, "MIN-OK-STATE-INIT")
        if child is not None:
            min_ok_state_init_value = child.text
            obj.min_ok_state_init = min_ok_state_init_value

        # Parse min_ok_state
        child = SerializationHelper.find_child_element(element, "MIN-OK-STATE")
        if child is not None:
            min_ok_state_value = child.text
            obj.min_ok_state = min_ok_state_value

        # Parse offset
        child = SerializationHelper.find_child_element(element, "OFFSET")
        if child is not None:
            offset_value = child.text
            obj.offset = offset_value

        # Parse profile_behavior_behavior_enum
        child = SerializationHelper.find_child_element(element, "PROFILE-BEHAVIOR-BEHAVIOR-ENUM")
        if child is not None:
            profile_behavior_behavior_enum_value = EndToEndProfileBehaviorEnum.deserialize(child)
            obj.profile_behavior_behavior_enum = profile_behavior_behavior_enum_value

        # Parse profile_name
        child = SerializationHelper.find_child_element(element, "PROFILE-NAME")
        if child is not None:
            profile_name_value = child.text
            obj.profile_name = profile_name_value

        # Parse sync_counter_init
        child = SerializationHelper.find_child_element(element, "SYNC-COUNTER-INIT")
        if child is not None:
            sync_counter_init_value = child.text
            obj.sync_counter_init = sync_counter_init_value

        # Parse upper_header
        child = SerializationHelper.find_child_element(element, "UPPER-HEADER")
        if child is not None:
            upper_header_value = child.text
            obj.upper_header = upper_header_value

        # Parse window_size_init
        child = SerializationHelper.find_child_element(element, "WINDOW-SIZE-INIT")
        if child is not None:
            window_size_init_value = child.text
            obj.window_size_init = window_size_init_value

        # Parse window_size
        child = SerializationHelper.find_child_element(element, "WINDOW-SIZE")
        if child is not None:
            window_size_value = child.text
            obj.window_size = window_size_value

        return obj



class EndToEndTransformationDescriptionBuilder(TransformationDescriptionBuilder):
    """Builder for EndToEndTransformationDescription with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EndToEndTransformationDescription = EndToEndTransformationDescription()


    def with_clear_from_valid(self, value: Optional[Boolean]) -> "EndToEndTransformationDescriptionBuilder":
        """Set clear_from_valid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.clear_from_valid = value
        return self

    def with_counter_offset(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationDescriptionBuilder":
        """Set counter_offset attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.counter_offset = value
        return self

    def with_crc_offset(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationDescriptionBuilder":
        """Set crc_offset attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.crc_offset = value
        return self

    def with_data_id_mode(self, value: Optional[DataIdModeEnum]) -> "EndToEndTransformationDescriptionBuilder":
        """Set data_id_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_id_mode = value
        return self

    def with_data_id_nibble(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationDescriptionBuilder":
        """Set data_id_nibble attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_id_nibble = value
        return self

    def with_e2e_profile(self, value: Optional[E2EProfileCompatibilityProps]) -> "EndToEndTransformationDescriptionBuilder":
        """Set e2e_profile attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.e2e_profile = value
        return self

    def with_max_delta(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationDescriptionBuilder":
        """Set max_delta attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_delta = value
        return self

    def with_max_error_state(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationDescriptionBuilder":
        """Set max_error_state attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_error_state = value
        return self

    def with_max_no_new_or(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationDescriptionBuilder":
        """Set max_no_new_or attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_no_new_or = value
        return self

    def with_min_ok_state_init(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationDescriptionBuilder":
        """Set min_ok_state_init attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.min_ok_state_init = value
        return self

    def with_min_ok_state(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationDescriptionBuilder":
        """Set min_ok_state attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.min_ok_state = value
        return self

    def with_offset(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationDescriptionBuilder":
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

    def with_profile_behavior_behavior_enum(self, value: Optional[EndToEndProfileBehaviorEnum]) -> "EndToEndTransformationDescriptionBuilder":
        """Set profile_behavior_behavior_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.profile_behavior_behavior_enum = value
        return self

    def with_profile_name(self, value: Optional[NameToken]) -> "EndToEndTransformationDescriptionBuilder":
        """Set profile_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.profile_name = value
        return self

    def with_sync_counter_init(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationDescriptionBuilder":
        """Set sync_counter_init attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sync_counter_init = value
        return self

    def with_upper_header(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationDescriptionBuilder":
        """Set upper_header attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.upper_header = value
        return self

    def with_window_size_init(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationDescriptionBuilder":
        """Set window_size_init attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.window_size_init = value
        return self

    def with_window_size(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationDescriptionBuilder":
        """Set window_size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.window_size = value
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


    def build(self) -> EndToEndTransformationDescription:
        """Build and return the EndToEndTransformationDescription instance with validation."""
        self._validate_instance()
        pass
        return self._obj