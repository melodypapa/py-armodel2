"""SwAxisType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 355)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_Axis.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.MSR.DataDictionary.Axis.sw_generic_axis_param import (
    SwGenericAxisParam,
)


class SwAxisType(ARElement):
    """AUTOSAR SwAxisType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sw_generic_axis: Optional[DocumentationBlock]
    sw_generic_axis_params: list[SwGenericAxisParam]
    def __init__(self) -> None:
        """Initialize SwAxisType."""
        super().__init__()
        self.sw_generic_axis: Optional[DocumentationBlock] = None
        self.sw_generic_axis_params: list[SwGenericAxisParam] = []
    def serialize(self) -> ET.Element:
        """Serialize SwAxisType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwAxisType, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sw_generic_axis
        if self.sw_generic_axis is not None:
            serialized = ARObject._serialize_item(self.sw_generic_axis, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-GENERIC-AXIS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_generic_axis_params (list to container "SW-GENERIC-AXIS-PARAMS")
        if self.sw_generic_axis_params:
            wrapper = ET.Element("SW-GENERIC-AXIS-PARAMS")
            for item in self.sw_generic_axis_params:
                serialized = ARObject._serialize_item(item, "SwGenericAxisParam")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwAxisType":
        """Deserialize XML element to SwAxisType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwAxisType object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwAxisType, cls).deserialize(element)

        # Parse sw_generic_axis
        child = ARObject._find_child_element(element, "SW-GENERIC-AXIS")
        if child is not None:
            sw_generic_axis_value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.sw_generic_axis = sw_generic_axis_value

        # Parse sw_generic_axis_params (list from container "SW-GENERIC-AXIS-PARAMS")
        obj.sw_generic_axis_params = []
        container = ARObject._find_child_element(element, "SW-GENERIC-AXIS-PARAMS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_generic_axis_params.append(child_value)

        return obj



class SwAxisTypeBuilder:
    """Builder for SwAxisType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwAxisType = SwAxisType()

    def build(self) -> SwAxisType:
        """Build and return SwAxisType object.

        Returns:
            SwAxisType instance
        """
        # TODO: Add validation
        return self._obj
