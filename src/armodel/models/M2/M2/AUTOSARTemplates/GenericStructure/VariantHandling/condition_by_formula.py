"""ConditionByFormula AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 613)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2012)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 73)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 231)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    BindingTimeEnum,
)


class ConditionByFormula(ARObject):
    """AUTOSAR ConditionByFormula."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "binding_time_enum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=BindingTimeEnum,
        ),  # bindingTimeEnum
    }

    def __init__(self) -> None:
        """Initialize ConditionByFormula."""
        super().__init__()
        self.binding_time_enum: BindingTimeEnum = None


class ConditionByFormulaBuilder:
    """Builder for ConditionByFormula."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConditionByFormula = ConditionByFormula()

    def build(self) -> ConditionByFormula:
        """Build and return ConditionByFormula object.

        Returns:
            ConditionByFormula instance
        """
        # TODO: Add validation
        return self._obj
