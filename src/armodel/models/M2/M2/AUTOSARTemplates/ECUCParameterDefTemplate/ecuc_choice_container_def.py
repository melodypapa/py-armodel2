"""EcucChoiceContainerDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 41)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_param_conf_container_def import (
    EcucParamConfContainerDef,
)


class EcucChoiceContainerDef(EcucContainerDef):
    """AUTOSAR EcucChoiceContainerDef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "choices": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=EcucParamConfContainerDef,
        ),  # choices
    }

    def __init__(self) -> None:
        """Initialize EcucChoiceContainerDef."""
        super().__init__()
        self.choices: list[EcucParamConfContainerDef] = []


class EcucChoiceContainerDefBuilder:
    """Builder for EcucChoiceContainerDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucChoiceContainerDef = EcucChoiceContainerDef()

    def build(self) -> EcucChoiceContainerDef:
        """Build and return EcucChoiceContainerDef object.

        Returns:
            EcucChoiceContainerDef instance
        """
        # TODO: Add validation
        return self._obj
