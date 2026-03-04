"""ObdRatioDenominatorNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 802)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import DiagnosticCapabilityElementBuilder
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticDenominatorConditionEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ObdRatioDenominatorNeeds(DiagnosticCapabilityElement):
    """AUTOSAR ObdRatioDenominatorNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "OBD-RATIO-DENOMINATOR-NEEDS"


    denominator: Optional[DiagnosticDenominatorConditionEnum]
    _DESERIALIZE_DISPATCH = {
        "DENOMINATOR": lambda obj, elem: setattr(obj, "denominator", DiagnosticDenominatorConditionEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ObdRatioDenominatorNeeds."""
        super().__init__()
        self.denominator: Optional[DiagnosticDenominatorConditionEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize ObdRatioDenominatorNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ObdRatioDenominatorNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize denominator
        if self.denominator is not None:
            serialized = SerializationHelper.serialize_item(self.denominator, "DiagnosticDenominatorConditionEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DENOMINATOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ObdRatioDenominatorNeeds":
        """Deserialize XML element to ObdRatioDenominatorNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ObdRatioDenominatorNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ObdRatioDenominatorNeeds, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DENOMINATOR":
                setattr(obj, "denominator", DiagnosticDenominatorConditionEnum.deserialize(child))

        return obj



class ObdRatioDenominatorNeedsBuilder(DiagnosticCapabilityElementBuilder):
    """Builder for ObdRatioDenominatorNeeds with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ObdRatioDenominatorNeeds = ObdRatioDenominatorNeeds()


    def with_denominator(self, value: Optional[DiagnosticDenominatorConditionEnum]) -> "ObdRatioDenominatorNeedsBuilder":
        """Set denominator attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.denominator = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "denominator",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ObdRatioDenominatorNeeds:
        """Build and return the ObdRatioDenominatorNeeds instance with validation."""
        self._validate_instance()
        return self._obj