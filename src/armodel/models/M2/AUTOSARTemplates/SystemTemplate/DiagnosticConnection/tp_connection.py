"""TpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 633)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DiagnosticConnection.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection_ident import (
    TpConnectionIdent,
)


class TpConnection(ARObject):
    """AUTOSAR TpConnection."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ident": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TpConnectionIdent,
        ),  # ident
    }

    def __init__(self) -> None:
        """Initialize TpConnection."""
        super().__init__()
        self.ident: Optional[TpConnectionIdent] = None


class TpConnectionBuilder:
    """Builder for TpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TpConnection = TpConnection()

    def build(self) -> TpConnection:
        """Build and return TpConnection object.

        Returns:
            TpConnection instance
        """
        # TODO: Add validation
        return self._obj
