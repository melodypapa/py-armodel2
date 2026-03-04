"""RptExecutableEntityProperties AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 203)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 859)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_RPTScenario.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport import (
    RptExecutionControlEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import (
    RptServicePointEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class RptExecutableEntityProperties(ARObject):
    """AUTOSAR RptExecutableEntityProperties."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "RPT-EXECUTABLE-ENTITY-PROPERTIES"


    max_rpt_event_id: Optional[PositiveInteger]
    min_rpt_event_id: Optional[PositiveInteger]
    rpt_execution_control: Optional[RptExecutionControlEnum]
    rpt_service_point_enum: Optional[RptServicePointEnum]
    _DESERIALIZE_DISPATCH = {
        "MAX-RPT-EVENT-ID": lambda obj, elem: setattr(obj, "max_rpt_event_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MIN-RPT-EVENT-ID": lambda obj, elem: setattr(obj, "min_rpt_event_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "RPT-EXECUTION-CONTROL": lambda obj, elem: setattr(obj, "rpt_execution_control", RptExecutionControlEnum.deserialize(elem)),
        "RPT-SERVICE-POINT-ENUM": lambda obj, elem: setattr(obj, "rpt_service_point_enum", RptServicePointEnum.deserialize(elem)),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MAX-RPT-EVENT-ID":
                setattr(obj, "max_rpt_event_id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "MIN-RPT-EVENT-ID":
                setattr(obj, "min_rpt_event_id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "RPT-EXECUTION-CONTROL":
                setattr(obj, "rpt_execution_control", RptExecutionControlEnum.deserialize(child))
            elif tag == "RPT-SERVICE-POINT-ENUM":
                setattr(obj, "rpt_service_point_enum", RptServicePointEnum.deserialize(child))

        return obj



class RptExecutableEntityPropertiesBuilder(BuilderBase):
    """Builder for RptExecutableEntityProperties with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RptExecutableEntityProperties = RptExecutableEntityProperties()


    def with_max_rpt_event_id(self, value: Optional[PositiveInteger]) -> "RptExecutableEntityPropertiesBuilder":
        """Set max_rpt_event_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_rpt_event_id = value
        return self

    def with_min_rpt_event_id(self, value: Optional[PositiveInteger]) -> "RptExecutableEntityPropertiesBuilder":
        """Set min_rpt_event_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.min_rpt_event_id = value
        return self

    def with_rpt_execution_control(self, value: Optional[RptExecutionControlEnum]) -> "RptExecutableEntityPropertiesBuilder":
        """Set rpt_execution_control attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rpt_execution_control = value
        return self

    def with_rpt_service_point_enum(self, value: Optional[RptServicePointEnum]) -> "RptExecutableEntityPropertiesBuilder":
        """Set rpt_service_point_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rpt_service_point_enum = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "maxRptEventId",
        "minRptEventId",
        "rptExecutionControl",
        "rptServicePointEnum",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> RptExecutableEntityProperties:
        """Build and return the RptExecutableEntityProperties instance with validation."""
        self._validate_instance()
        return self._obj