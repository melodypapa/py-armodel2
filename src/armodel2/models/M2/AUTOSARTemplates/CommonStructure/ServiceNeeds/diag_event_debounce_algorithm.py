"""DiagEventDebounceAlgorithm AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 259)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 196)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 756)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagEventDebounceAlgorithm(Identifiable, ABC):
    """AUTOSAR DiagEventDebounceAlgorithm."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize DiagEventDebounceAlgorithm."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize DiagEventDebounceAlgorithm to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagEventDebounceAlgorithm, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "DiagEventDebounceAlgorithm":
        """Deserialize XML element to DiagEventDebounceAlgorithm object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagEventDebounceAlgorithm object
        """
        # Delegate to parent class to handle inherited attributes
        return super(DiagEventDebounceAlgorithm, cls).deserialize(element)



class DiagEventDebounceAlgorithmBuilder(IdentifiableBuilder):
    """Builder for DiagEventDebounceAlgorithm with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagEventDebounceAlgorithm = DiagEventDebounceAlgorithm()






    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> DiagEventDebounceAlgorithm:
        """Build and return the DiagEventDebounceAlgorithm instance (abstract)."""
        raise NotImplementedError