"""EcucTextualParamValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 127)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 443)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 190)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_parameter_value import (
    EcucParameterValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    VerbatimString,
)


class EcucTextualParamValue(EcucParameterValue):
    """AUTOSAR EcucTextualParamValue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # value
    }

    def __init__(self) -> None:
        """Initialize EcucTextualParamValue."""
        super().__init__()
        self.value: Optional[VerbatimString] = None


class EcucTextualParamValueBuilder:
    """Builder for EcucTextualParamValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucTextualParamValue = EcucTextualParamValue()

    def build(self) -> EcucTextualParamValue:
        """Build and return EcucTextualParamValue object.

        Returns:
            EcucTextualParamValue instance
        """
        # TODO: Add validation
        return self._obj
