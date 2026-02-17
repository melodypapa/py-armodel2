"""BswVariableAccess AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 81)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "accessed_variable": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=VariableDataPrototype,
        ),  # accessedVariable
        "contexts": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BswDistinguishedPartition,
        ),  # contexts
    }

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
