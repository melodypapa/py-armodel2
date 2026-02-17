"""SdgContents AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 90)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_SpecialData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData.sd import (
    Sd,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData.sdf import (
    Sdf,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData.sdg import (
    Sdg,
)


class SdgContents(ARObject):
    """AUTOSAR SdgContents."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "sd": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Sd,
        ),  # sd
        "sdf": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Sdf,
        ),  # sdf
        "sdg": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Sdg,
        ),  # sdg
        "sdx": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Referrable,
        ),  # sdx
        "sdxf": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Referrable,
        ),  # sdxf
    }

    def __init__(self) -> None:
        """Initialize SdgContents."""
        super().__init__()
        self.sd: Optional[Sd] = None
        self.sdf: Optional[Sdf] = None
        self.sdg: Optional[Sdg] = None
        self.sdx: Optional[Referrable] = None
        self.sdxf: Optional[Referrable] = None


class SdgContentsBuilder:
    """Builder for SdgContents."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgContents = SdgContents()

    def build(self) -> SdgContents:
        """Build and return SdgContents object.

        Returns:
            SdgContents instance
        """
        # TODO: Add validation
        return self._obj
