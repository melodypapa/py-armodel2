"""ComManagementMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 282)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_group import (
    PortGroup,
)


class ComManagementMapping(Identifiable):
    """AUTOSAR ComManagementMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    com_refs: list[ARRef]
    physical_channels: list[PhysicalChannel]
    def __init__(self) -> None:
        """Initialize ComManagementMapping."""
        super().__init__()
        self.com_refs: list[ARRef] = []
        self.physical_channels: list[PhysicalChannel] = []


class ComManagementMappingBuilder:
    """Builder for ComManagementMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ComManagementMapping = ComManagementMapping()

    def build(self) -> ComManagementMapping:
        """Build and return ComManagementMapping object.

        Returns:
            ComManagementMapping instance
        """
        # TODO: Add validation
        return self._obj
