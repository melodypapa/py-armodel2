"""AppOsTaskProxyToEcuTaskProxyMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 209)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_RteEventToOsTaskMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
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


class AppOsTaskProxyToEcuTaskProxyMapping(Identifiable):
    """AUTOSAR AppOsTaskProxyToEcuTaskProxyMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "app_task_proxy": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=OsTaskProxy,
        ),  # appTaskProxy
        "ecu_task_proxy": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=OsTaskProxy,
        ),  # ecuTaskProxy
        "offset": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # offset
    }

    def __init__(self) -> None:
        """Initialize AppOsTaskProxyToEcuTaskProxyMapping."""
        super().__init__()
        self.app_task_proxy: Optional[OsTaskProxy] = None
        self.ecu_task_proxy: Optional[OsTaskProxy] = None
        self.offset: Optional[Integer] = None


class AppOsTaskProxyToEcuTaskProxyMappingBuilder:
    """Builder for AppOsTaskProxyToEcuTaskProxyMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AppOsTaskProxyToEcuTaskProxyMapping = AppOsTaskProxyToEcuTaskProxyMapping()

    def build(self) -> AppOsTaskProxyToEcuTaskProxyMapping:
        """Build and return AppOsTaskProxyToEcuTaskProxyMapping object.

        Returns:
            AppOsTaskProxyToEcuTaskProxyMapping instance
        """
        # TODO: Add validation
        return self._obj
