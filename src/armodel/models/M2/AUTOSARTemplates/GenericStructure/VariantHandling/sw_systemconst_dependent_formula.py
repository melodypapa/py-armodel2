"""SwSystemconstDependentFormula AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1006)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 79)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 240)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.DataDictionary.SystemConstant.sw_systemconst import (
    SwSystemconst,
)


class SwSystemconstDependentFormula(ARObject):
    """AUTOSAR SwSystemconstDependentFormula."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "sysc": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwSystemconst,
        ),  # sysc
        "sysc_string": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwSystemconst,
        ),  # syscString
    }

    def __init__(self) -> None:
        """Initialize SwSystemconstDependentFormula."""
        super().__init__()
        self.sysc: Optional[SwSystemconst] = None
        self.sysc_string: Optional[SwSystemconst] = None


class SwSystemconstDependentFormulaBuilder:
    """Builder for SwSystemconstDependentFormula."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwSystemconstDependentFormula = SwSystemconstDependentFormula()

    def build(self) -> SwSystemconstDependentFormula:
        """Build and return SwSystemconstDependentFormula object.

        Returns:
            SwSystemconstDependentFormula instance
        """
        # TODO: Add validation
        return self._obj
