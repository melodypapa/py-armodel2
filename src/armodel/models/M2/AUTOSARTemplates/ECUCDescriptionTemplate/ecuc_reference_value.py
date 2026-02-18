"""EcucReferenceValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 132)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 443)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_abstract_reference_value import (
    EcucAbstractReferenceValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)


class EcucReferenceValue(EcucAbstractReferenceValue):
    """AUTOSAR EcucReferenceValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    value_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize EcucReferenceValue."""
        super().__init__()
        self.value_ref: Optional[ARRef] = None


class EcucReferenceValueBuilder:
    """Builder for EcucReferenceValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucReferenceValue = EcucReferenceValue()

    def build(self) -> EcucReferenceValue:
        """Build and return EcucReferenceValue object.

        Returns:
            EcucReferenceValue instance
        """
        # TODO: Add validation
        return self._obj
