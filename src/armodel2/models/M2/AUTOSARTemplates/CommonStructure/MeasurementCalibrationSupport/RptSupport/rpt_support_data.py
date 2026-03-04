"""RptSupportData AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 198)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport_RptSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_component import (
    RptComponent,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_execution_context import (
    RptExecutionContext,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_service_point import (
    RptServicePoint,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class RptSupportData(ARObject):
    """AUTOSAR RptSupportData."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "RPT-SUPPORT-DATA"


    executions: list[RptExecutionContext]
    rpt_components: list[RptComponent]
    rpt_service_points: list[RptServicePoint]
    _DESERIALIZE_DISPATCH = {
        "EXECUTIONS": lambda obj, elem: obj.executions.append(SerializationHelper.deserialize_by_tag(elem, "RptExecutionContext")),
        "RPT-COMPONENTS": lambda obj, elem: obj.rpt_components.append(SerializationHelper.deserialize_by_tag(elem, "RptComponent")),
        "RPT-SERVICE-POINTS": lambda obj, elem: obj.rpt_service_points.append(SerializationHelper.deserialize_by_tag(elem, "RptServicePoint")),
    }


    def __init__(self) -> None:
        """Initialize RptSupportData."""
        super().__init__()
        self.executions: list[RptExecutionContext] = []
        self.rpt_components: list[RptComponent] = []
        self.rpt_service_points: list[RptServicePoint] = []

    def serialize(self) -> ET.Element:
        """Serialize RptSupportData to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RptSupportData, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize executions (list to container "EXECUTIONS")
        if self.executions:
            wrapper = ET.Element("EXECUTIONS")
            for item in self.executions:
                serialized = SerializationHelper.serialize_item(item, "RptExecutionContext")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rpt_components (list to container "RPT-COMPONENTS")
        if self.rpt_components:
            wrapper = ET.Element("RPT-COMPONENTS")
            for item in self.rpt_components:
                serialized = SerializationHelper.serialize_item(item, "RptComponent")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rpt_service_points (list to container "RPT-SERVICE-POINTS")
        if self.rpt_service_points:
            wrapper = ET.Element("RPT-SERVICE-POINTS")
            for item in self.rpt_service_points:
                serialized = SerializationHelper.serialize_item(item, "RptServicePoint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptSupportData":
        """Deserialize XML element to RptSupportData object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RptSupportData object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RptSupportData, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "EXECUTIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.executions.append(SerializationHelper.deserialize_by_tag(item_elem, "RptExecutionContext"))
            elif tag == "RPT-COMPONENTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.rpt_components.append(SerializationHelper.deserialize_by_tag(item_elem, "RptComponent"))
            elif tag == "RPT-SERVICE-POINTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.rpt_service_points.append(SerializationHelper.deserialize_by_tag(item_elem, "RptServicePoint"))

        return obj



class RptSupportDataBuilder(BuilderBase):
    """Builder for RptSupportData with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RptSupportData = RptSupportData()


    def with_executions(self, items: list[RptExecutionContext]) -> "RptSupportDataBuilder":
        """Set executions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.executions = list(items) if items else []
        return self

    def with_rpt_components(self, items: list[RptComponent]) -> "RptSupportDataBuilder":
        """Set rpt_components list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.rpt_components = list(items) if items else []
        return self

    def with_rpt_service_points(self, items: list[RptServicePoint]) -> "RptSupportDataBuilder":
        """Set rpt_service_points list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.rpt_service_points = list(items) if items else []
        return self


    def add_execution(self, item: RptExecutionContext) -> "RptSupportDataBuilder":
        """Add a single item to executions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.executions.append(item)
        return self

    def clear_executions(self) -> "RptSupportDataBuilder":
        """Clear all items from executions list.

        Returns:
            self for method chaining
        """
        self._obj.executions = []
        return self

    def add_rpt_component(self, item: RptComponent) -> "RptSupportDataBuilder":
        """Add a single item to rpt_components list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.rpt_components.append(item)
        return self

    def clear_rpt_components(self) -> "RptSupportDataBuilder":
        """Clear all items from rpt_components list.

        Returns:
            self for method chaining
        """
        self._obj.rpt_components = []
        return self

    def add_rpt_service_point(self, item: RptServicePoint) -> "RptSupportDataBuilder":
        """Add a single item to rpt_service_points list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.rpt_service_points.append(item)
        return self

    def clear_rpt_service_points(self) -> "RptSupportDataBuilder":
        """Clear all items from rpt_service_points list.

        Returns:
            self for method chaining
        """
        self._obj.rpt_service_points = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "execution",
        "rptComponent",
        "rptServicePoint",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> RptSupportData:
        """Build and return the RptSupportData instance with validation."""
        self._validate_instance()
        return self._obj