"""DiagnosticStorageCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 194)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticCondition.diagnostic_condition import (
    DiagnosticCondition,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticCondition.diagnostic_condition import DiagnosticConditionBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticStorageCondition(DiagnosticCondition):
    """AUTOSAR DiagnosticStorageCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-STORAGE-CONDITION"


    def __init__(self) -> None:
        """Initialize DiagnosticStorageCondition."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticStorageCondition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticStorageCondition, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "DiagnosticStorageCondition":
        """Deserialize XML element to DiagnosticStorageCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticStorageCondition object
        """
        # Delegate to parent class to handle inherited attributes
        return super(DiagnosticStorageCondition, cls).deserialize(element)



class DiagnosticStorageConditionBuilder(DiagnosticConditionBuilder):
    """Builder for DiagnosticStorageCondition with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticStorageCondition = DiagnosticStorageCondition()






    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticStorageCondition:
        """Build and return the DiagnosticStorageCondition instance with validation."""
        self._validate_instance()
        return self._obj