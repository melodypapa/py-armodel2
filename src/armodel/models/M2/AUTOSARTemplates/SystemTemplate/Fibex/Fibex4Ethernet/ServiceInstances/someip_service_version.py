"""SomeipServiceVersion AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2059)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SomeipServiceVersion(ARObject):
    """AUTOSAR SomeipServiceVersion."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "major_version": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # majorVersion
        "minor_version": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # minorVersion
    }

    def __init__(self) -> None:
        """Initialize SomeipServiceVersion."""
        super().__init__()
        self.major_version: Optional[PositiveInteger] = None
        self.minor_version: Optional[PositiveInteger] = None


class SomeipServiceVersionBuilder:
    """Builder for SomeipServiceVersion."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SomeipServiceVersion = SomeipServiceVersion()

    def build(self) -> SomeipServiceVersion:
        """Build and return SomeipServiceVersion object.

        Returns:
            SomeipServiceVersion instance
        """
        # TODO: Add validation
        return self._obj
