"""SwAxisGrouped AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 357)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_Axis.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.DataDictionary.CalibrationParameter.sw_calprm_axis_type_props import (
    SwCalprmAxisTypeProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.DataDictionary.RecordLayout import (
    AxisIndexType,
)
from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies.sw_calprm_ref_proxy import (
    SwCalprmRefProxy,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_primitive_data_type import (
        ApplicationPrimitiveDataType,
    )



class SwAxisGrouped(SwCalprmAxisTypeProps):
    """AUTOSAR SwAxisGrouped."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    shared_axis_type_ref: Optional[ARRef]
    sw_axis_index: Optional[AxisIndexType]
    sw_calprm_ref_proxy_ref: ARRef
    def __init__(self) -> None:
        """Initialize SwAxisGrouped."""
        super().__init__()
        self.shared_axis_type_ref: Optional[ARRef] = None
        self.sw_axis_index: Optional[AxisIndexType] = None
        self.sw_calprm_ref_proxy_ref: ARRef = None

    def serialize(self) -> ET.Element:
        """Serialize SwAxisGrouped to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwAxisGrouped, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize shared_axis_type_ref
        if self.shared_axis_type_ref is not None:
            serialized = ARObject._serialize_item(self.shared_axis_type_ref, "ApplicationPrimitiveDataType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHARED-AXIS-TYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_axis_index
        if self.sw_axis_index is not None:
            serialized = ARObject._serialize_item(self.sw_axis_index, "AxisIndexType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-AXIS-INDEX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_calprm_ref_proxy_ref
        if self.sw_calprm_ref_proxy_ref is not None:
            serialized = ARObject._serialize_item(self.sw_calprm_ref_proxy_ref, "SwCalprmRefProxy")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-CALPRM-REF-PROXY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwAxisGrouped":
        """Deserialize XML element to SwAxisGrouped object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwAxisGrouped object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwAxisGrouped, cls).deserialize(element)

        # Parse shared_axis_type_ref
        child = ARObject._find_child_element(element, "SHARED-AXIS-TYPE-REF")
        if child is not None:
            shared_axis_type_ref_value = ARRef.deserialize(child)
            obj.shared_axis_type_ref = shared_axis_type_ref_value

        # Parse sw_axis_index
        child = ARObject._find_child_element(element, "SW-AXIS-INDEX")
        if child is not None:
            sw_axis_index_value = child.text
            obj.sw_axis_index = sw_axis_index_value

        # Parse sw_calprm_ref_proxy_ref
        child = ARObject._find_child_element(element, "SW-CALPRM-REF-PROXY-REF")
        if child is not None:
            sw_calprm_ref_proxy_ref_value = ARRef.deserialize(child)
            obj.sw_calprm_ref_proxy_ref = sw_calprm_ref_proxy_ref_value

        return obj



class SwAxisGroupedBuilder:
    """Builder for SwAxisGrouped."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwAxisGrouped = SwAxisGrouped()

    def build(self) -> SwAxisGrouped:
        """Build and return SwAxisGrouped object.

        Returns:
            SwAxisGrouped instance
        """
        # TODO: Add validation
        return self._obj
