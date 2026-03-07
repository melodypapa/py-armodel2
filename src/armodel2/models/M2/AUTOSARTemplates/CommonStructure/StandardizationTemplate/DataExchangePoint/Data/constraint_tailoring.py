"""ConstraintTailoring AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 117)

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
from armodel2.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable_text import (
    TraceableText,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ConstraintTailoring(RestrictionWithSeverity):
    """AUTOSAR ConstraintTailoring."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CONSTRAINT-TAILORING"


    constraint_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "CONSTRAINT-REF": lambda obj, elem: setattr(obj, "constraint_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ConstraintTailoring."""
        super().__init__()
        self.constraint_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ConstraintTailoring to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ConstraintTailoring, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize constraint_ref
        if self.constraint_ref is not None:
            serialized = SerializationHelper.serialize_item(self.constraint_ref, "TraceableText")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONSTRAINT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConstraintTailoring":
        """Deserialize XML element to ConstraintTailoring object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConstraintTailoring object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ConstraintTailoring, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONSTRAINT-REF":
                setattr(obj, "constraint_ref", ARRef.deserialize(child))

        return obj



class ConstraintTailoringBuilder(RestrictionWithSeverityBuilder):
    """Builder for ConstraintTailoring with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ConstraintTailoring = ConstraintTailoring()


    def with_constraint(self, value: Optional[TraceableText]) -> "ConstraintTailoringBuilder":
        """Set constraint attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'constraint' is required and cannot be None")
        self._obj.constraint = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "constraint",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ConstraintTailoring:
        """Build and return the ConstraintTailoring instance with validation."""
        self._validate_instance()
        return self._obj