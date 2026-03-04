"""DiagnosticDataByIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 113)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_DataByIdentifier.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import DiagnosticServiceInstanceBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_abstract_data_identifier import (
    DiagnosticAbstractDataIdentifier,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticDataByIdentifier(DiagnosticServiceInstance, ABC):
    """AUTOSAR DiagnosticDataByIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    data_identifier_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "DATA-IDENTIFIER-REF": ("_POLYMORPHIC", "data_identifier_ref", ["DiagnosticDataIdentifier", "DiagnosticDynamicDataIdentifier"]),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticDataByIdentifier."""
        super().__init__()
        self.data_identifier_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticDataByIdentifier to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticDataByIdentifier, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_identifier_ref
        if self.data_identifier_ref is not None:
            serialized = SerializationHelper.serialize_item(self.data_identifier_ref, "DiagnosticAbstractDataIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-IDENTIFIER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticDataByIdentifier":
        """Deserialize XML element to DiagnosticDataByIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticDataByIdentifier object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticDataByIdentifier, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATA-IDENTIFIER-REF":
                setattr(obj, "data_identifier_ref", ARRef.deserialize(child))

        return obj



class DiagnosticDataByIdentifierBuilder(DiagnosticServiceInstanceBuilder):
    """Builder for DiagnosticDataByIdentifier with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticDataByIdentifier = DiagnosticDataByIdentifier()


    def with_data_identifier(self, value: Optional[DiagnosticAbstractDataIdentifier]) -> "DiagnosticDataByIdentifierBuilder":
        """Set data_identifier attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_identifier = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dataIdentifier",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> DiagnosticDataByIdentifier:
        """Build and return the DiagnosticDataByIdentifier instance (abstract)."""
        raise NotImplementedError