"""DiagnosticEnvConditionFormulaPart AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 80)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_EnvironmentalCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticEnvConditionFormulaPart(ARObject, ABC):
    """AUTOSAR DiagnosticEnvConditionFormulaPart."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize DiagnosticEnvConditionFormulaPart."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEnvConditionFormulaPart to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEnvConditionFormulaPart, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "DiagnosticEnvConditionFormulaPart":
        """Deserialize XML element to DiagnosticEnvConditionFormulaPart object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEnvConditionFormulaPart object
        """
        # Delegate to parent class to handle inherited attributes
        return super(DiagnosticEnvConditionFormulaPart, cls).deserialize(element)



class DiagnosticEnvConditionFormulaPartBuilder(BuilderBase, ABC):
    """Builder for DiagnosticEnvConditionFormulaPart with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticEnvConditionFormulaPart = DiagnosticEnvConditionFormulaPart()






    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> DiagnosticEnvConditionFormulaPart:
        """Build and return the DiagnosticEnvConditionFormulaPart instance (abstract)."""
        raise NotImplementedError