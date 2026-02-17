"""DiagnosticComControlSubNodeChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 110)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_CommunicationControl.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class DiagnosticComControlSubNodeChannel(ARObject):
    """AUTOSAR DiagnosticComControlSubNodeChannel."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "sub_node": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (EthernetPhysical),
        ),  # subNode
    }

    def __init__(self) -> None:
        """Initialize DiagnosticComControlSubNodeChannel."""
        super().__init__()
        self.sub_node: Optional[Any] = None


class DiagnosticComControlSubNodeChannelBuilder:
    """Builder for DiagnosticComControlSubNodeChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticComControlSubNodeChannel = DiagnosticComControlSubNodeChannel()

    def build(self) -> DiagnosticComControlSubNodeChannel:
        """Build and return DiagnosticComControlSubNodeChannel object.

        Returns:
            DiagnosticComControlSubNodeChannel instance
        """
        # TODO: Add validation
        return self._obj
