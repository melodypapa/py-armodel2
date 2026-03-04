"""ObdInfoServiceNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 324)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 233)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 797)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import DiagnosticCapabilityElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ObdInfoServiceNeeds(DiagnosticCapabilityElement):
    """AUTOSAR ObdInfoServiceNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "OBD-INFO-SERVICE-NEEDS"


    def __init__(self) -> None:
        """Initialize ObdInfoServiceNeeds."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize ObdInfoServiceNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ObdInfoServiceNeeds, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "ObdInfoServiceNeeds":
        """Deserialize XML element to ObdInfoServiceNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ObdInfoServiceNeeds object
        """
        # Delegate to parent class to handle inherited attributes
        return super(ObdInfoServiceNeeds, cls).deserialize(element)



class ObdInfoServiceNeedsBuilder(DiagnosticCapabilityElementBuilder):
    """Builder for ObdInfoServiceNeeds with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ObdInfoServiceNeeds = ObdInfoServiceNeeds()






    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ObdInfoServiceNeeds:
        """Build and return the ObdInfoServiceNeeds instance with validation."""
        self._validate_instance()
        return self._obj