"""SwAxisGeneric AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 355)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_Axis.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.DataDictionary.Axis.sw_axis_type import (
    SwAxisType,
)
from armodel.models.M2.MSR.DataDictionary.Axis.sw_generic_axis_param import (
    SwGenericAxisParam,
)


class SwAxisGeneric(ARObject):
    """AUTOSAR SwAxisGeneric."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sw_axis_type_ref: Optional[ARRef]
    sw_generic_axis_params: list[SwGenericAxisParam]
    def __init__(self) -> None:
        """Initialize SwAxisGeneric."""
        super().__init__()
        self.sw_axis_type_ref: Optional[ARRef] = None
        self.sw_generic_axis_params: list[SwGenericAxisParam] = []

    def serialize(self) -> ET.Element:
        """Serialize SwAxisGeneric to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize sw_axis_type_ref
        if self.sw_axis_type_ref is not None:
            serialized = ARObject._serialize_item(self.sw_axis_type_ref, "SwAxisType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-AXIS-TYPE-REF")
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
    def deserialize(cls, element: ET.Element) -> "SwAxisGeneric":
        """Deserialize XML element to SwAxisGeneric object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwAxisGeneric object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse sw_axis_type_ref
        child = ARObject._find_child_element(element, "SW-AXIS-TYPE-REF")
        if child is not None:
            sw_axis_type_ref_value = ARRef.deserialize(child)
            obj.sw_axis_type_ref = sw_axis_type_ref_value

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



class SwAxisGenericBuilder:
    """Builder for SwAxisGeneric."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwAxisGeneric = SwAxisGeneric()

    def build(self) -> SwAxisGeneric:
        """Build and return SwAxisGeneric object.

        Returns:
            SwAxisGeneric instance
        """
        # TODO: Add validation
        return self._obj
