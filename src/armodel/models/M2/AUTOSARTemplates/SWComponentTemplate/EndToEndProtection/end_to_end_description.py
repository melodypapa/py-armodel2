"""EndToEndDescription AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 205)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 385)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_EndToEndProtection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    PositiveInteger,
)


class EndToEndDescription(ARObject):
    """AUTOSAR EndToEndDescription."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "category": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # category
        "counter_offset": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # counterOffset
        "crc_offset": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # crcOffset
        "data_id_mode": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # dataIdMode
        "data_id_nibble": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # dataIdNibble
        "data_length": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # dataLength
        "max_delta": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxDelta
    }

    def __init__(self) -> None:
        """Initialize EndToEndDescription."""
        super().__init__()
        self.category: Optional[NameToken] = None
        self.counter_offset: Optional[PositiveInteger] = None
        self.crc_offset: Optional[PositiveInteger] = None
        self.data_id_mode: Optional[PositiveInteger] = None
        self.data_id_nibble: Optional[PositiveInteger] = None
        self.data_length: Optional[PositiveInteger] = None
        self.max_delta: Optional[PositiveInteger] = None


class EndToEndDescriptionBuilder:
    """Builder for EndToEndDescription."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EndToEndDescription = EndToEndDescription()

    def build(self) -> EndToEndDescription:
        """Build and return EndToEndDescription object.

        Returns:
            EndToEndDescription instance
        """
        # TODO: Add validation
        return self._obj
