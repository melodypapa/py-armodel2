"""EcucFloatParamDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 61)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 186)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import (
    EcucParameterDef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
    Limit,
)


class EcucFloatParamDef(EcucParameterDef):
    """AUTOSAR EcucFloatParamDef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "default_value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # defaultValue
        "max": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # max
        "min": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # min
    }

    def __init__(self) -> None:
        """Initialize EcucFloatParamDef."""
        super().__init__()
        self.default_value: Optional[Float] = None
        self.max: Optional[Limit] = None
        self.min: Optional[Limit] = None


class EcucFloatParamDefBuilder:
    """Builder for EcucFloatParamDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucFloatParamDef = EcucFloatParamDef()

    def build(self) -> EcucFloatParamDef:
        """Build and return EcucFloatParamDef object.

        Returns:
            EcucFloatParamDef instance
        """
        # TODO: Add validation
        return self._obj
