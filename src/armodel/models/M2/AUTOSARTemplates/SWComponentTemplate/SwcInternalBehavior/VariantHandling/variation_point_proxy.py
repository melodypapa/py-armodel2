"""VariationPointProxy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 613)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 479)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import (
    AbstractImplementationDataType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.condition_by_formula import (
    ConditionByFormula,
)


class VariationPointProxy(Identifiable):
    """AUTOSAR VariationPointProxy."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "condition_access": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ConditionByFormula,
        ),  # conditionAccess
        "implementation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AbstractImplementationDataType,
        ),  # implementation
        "post_build_value": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (PostBuildVariant),
        ),  # postBuildValue
    }

    def __init__(self) -> None:
        """Initialize VariationPointProxy."""
        super().__init__()
        self.condition_access: Optional[ConditionByFormula] = None
        self.implementation: Optional[AbstractImplementationDataType] = None
        self.post_build_value: Optional[Any] = None


class VariationPointProxyBuilder:
    """Builder for VariationPointProxy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VariationPointProxy = VariationPointProxy()

    def build(self) -> VariationPointProxy:
        """Build and return VariationPointProxy object.

        Returns:
            VariationPointProxy instance
        """
        # TODO: Add validation
        return self._obj
