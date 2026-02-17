"""FramePid AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 437)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    PositiveInteger,
)


class FramePid(ARObject):
    """AUTOSAR FramePid."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "index": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # index
        "pid": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # pid
    }

    def __init__(self) -> None:
        """Initialize FramePid."""
        super().__init__()
        self.index: Optional[Integer] = None
        self.pid: Optional[PositiveInteger] = None


class FramePidBuilder:
    """Builder for FramePid."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FramePid = FramePid()

    def build(self) -> FramePid:
        """Build and return FramePid object.

        Returns:
            FramePid instance
        """
        # TODO: Add validation
        return self._obj
