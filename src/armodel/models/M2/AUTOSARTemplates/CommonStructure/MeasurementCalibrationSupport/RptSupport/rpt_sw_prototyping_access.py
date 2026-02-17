"""RptSwPrototypingAccess AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 199)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 856)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport_RptSupport.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class RptSwPrototypingAccess(ARObject):
    """AUTOSAR RptSwPrototypingAccess."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "rpt_hook_access": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RptAccessEnum,
        ),  # rptHookAccess
        "rpt_read_access": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RptAccessEnum,
        ),  # rptReadAccess
        "rpt_write_access": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RptAccessEnum,
        ),  # rptWriteAccess
    }

    def __init__(self) -> None:
        """Initialize RptSwPrototypingAccess."""
        super().__init__()
        self.rpt_hook_access: Optional[RptAccessEnum] = None
        self.rpt_read_access: Optional[RptAccessEnum] = None
        self.rpt_write_access: Optional[RptAccessEnum] = None


class RptSwPrototypingAccessBuilder:
    """Builder for RptSwPrototypingAccess."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RptSwPrototypingAccess = RptSwPrototypingAccess()

    def build(self) -> RptSwPrototypingAccess:
        """Build and return RptSwPrototypingAccess object.

        Returns:
            RptSwPrototypingAccess instance
        """
        # TODO: Add validation
        return self._obj
