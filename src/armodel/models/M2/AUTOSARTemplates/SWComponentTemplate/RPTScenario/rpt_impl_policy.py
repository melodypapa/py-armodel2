"""RptImplPolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 202)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 854)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_RPTScenario.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class RptImplPolicy(ARObject):
    """AUTOSAR RptImplPolicy."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "rpt_enabler_impl": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RptEnablerImplTypeEnum,
        ),  # rptEnablerImpl
        "rpt_preparation_enum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RptPreparationEnum,
        ),  # rptPreparationEnum
    }

    def __init__(self) -> None:
        """Initialize RptImplPolicy."""
        super().__init__()
        self.rpt_enabler_impl: Optional[RptEnablerImplTypeEnum] = None
        self.rpt_preparation_enum: Optional[RptPreparationEnum] = None


class RptImplPolicyBuilder:
    """Builder for RptImplPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RptImplPolicy = RptImplPolicy()

    def build(self) -> RptImplPolicy:
        """Build and return RptImplPolicy object.

        Returns:
            RptImplPolicy instance
        """
        # TODO: Add validation
        return self._obj
