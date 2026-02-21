"""RptExecutableEntityProperties AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 203)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 859)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_RPTScenario.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport import (
    RptExecutionControlEnum,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import (
    RptServicePointEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class RptExecutableEntityProperties(ARObject):
    """AUTOSAR RptExecutableEntityProperties."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    max_rpt_event_id: Optional[PositiveInteger]
    min_rpt_event_id: Optional[PositiveInteger]
    rpt_execution_control: Optional[RptExecutionControlEnum]
    rpt_service_point_enum: Optional[RptServicePointEnum]
    def __init__(self) -> None:
        """Initialize RptExecutableEntityProperties."""
        super().__init__()
        self.max_rpt_event_id: Optional[PositiveInteger] = None
        self.min_rpt_event_id: Optional[PositiveInteger] = None
        self.rpt_execution_control: Optional[RptExecutionControlEnum] = None
        self.rpt_service_point_enum: Optional[RptServicePointEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize RptExecutableEntityProperties to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RptExecutableEntityProperties, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize max_rpt_event_id
        if self.max_rpt_event_id is not None:
            serialized = SerializationHelper.serialize_item(self.max_rpt_event_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-RPT-EVENT-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_rpt_event_id
        if self.min_rpt_event_id is not None:
            serialized = SerializationHelper.serialize_item(self.min_rpt_event_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-RPT-EVENT-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rpt_execution_control
        if self.rpt_execution_control is not None:
            serialized = SerializationHelper.serialize_item(self.rpt_execution_control, "RptExecutionControlEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RPT-EXECUTION-CONTROL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rpt_service_point_enum
        if self.rpt_service_point_enum is not None:
            serialized = SerializationHelper.serialize_item(self.rpt_service_point_enum, "RptServicePointEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RPT-SERVICE-POINT-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptExecutableEntityProperties":
        """Deserialize XML element to RptExecutableEntityProperties object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RptExecutableEntityProperties object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RptExecutableEntityProperties, cls).deserialize(element)

        # Parse max_rpt_event_id
        child = SerializationHelper.find_child_element(element, "MAX-RPT-EVENT-ID")
        if child is not None:
            max_rpt_event_id_value = child.text
            obj.max_rpt_event_id = max_rpt_event_id_value

        # Parse min_rpt_event_id
        child = SerializationHelper.find_child_element(element, "MIN-RPT-EVENT-ID")
        if child is not None:
            min_rpt_event_id_value = child.text
            obj.min_rpt_event_id = min_rpt_event_id_value

        # Parse rpt_execution_control
        child = SerializationHelper.find_child_element(element, "RPT-EXECUTION-CONTROL")
        if child is not None:
            rpt_execution_control_value = RptExecutionControlEnum.deserialize(child)
            obj.rpt_execution_control = rpt_execution_control_value

        # Parse rpt_service_point_enum
        child = SerializationHelper.find_child_element(element, "RPT-SERVICE-POINT-ENUM")
        if child is not None:
            rpt_service_point_enum_value = RptServicePointEnum.deserialize(child)
            obj.rpt_service_point_enum = rpt_service_point_enum_value

        return obj



class RptExecutableEntityPropertiesBuilder:
    """Builder for RptExecutableEntityProperties."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RptExecutableEntityProperties = RptExecutableEntityProperties()

    def build(self) -> RptExecutableEntityProperties:
        """Build and return RptExecutableEntityProperties object.

        Returns:
            RptExecutableEntityProperties instance
        """
        # TODO: Add validation
        return self._obj
