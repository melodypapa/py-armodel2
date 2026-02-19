"""CanControllerFdConfigurationRequirements AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 66)

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


class CanControllerFdConfigurationRequirements(ARObject):
    """AUTOSAR CanControllerFdConfigurationRequirements."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    max_number_of_time_quanta_per: Optional[Any]
    max_sample: Optional[Float]
    max_sync_jump: Optional[Float]
    max_trcv_delay: Optional[TimeValue]
    min_number_of_time_quanta_per: Optional[Any]
    min_sample_point: Optional[Float]
    min_sync_jump: Optional[Float]
    min_trcv_delay: Optional[TimeValue]
    padding_value: Optional[PositiveInteger]
    tx_bit_rate_switch: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize CanControllerFdConfigurationRequirements."""
        super().__init__()
        self.max_number_of_time_quanta_per: Optional[Any] = None
        self.max_sample: Optional[Float] = None
        self.max_sync_jump: Optional[Float] = None
        self.max_trcv_delay: Optional[TimeValue] = None
        self.min_number_of_time_quanta_per: Optional[Any] = None
        self.min_sample_point: Optional[Float] = None
        self.min_sync_jump: Optional[Float] = None
        self.min_trcv_delay: Optional[TimeValue] = None
        self.padding_value: Optional[PositiveInteger] = None
        self.tx_bit_rate_switch: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanControllerFdConfigurationRequirements":
        """Deserialize XML element to CanControllerFdConfigurationRequirements object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanControllerFdConfigurationRequirements object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse max_number_of_time_quanta_per
        child = ARObject._find_child_element(element, "MAX-NUMBER-OF-TIME-QUANTA-PER")
        if child is not None:
            max_number_of_time_quanta_per_value = child.text
            obj.max_number_of_time_quanta_per = max_number_of_time_quanta_per_value

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

        # Parse padding_value
        child = ARObject._find_child_element(element, "PADDING-VALUE")
        if child is not None:
            padding_value_value = child.text
            obj.padding_value = padding_value_value

        # Parse tx_bit_rate_switch
        child = ARObject._find_child_element(element, "TX-BIT-RATE-SWITCH")
        if child is not None:
            tx_bit_rate_switch_value = child.text
            obj.tx_bit_rate_switch = tx_bit_rate_switch_value

        return obj



class CanControllerFdConfigurationRequirementsBuilder:
    """Builder for CanControllerFdConfigurationRequirements."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanControllerFdConfigurationRequirements = CanControllerFdConfigurationRequirements()

    def build(self) -> CanControllerFdConfigurationRequirements:
        """Build and return CanControllerFdConfigurationRequirements object.

        Returns:
            CanControllerFdConfigurationRequirements instance
        """
        # TODO: Add validation
        return self._obj
