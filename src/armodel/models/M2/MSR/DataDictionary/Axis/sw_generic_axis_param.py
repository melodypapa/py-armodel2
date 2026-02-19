"""SwGenericAxisParam AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 356)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_Axis.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class SwGenericAxisParam(ARObject):
    """AUTOSAR SwGenericAxisParam."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sw_generic_axis_param: Optional[SwGenericAxisParam]
    def __init__(self) -> None:
        """Initialize SwGenericAxisParam."""
        super().__init__()
        self.sw_generic_axis_param: Optional[SwGenericAxisParam] = None
    def serialize(self) -> ET.Element:
        """Serialize SwGenericAxisParam to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize sw_generic_axis_param
        if self.sw_generic_axis_param is not None:
            serialized = ARObject._serialize_item(self.sw_generic_axis_param, "SwGenericAxisParam")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-GENERIC-AXIS-PARAM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwGenericAxisParam":
        """Deserialize XML element to SwGenericAxisParam object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwGenericAxisParam object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse sw_generic_axis_param
        child = ARObject._find_child_element(element, "SW-GENERIC-AXIS-PARAM")
        if child is not None:
            sw_generic_axis_param_value = ARObject._deserialize_by_tag(child, "SwGenericAxisParam")
            obj.sw_generic_axis_param = sw_generic_axis_param_value

        return obj



class SwGenericAxisParamBuilder:
    """Builder for SwGenericAxisParam."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwGenericAxisParam = SwGenericAxisParam()

    def build(self) -> SwGenericAxisParam:
        """Build and return SwGenericAxisParam object.

        Returns:
            SwGenericAxisParam instance
        """
        # TODO: Add validation
        return self._obj
