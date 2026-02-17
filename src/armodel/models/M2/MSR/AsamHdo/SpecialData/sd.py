"""Sd AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 91)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_SpecialData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    VerbatimStringPlain,
)


class Sd(ARObject):
    """AUTOSAR Sd."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "gid": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # gid
        "value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # value
        "xml_space": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (XmlSpaceEnum),
        ),  # xmlSpace
    }

    def __init__(self) -> None:
        """Initialize Sd."""
        super().__init__()
        self.gid: NameToken = None
        self.value: VerbatimStringPlain = None
        self.xml_space: Optional[Any] = None


class SdBuilder:
    """Builder for Sd."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Sd = Sd()

    def build(self) -> Sd:
        """Build and return Sd object.

        Returns:
            Sd instance
        """
        # TODO: Add validation
        return self._obj
