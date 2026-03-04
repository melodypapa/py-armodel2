"""DiagnosticRoutineNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 247)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 126)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 780)

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
    DiagnosticRoutineTypeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticRoutineNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticRoutineNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-ROUTINE-NEEDS"


    diag_routine: Optional[DiagnosticRoutineTypeEnum]
    _DESERIALIZE_DISPATCH = {
        "DIAG-ROUTINE": lambda obj, elem: setattr(obj, "diag_routine", DiagnosticRoutineTypeEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticRoutineNeeds."""
        super().__init__()
        self.diag_routine: Optional[DiagnosticRoutineTypeEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticRoutineNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticRoutineNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize diag_routine
        if self.diag_routine is not None:
            serialized = SerializationHelper.serialize_item(self.diag_routine, "DiagnosticRoutineTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAG-ROUTINE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRoutineNeeds":
        """Deserialize XML element to DiagnosticRoutineNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRoutineNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticRoutineNeeds, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DIAG-ROUTINE":
                setattr(obj, "diag_routine", DiagnosticRoutineTypeEnum.deserialize(child))

        return obj



class DiagnosticRoutineNeedsBuilder(DiagnosticCapabilityElementBuilder):
    """Builder for DiagnosticRoutineNeeds with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticRoutineNeeds = DiagnosticRoutineNeeds()


    def with_diag_routine(self, value: Optional[DiagnosticRoutineTypeEnum]) -> "DiagnosticRoutineNeedsBuilder":
        """Set diag_routine attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.diag_routine = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "diagRoutine",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticRoutineNeeds:
        """Build and return the DiagnosticRoutineNeeds instance with validation."""
        self._validate_instance()
        return self._obj