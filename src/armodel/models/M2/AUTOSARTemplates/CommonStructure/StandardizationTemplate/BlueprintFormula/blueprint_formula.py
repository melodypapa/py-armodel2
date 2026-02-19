"""BlueprintFormula AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 163)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_BlueprintFormula.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_definition_element import (
    EcucDefinitionElement,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_verbatim import (
    MultiLanguageVerbatim,
)


class BlueprintFormula(ARObject):
    """AUTOSAR BlueprintFormula."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ecuc: EcucDefinitionElement
    verbatim: MultiLanguageVerbatim
    def __init__(self) -> None:
        """Initialize BlueprintFormula."""
        super().__init__()
        self.ecuc: EcucDefinitionElement = None
        self.verbatim: MultiLanguageVerbatim = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BlueprintFormula":
        """Deserialize XML element to BlueprintFormula object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BlueprintFormula object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ecuc
        child = ARObject._find_child_element(element, "ECUC")
        if child is not None:
            ecuc_value = ARObject._deserialize_by_tag(child, "EcucDefinitionElement")
            obj.ecuc = ecuc_value

        # Parse verbatim
        child = ARObject._find_child_element(element, "VERBATIM")
        if child is not None:
            verbatim_value = ARObject._deserialize_by_tag(child, "MultiLanguageVerbatim")
            obj.verbatim = verbatim_value

        return obj



class BlueprintFormulaBuilder:
    """Builder for BlueprintFormula."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BlueprintFormula = BlueprintFormula()

    def build(self) -> BlueprintFormula:
        """Build and return BlueprintFormula object.

        Returns:
            BlueprintFormula instance
        """
        # TODO: Add validation
        return self._obj
