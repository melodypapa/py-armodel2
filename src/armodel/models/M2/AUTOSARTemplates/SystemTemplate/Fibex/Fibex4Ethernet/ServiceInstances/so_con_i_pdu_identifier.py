"""SoConIPduIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 489)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class SoConIPduIdentifier(Referrable):
    """AUTOSAR SoConIPduIdentifier."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "header_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # headerId
        "pdu_collection": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (PduCollection),
        ),  # pduCollection
        "pdu_collection_trigger": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PduCollectionTriggerEnum,
        ),  # pduCollectionTrigger
        "pdu_triggering": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PduTriggering,
        ),  # pduTriggering
    }

    def __init__(self) -> None:
        """Initialize SoConIPduIdentifier."""
        super().__init__()
        self.header_id: Optional[PositiveInteger] = None
        self.pdu_collection: Optional[Any] = None
        self.pdu_collection_trigger: Optional[PduCollectionTriggerEnum] = None
        self.pdu_triggering: Optional[PduTriggering] = None


class SoConIPduIdentifierBuilder:
    """Builder for SoConIPduIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SoConIPduIdentifier = SoConIPduIdentifier()

    def build(self) -> SoConIPduIdentifier:
        """Build and return SoConIPduIdentifier object.

        Returns:
            SoConIPduIdentifier instance
        """
        # TODO: Add validation
        return self._obj
