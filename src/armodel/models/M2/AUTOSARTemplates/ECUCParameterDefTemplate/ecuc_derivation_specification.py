"""EcucDerivationSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 87)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_query import (
    EcucQuery,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Formula.ml_formula import (
    MlFormula,
)


class EcucDerivationSpecification(ARObject):
    """AUTOSAR EcucDerivationSpecification."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "calculation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (EcucParameter),
        ),  # calculation
        "ecuc_queries": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=EcucQuery,
        ),  # ecucQueries
        "informal_formula": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MlFormula,
        ),  # informalFormula
    }

    def __init__(self) -> None:
        """Initialize EcucDerivationSpecification."""
        super().__init__()
        self.calculation: Optional[Any] = None
        self.ecuc_queries: list[EcucQuery] = []
        self.informal_formula: Optional[MlFormula] = None


class EcucDerivationSpecificationBuilder:
    """Builder for EcucDerivationSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucDerivationSpecification = EcucDerivationSpecification()

    def build(self) -> EcucDerivationSpecification:
        """Build and return EcucDerivationSpecification object.

        Returns:
            EcucDerivationSpecification instance
        """
        # TODO: Add validation
        return self._obj
