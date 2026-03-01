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


    emulations: list[McSwEmulationMethodSupport]
    mc_parameters: list[McDataInstance]
    mc_variables: list[McDataInstance]
    measurable_refs: list[ARRef]
    rpt_support_data: Optional[RptSupportData]
    _DESERIALIZE_DISPATCH = {
        "EMULATIONS": lambda obj, elem: obj.emulations.append(SerializationHelper.deserialize_by_tag(elem, "McSwEmulationMethodSupport")),
        "MC-PARAMETERS": lambda obj, elem: obj.mc_parameters.append(SerializationHelper.deserialize_by_tag(elem, "McDataInstance")),
        "MC-VARIABLES": lambda obj, elem: obj.mc_variables.append(SerializationHelper.deserialize_by_tag(elem, "McDataInstance")),
        "MEASURABLES": lambda obj, elem: obj.measurable_refs.append(ARRef.deserialize(elem)),
        "RPT-SUPPORT-DATA": lambda obj, elem: setattr(obj, "rpt_support_data", SerializationHelper.deserialize_by_tag(elem, "RptSupportData")),
    }


    def __init__(self) -> None:
        """Initialize McSupportData."""
        super().__init__()
        self.emulations: list[McSwEmulationMethodSupport] = []
        self.mc_parameters: list[McDataInstance] = []
        self.mc_variables: list[McDataInstance] = []
        self.measurable_refs: list[ARRef] = []
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

        # Serialize emulations (list to container "EMULATIONS")
        if self.emulations:
            wrapper = ET.Element("EMULATIONS")
            for item in self.emulations:
                serialized = SerializationHelper.serialize_item(item, "McSwEmulationMethodSupport")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mc_parameters (list to container "MC-PARAMETERS")
        if self.mc_parameters:
            wrapper = ET.Element("MC-PARAMETERS")
            for item in self.mc_parameters:
                serialized = SerializationHelper.serialize_item(item, "McDataInstance")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mc_variables (list to container "MC-VARIABLES")
        if self.mc_variables:
            wrapper = ET.Element("MC-VARIABLES")
            for item in self.mc_variables:
                serialized = SerializationHelper.serialize_item(item, "McDataInstance")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize measurable_refs (list to container "MEASURABLE-REFS")
        if self.measurable_refs:
            wrapper = ET.Element("MEASURABLE-REFS")
            for item in self.measurable_refs:
                serialized = SerializationHelper.serialize_item(item, "SwSystemconstantValueSet")
                if serialized is not None:
                    child_elem = ET.Element("MEASURABLE-REF")
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
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "EMULATIONS":
                obj.emulations.append(SerializationHelper.deserialize_by_tag(child, "McSwEmulationMethodSupport"))
            elif tag == "MC-PARAMETERS":
                obj.mc_parameters.append(SerializationHelper.deserialize_by_tag(child, "McDataInstance"))
            elif tag == "MC-VARIABLES":
                obj.mc_variables.append(SerializationHelper.deserialize_by_tag(child, "McDataInstance"))
            elif tag == "MEASURABLES":
                obj.measurable_refs.append(ARRef.deserialize(child))
            elif tag == "RPT-SUPPORT-DATA":
                setattr(obj, "rpt_support_data", SerializationHelper.deserialize_by_tag(child, "RptSupportData"))

        return obj



class McSupportDataBuilder(BuilderBase):
    """Builder for McSupportData with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: McSupportData = McSupportData()


    def with_emulations(self, items: list[McSwEmulationMethodSupport]) -> "McSupportDataBuilder":
        """Set emulations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.emulations = list(items) if items else []
        return self

    def with_mc_parameters(self, items: list[McDataInstance]) -> "McSupportDataBuilder":
        """Set mc_parameters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mc_parameters = list(items) if items else []
        return self

    def with_mc_variables(self, items: list[McDataInstance]) -> "McSupportDataBuilder":
        """Set mc_variables list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mc_variables = list(items) if items else []
        return self

    def with_measurables(self, items: list[SwSystemconstantValueSet]) -> "McSupportDataBuilder":
        """Set measurables list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.measurables = list(items) if items else []
        return self

    def with_rpt_support_data(self, value: Optional[RptSupportData]) -> "McSupportDataBuilder":
        """Set rpt_support_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rpt_support_data = value
        return self


    def add_emulation(self, item: McSwEmulationMethodSupport) -> "McSupportDataBuilder":
        """Add a single item to emulations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.emulations.append(item)
        return self

    def clear_emulations(self) -> "McSupportDataBuilder":
        """Clear all items from emulations list.

        Returns:
            self for method chaining
        """
        self._obj.emulations = []
        return self

    def add_mc_parameter(self, item: McDataInstance) -> "McSupportDataBuilder":
        """Add a single item to mc_parameters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mc_parameters.append(item)
        return self

    def clear_mc_parameters(self) -> "McSupportDataBuilder":
        """Clear all items from mc_parameters list.

        Returns:
            self for method chaining
        """
        self._obj.mc_parameters = []
        return self

    def add_mc_variable(self, item: McDataInstance) -> "McSupportDataBuilder":
        """Add a single item to mc_variables list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mc_variables.append(item)
        return self

    def clear_mc_variables(self) -> "McSupportDataBuilder":
        """Clear all items from mc_variables list.

        Returns:
            self for method chaining
        """
        self._obj.mc_variables = []
        return self

    def add_measurable(self, item: SwSystemconstantValueSet) -> "McSupportDataBuilder":
        """Add a single item to measurables list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.measurables.append(item)
        return self

    def clear_measurables(self) -> "McSupportDataBuilder":
        """Clear all items from measurables list.

        Returns:
            self for method chaining
        """
        self._obj.measurables = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> McSupportData:
        """Build and return the McSupportData instance with validation."""
        self._validate_instance()
        pass
        return self._obj