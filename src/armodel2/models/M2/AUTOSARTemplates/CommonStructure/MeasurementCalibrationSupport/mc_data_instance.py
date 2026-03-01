"""McDataInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 177)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 997)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    McdIdentifier,
    PositiveInteger,
    SymbolString,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.rpt_impl_policy import (
    RptImplPolicy,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_sw_prototyping_access import (
    RptSwPrototypingAccess,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_instance_descriptor import (
        FlatInstanceDescriptor,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.implementation_element_in_parameter_instance_ref import (
        ImplementationElementInParameterInstanceRef,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_data_access_details import (
        McDataAccessDetails,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.role_based_mc_data_assignment import (
        RoleBasedMcDataAssignment,
    )
    from armodel2.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class McDataInstance(Identifiable):
    """AUTOSAR McDataInstance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MC-DATA-INSTANCE"


    array_size: Optional[PositiveInteger]
    display_identifier: Optional[McdIdentifier]
    flat_map_entry_ref: Optional[ARRef]
    instance_in: Optional[ImplementationElementInParameterInstanceRef]
    mc_data_access_details: Optional[McDataAccessDetails]
    mc_datas: list[RoleBasedMcDataAssignment]
    resulting: Optional[SwDataDefProps]
    resulting_rpt_sw: Optional[RptSwPrototypingAccess]
    role: Optional[Identifier]
    rpt_impl_policy: Optional[RptImplPolicy]
    sub_elements: list[McDataInstance]
    symbol: Optional[SymbolString]
    _DESERIALIZE_DISPATCH = {
        "ARRAY-SIZE": lambda obj, elem: setattr(obj, "array_size", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "DISPLAY-IDENTIFIER": lambda obj, elem: setattr(obj, "display_identifier", SerializationHelper.deserialize_by_tag(elem, "McdIdentifier")),
        "FLAT-MAP-ENTRY-REF": lambda obj, elem: setattr(obj, "flat_map_entry_ref", ARRef.deserialize(elem)),
        "INSTANCE-IN": lambda obj, elem: setattr(obj, "instance_in", SerializationHelper.deserialize_by_tag(elem, "ImplementationElementInParameterInstanceRef")),
        "MC-DATA-ACCESS-DETAILS": lambda obj, elem: setattr(obj, "mc_data_access_details", SerializationHelper.deserialize_by_tag(elem, "McDataAccessDetails")),
        "MC-DATAS": lambda obj, elem: obj.mc_datas.append(SerializationHelper.deserialize_by_tag(elem, "RoleBasedMcDataAssignment")),
        "RESULTING": lambda obj, elem: setattr(obj, "resulting", SerializationHelper.deserialize_by_tag(elem, "SwDataDefProps")),
        "RESULTING-RPT-SW": lambda obj, elem: setattr(obj, "resulting_rpt_sw", SerializationHelper.deserialize_by_tag(elem, "RptSwPrototypingAccess")),
        "ROLE": lambda obj, elem: setattr(obj, "role", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
        "RPT-IMPL-POLICY": lambda obj, elem: setattr(obj, "rpt_impl_policy", SerializationHelper.deserialize_by_tag(elem, "RptImplPolicy")),
        "SUB-ELEMENTS": lambda obj, elem: obj.sub_elements.append(SerializationHelper.deserialize_by_tag(elem, "McDataInstance")),
        "SYMBOL": lambda obj, elem: setattr(obj, "symbol", SerializationHelper.deserialize_by_tag(elem, "SymbolString")),
    }


    def __init__(self) -> None:
        """Initialize McDataInstance."""
        super().__init__()
        self.array_size: Optional[PositiveInteger] = None
        self.display_identifier: Optional[McdIdentifier] = None
        self.flat_map_entry_ref: Optional[ARRef] = None
        self.instance_in: Optional[ImplementationElementInParameterInstanceRef] = None
        self.mc_data_access_details: Optional[McDataAccessDetails] = None
        self.mc_datas: list[RoleBasedMcDataAssignment] = []
        self.resulting: Optional[SwDataDefProps] = None
        self.resulting_rpt_sw: Optional[RptSwPrototypingAccess] = None
        self.role: Optional[Identifier] = None
        self.rpt_impl_policy: Optional[RptImplPolicy] = None
        self.sub_elements: list[McDataInstance] = []
        self.symbol: Optional[SymbolString] = None

    def serialize(self) -> ET.Element:
        """Serialize McDataInstance to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(McDataInstance, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize array_size
        if self.array_size is not None:
            serialized = SerializationHelper.serialize_item(self.array_size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ARRAY-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize display_identifier
        if self.display_identifier is not None:
            serialized = SerializationHelper.serialize_item(self.display_identifier, "McdIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DISPLAY-IDENTIFIER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize flat_map_entry_ref
        if self.flat_map_entry_ref is not None:
            serialized = SerializationHelper.serialize_item(self.flat_map_entry_ref, "FlatInstanceDescriptor")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FLAT-MAP-ENTRY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize instance_in
        if self.instance_in is not None:
            serialized = SerializationHelper.serialize_item(self.instance_in, "ImplementationElementInParameterInstanceRef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INSTANCE-IN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mc_data_access_details
        if self.mc_data_access_details is not None:
            serialized = SerializationHelper.serialize_item(self.mc_data_access_details, "McDataAccessDetails")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MC-DATA-ACCESS-DETAILS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mc_datas (list to container "MC-DATAS")
        if self.mc_datas:
            wrapper = ET.Element("MC-DATAS")
            for item in self.mc_datas:
                serialized = SerializationHelper.serialize_item(item, "RoleBasedMcDataAssignment")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize resulting
        if self.resulting is not None:
            serialized = SerializationHelper.serialize_item(self.resulting, "SwDataDefProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESULTING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize resulting_rpt_sw
        if self.resulting_rpt_sw is not None:
            serialized = SerializationHelper.serialize_item(self.resulting_rpt_sw, "RptSwPrototypingAccess")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESULTING-RPT-SW")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize role
        if self.role is not None:
            serialized = SerializationHelper.serialize_item(self.role, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rpt_impl_policy
        if self.rpt_impl_policy is not None:
            serialized = SerializationHelper.serialize_item(self.rpt_impl_policy, "RptImplPolicy")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RPT-IMPL-POLICY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sub_elements (list to container "SUB-ELEMENTS")
        if self.sub_elements:
            wrapper = ET.Element("SUB-ELEMENTS")
            for item in self.sub_elements:
                serialized = SerializationHelper.serialize_item(item, "McDataInstance")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize symbol
        if self.symbol is not None:
            serialized = SerializationHelper.serialize_item(self.symbol, "SymbolString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYMBOL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "McDataInstance":
        """Deserialize XML element to McDataInstance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized McDataInstance object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(McDataInstance, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "ARRAY-SIZE":
                setattr(obj, "array_size", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "DISPLAY-IDENTIFIER":
                setattr(obj, "display_identifier", SerializationHelper.deserialize_by_tag(child, "McdIdentifier"))
            elif tag == "FLAT-MAP-ENTRY-REF":
                setattr(obj, "flat_map_entry_ref", ARRef.deserialize(child))
            elif tag == "INSTANCE-IN":
                setattr(obj, "instance_in", SerializationHelper.deserialize_by_tag(child, "ImplementationElementInParameterInstanceRef"))
            elif tag == "MC-DATA-ACCESS-DETAILS":
                setattr(obj, "mc_data_access_details", SerializationHelper.deserialize_by_tag(child, "McDataAccessDetails"))
            elif tag == "MC-DATAS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.mc_datas.append(SerializationHelper.deserialize_by_tag(item_elem, "RoleBasedMcDataAssignment"))
            elif tag == "RESULTING":
                setattr(obj, "resulting", SerializationHelper.deserialize_by_tag(child, "SwDataDefProps"))
            elif tag == "RESULTING-RPT-SW":
                setattr(obj, "resulting_rpt_sw", SerializationHelper.deserialize_by_tag(child, "RptSwPrototypingAccess"))
            elif tag == "ROLE":
                setattr(obj, "role", SerializationHelper.deserialize_by_tag(child, "Identifier"))
            elif tag == "RPT-IMPL-POLICY":
                setattr(obj, "rpt_impl_policy", SerializationHelper.deserialize_by_tag(child, "RptImplPolicy"))
            elif tag == "SUB-ELEMENTS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.sub_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "McDataInstance"))
            elif tag == "SYMBOL":
                setattr(obj, "symbol", SerializationHelper.deserialize_by_tag(child, "SymbolString"))

        return obj



class McDataInstanceBuilder(IdentifiableBuilder):
    """Builder for McDataInstance with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: McDataInstance = McDataInstance()


    def with_array_size(self, value: Optional[PositiveInteger]) -> "McDataInstanceBuilder":
        """Set array_size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.array_size = value
        return self

    def with_display_identifier(self, value: Optional[McdIdentifier]) -> "McDataInstanceBuilder":
        """Set display_identifier attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.display_identifier = value
        return self

    def with_flat_map_entry(self, value: Optional[FlatInstanceDescriptor]) -> "McDataInstanceBuilder":
        """Set flat_map_entry attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.flat_map_entry = value
        return self

    def with_instance_in(self, value: Optional[ImplementationElementInParameterInstanceRef]) -> "McDataInstanceBuilder":
        """Set instance_in attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.instance_in = value
        return self

    def with_mc_data_access_details(self, value: Optional[McDataAccessDetails]) -> "McDataInstanceBuilder":
        """Set mc_data_access_details attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mc_data_access_details = value
        return self

    def with_mc_datas(self, items: list[RoleBasedMcDataAssignment]) -> "McDataInstanceBuilder":
        """Set mc_datas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mc_datas = list(items) if items else []
        return self

    def with_resulting(self, value: Optional[SwDataDefProps]) -> "McDataInstanceBuilder":
        """Set resulting attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.resulting = value
        return self

    def with_resulting_rpt_sw(self, value: Optional[RptSwPrototypingAccess]) -> "McDataInstanceBuilder":
        """Set resulting_rpt_sw attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.resulting_rpt_sw = value
        return self

    def with_role(self, value: Optional[Identifier]) -> "McDataInstanceBuilder":
        """Set role attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.role = value
        return self

    def with_rpt_impl_policy(self, value: Optional[RptImplPolicy]) -> "McDataInstanceBuilder":
        """Set rpt_impl_policy attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rpt_impl_policy = value
        return self

    def with_sub_elements(self, items: list[McDataInstance]) -> "McDataInstanceBuilder":
        """Set sub_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sub_elements = list(items) if items else []
        return self

    def with_symbol(self, value: Optional[SymbolString]) -> "McDataInstanceBuilder":
        """Set symbol attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.symbol = value
        return self


    def add_mc_data(self, item: RoleBasedMcDataAssignment) -> "McDataInstanceBuilder":
        """Add a single item to mc_datas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mc_datas.append(item)
        return self

    def clear_mc_datas(self) -> "McDataInstanceBuilder":
        """Clear all items from mc_datas list.

        Returns:
            self for method chaining
        """
        self._obj.mc_datas = []
        return self

    def add_sub_element(self, item: McDataInstance) -> "McDataInstanceBuilder":
        """Add a single item to sub_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sub_elements.append(item)
        return self

    def clear_sub_elements(self) -> "McDataInstanceBuilder":
        """Clear all items from sub_elements list.

        Returns:
            self for method chaining
        """
        self._obj.sub_elements = []
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


    def build(self) -> McDataInstance:
        """Build and return the McDataInstance instance with validation."""
        self._validate_instance()
        pass
        return self._obj