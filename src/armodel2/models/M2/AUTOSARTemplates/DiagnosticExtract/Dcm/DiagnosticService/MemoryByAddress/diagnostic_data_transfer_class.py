"""DiagnosticDataTransferClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 144)

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


class DiagnosticDataTransferClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticDataTransferClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-DATA-TRANSFER-CLASS"


    def __init__(self) -> None:
        """Initialize DiagnosticDataTransferClass."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticDataTransferClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticDataTransferClass, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "DiagnosticDataTransferClass":
        """Deserialize XML element to DiagnosticDataTransferClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticDataTransferClass object
        """
        # Delegate to parent class to handle inherited attributes
        return super(DiagnosticDataTransferClass, cls).deserialize(element)



class DiagnosticDataTransferClassBuilder(DiagnosticServiceClassBuilder):
    """Builder for DiagnosticDataTransferClass with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticDataTransferClass = DiagnosticDataTransferClass()






    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticDataTransferClass:
        """Build and return the DiagnosticDataTransferClass instance with validation."""
        self._validate_instance()
        return self._obj