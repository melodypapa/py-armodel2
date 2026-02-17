"""EcucInstanceReferenceValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 134)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_abstract_reference_value import (
    EcucAbstractReferenceValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)


class EcucInstanceReferenceValue(EcucAbstractReferenceValue):
    """AUTOSAR EcucInstanceReferenceValue."""

    def __init__(self) -> None:
        """Initialize EcucInstanceReferenceValue."""
        super().__init__()
        self.value: Optional[AtpFeature] = None


class EcucInstanceReferenceValueBuilder:
    """Builder for EcucInstanceReferenceValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucInstanceReferenceValue = EcucInstanceReferenceValue()

    def build(self) -> EcucInstanceReferenceValue:
        """Build and return EcucInstanceReferenceValue object.

        Returns:
            EcucInstanceReferenceValue instance
        """
        # TODO: Add validation
        return self._obj
