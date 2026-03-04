"""DiagnosticComControl AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 108)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_CommunicationControl.classes.json"""

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


class DiagnosticComControl(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticComControl."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-COM-CONTROL"


    com_control_ref: Optional[ARRef]
    custom_sub: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "COM-CONTROL-REF": lambda obj, elem: setattr(obj, "com_control_ref", ARRef.deserialize(elem)),
        "CUSTOM-SUB": lambda obj, elem: setattr(obj, "custom_sub", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticComControl."""
        super().__init__()
        self.com_control_ref: Optional[ARRef] = None
        self.custom_sub: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticComControl to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticComControl, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize com_control_ref
        if self.com_control_ref is not None:
            serialized = SerializationHelper.serialize_item(self.com_control_ref, "DiagnosticComControl")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COM-CONTROL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticComControl":
        """Deserialize XML element to DiagnosticComControl object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticComControl object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticComControl, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "COM-CONTROL-REF":
                setattr(obj, "com_control_ref", ARRef.deserialize(child))
            elif tag == "CUSTOM-SUB":
                setattr(obj, "custom_sub", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class DiagnosticComControlBuilder(DiagnosticServiceInstanceBuilder):
    """Builder for DiagnosticComControl with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticComControl = DiagnosticComControl()


    def with_com_control(self, value: Optional[DiagnosticComControl]) -> "DiagnosticComControlBuilder":
        """Set com_control attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.com_control = value
        return self

    def with_custom_sub(self, value: Optional[PositiveInteger]) -> "DiagnosticComControlBuilder":
        """Set custom_sub attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.custom_sub = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "comControl",
        "customSub",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticComControl:
        """Build and return the DiagnosticComControl instance with validation."""
        self._validate_instance()
        return self._obj