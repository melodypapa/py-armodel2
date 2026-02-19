"""CanControllerXlConfigurationRequirements AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 71)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Float,
    PositiveInteger,
    TimeValue,
)


class CanControllerXlConfigurationRequirements(ARObject):
    """AUTOSAR CanControllerXlConfigurationRequirements."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    error_signaling: Optional[Boolean]
    max_number_of_time_quanta_per: Optional[Any]
    max_pwm_l: Optional[PositiveInteger]
    max_pwm_o: Optional[PositiveInteger]
    max_pwm_s: Optional[PositiveInteger]
    max_sample: Optional[Float]
    max_sync_jump: Optional[Float]
    max_trcv_delay: Optional[TimeValue]
    min_number_of_time_quanta_per: Optional[Any]
    min_pwm_l: Optional[PositiveInteger]
    min_pwm_o: Optional[PositiveInteger]
    min_pwm_s: Optional[PositiveInteger]
    min_sample_point: Optional[Float]
    min_sync_jump: Optional[Float]
    min_trcv_delay: Optional[TimeValue]
    trcv_pwm_mode: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize CanControllerXlConfigurationRequirements."""
        super().__init__()
        self.error_signaling: Optional[Boolean] = None
        self.max_number_of_time_quanta_per: Optional[Any] = None
        self.max_pwm_l: Optional[PositiveInteger] = None
        self.max_pwm_o: Optional[PositiveInteger] = None
        self.max_pwm_s: Optional[PositiveInteger] = None
        self.max_sample: Optional[Float] = None
        self.max_sync_jump: Optional[Float] = None
        self.max_trcv_delay: Optional[TimeValue] = None
        self.min_number_of_time_quanta_per: Optional[Any] = None
        self.min_pwm_l: Optional[PositiveInteger] = None
        self.min_pwm_o: Optional[PositiveInteger] = None
        self.min_pwm_s: Optional[PositiveInteger] = None
        self.min_sample_point: Optional[Float] = None
        self.min_sync_jump: Optional[Float] = None
        self.min_trcv_delay: Optional[TimeValue] = None
        self.trcv_pwm_mode: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanControllerXlConfigurationRequirements":
        """Deserialize XML element to CanControllerXlConfigurationRequirements object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanControllerXlConfigurationRequirements object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse error_signaling
        child = ARObject._find_child_element(element, "ERROR-SIGNALING")
        if child is not None:
            error_signaling_value = child.text
            obj.error_signaling = error_signaling_value

        # Parse max_number_of_time_quanta_per
        child = ARObject._find_child_element(element, "MAX-NUMBER-OF-TIME-QUANTA-PER")
        if child is not None:
            max_number_of_time_quanta_per_value = child.text
            obj.max_number_of_time_quanta_per = max_number_of_time_quanta_per_value

        # Parse max_pwm_l
        child = ARObject._find_child_element(element, "MAX-PWM-L")
        if child is not None:
            max_pwm_l_value = child.text
            obj.max_pwm_l = max_pwm_l_value

        # Parse max_pwm_o
        child = ARObject._find_child_element(element, "MAX-PWM-O")
        if child is not None:
            max_pwm_o_value = child.text
            obj.max_pwm_o = max_pwm_o_value

        # Parse max_pwm_s
        child = ARObject._find_child_element(element, "MAX-PWM-S")
        if child is not None:
            max_pwm_s_value = child.text
            obj.max_pwm_s = max_pwm_s_value

        # Parse max_sample
        child = ARObject._find_child_element(element, "MAX-SAMPLE")
        if child is not None:
            max_sample_value = child.text
            obj.max_sample = max_sample_value

        # Parse max_sync_jump
        child = ARObject._find_child_element(element, "MAX-SYNC-JUMP")
        if child is not None:
            max_sync_jump_value = child.text
            obj.max_sync_jump = max_sync_jump_value

        # Parse max_trcv_delay
        child = ARObject._find_child_element(element, "MAX-TRCV-DELAY")
        if child is not None:
            max_trcv_delay_value = child.text
            obj.max_trcv_delay = max_trcv_delay_value

        # Parse min_number_of_time_quanta_per
        child = ARObject._find_child_element(element, "MIN-NUMBER-OF-TIME-QUANTA-PER")
        if child is not None:
            min_number_of_time_quanta_per_value = child.text
            obj.min_number_of_time_quanta_per = min_number_of_time_quanta_per_value

        # Parse min_pwm_l
        child = ARObject._find_child_element(element, "MIN-PWM-L")
        if child is not None:
            min_pwm_l_value = child.text
            obj.min_pwm_l = min_pwm_l_value

        # Parse min_pwm_o
        child = ARObject._find_child_element(element, "MIN-PWM-O")
        if child is not None:
            min_pwm_o_value = child.text
            obj.min_pwm_o = min_pwm_o_value

        # Parse min_pwm_s
        child = ARObject._find_child_element(element, "MIN-PWM-S")
        if child is not None:
            min_pwm_s_value = child.text
            obj.min_pwm_s = min_pwm_s_value

        # Parse min_sample_point
        child = ARObject._find_child_element(element, "MIN-SAMPLE-POINT")
        if child is not None:
            min_sample_point_value = child.text
            obj.min_sample_point = min_sample_point_value

        # Parse min_sync_jump
        child = ARObject._find_child_element(element, "MIN-SYNC-JUMP")
        if child is not None:
            min_sync_jump_value = child.text
            obj.min_sync_jump = min_sync_jump_value

        # Parse min_trcv_delay
        child = ARObject._find_child_element(element, "MIN-TRCV-DELAY")
        if child is not None:
            min_trcv_delay_value = child.text
            obj.min_trcv_delay = min_trcv_delay_value

        # Parse trcv_pwm_mode
        child = ARObject._find_child_element(element, "TRCV-PWM-MODE")
        if child is not None:
            trcv_pwm_mode_value = child.text
            obj.trcv_pwm_mode = trcv_pwm_mode_value

        return obj



class CanControllerXlConfigurationRequirementsBuilder:
    """Builder for CanControllerXlConfigurationRequirements."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanControllerXlConfigurationRequirements = CanControllerXlConfigurationRequirements()

    def build(self) -> CanControllerXlConfigurationRequirements:
        """Build and return CanControllerXlConfigurationRequirements object.

        Returns:
            CanControllerXlConfigurationRequirements instance
        """
        # TODO: Add validation
        return self._obj
