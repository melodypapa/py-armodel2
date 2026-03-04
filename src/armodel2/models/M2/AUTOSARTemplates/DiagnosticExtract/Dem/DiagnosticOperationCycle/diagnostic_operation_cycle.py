"""DiagnosticOperationCycle AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 201)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticOperationCycle.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import DiagnosticCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticOperationCycle(DiagnosticCommonElement):
    """AUTOSAR DiagnosticOperationCycle."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-OPERATION-CYCLE"


    type_cycle_type_enum: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "TYPE-CYCLE-TYPE-ENUM": lambda obj, elem: setattr(obj, "type_cycle_type_enum", SerializationHelper.deserialize_by_tag(elem, "any (DiagnosticOperation)")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticOperationCycle."""
        super().__init__()
        self.type_cycle_type_enum: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticOperationCycle to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticOperationCycle, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize type_cycle_type_enum
        if self.type_cycle_type_enum is not None:
            serialized = SerializationHelper.serialize_item(self.type_cycle_type_enum, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TYPE-CYCLE-TYPE-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticOperationCycle":
        """Deserialize XML element to DiagnosticOperationCycle object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticOperationCycle object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticOperationCycle, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TYPE-CYCLE-TYPE-ENUM":
                setattr(obj, "type_cycle_type_enum", SerializationHelper.deserialize_by_tag(child, "any (DiagnosticOperation)"))

        return obj



class DiagnosticOperationCycleBuilder(DiagnosticCommonElementBuilder):
    """Builder for DiagnosticOperationCycle with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticOperationCycle = DiagnosticOperationCycle()


    def with_type_cycle_type_enum(self, value: Optional[any (DiagnosticOperation)]) -> "DiagnosticOperationCycleBuilder":
        """Set type_cycle_type_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.type_cycle_type_enum = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "typeCycleTypeEnum",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticOperationCycle:
        """Build and return the DiagnosticOperationCycle instance with validation."""
        self._validate_instance()
        return self._obj