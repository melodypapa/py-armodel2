"""VariableAccess AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_variable_ref import (
    AutosarVariableRef,
)


class VariableAccess(AbstractAccessPoint):
    """AUTOSAR VariableAccess."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "accessed_variable": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AutosarVariableRef,
        ),  # accessedVariable
        "scope": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=VariableAccessScopeEnum,
        ),  # scope
    }

    def __init__(self) -> None:
        """Initialize VariableAccess."""
        super().__init__()
        self.accessed_variable: Optional[AutosarVariableRef] = None
        self.scope: Optional[VariableAccessScopeEnum] = None


class VariableAccessBuilder:
    """Builder for VariableAccess."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VariableAccess = VariableAccess()

    def build(self) -> VariableAccess:
        """Build and return VariableAccess object.

        Returns:
            VariableAccess instance
        """
        # TODO: Add validation
        return self._obj
