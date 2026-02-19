"""RptHook AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 848)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_RPTScenario.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    code_label: Optional[CIdentifier]
    mcd_identifier: Optional[NameToken]
    rpt_ar_hook: Optional[AtpFeature]
    sdgs: list[Sdg]
    def __init__(self) -> None:
        """Initialize RptHook."""
        super().__init__()
        self.code_label: Optional[CIdentifier] = None
        self.mcd_identifier: Optional[NameToken] = None
        self.rpt_ar_hook: Optional[AtpFeature] = None
        self.sdgs: list[Sdg] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptHook":
        """Deserialize XML element to RptHook object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RptHook object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse code_label
        child = ARObject._find_child_element(element, "CODE-LABEL")
        if child is not None:
            code_label_value = child.text
            obj.code_label = code_label_value

        # Parse mcd_identifier
        child = ARObject._find_child_element(element, "MCD-IDENTIFIER")
        if child is not None:
            mcd_identifier_value = child.text
            obj.mcd_identifier = mcd_identifier_value

        # Parse rpt_ar_hook
        child = ARObject._find_child_element(element, "RPT-AR-HOOK")
        if child is not None:
            rpt_ar_hook_value = ARObject._deserialize_by_tag(child, "AtpFeature")
            obj.rpt_ar_hook = rpt_ar_hook_value

        # Parse sdgs (list)
        obj.sdgs = []
        for child in ARObject._find_all_child_elements(element, "SDGS"):
            sdgs_value = ARObject._deserialize_by_tag(child, "Sdg")
            obj.sdgs.append(sdgs_value)

        return obj



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
