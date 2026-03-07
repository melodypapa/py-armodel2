"""DdsDeadline AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 532)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DdsDeadline(ARObject):
    """AUTOSAR DdsDeadline."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DDS-DEADLINE"


    deadline_period: Optional[Float]
    _DESERIALIZE_DISPATCH = {
        "DEADLINE-PERIOD": lambda obj, elem: setattr(obj, "deadline_period", SerializationHelper.deserialize_by_tag(elem, "Float")),
    }


    def __init__(self) -> None:
        """Initialize DdsDeadline."""
        super().__init__()
        self.deadline_period: Optional[Float] = None

    def serialize(self) -> ET.Element:
        """Serialize DdsDeadline to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsDeadline, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize deadline_period
        if self.deadline_period is not None:
            serialized = SerializationHelper.serialize_item(self.deadline_period, "Float")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEADLINE-PERIOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsDeadline":
        """Deserialize XML element to DdsDeadline object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsDeadline object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DdsDeadline, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DEADLINE-PERIOD":
                setattr(obj, "deadline_period", SerializationHelper.deserialize_by_tag(child, "Float"))

        return obj



class DdsDeadlineBuilder(BuilderBase):
    """Builder for DdsDeadline with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DdsDeadline = DdsDeadline()


    def with_deadline_period(self, value: Optional[Float]) -> "DdsDeadlineBuilder":
        """Set deadline_period attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'deadline_period' is required and cannot be None")
        self._obj.deadline_period = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "deadlinePeriod",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DdsDeadline:
        """Build and return the DdsDeadline instance with validation."""
        self._validate_instance()
        return self._obj