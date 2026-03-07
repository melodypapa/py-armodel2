"""McGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 190)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2034)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_McGroups.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_function import (
    McFunction,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.McGroups.mc_group_data_ref_set import (
    McGroupDataRefSet,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class McGroup(ARElement):
    """AUTOSAR McGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MC-GROUP"


    mc_function_refs: list[ARRef]
    ref_calprm_set_ref: Optional[ARRef]
    ref_ref: Optional[ARRef]
    sub_group_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "MC-FUNCTION-REFS": lambda obj, elem: [obj.mc_function_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "REF-CALPRM-SET-REF": lambda obj, elem: setattr(obj, "ref_calprm_set_ref", ARRef.deserialize(elem)),
        "REF-REF": lambda obj, elem: setattr(obj, "ref_ref", ARRef.deserialize(elem)),
        "SUB-GROUP-REFS": lambda obj, elem: [obj.sub_group_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize McGroup."""
        super().__init__()
        self.mc_function_refs: list[ARRef] = []
        self.ref_calprm_set_ref: Optional[ARRef] = None
        self.ref_ref: Optional[ARRef] = None
        self.sub_group_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize McGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(McGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mc_function_refs (list to container "MC-FUNCTION-REFS")
        if self.mc_function_refs:
            wrapper = ET.Element("MC-FUNCTION-REFS")
            for item in self.mc_function_refs:
                serialized = SerializationHelper.serialize_item(item, "McFunction")
                if serialized is not None:
                    child_elem = ET.Element("MC-FUNCTION-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ref_calprm_set_ref
        if self.ref_calprm_set_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ref_calprm_set_ref, "McGroupDataRefSet")
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

        # Serialize ref_ref
        if self.ref_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ref_ref, "McGroupDataRefSet")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REF-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sub_group_refs (list to container "SUB-GROUP-REFS")
        if self.sub_group_refs:
            wrapper = ET.Element("SUB-GROUP-REFS")
            for item in self.sub_group_refs:
                serialized = SerializationHelper.serialize_item(item, "McGroup")
                if serialized is not None:
                    child_elem = ET.Element("SUB-GROUP-REF")
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
    def deserialize(cls, element: ET.Element) -> "McGroup":
        """Deserialize XML element to McGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized McGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(McGroup, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MC-FUNCTION-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.mc_function_refs.append(ARRef.deserialize(item_elem))
            elif tag == "REF-CALPRM-SET-REF":
                setattr(obj, "ref_calprm_set_ref", ARRef.deserialize(child))
            elif tag == "REF-REF":
                setattr(obj, "ref_ref", ARRef.deserialize(child))
            elif tag == "SUB-GROUP-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.sub_group_refs.append(ARRef.deserialize(item_elem))

        return obj



class McGroupBuilder(ARElementBuilder):
    """Builder for McGroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: McGroup = McGroup()


    def with_mc_functions(self, items: list[McFunction]) -> "McGroupBuilder":
        """Set mc_functions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mc_functions = list(items) if items else []
        return self

    def with_ref_calprm_set(self, value: Optional[McGroupDataRefSet]) -> "McGroupBuilder":
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

    def with_ref(self, value: Optional[McGroupDataRefSet]) -> "McGroupBuilder":
        """Set ref attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'ref' is required and cannot be None")
        self._obj.ref = value
        return self

    def with_sub_groups(self, items: list[McGroup]) -> "McGroupBuilder":
        """Set sub_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sub_groups = list(items) if items else []
        return self


    def add_mc_function(self, item: McFunction) -> "McGroupBuilder":
        """Add a single item to mc_functions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mc_functions.append(item)
        return self

    def clear_mc_functions(self) -> "McGroupBuilder":
        """Clear all items from mc_functions list.

        Returns:
            self for method chaining
        """
        self._obj.mc_functions = []
        return self

    def add_sub_group(self, item: McGroup) -> "McGroupBuilder":
        """Add a single item to sub_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sub_groups.append(item)
        return self

    def clear_sub_groups(self) -> "McGroupBuilder":
        """Clear all items from sub_groups list.

        Returns:
            self for method chaining
        """
        self._obj.sub_groups = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "mcFunction",
        "ref",
        "refCalprmSet",
        "subGroup",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> McGroup:
        """Build and return the McGroup instance with validation."""
        self._validate_instance()
        return self._obj