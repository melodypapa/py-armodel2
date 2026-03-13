"""McSupportData AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 172)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 999)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_data_instance import (
    McDataInstance,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_sw_emulation_method_support import (
    McSwEmulationMethodSupport,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_support_data import (
    RptSupportData,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.sw_systemconstant_value_set import (
    SwSystemconstantValueSet,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class McSupportData(ARObject):
    """AUTOSAR McSupportData."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MC-SUPPORT-DATA"


    emulation_supports: list[McSwEmulationMethodSupport]
    mc_parameter_instances: list[McDataInstance]
    mc_variable_instances: list[McDataInstance]
    measurable_system_constant_value_refs: list[ARRef]
    rpt_support_data: Optional[RptSupportData]
    _DESERIALIZE_DISPATCH = {
        "EMULATION-SUPPORTS": lambda obj, elem: obj.emulation_supports.append(SerializationHelper.deserialize_by_tag(elem, "McSwEmulationMethodSupport")),
        "MC-PARAMETER-INSTANCES": lambda obj, elem: obj.mc_parameter_instances.append(SerializationHelper.deserialize_by_tag(elem, "McDataInstance")),
        "MC-VARIABLE-INSTANCES": lambda obj, elem: obj.mc_variable_instances.append(SerializationHelper.deserialize_by_tag(elem, "McDataInstance")),
        "MEASURABLE-SYSTEM-CONSTANT-VALUES-REFS": lambda obj, elem: [obj.measurable_system_constant_value_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "RPT-SUPPORT-DATA": lambda obj, elem: setattr(obj, "rpt_support_data", SerializationHelper.deserialize_by_tag(elem, "RptSupportData")),
    }


    def __init__(self) -> None:
        """Initialize McSupportData."""
        super().__init__()
        self.emulation_supports: list[McSwEmulationMethodSupport] = []
        self.mc_parameter_instances: list[McDataInstance] = []
        self.mc_variable_instances: list[McDataInstance] = []
        self.measurable_system_constant_value_refs: list[ARRef] = []
        self.rpt_support_data: Optional[RptSupportData] = None

    def serialize(self) -> ET.Element:
        """Serialize McSupportData to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(McSupportData, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize emulation_supports (list to container "EMULATION-SUPPORTS")
        if self.emulation_supports:
            wrapper = ET.Element("EMULATION-SUPPORTS")
            for item in self.emulation_supports:
                serialized = SerializationHelper.serialize_item(item, "McSwEmulationMethodSupport")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mc_parameter_instances (list to container "MC-PARAMETER-INSTANCES")
        if self.mc_parameter_instances:
            wrapper = ET.Element("MC-PARAMETER-INSTANCES")
            for item in self.mc_parameter_instances:
                serialized = SerializationHelper.serialize_item(item, "McDataInstance")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mc_variable_instances (list to container "MC-VARIABLE-INSTANCES")
        if self.mc_variable_instances:
            wrapper = ET.Element("MC-VARIABLE-INSTANCES")
            for item in self.mc_variable_instances:
                serialized = SerializationHelper.serialize_item(item, "McDataInstance")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize measurable_system_constant_value_refs (list to container "MEASURABLE-SYSTEM-CONSTANT-VALUES-REFS")
        if self.measurable_system_constant_value_refs:
            wrapper = ET.Element("MEASURABLE-SYSTEM-CONSTANT-VALUES-REFS")
            for item in self.measurable_system_constant_value_refs:
                serialized = SerializationHelper.serialize_item(item, "SwSystemconstantValueSet")
                if serialized is not None:
                    child_elem = ET.Element("MEASURABLE-SYSTEM-CONSTANT-VALUE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rpt_support_data
        if self.rpt_support_data is not None:
            serialized = SerializationHelper.serialize_item(self.rpt_support_data, "RptSupportData")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RPT-SUPPORT-DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "McSupportData":
        """Deserialize XML element to McSupportData object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized McSupportData object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(McSupportData, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "EMULATION-SUPPORTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.emulation_supports.append(SerializationHelper.deserialize_by_tag(item_elem, "McSwEmulationMethodSupport"))
            elif tag == "MC-PARAMETER-INSTANCES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.mc_parameter_instances.append(SerializationHelper.deserialize_by_tag(item_elem, "McDataInstance"))
            elif tag == "MC-VARIABLE-INSTANCES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.mc_variable_instances.append(SerializationHelper.deserialize_by_tag(item_elem, "McDataInstance"))
            elif tag == "MEASURABLE-SYSTEM-CONSTANT-VALUES-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.measurable_system_constant_value_refs.append(ARRef.deserialize(item_elem))
            elif tag == "RPT-SUPPORT-DATA":
                setattr(obj, "rpt_support_data", SerializationHelper.deserialize_by_tag(child, "RptSupportData"))

        return obj



class McSupportDataBuilder(BuilderBase):
    """Builder for McSupportData with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: McSupportData = McSupportData()


    def with_emulation_supports(self, items: list[McSwEmulationMethodSupport]) -> "McSupportDataBuilder":
        """Set emulation_supports list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.emulation_supports = list(items) if items else []
        return self

    def with_mc_parameter_instances(self, items: list[McDataInstance]) -> "McSupportDataBuilder":
        """Set mc_parameter_instances list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mc_parameter_instances = list(items) if items else []
        return self

    def with_mc_variable_instances(self, items: list[McDataInstance]) -> "McSupportDataBuilder":
        """Set mc_variable_instances list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mc_variable_instances = list(items) if items else []
        return self

    def with_measurable_system_constant_valueses(self, items: list[SwSystemconstantValueSet]) -> "McSupportDataBuilder":
        """Set measurable_system_constant_valueses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.measurable_system_constant_valueses = list(items) if items else []
        return self

    def with_rpt_support_data(self, value: Optional[RptSupportData]) -> "McSupportDataBuilder":
        """Set rpt_support_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'rpt_support_data' is required and cannot be None")
        self._obj.rpt_support_data = value
        return self


    def add_emulation_support(self, item: McSwEmulationMethodSupport) -> "McSupportDataBuilder":
        """Add a single item to emulation_supports list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.emulation_supports.append(item)
        return self

    def clear_emulation_supports(self) -> "McSupportDataBuilder":
        """Clear all items from emulation_supports list.

        Returns:
            self for method chaining
        """
        self._obj.emulation_supports = []
        return self

    def add_mc_parameter_instance(self, item: McDataInstance) -> "McSupportDataBuilder":
        """Add a single item to mc_parameter_instances list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mc_parameter_instances.append(item)
        return self

    def clear_mc_parameter_instances(self) -> "McSupportDataBuilder":
        """Clear all items from mc_parameter_instances list.

        Returns:
            self for method chaining
        """
        self._obj.mc_parameter_instances = []
        return self

    def add_mc_variable_instance(self, item: McDataInstance) -> "McSupportDataBuilder":
        """Add a single item to mc_variable_instances list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mc_variable_instances.append(item)
        return self

    def clear_mc_variable_instances(self) -> "McSupportDataBuilder":
        """Clear all items from mc_variable_instances list.

        Returns:
            self for method chaining
        """
        self._obj.mc_variable_instances = []
        return self

    def add_measurable_system_constant_values(self, item: SwSystemconstantValueSet) -> "McSupportDataBuilder":
        """Add a single item to measurable_system_constant_valueses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.measurable_system_constant_valueses.append(item)
        return self

    def clear_measurable_system_constant_valueses(self) -> "McSupportDataBuilder":
        """Clear all items from measurable_system_constant_valueses list.

        Returns:
            self for method chaining
        """
        self._obj.measurable_system_constant_valueses = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "emulationSupport",
        "mcParameterInstance",
        "mcVariableInstance",
        "measurableSystemConstantValues",
        "rptSupportData",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> McSupportData:
        """Build and return the McSupportData instance with validation."""
        self._validate_instance()
        return self._obj