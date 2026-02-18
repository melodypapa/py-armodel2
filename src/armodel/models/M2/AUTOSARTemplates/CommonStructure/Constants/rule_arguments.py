"""RuleArguments AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 329)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 469)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
    VerbatimString,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.numerical_or_text import (
    NumericalOrText,
)


class RuleArguments(ARObject):
    """AUTOSAR RuleArguments."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    v: Optional[Numerical]
    vf: Optional[Numerical]
    vt: Optional[VerbatimString]
    vtf: Optional[NumericalOrText]
    def __init__(self) -> None:
        """Initialize RuleArguments."""
        super().__init__()
        self.v: Optional[Numerical] = None
        self.vf: Optional[Numerical] = None
        self.vt: Optional[VerbatimString] = None
        self.vtf: Optional[NumericalOrText] = None


class RuleArgumentsBuilder:
    """Builder for RuleArguments."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RuleArguments = RuleArguments()

    def build(self) -> RuleArguments:
        """Build and return RuleArguments object.

        Returns:
            RuleArguments instance
        """
        # TODO: Add validation
        return self._obj
