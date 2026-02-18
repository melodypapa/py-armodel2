"""BswVariableAccess AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 81)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_distinguished_partition import (
    BswDistinguishedPartition,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class BswVariableAccess(Referrable):
    """AUTOSAR BswVariableAccess."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    accessed_variable: Optional[VariableDataPrototype]
    contexts: list[BswDistinguishedPartition]
    def __init__(self) -> None:
        """Initialize BswVariableAccess."""
        super().__init__()
        self.accessed_variable: Optional[VariableDataPrototype] = None
        self.contexts: list[BswDistinguishedPartition] = []


class BswVariableAccessBuilder:
    """Builder for BswVariableAccess."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswVariableAccess = BswVariableAccess()

    def build(self) -> BswVariableAccess:
        """Build and return BswVariableAccess object.

        Returns:
            BswVariableAccess instance
        """
        # TODO: Add validation
        return self._obj
