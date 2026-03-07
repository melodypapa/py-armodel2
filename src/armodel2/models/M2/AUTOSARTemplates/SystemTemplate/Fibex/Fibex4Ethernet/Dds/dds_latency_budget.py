"""DdsLatencyBudget AUTOSAR element.

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


class DdsLatencyBudget(ARObject):
    """AUTOSAR DdsLatencyBudget."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DDS-LATENCY-BUDGET"


    latency_budget: Optional[Float]
    _DESERIALIZE_DISPATCH = {
        "LATENCY-BUDGET": lambda obj, elem: setattr(obj, "latency_budget", SerializationHelper.deserialize_by_tag(elem, "Float")),
    }


    def __init__(self) -> None:
        """Initialize DdsLatencyBudget."""
        super().__init__()
        self.latency_budget: Optional[Float] = None

    def serialize(self) -> ET.Element:
        """Serialize DdsLatencyBudget to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsLatencyBudget, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize latency_budget
        if self.latency_budget is not None:
            serialized = SerializationHelper.serialize_item(self.latency_budget, "Float")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LATENCY-BUDGET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsLatencyBudget":
        """Deserialize XML element to DdsLatencyBudget object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsLatencyBudget object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DdsLatencyBudget, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "LATENCY-BUDGET":
                setattr(obj, "latency_budget", SerializationHelper.deserialize_by_tag(child, "Float"))

        return obj



class DdsLatencyBudgetBuilder(BuilderBase):
    """Builder for DdsLatencyBudget with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DdsLatencyBudget = DdsLatencyBudget()


    def with_latency_budget(self, value: Optional[Float]) -> "DdsLatencyBudgetBuilder":
        """Set latency_budget attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'latency_budget' is required and cannot be None")
        self._obj.latency_budget = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "latencyBudget",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DdsLatencyBudget:
        """Build and return the DdsLatencyBudget instance with validation."""
        self._validate_instance()
        return self._obj