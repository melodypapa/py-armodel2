"""SoConIPduIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 489)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    PduCollectionTriggerEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class SoConIPduIdentifier(Referrable):
    """AUTOSAR SoConIPduIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    header_id: Optional[PositiveInteger]
    pdu_collection_ref: Optional[ARRef]
    pdu_collection_trigger_ref: Optional[ARRef]
    pdu_triggering_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SoConIPduIdentifier."""
        super().__init__()
        self.header_id: Optional[PositiveInteger] = None
        self.pdu_collection_ref: Optional[ARRef] = None
        self.pdu_collection_trigger_ref: Optional[ARRef] = None
        self.pdu_triggering_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SoConIPduIdentifier":
        """Deserialize XML element to SoConIPduIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SoConIPduIdentifier object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SoConIPduIdentifier, cls).deserialize(element)

        # Parse header_id
        child = ARObject._find_child_element(element, "HEADER-ID")
        if child is not None:
            header_id_value = child.text
            obj.header_id = header_id_value

        # Parse pdu_collection_ref
        child = ARObject._find_child_element(element, "PDU-COLLECTION")
        if child is not None:
            pdu_collection_ref_value = child.text
            obj.pdu_collection_ref = pdu_collection_ref_value

        # Parse pdu_collection_trigger_ref
        child = ARObject._find_child_element(element, "PDU-COLLECTION-TRIGGER")
        if child is not None:
            pdu_collection_trigger_ref_value = PduCollectionTriggerEnum.deserialize(child)
            obj.pdu_collection_trigger_ref = pdu_collection_trigger_ref_value

        # Parse pdu_triggering_ref
        child = ARObject._find_child_element(element, "PDU-TRIGGERING")
        if child is not None:
            pdu_triggering_ref_value = ARObject._deserialize_by_tag(child, "PduTriggering")
            obj.pdu_triggering_ref = pdu_triggering_ref_value

        return obj



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
