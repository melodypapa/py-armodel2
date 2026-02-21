"""McFunction AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 186)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.mc_function_data_ref_set import (
    McFunctionDataRefSet,
)


class McFunction(ARElement):
    """AUTOSAR McFunction."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def_calprm_set_ref: Optional[ARRef]
    in_measurement_ref: Optional[ARRef]
    loc_ref: Optional[ARRef]
    out_ref: Optional[ARRef]
    ref_calprm_set_ref: Optional[ARRef]
    sub_function_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize McFunction."""
        super().__init__()
        self.def_calprm_set_ref: Optional[ARRef] = None
        self.in_measurement_ref: Optional[ARRef] = None
        self.loc_ref: Optional[ARRef] = None
        self.out_ref: Optional[ARRef] = None
        self.ref_calprm_set_ref: Optional[ARRef] = None
        self.sub_function_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize McFunction to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(McFunction, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize def_calprm_set_ref
        if self.def_calprm_set_ref is not None:
            serialized = SerializationHelper.serialize_item(self.def_calprm_set_ref, "McFunctionDataRefSet")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEF-CALPRM-SET-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize in_measurement_ref
        if self.in_measurement_ref is not None:
            serialized = SerializationHelper.serialize_item(self.in_measurement_ref, "McFunctionDataRefSet")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IN-MEASUREMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize loc_ref
        if self.loc_ref is not None:
            serialized = SerializationHelper.serialize_item(self.loc_ref, "McFunctionDataRefSet")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOC-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize out_ref
        if self.out_ref is not None:
            serialized = SerializationHelper.serialize_item(self.out_ref, "McFunctionDataRefSet")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OUT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ref_calprm_set_ref
        if self.ref_calprm_set_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ref_calprm_set_ref, "McFunctionDataRefSet")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REF-CALPRM-SET-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sub_function_refs (list to container "SUB-FUNCTION-REFS")
        if self.sub_function_refs:
            wrapper = ET.Element("SUB-FUNCTION-REFS")
            for item in self.sub_function_refs:
                serialized = SerializationHelper.serialize_item(item, "McFunction")
                if serialized is not None:
                    child_elem = ET.Element("SUB-FUNCTION-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "McFunction":
        """Deserialize XML element to McFunction object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized McFunction object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(McFunction, cls).deserialize(element)

        # Parse def_calprm_set_ref
        child = SerializationHelper.find_child_element(element, "DEF-CALPRM-SET-REF")
        if child is not None:
            def_calprm_set_ref_value = ARRef.deserialize(child)
            obj.def_calprm_set_ref = def_calprm_set_ref_value

        # Parse in_measurement_ref
        child = SerializationHelper.find_child_element(element, "IN-MEASUREMENT-REF")
        if child is not None:
            in_measurement_ref_value = ARRef.deserialize(child)
            obj.in_measurement_ref = in_measurement_ref_value

        # Parse loc_ref
        child = SerializationHelper.find_child_element(element, "LOC-REF")
        if child is not None:
            loc_ref_value = ARRef.deserialize(child)
            obj.loc_ref = loc_ref_value

        # Parse out_ref
        child = SerializationHelper.find_child_element(element, "OUT-REF")
        if child is not None:
            out_ref_value = ARRef.deserialize(child)
            obj.out_ref = out_ref_value

        # Parse ref_calprm_set_ref
        child = SerializationHelper.find_child_element(element, "REF-CALPRM-SET-REF")
        if child is not None:
            ref_calprm_set_ref_value = ARRef.deserialize(child)
            obj.ref_calprm_set_ref = ref_calprm_set_ref_value

        # Parse sub_function_refs (list from container "SUB-FUNCTION-REFS")
        obj.sub_function_refs = []
        container = SerializationHelper.find_child_element(element, "SUB-FUNCTION-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sub_function_refs.append(child_value)

        return obj



class McFunctionBuilder:
    """Builder for McFunction."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: McFunction = McFunction()

    def build(self) -> McFunction:
        """Build and return McFunction object.

        Returns:
            McFunction instance
        """
        # TODO: Add validation
        return self._obj
