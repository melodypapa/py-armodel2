"""RptHook AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 848)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_RPTScenario.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
    NameToken,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData.sdg import (
    Sdg,
)


class RptHook(ARObject):
    """AUTOSAR RptHook."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "code_label": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # codeLabel
        "mcd_identifier": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # mcdIdentifier
        "rpt_ar_hook": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AtpFeature,
        ),  # rptArHook
        "sdgs": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Sdg,
        ),  # sdgs
    }

    def __init__(self) -> None:
        """Initialize RptHook."""
        super().__init__()
        self.code_label: Optional[CIdentifier] = None
        self.mcd_identifier: Optional[NameToken] = None
        self.rpt_ar_hook: Optional[AtpFeature] = None
        self.sdgs: list[Sdg] = []


class RptHookBuilder:
    """Builder for RptHook."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RptHook = RptHook()

    def build(self) -> RptHook:
        """Build and return RptHook object.

        Returns:
            RptHook instance
        """
        # TODO: Add validation
        return self._obj
