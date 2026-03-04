"""DiagnosticWriteMemoryByAddressClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 141)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import DiagnosticServiceClassBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticWriteMemoryByAddressClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticWriteMemoryByAddressClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS-CLASS"


    def __init__(self) -> None:
        """Initialize DiagnosticWriteMemoryByAddressClass."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticWriteMemoryByAddressClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticWriteMemoryByAddressClass, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticWriteMemoryByAddressClass":
        """Deserialize XML element to DiagnosticWriteMemoryByAddressClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticWriteMemoryByAddressClass object
        """
        # Delegate to parent class to handle inherited attributes
        return super(DiagnosticWriteMemoryByAddressClass, cls).deserialize(element)



class DiagnosticWriteMemoryByAddressClassBuilder(DiagnosticServiceClassBuilder):
    """Builder for DiagnosticWriteMemoryByAddressClass with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticWriteMemoryByAddressClass = DiagnosticWriteMemoryByAddressClass()






    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticWriteMemoryByAddressClass:
        """Build and return the DiagnosticWriteMemoryByAddressClass instance with validation."""
        self._validate_instance()
        return self._obj