"""ContainedIPduProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 355)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    PduCollectionTriggerEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class ContainedIPduProps(ARObject):
    """AUTOSAR ContainedIPduProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "collection": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (ContainedIPdu),
        ),  # collection
        "contained_pdu": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PduTriggering,
        ),  # containedPdu
        "header_id_long": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # headerIdLong
        "header_id_short": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # headerIdShort
        "offset": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # offset
        "priority": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # priority
        "timeout": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timeout
        "trigger": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PduCollectionTriggerEnum,
        ),  # trigger
        "update": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # update
    }

    def __init__(self) -> None:
        """Initialize ContainedIPduProps."""
        super().__init__()
        self.collection: Optional[Any] = None
        self.contained_pdu: Optional[PduTriggering] = None
        self.header_id_long: Optional[PositiveInteger] = None
        self.header_id_short: Optional[PositiveInteger] = None
        self.offset: Optional[PositiveInteger] = None
        self.priority: Optional[PositiveInteger] = None
        self.timeout: Optional[TimeValue] = None
        self.trigger: Optional[PduCollectionTriggerEnum] = None
        self.update: Optional[PositiveInteger] = None


class ContainedIPduPropsBuilder:
    """Builder for ContainedIPduProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ContainedIPduProps = ContainedIPduProps()

    def build(self) -> ContainedIPduProps:
        """Build and return ContainedIPduProps object.

        Returns:
            ContainedIPduProps instance
        """
        # TODO: Add validation
        return self._obj
