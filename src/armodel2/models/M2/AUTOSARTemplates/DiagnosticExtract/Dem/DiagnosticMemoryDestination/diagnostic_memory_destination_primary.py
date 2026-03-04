"""DiagnosticMemoryDestinationPrimary AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 184)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticMemoryDestination.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticMemoryDestination.diagnostic_memory_destination import (
    DiagnosticMemoryDestination,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticMemoryDestination.diagnostic_memory_destination import DiagnosticMemoryDestinationBuilder
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode import (
    DiagnosticTypeOfDtcSupportedEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticMemoryDestinationPrimary(DiagnosticMemoryDestination):
    """AUTOSAR DiagnosticMemoryDestinationPrimary."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-MEMORY-DESTINATION-PRIMARY"


    type_of_dtc: Optional[DiagnosticTypeOfDtcSupportedEnum]
    _DESERIALIZE_DISPATCH = {
        "TYPE-OF-DTC": lambda obj, elem: setattr(obj, "type_of_dtc", DiagnosticTypeOfDtcSupportedEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticMemoryDestinationPrimary."""
        super().__init__()
        self.type_of_dtc: Optional[DiagnosticTypeOfDtcSupportedEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticMemoryDestinationPrimary to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticMemoryDestinationPrimary, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize type_of_dtc
        if self.type_of_dtc is not None:
            serialized = SerializationHelper.serialize_item(self.type_of_dtc, "DiagnosticTypeOfDtcSupportedEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TYPE-OF-DTC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticMemoryDestinationPrimary":
        """Deserialize XML element to DiagnosticMemoryDestinationPrimary object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticMemoryDestinationPrimary object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticMemoryDestinationPrimary, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TYPE-OF-DTC":
                setattr(obj, "type_of_dtc", DiagnosticTypeOfDtcSupportedEnum.deserialize(child))

        return obj



class DiagnosticMemoryDestinationPrimaryBuilder(DiagnosticMemoryDestinationBuilder):
    """Builder for DiagnosticMemoryDestinationPrimary with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticMemoryDestinationPrimary = DiagnosticMemoryDestinationPrimary()


    def with_type_of_dtc(self, value: Optional[DiagnosticTypeOfDtcSupportedEnum]) -> "DiagnosticMemoryDestinationPrimaryBuilder":
        """Set type_of_dtc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.type_of_dtc = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "typeOfDtc",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticMemoryDestinationPrimary:
        """Build and return the DiagnosticMemoryDestinationPrimary instance with validation."""
        self._validate_instance()
        return self._obj