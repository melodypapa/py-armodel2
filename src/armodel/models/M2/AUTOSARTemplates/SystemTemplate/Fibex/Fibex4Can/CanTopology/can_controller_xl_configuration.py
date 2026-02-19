"""CanControllerXlConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 70)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class CanControllerXlConfiguration(ARObject):
    """AUTOSAR CanControllerXlConfiguration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    error_signaling: Optional[Boolean]
    prop_seg: Optional[PositiveInteger]
    pwm_l: Optional[PositiveInteger]
    pwm_o: Optional[PositiveInteger]
    pwm_s: Optional[PositiveInteger]
    ssp_offset: Optional[PositiveInteger]
    sync_jump_width: Optional[PositiveInteger]
    time_seg1: Optional[PositiveInteger]
    time_seg2: Optional[PositiveInteger]
    trcv_pwm_mode: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize CanControllerXlConfiguration."""
        super().__init__()
        self.error_signaling: Optional[Boolean] = None
        self.prop_seg: Optional[PositiveInteger] = None
        self.pwm_l: Optional[PositiveInteger] = None
        self.pwm_o: Optional[PositiveInteger] = None
        self.pwm_s: Optional[PositiveInteger] = None
        self.ssp_offset: Optional[PositiveInteger] = None
        self.sync_jump_width: Optional[PositiveInteger] = None
        self.time_seg1: Optional[PositiveInteger] = None
        self.time_seg2: Optional[PositiveInteger] = None
        self.trcv_pwm_mode: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanControllerXlConfiguration":
        """Deserialize XML element to CanControllerXlConfiguration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanControllerXlConfiguration object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse error_signaling
        child = ARObject._find_child_element(element, "ERROR-SIGNALING")
        if child is not None:
            error_signaling_value = child.text
            obj.error_signaling = error_signaling_value

        # Parse prop_seg
        child = ARObject._find_child_element(element, "PROP-SEG")
        if child is not None:
            prop_seg_value = child.text
            obj.prop_seg = prop_seg_value

        # Parse pwm_l
        child = ARObject._find_child_element(element, "PWM-L")
        if child is not None:
            pwm_l_value = child.text
            obj.pwm_l = pwm_l_value

        # Parse pwm_o
        child = ARObject._find_child_element(element, "PWM-O")
        if child is not None:
            pwm_o_value = child.text
            obj.pwm_o = pwm_o_value

        # Parse pwm_s
        child = ARObject._find_child_element(element, "PWM-S")
        if child is not None:
            pwm_s_value = child.text
            obj.pwm_s = pwm_s_value

        # Parse ssp_offset
        child = ARObject._find_child_element(element, "SSP-OFFSET")
        if child is not None:
            ssp_offset_value = child.text
            obj.ssp_offset = ssp_offset_value

        # Parse sync_jump_width
        child = ARObject._find_child_element(element, "SYNC-JUMP-WIDTH")
        if child is not None:
            sync_jump_width_value = child.text
            obj.sync_jump_width = sync_jump_width_value

        # Parse time_seg1
        child = ARObject._find_child_element(element, "TIME-SEG1")
        if child is not None:
            time_seg1_value = child.text
            obj.time_seg1 = time_seg1_value

        # Parse time_seg2
        child = ARObject._find_child_element(element, "TIME-SEG2")
        if child is not None:
            time_seg2_value = child.text
            obj.time_seg2 = time_seg2_value

        # Parse trcv_pwm_mode
        child = ARObject._find_child_element(element, "TRCV-PWM-MODE")
        if child is not None:
            trcv_pwm_mode_value = child.text
            obj.trcv_pwm_mode = trcv_pwm_mode_value

        return obj



class CanControllerXlConfigurationBuilder:
    """Builder for CanControllerXlConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanControllerXlConfiguration = CanControllerXlConfiguration()

    def build(self) -> CanControllerXlConfiguration:
        """Build and return CanControllerXlConfiguration object.

        Returns:
            CanControllerXlConfiguration instance
        """
        # TODO: Add validation
        return self._obj
