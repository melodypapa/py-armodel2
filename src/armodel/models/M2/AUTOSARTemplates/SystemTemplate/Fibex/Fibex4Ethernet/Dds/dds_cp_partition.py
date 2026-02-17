"""DdsCpPartition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 527)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class DdsCpPartition(Identifiable):
    """AUTOSAR DdsCpPartition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "partition_name": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # partitionName
    }

    def __init__(self) -> None:
        """Initialize DdsCpPartition."""
        super().__init__()
        self.partition_name: Optional[String] = None


class DdsCpPartitionBuilder:
    """Builder for DdsCpPartition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsCpPartition = DdsCpPartition()

    def build(self) -> DdsCpPartition:
        """Build and return DdsCpPartition object.

        Returns:
            DdsCpPartition instance
        """
        # TODO: Add validation
        return self._obj
