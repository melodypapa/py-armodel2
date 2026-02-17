"""Sdf AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 92)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_SpecialData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    Numerical,
)


class Sdf(ARObject):
    """AUTOSAR Sdf."""

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
            multiplicity="0..1",
        ),  # value
    }

    def __init__(self) -> None:
        """Initialize Sdf."""
        super().__init__()
        self.gid: NameToken = None
        self.value: Optional[Numerical] = None


class SdfBuilder:
    """Builder for Sdf."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Sdf = Sdf()

    def build(self) -> Sdf:
        """Build and return Sdf object.

        Returns:
            Sdf instance
        """
        # TODO: Add validation
        return self._obj
