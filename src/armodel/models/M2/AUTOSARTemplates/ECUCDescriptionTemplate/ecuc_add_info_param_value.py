"""EcucAddInfoParamValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 129)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_parameter_value import (
    EcucParameterValue,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)


class EcucAddInfoParamValue(EcucParameterValue):
    """AUTOSAR EcucAddInfoParamValue."""

    value: Optional[DocumentationBlock]
    def __init__(self) -> None:
        """Initialize EcucAddInfoParamValue."""
        super().__init__()
        self.value: Optional[DocumentationBlock] = None


class EcucAddInfoParamValueBuilder:
    """Builder for EcucAddInfoParamValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucAddInfoParamValue = EcucAddInfoParamValue()

    def build(self) -> EcucAddInfoParamValue:
        """Build and return EcucAddInfoParamValue object.

        Returns:
            EcucAddInfoParamValue instance
        """
        # TODO: Add validation
        return self._obj
