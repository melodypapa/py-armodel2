"""DiagnosticEcuResetClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_EcuReset.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import DiagnosticServiceClassBuilder
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.EcuReset import (
    DiagnosticResponseToEcuResetEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticEcuResetClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticEcuResetClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-ECU-RESET-CLASS"


    respond_to: Optional[DiagnosticResponseToEcuResetEnum]
    _DESERIALIZE_DISPATCH = {
        "RESPOND-TO": lambda obj, elem: setattr(obj, "respond_to", DiagnosticResponseToEcuResetEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticEcuResetClass."""
        super().__init__()
        self.respond_to: Optional[DiagnosticResponseToEcuResetEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEcuResetClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEcuResetClass, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize respond_to
        if self.respond_to is not None:
            serialized = SerializationHelper.serialize_item(self.respond_to, "DiagnosticResponseToEcuResetEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESPOND-TO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEcuResetClass":
        """Deserialize XML element to DiagnosticEcuResetClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEcuResetClass object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEcuResetClass, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "RESPOND-TO":
                setattr(obj, "respond_to", DiagnosticResponseToEcuResetEnum.deserialize(child))

        return obj



class DiagnosticEcuResetClassBuilder(DiagnosticServiceClassBuilder):
    """Builder for DiagnosticEcuResetClass with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticEcuResetClass = DiagnosticEcuResetClass()


    def with_respond_to(self, value: Optional[DiagnosticResponseToEcuResetEnum]) -> "DiagnosticEcuResetClassBuilder":
        """Set respond_to attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.respond_to = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "respondTo",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticEcuResetClass:
        """Build and return the DiagnosticEcuResetClass instance with validation."""
        self._validate_instance()
        return self._obj