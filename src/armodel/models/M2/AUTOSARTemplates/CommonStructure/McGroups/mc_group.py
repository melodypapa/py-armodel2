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
    def serialize(self) -> ET.Element:
        """Serialize McGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(McGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mc_functions (list to container "MC-FUNCTIONS")
        if self.mc_functions:
            wrapper = ET.Element("MC-FUNCTIONS")
            for item in self.mc_functions:
                serialized = ARObject._serialize_item(item, "McFunction")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ref_calprm_set_ref
        if self.ref_calprm_set_ref is not None:
            serialized = ARObject._serialize_item(self.ref_calprm_set_ref, "McGroupDataRefSet")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REF-CALPRM-SET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ref_ref
        if self.ref_ref is not None:
            serialized = ARObject._serialize_item(self.ref_ref, "McGroupDataRefSet")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sub_group_refs (list to container "SUB-GROUPS")
        if self.sub_group_refs:
            wrapper = ET.Element("SUB-GROUPS")
            for item in self.sub_group_refs:
                serialized = ARObject._serialize_item(item, "McGroup")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

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
