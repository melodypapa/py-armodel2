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
    e2e_profile: Optional[E2EProfileCompatibilityProps]
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
        self.e2e_profile: Optional[E2EProfileCompatibilityProps] = None
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
        child = ARObject._find_child_element(element, "CLEAR-FROM-VALID")
        if child is not None:
            clear_from_valid_value = child.text
            obj.clear_from_valid = clear_from_valid_value

        # Parse counter_offset
        child = ARObject._find_child_element(element, "COUNTER-OFFSET")
        if child is not None:
            counter_offset_value = child.text
            obj.counter_offset = counter_offset_value

        # Parse crc_offset
        child = ARObject._find_child_element(element, "CRC-OFFSET")
        if child is not None:
            crc_offset_value = child.text
            obj.crc_offset = crc_offset_value

        # Parse data_id_mode
        child = ARObject._find_child_element(element, "DATA-ID-MODE")
        if child is not None:
            data_id_mode_value = DataIdModeEnum.deserialize(child)
            obj.data_id_mode = data_id_mode_value

        # Parse data_id_nibble
        child = ARObject._find_child_element(element, "DATA-ID-NIBBLE")
        if child is not None:
            data_id_nibble_value = child.text
            obj.data_id_nibble = data_id_nibble_value

        # Parse e2e_profile
        child = ARObject._find_child_element(element, "E2E-PROFILE")
        if child is not None:
            e2e_profile_value = ARObject._deserialize_by_tag(child, "E2EProfileCompatibilityProps")
            obj.e2e_profile = e2e_profile_value

        # Parse max_delta
        child = ARObject._find_child_element(element, "MAX-DELTA")
        if child is not None:
            max_delta_value = child.text
            obj.max_delta = max_delta_value

        # Parse max_error_state
        child = ARObject._find_child_element(element, "MAX-ERROR-STATE")
        if child is not None:
            max_error_state_value = child.text
            obj.max_error_state = max_error_state_value

        # Parse max_no_new_or
        child = ARObject._find_child_element(element, "MAX-NO-NEW-OR")
        if child is not None:
            max_no_new_or_value = child.text
            obj.max_no_new_or = max_no_new_or_value

        # Parse min_ok_state_init
        child = ARObject._find_child_element(element, "MIN-OK-STATE-INIT")
        if child is not None:
            min_ok_state_init_value = child.text
            obj.min_ok_state_init = min_ok_state_init_value

        # Parse min_ok_state
        child = ARObject._find_child_element(element, "MIN-OK-STATE")
        if child is not None:
            min_ok_state_value = child.text
            obj.min_ok_state = min_ok_state_value

        # Parse offset
        child = ARObject._find_child_element(element, "OFFSET")
        if child is not None:
            offset_value = child.text
            obj.offset = offset_value

        # Parse profile_behavior_behavior_enum
        child = ARObject._find_child_element(element, "PROFILE-BEHAVIOR-BEHAVIOR-ENUM")
        if child is not None:
            profile_behavior_behavior_enum_value = EndToEndProfileBehaviorEnum.deserialize(child)
            obj.profile_behavior_behavior_enum = profile_behavior_behavior_enum_value

        # Parse profile_name
        child = ARObject._find_child_element(element, "PROFILE-NAME")
        if child is not None:
            profile_name_value = child.text
            obj.profile_name = profile_name_value

        # Parse sync_counter_init
        child = ARObject._find_child_element(element, "SYNC-COUNTER-INIT")
        if child is not None:
            sync_counter_init_value = child.text
            obj.sync_counter_init = sync_counter_init_value

        # Parse upper_header
        child = ARObject._find_child_element(element, "UPPER-HEADER")
        if child is not None:
            upper_header_value = child.text
            obj.upper_header = upper_header_value

        # Parse window_size_init
        child = ARObject._find_child_element(element, "WINDOW-SIZE-INIT")
        if child is not None:
            window_size_init_value = child.text
            obj.window_size_init = window_size_init_value

        # Parse window_size
        child = ARObject._find_child_element(element, "WINDOW-SIZE")
        if child is not None:
            window_size_value = child.text
            obj.window_size = window_size_value

        return obj



class EndToEndTransformationDescriptionBuilder:
    """Builder for EndToEndTransformationDescription."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EndToEndTransformationDescription = EndToEndTransformationDescription()

    def build(self) -> EndToEndTransformationDescription:
        """Build and return EndToEndTransformationDescription object.

        Returns:
            EndToEndTransformationDescription instance
        """
        # TODO: Add validation
        return self._obj
