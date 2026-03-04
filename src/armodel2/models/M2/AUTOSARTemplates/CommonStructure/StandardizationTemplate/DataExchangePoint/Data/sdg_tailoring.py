"""SdgTailoring AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 118)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.restriction_with_severity import (
    RestrictionWithSeverity,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.restriction_with_severity import RestrictionWithSeverityBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_class import (
    SdgClass,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SdgTailoring(RestrictionWithSeverity):
    """AUTOSAR SdgTailoring."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SDG-TAILORING"


    sdg_class_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "SDG-CLASS-REF": lambda obj, elem: setattr(obj, "sdg_class_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize SdgTailoring."""
        super().__init__()
        self.sdg_class_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SdgTailoring to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SdgTailoring, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sdg_class_ref
        if self.sdg_class_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sdg_class_ref, "SdgClass")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SDG-CLASS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgTailoring":
        """Deserialize XML element to SdgTailoring object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SdgTailoring object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SdgTailoring, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SDG-CLASS-REF":
                setattr(obj, "sdg_class_ref", ARRef.deserialize(child))

        return obj



class SdgTailoringBuilder(RestrictionWithSeverityBuilder):
    """Builder for SdgTailoring with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SdgTailoring = SdgTailoring()


    def with_sdg_class(self, value: Optional[SdgClass]) -> "SdgTailoringBuilder":
        """Set sdg_class attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sdg_class = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "sdgClass",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SdgTailoring:
        """Build and return the SdgTailoring instance with validation."""
        self._validate_instance()
        return self._obj