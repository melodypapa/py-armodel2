"""BlueprintFormula AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 163)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_BlueprintFormula.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_definition_element import (
    EcucDefinitionElement,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_verbatim import (
    MultiLanguageVerbatim,
)


class BlueprintFormula(ARObject):
    """AUTOSAR BlueprintFormula."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ecuc": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=EcucDefinitionElement,
        ),  # ecuc
        "verbatim": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=MultiLanguageVerbatim,
        ),  # verbatim
    }

    def __init__(self) -> None:
        """Initialize BlueprintFormula."""
        super().__init__()
        self.ecuc: EcucDefinitionElement = None
        self.verbatim: MultiLanguageVerbatim = None


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
