"""EndToEndTransformationComSpecProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 200)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2023)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.transformation_com_spec_props import (
    TransformationComSpecProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.e2_e_profile_compatibility_props import (
    E2EProfileCompatibilityProps,
)


class EndToEndTransformationComSpecProps(TransformationComSpecProps):
    """AUTOSAR EndToEndTransformationComSpecProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    clear_from_valid: Optional[Boolean]
    disable_end_to: Optional[Boolean]
    e2e_profile: Optional[E2EProfileCompatibilityProps]
    max_delta: Optional[PositiveInteger]
    max_error_state: Optional[PositiveInteger]
    max_no_new_or: Optional[PositiveInteger]
    min_ok_state_init: Optional[PositiveInteger]
    min_ok_state: Optional[PositiveInteger]
    sync_counter_init: Optional[PositiveInteger]
    window_size_init: Optional[PositiveInteger]
    window_size: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize EndToEndTransformationComSpecProps."""
        super().__init__()
        self.clear_from_valid: Optional[Boolean] = None
        self.disable_end_to: Optional[Boolean] = None
        self.e2e_profile: Optional[E2EProfileCompatibilityProps] = None
        self.max_delta: Optional[PositiveInteger] = None
        self.max_error_state: Optional[PositiveInteger] = None
        self.max_no_new_or: Optional[PositiveInteger] = None
        self.min_ok_state_init: Optional[PositiveInteger] = None
        self.min_ok_state: Optional[PositiveInteger] = None
        self.sync_counter_init: Optional[PositiveInteger] = None
        self.window_size_init: Optional[PositiveInteger] = None
        self.window_size: Optional[PositiveInteger] = None
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

        # Parse clear_from_valid
        child = ARObject._find_child_element(element, "CLEAR-FROM-VALID")
        if child is not None:
            clear_from_valid_value = child.text
            obj.clear_from_valid = clear_from_valid_value

        # Parse disable_end_to
        child = ARObject._find_child_element(element, "DISABLE-END-TO")
        if child is not None:
            disable_end_to_value = child.text
            obj.disable_end_to = disable_end_to_value

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

        # Parse sync_counter_init
        child = ARObject._find_child_element(element, "SYNC-COUNTER-INIT")
        if child is not None:
            sync_counter_init_value = child.text
            obj.sync_counter_init = sync_counter_init_value

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



class EndToEndTransformationComSpecPropsBuilder:
    """Builder for EndToEndTransformationComSpecProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EndToEndTransformationComSpecProps = EndToEndTransformationComSpecProps()

    def build(self) -> EndToEndTransformationComSpecProps:
        """Build and return EndToEndTransformationComSpecProps object.

        Returns:
            EndToEndTransformationComSpecProps instance
        """
        # TODO: Add validation
        return self._obj
