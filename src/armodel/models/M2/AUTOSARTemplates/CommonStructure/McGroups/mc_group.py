"""McGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_function import (
    McFunction,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.McGroups.mc_group import (
    McGroup,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.McGroups.mc_group_data_ref_set import (
    McGroupDataRefSet,
)


class McGroup(ARElement):
    """AUTOSAR McGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("mc_functions", None, False, True, McFunction),  # mcFunctions
        ("ref_calprm_set", None, False, False, McGroupDataRefSet),  # refCalprmSet
        ("ref", None, False, False, McGroupDataRefSet),  # ref
        ("sub_groups", None, False, True, McGroup),  # subGroups
    ]

    def __init__(self) -> None:
        """Initialize McGroup."""
        super().__init__()
        self.mc_functions: list[McFunction] = []
        self.ref_calprm_set: Optional[McGroupDataRefSet] = None
        self.ref: Optional[McGroupDataRefSet] = None
        self.sub_groups: list[McGroup] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert McGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "McGroup":
        """Create McGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            McGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to McGroup since parent returns ARObject
        return cast("McGroup", obj)


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
