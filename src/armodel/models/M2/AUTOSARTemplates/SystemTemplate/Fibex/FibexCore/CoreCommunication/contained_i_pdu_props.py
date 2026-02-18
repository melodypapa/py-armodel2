"""ContainedIPduProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 355)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    collection: Optional[Any]
    contained_pdu_ref: Optional[ARRef]
    header_id_long: Optional[PositiveInteger]
    header_id_short: Optional[PositiveInteger]
    offset: Optional[PositiveInteger]
    priority: Optional[PositiveInteger]
    timeout: Optional[TimeValue]
    trigger_ref: Optional[ARRef]
    update: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize ContainedIPduProps."""
        super().__init__()
        self.collection: Optional[Any] = None
        self.contained_pdu_ref: Optional[ARRef] = None
        self.header_id_long: Optional[PositiveInteger] = None
        self.header_id_short: Optional[PositiveInteger] = None
        self.offset: Optional[PositiveInteger] = None
        self.priority: Optional[PositiveInteger] = None
        self.timeout: Optional[TimeValue] = None
        self.trigger_ref: Optional[ARRef] = None
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
