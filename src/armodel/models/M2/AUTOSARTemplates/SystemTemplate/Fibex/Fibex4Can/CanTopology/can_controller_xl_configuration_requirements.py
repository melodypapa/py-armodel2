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

    def serialize(self) -> ET.Element:
        """Serialize CanControllerXlConfigurationRequirements to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize error_signaling
        if self.error_signaling is not None:
            serialized = ARObject._serialize_item(self.error_signaling, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ERROR-SIGNALING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_number_of_time_quanta_per
        if self.max_number_of_time_quanta_per is not None:
            serialized = ARObject._serialize_item(self.max_number_of_time_quanta_per, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-NUMBER-OF-TIME-QUANTA-PER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_pwm_l
        if self.max_pwm_l is not None:
            serialized = ARObject._serialize_item(self.max_pwm_l, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-PWM-L")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_pwm_o
        if self.max_pwm_o is not None:
            serialized = ARObject._serialize_item(self.max_pwm_o, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-PWM-O")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_pwm_s
        if self.max_pwm_s is not None:
            serialized = ARObject._serialize_item(self.max_pwm_s, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-PWM-S")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_sample
        if self.max_sample is not None:
            serialized = ARObject._serialize_item(self.max_sample, "Float")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-SAMPLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_sync_jump
        if self.max_sync_jump is not None:
            serialized = ARObject._serialize_item(self.max_sync_jump, "Float")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-SYNC-JUMP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_trcv_delay
        if self.max_trcv_delay is not None:
            serialized = ARObject._serialize_item(self.max_trcv_delay, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-TRCV-DELAY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_number_of_time_quanta_per
        if self.min_number_of_time_quanta_per is not None:
            serialized = ARObject._serialize_item(self.min_number_of_time_quanta_per, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-NUMBER-OF-TIME-QUANTA-PER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_pwm_l
        if self.min_pwm_l is not None:
            serialized = ARObject._serialize_item(self.min_pwm_l, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-PWM-L")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_pwm_o
        if self.min_pwm_o is not None:
            serialized = ARObject._serialize_item(self.min_pwm_o, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-PWM-O")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_pwm_s
        if self.min_pwm_s is not None:
            serialized = ARObject._serialize_item(self.min_pwm_s, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-PWM-S")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_sample_point
        if self.min_sample_point is not None:
            serialized = ARObject._serialize_item(self.min_sample_point, "Float")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-SAMPLE-POINT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_sync_jump
        if self.min_sync_jump is not None:
            serialized = ARObject._serialize_item(self.min_sync_jump, "Float")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-SYNC-JUMP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_trcv_delay
        if self.min_trcv_delay is not None:
            serialized = ARObject._serialize_item(self.min_trcv_delay, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-TRCV-DELAY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize trcv_pwm_mode
        if self.trcv_pwm_mode is not None:
            serialized = ARObject._serialize_item(self.trcv_pwm_mode, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRCV-PWM-MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

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
