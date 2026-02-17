"""ISignalIPduGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 316)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 350)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_i_pdu import (
    ISignalIPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.nm_pdu import (
    NmPdu,
)


class ISignalIPduGroup(FibexElement):
    """AUTOSAR ISignalIPduGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "communication": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # communication
        "containeds": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ISignalIPduGroup,
        ),  # containeds
        "i_signal_i_pdus": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ISignalIPdu,
        ),  # iSignalIPdus
        "nm_pdus": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=NmPdu,
        ),  # nmPdus
    }

    def __init__(self) -> None:
        """Initialize ISignalIPduGroup."""
        super().__init__()
        self.communication: Optional[String] = None
        self.containeds: list[ISignalIPduGroup] = []
        self.i_signal_i_pdus: list[ISignalIPdu] = []
        self.nm_pdus: list[NmPdu] = []


class ISignalIPduGroupBuilder:
    """Builder for ISignalIPduGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ISignalIPduGroup = ISignalIPduGroup()

    def build(self) -> ISignalIPduGroup:
        """Build and return ISignalIPduGroup object.

        Returns:
            ISignalIPduGroup instance
        """
        # TODO: Add validation
        return self._obj
