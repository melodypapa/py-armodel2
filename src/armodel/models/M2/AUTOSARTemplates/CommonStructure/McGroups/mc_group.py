"""McGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 190)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2034)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_McGroups.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_function import (
    McFunction,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.McGroups.mc_group_data_ref_set import (
    McGroupDataRefSet,
)


class McGroup(ARElement):
    """AUTOSAR McGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mc_functions: list[McFunction]
    ref_calprm_set_ref: Optional[ARRef]
    ref_ref: Optional[ARRef]
    sub_group_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize McGroup."""
        super().__init__()
        self.mc_functions: list[McFunction] = []
        self.ref_calprm_set_ref: Optional[ARRef] = None
        self.ref_ref: Optional[ARRef] = None
        self.sub_group_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "McGroup":
        """Deserialize XML element to McGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized McGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(McGroup, cls).deserialize(element)

        # Parse mc_functions (list from container "MC-FUNCTIONS")
        obj.mc_functions = []
        container = ARObject._find_child_element(element, "MC-FUNCTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mc_functions.append(child_value)

        # Parse ref_calprm_set_ref
        child = ARObject._find_child_element(element, "REF-CALPRM-SET")
        if child is not None:
            ref_calprm_set_ref_value = ARObject._deserialize_by_tag(child, "McGroupDataRefSet")
            obj.ref_calprm_set_ref = ref_calprm_set_ref_value

        # Parse ref_ref
        child = ARObject._find_child_element(element, "REF")
        if child is not None:
            ref_ref_value = ARObject._deserialize_by_tag(child, "McGroupDataRefSet")
            obj.ref_ref = ref_ref_value

        # Parse sub_group_refs (list from container "SUB-GROUPS")
        obj.sub_group_refs = []
        container = ARObject._find_child_element(element, "SUB-GROUPS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sub_group_refs.append(child_value)

        return obj



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
