"""EcucParameterDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 57)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 188)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_common_attributes import (
    EcucCommonAttributes,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_derivation_specification import (
    EcucDerivationSpecification,
)
from abc import ABC, abstractmethod


class EcucParameterDef(EcucCommonAttributes, ABC):
    """AUTOSAR EcucParameterDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    derivation: Optional[EcucDerivationSpecification]
    symbolic_name: Optional[Boolean]
    with_auto: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize EcucParameterDef."""
        super().__init__()
        self.derivation: Optional[EcucDerivationSpecification] = None
        self.symbolic_name: Optional[Boolean] = None
        self.with_auto: Optional[Boolean] = None


class EcucParameterDefBuilder:
    """Builder for EcucParameterDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucParameterDef = EcucParameterDef()

    def build(self) -> EcucParameterDef:
        """Build and return EcucParameterDef object.

        Returns:
            EcucParameterDef instance
        """
        # TODO: Add validation
        return self._obj
