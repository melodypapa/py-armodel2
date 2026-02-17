"""SwSystemconstValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2068)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 80)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 235)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)
from armodel.models.M2.MSR.Documentation.Annotation.annotation import (
    Annotation,
)
from armodel.models.M2.MSR.DataDictionary.SystemConstant.sw_systemconst import (
    SwSystemconst,
)


class SwSystemconstValue(ARObject):
    """AUTOSAR SwSystemconstValue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "annotations": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Annotation,
        ),  # annotations
        "sw_systemconst": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=SwSystemconst,
        ),  # swSystemconst
        "value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # value
    }

    def __init__(self) -> None:
        """Initialize SwSystemconstValue."""
        super().__init__()
        self.annotations: list[Annotation] = []
        self.sw_systemconst: SwSystemconst = None
        self.value: Numerical = None


class SwSystemconstValueBuilder:
    """Builder for SwSystemconstValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwSystemconstValue = SwSystemconstValue()

    def build(self) -> SwSystemconstValue:
        """Build and return SwSystemconstValue object.

        Returns:
            SwSystemconstValue instance
        """
        # TODO: Add validation
        return self._obj
