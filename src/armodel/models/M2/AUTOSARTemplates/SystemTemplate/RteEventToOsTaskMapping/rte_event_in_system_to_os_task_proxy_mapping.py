"""RteEventInSystemToOsTaskProxyMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 213)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_RteEventToOsTaskMapping.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping.os_task_proxy import (
    OsTaskProxy,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)


class RteEventInSystemToOsTaskProxyMapping(Identifiable):
    """AUTOSAR RteEventInSystemToOsTaskProxyMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "offset": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # offset
        "os_task_proxy": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=OsTaskProxy,
        ),  # osTaskProxy
        "rte_event_instance_ref": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RTEEvent,
        ),  # rteEventInstanceRef
    }

    def __init__(self) -> None:
        """Initialize RteEventInSystemToOsTaskProxyMapping."""
        super().__init__()
        self.offset: Optional[Integer] = None
        self.os_task_proxy: Optional[OsTaskProxy] = None
        self.rte_event_instance_ref: Optional[RTEEvent] = None


class RteEventInSystemToOsTaskProxyMappingBuilder:
    """Builder for RteEventInSystemToOsTaskProxyMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RteEventInSystemToOsTaskProxyMapping = RteEventInSystemToOsTaskProxyMapping()

    def build(self) -> RteEventInSystemToOsTaskProxyMapping:
        """Build and return RteEventInSystemToOsTaskProxyMapping object.

        Returns:
            RteEventInSystemToOsTaskProxyMapping instance
        """
        # TODO: Add validation
        return self._obj
