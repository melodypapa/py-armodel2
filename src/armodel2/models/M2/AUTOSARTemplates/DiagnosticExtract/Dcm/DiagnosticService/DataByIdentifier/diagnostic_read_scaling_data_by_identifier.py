"""DiagnosticReadScalingDataByIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 116)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_DataByIdentifier.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.DataByIdentifier.diagnostic_data_by_identifier import (
    DiagnosticDataByIdentifier,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.DataByIdentifier.diagnostic_data_by_identifier import DiagnosticDataByIdentifierBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticReadScalingDataByIdentifier(DiagnosticDataByIdentifier):
    """AUTOSAR DiagnosticReadScalingDataByIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER"


    read_scaling_ref: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "READ-SCALING-REF": lambda obj, elem: setattr(obj, "read_scaling_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticReadScalingDataByIdentifier."""
        super().__init__()
        self.read_scaling_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticReadScalingDataByIdentifier to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticReadScalingDataByIdentifier, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize read_scaling_ref
        if self.read_scaling_ref is not None:
            serialized = SerializationHelper.serialize_item(self.read_scaling_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("READ-SCALING-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticReadScalingDataByIdentifier":
        """Deserialize XML element to DiagnosticReadScalingDataByIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticReadScalingDataByIdentifier object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticReadScalingDataByIdentifier, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "READ-SCALING-REF":
                setattr(obj, "read_scaling_ref", ARRef.deserialize(child))

        return obj



class DiagnosticReadScalingDataByIdentifierBuilder(DiagnosticDataByIdentifierBuilder):
    """Builder for DiagnosticReadScalingDataByIdentifier with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticReadScalingDataByIdentifier = DiagnosticReadScalingDataByIdentifier()


    def with_read_scaling(self, value: Optional[any (DiagnosticReadScaling)]) -> "DiagnosticReadScalingDataByIdentifierBuilder":
        """Set read_scaling attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.read_scaling = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "readScaling",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticReadScalingDataByIdentifier:
        """Build and return the DiagnosticReadScalingDataByIdentifier instance with validation."""
        self._validate_instance()
        return self._obj