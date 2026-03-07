"""DiagnosticEcuReset AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_EcuReset.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import DiagnosticServiceInstanceBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticEcuReset(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticEcuReset."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-ECU-RESET"


    custom_sub: Optional[PositiveInteger]
    ecu_reset_class_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "CUSTOM-SUB": lambda obj, elem: setattr(obj, "custom_sub", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "ECU-RESET-CLASS-REF": lambda obj, elem: setattr(obj, "ecu_reset_class_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticEcuReset."""
        super().__init__()
        self.custom_sub: Optional[PositiveInteger] = None
        self.ecu_reset_class_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEcuReset to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEcuReset, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize custom_sub
        if self.custom_sub is not None:
            serialized = SerializationHelper.serialize_item(self.custom_sub, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CUSTOM-SUB")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ecu_reset_class_ref
        if self.ecu_reset_class_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ecu_reset_class_ref, "DiagnosticEcuReset")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-RESET-CLASS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEcuReset":
        """Deserialize XML element to DiagnosticEcuReset object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEcuReset object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEcuReset, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CUSTOM-SUB":
                setattr(obj, "custom_sub", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "ECU-RESET-CLASS-REF":
                setattr(obj, "ecu_reset_class_ref", ARRef.deserialize(child))

        return obj



class DiagnosticEcuResetBuilder(DiagnosticServiceInstanceBuilder):
    """Builder for DiagnosticEcuReset with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticEcuReset = DiagnosticEcuReset()


    def with_custom_sub(self, value: Optional[PositiveInteger]) -> "DiagnosticEcuResetBuilder":
        """Set custom_sub attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'custom_sub' is required and cannot be None")
        self._obj.custom_sub = value
        return self

    def with_ecu_reset_class(self, value: Optional[DiagnosticEcuReset]) -> "DiagnosticEcuResetBuilder":
        """Set ecu_reset_class attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'ecu_reset_class' is required and cannot be None")
        self._obj.ecu_reset_class = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "customSub",
        "ecuResetClass",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticEcuReset:
        """Build and return the DiagnosticEcuReset instance with validation."""
        self._validate_instance()
        return self._obj