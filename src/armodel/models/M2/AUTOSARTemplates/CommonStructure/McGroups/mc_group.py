"""McGroup AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_function import (
    McFunction,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.McGroups.mc_group_data_ref_set import (
    McGroupDataRefSet,
)


class McGroup(ARElement):
    """AUTOSAR McGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "mc_functions": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=McFunction,
        ),  # mcFunctions
        "ref_calprm_set": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=McGroupDataRefSet,
        ),  # refCalprmSet
        "ref": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=McGroupDataRefSet,
        ),  # ref
        "sub_groups": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=McGroup,
        ),  # subGroups
    }

    def __init__(self) -> None:
        """Initialize McGroup."""
        super().__init__()
        self.mc_functions: list[McFunction] = []
        self.ref_calprm_set: Optional[McGroupDataRefSet] = None
        self.ref: Optional[McGroupDataRefSet] = None
        self.sub_groups: list[McGroup] = []


class McGroupBuilder:
    """Builder for McGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: McGroup = McGroup()

    def build(self) -> McGroup:
        """Build and return McGroup object.

        Returns:
            McGroup instance
        """
        # TODO: Add validation
        return self._obj
