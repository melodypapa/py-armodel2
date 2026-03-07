"""McFunction AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 186)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.mc_function_data_ref_set import (
    McFunctionDataRefSet,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class McFunction(ARElement):
    """AUTOSAR McFunction."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MC-FUNCTION"


    def_calprm_set_ref: Optional[ARRef]
    in_measurement_ref: Optional[ARRef]
    loc_ref: Optional[ARRef]
    out_ref: Optional[ARRef]
    ref_calprm_set_ref: Optional[ARRef]
    sub_function_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "DEF-CALPRM-SET-REF": lambda obj, elem: setattr(obj, "def_calprm_set_ref", ARRef.deserialize(elem)),
        "IN-MEASUREMENT-REF": lambda obj, elem: setattr(obj, "in_measurement_ref", ARRef.deserialize(elem)),
        "LOC-REF": lambda obj, elem: setattr(obj, "loc_ref", ARRef.deserialize(elem)),
        "OUT-REF": lambda obj, elem: setattr(obj, "out_ref", ARRef.deserialize(elem)),
        "REF-CALPRM-SET-REF": lambda obj, elem: setattr(obj, "ref_calprm_set_ref", ARRef.deserialize(elem)),
        "SUB-FUNCTION-REFS": lambda obj, elem: [obj.sub_function_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DEF-CALPRM-SET-REF":
                setattr(obj, "def_calprm_set_ref", ARRef.deserialize(child))
            elif tag == "IN-MEASUREMENT-REF":
                setattr(obj, "in_measurement_ref", ARRef.deserialize(child))
            elif tag == "LOC-REF":
                setattr(obj, "loc_ref", ARRef.deserialize(child))
            elif tag == "OUT-REF":
                setattr(obj, "out_ref", ARRef.deserialize(child))
            elif tag == "REF-CALPRM-SET-REF":
                setattr(obj, "ref_calprm_set_ref", ARRef.deserialize(child))
            elif tag == "SUB-FUNCTION-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.sub_function_refs.append(ARRef.deserialize(item_elem))

        return obj



class McFunctionBuilder(ARElementBuilder):
    """Builder for McFunction with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: McFunction = McFunction()


    def with_def_calprm_set(self, value: Optional[McFunctionDataRefSet]) -> "McFunctionBuilder":
        """Set def_calprm_set attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'def_calprm_set' is required and cannot be None")
        self._obj.def_calprm_set = value
        return self

    def with_in_measurement(self, value: Optional[McFunctionDataRefSet]) -> "McFunctionBuilder":
        """Set in_measurement attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'in_measurement' is required and cannot be None")
        self._obj.in_measurement = value
        return self

    def with_loc(self, value: Optional[McFunctionDataRefSet]) -> "McFunctionBuilder":
        """Set loc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'loc' is required and cannot be None")
        self._obj.loc = value
        return self

    def with_out(self, value: Optional[McFunctionDataRefSet]) -> "McFunctionBuilder":
        """Set out attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'out' is required and cannot be None")
        self._obj.out = value
        return self

    def with_ref_calprm_set(self, value: Optional[McFunctionDataRefSet]) -> "McFunctionBuilder":
        """Set ref_calprm_set attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'ref_calprm_set' is required and cannot be None")
        self._obj.ref_calprm_set = value
        return self

    def with_sub_functions(self, items: list[McFunction]) -> "McFunctionBuilder":
        """Set sub_functions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sub_functions = list(items) if items else []
        return self


    def add_sub_function(self, item: McFunction) -> "McFunctionBuilder":
        """Add a single item to sub_functions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sub_functions.append(item)
        return self

    def clear_sub_functions(self) -> "McFunctionBuilder":
        """Clear all items from sub_functions list.

        Returns:
            self for method chaining
        """
        self._obj.sub_functions = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "defCalprmSet",
        "inMeasurement",
        "loc",
        "out",
        "refCalprmSet",
        "subFunction",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> McFunction:
        """Build and return the McFunction instance with validation."""
        self._validate_instance()
        return self._obj