"""IndicatorStatusNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 766)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import ServiceNeedsBuilder
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticIndicator import (
    DiagnosticIndicatorTypeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IndicatorStatusNeeds(ServiceNeeds):
    """AUTOSAR IndicatorStatusNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "INDICATOR-STATUS-NEEDS"


    type_enum: Optional[DiagnosticIndicatorTypeEnum]
    _DESERIALIZE_DISPATCH = {
        "TYPE-ENUM": lambda obj, elem: setattr(obj, "type_enum", DiagnosticIndicatorTypeEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize IndicatorStatusNeeds."""
        super().__init__()
        self.type_enum: Optional[DiagnosticIndicatorTypeEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize IndicatorStatusNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IndicatorStatusNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize type_enum
        if self.type_enum is not None:
            serialized = SerializationHelper.serialize_item(self.type_enum, "DiagnosticIndicatorTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TYPE-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IndicatorStatusNeeds":
        """Deserialize XML element to IndicatorStatusNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IndicatorStatusNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IndicatorStatusNeeds, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TYPE-ENUM":
                setattr(obj, "type_enum", DiagnosticIndicatorTypeEnum.deserialize(child))

        return obj



class IndicatorStatusNeedsBuilder(ServiceNeedsBuilder):
    """Builder for IndicatorStatusNeeds with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IndicatorStatusNeeds = IndicatorStatusNeeds()


    def with_type_enum(self, value: Optional[DiagnosticIndicatorTypeEnum]) -> "IndicatorStatusNeedsBuilder":
        """Set type_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.type_enum = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "typeEnum",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> IndicatorStatusNeeds:
        """Build and return the IndicatorStatusNeeds instance with validation."""
        self._validate_instance()
        return self._obj