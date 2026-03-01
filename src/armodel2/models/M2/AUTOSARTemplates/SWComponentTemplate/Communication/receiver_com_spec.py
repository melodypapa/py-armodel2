"""ReceiverComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 170)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2047)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import RPortComSpecBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    HandleOutOfRangeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.composite_network_representation import (
    CompositeNetworkRepresentation,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.reception_com_spec_props import (
    ReceptionComSpecProps,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.transformation_com_spec_props import (
    TransformationComSpecProps,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.variable_access import (
    VariableAccess,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ReceiverComSpec(RPortComSpec, ABC):
    """AUTOSAR ReceiverComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    composite_network_representations: list[CompositeNetworkRepresentation]
    data_element_ref: Optional[ARRef]
    handle_out_of_range: Optional[HandleOutOfRangeEnum]
    handle_out_of_range_status: Optional[HandleOutOfRangeEnum]
    max_delta_counter_init: Optional[PositiveInteger]
    max_no_new_or_repeated_data: Optional[PositiveInteger]
    network_representation: Optional[SwDataDefProps]
    reception_props: Optional[ReceptionComSpecProps]
    replace_with: Optional[VariableAccess]
    sync_counter_init: Optional[PositiveInteger]
    transformation_com_spec_propses: list[TransformationComSpecProps]
    uses_end_to_end_protection: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "COMPOSITE-NETWORK-REPRESENTATIONS": lambda obj, elem: obj.composite_network_representations.append(SerializationHelper.deserialize_by_tag(elem, "CompositeNetworkRepresentation")),
        "DATA-ELEMENT-REF": ("_POLYMORPHIC", "data_element_ref", ["ArgumentDataPrototype", "ParameterDataPrototype", "VariableDataPrototype"]),
        "HANDLE-OUT-OF-RANGE": lambda obj, elem: setattr(obj, "handle_out_of_range", HandleOutOfRangeEnum.deserialize(elem)),
        "HANDLE-OUT-OF-RANGE-STATUS": lambda obj, elem: setattr(obj, "handle_out_of_range_status", HandleOutOfRangeEnum.deserialize(elem)),
        "MAX-DELTA-COUNTER-INIT": lambda obj, elem: setattr(obj, "max_delta_counter_init", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MAX-NO-NEW-OR-REPEATED-DATA": lambda obj, elem: setattr(obj, "max_no_new_or_repeated_data", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "NETWORK-REPRESENTATION": lambda obj, elem: setattr(obj, "network_representation", SerializationHelper.deserialize_by_tag(elem, "SwDataDefProps")),
        "RECEPTION-PROPS": lambda obj, elem: setattr(obj, "reception_props", SerializationHelper.deserialize_by_tag(elem, "ReceptionComSpecProps")),
        "REPLACE-WITH": lambda obj, elem: setattr(obj, "replace_with", SerializationHelper.deserialize_by_tag(elem, "VariableAccess")),
        "SYNC-COUNTER-INIT": lambda obj, elem: setattr(obj, "sync_counter_init", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "TRANSFORMATION-COM-SPEC-PROPSES": ("_POLYMORPHIC_LIST", "transformation_com_spec_propses", ["EndToEndTransformationComSpecProps", "UserDefinedTransformationComSpecProps"]),
        "USES-END-TO-END-PROTECTION": lambda obj, elem: setattr(obj, "uses_end_to_end_protection", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize ReceiverComSpec."""
        super().__init__()
        self.composite_network_representations: list[CompositeNetworkRepresentation] = []
        self.data_element_ref: Optional[ARRef] = None
        self.handle_out_of_range: Optional[HandleOutOfRangeEnum] = None
        self.handle_out_of_range_status: Optional[HandleOutOfRangeEnum] = None
        self.max_delta_counter_init: Optional[PositiveInteger] = None
        self.max_no_new_or_repeated_data: Optional[PositiveInteger] = None
        self.network_representation: Optional[SwDataDefProps] = None
        self.reception_props: Optional[ReceptionComSpecProps] = None
        self.replace_with: Optional[VariableAccess] = None
        self.sync_counter_init: Optional[PositiveInteger] = None
        self.transformation_com_spec_propses: list[TransformationComSpecProps] = []
        self.uses_end_to_end_protection: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize ReceiverComSpec to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ReceiverComSpec, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize composite_network_representations (list to container "COMPOSITE-NETWORK-REPRESENTATIONS")
        if self.composite_network_representations:
            wrapper = ET.Element("COMPOSITE-NETWORK-REPRESENTATIONS")
            for item in self.composite_network_representations:
                serialized = SerializationHelper.serialize_item(item, "CompositeNetworkRepresentation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize data_element_ref
        if self.data_element_ref is not None:
            serialized = SerializationHelper.serialize_item(self.data_element_ref, "AutosarDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-ELEMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize handle_out_of_range
        if self.handle_out_of_range is not None:
            serialized = SerializationHelper.serialize_item(self.handle_out_of_range, "HandleOutOfRangeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HANDLE-OUT-OF-RANGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize handle_out_of_range_status
        if self.handle_out_of_range_status is not None:
            serialized = SerializationHelper.serialize_item(self.handle_out_of_range_status, "HandleOutOfRangeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HANDLE-OUT-OF-RANGE-STATUS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_delta_counter_init
        if self.max_delta_counter_init is not None:
            serialized = SerializationHelper.serialize_item(self.max_delta_counter_init, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-DELTA-COUNTER-INIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_no_new_or_repeated_data
        if self.max_no_new_or_repeated_data is not None:
            serialized = SerializationHelper.serialize_item(self.max_no_new_or_repeated_data, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-NO-NEW-OR-REPEATED-DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize network_representation
        if self.network_representation is not None:
            serialized = SerializationHelper.serialize_item(self.network_representation, "SwDataDefProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NETWORK-REPRESENTATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize reception_props
        if self.reception_props is not None:
            serialized = SerializationHelper.serialize_item(self.reception_props, "ReceptionComSpecProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RECEPTION-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize replace_with
        if self.replace_with is not None:
            serialized = SerializationHelper.serialize_item(self.replace_with, "VariableAccess")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REPLACE-WITH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sync_counter_init
        if self.sync_counter_init is not None:
            serialized = SerializationHelper.serialize_item(self.sync_counter_init, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYNC-COUNTER-INIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transformation_com_spec_propses (list to container "TRANSFORMATION-COM-SPEC-PROPSES")
        if self.transformation_com_spec_propses:
            wrapper = ET.Element("TRANSFORMATION-COM-SPEC-PROPSES")
            for item in self.transformation_com_spec_propses:
                serialized = SerializationHelper.serialize_item(item, "TransformationComSpecProps")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize uses_end_to_end_protection
        if self.uses_end_to_end_protection is not None:
            serialized = SerializationHelper.serialize_item(self.uses_end_to_end_protection, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USES-END-TO-END-PROTECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ReceiverComSpec":
        """Deserialize XML element to ReceiverComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ReceiverComSpec object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ReceiverComSpec, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "COMPOSITE-NETWORK-REPRESENTATIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.composite_network_representations.append(SerializationHelper.deserialize_by_tag(item_elem, "CompositeNetworkRepresentation"))
            elif tag == "DATA-ELEMENT-REF":
                setattr(obj, "data_element_ref", ARRef.deserialize(child))
            elif tag == "HANDLE-OUT-OF-RANGE":
                setattr(obj, "handle_out_of_range", HandleOutOfRangeEnum.deserialize(child))
            elif tag == "HANDLE-OUT-OF-RANGE-STATUS":
                setattr(obj, "handle_out_of_range_status", HandleOutOfRangeEnum.deserialize(child))
            elif tag == "MAX-DELTA-COUNTER-INIT":
                setattr(obj, "max_delta_counter_init", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "MAX-NO-NEW-OR-REPEATED-DATA":
                setattr(obj, "max_no_new_or_repeated_data", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "NETWORK-REPRESENTATION":
                setattr(obj, "network_representation", SerializationHelper.deserialize_by_tag(child, "SwDataDefProps"))
            elif tag == "RECEPTION-PROPS":
                setattr(obj, "reception_props", SerializationHelper.deserialize_by_tag(child, "ReceptionComSpecProps"))
            elif tag == "REPLACE-WITH":
                setattr(obj, "replace_with", SerializationHelper.deserialize_by_tag(child, "VariableAccess"))
            elif tag == "SYNC-COUNTER-INIT":
                setattr(obj, "sync_counter_init", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "TRANSFORMATION-COM-SPEC-PROPSES":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "END-TO-END-TRANSFORMATION-COM-SPEC-PROPS":
                        obj.transformation_com_spec_propses.append(SerializationHelper.deserialize_by_tag(item_elem, "EndToEndTransformationComSpecProps"))
                    elif concrete_tag == "USER-DEFINED-TRANSFORMATION-COM-SPEC-PROPS":
                        obj.transformation_com_spec_propses.append(SerializationHelper.deserialize_by_tag(item_elem, "UserDefinedTransformationComSpecProps"))
            elif tag == "USES-END-TO-END-PROTECTION":
                setattr(obj, "uses_end_to_end_protection", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class ReceiverComSpecBuilder(RPortComSpecBuilder):
    """Builder for ReceiverComSpec with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ReceiverComSpec = ReceiverComSpec()


    def with_composite_network_representations(self, items: list[CompositeNetworkRepresentation]) -> "ReceiverComSpecBuilder":
        """Set composite_network_representations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.composite_network_representations = list(items) if items else []
        return self

    def with_data_element(self, value: Optional[AutosarDataPrototype]) -> "ReceiverComSpecBuilder":
        """Set data_element attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_element = value
        return self

    def with_handle_out_of_range(self, value: Optional[HandleOutOfRangeEnum]) -> "ReceiverComSpecBuilder":
        """Set handle_out_of_range attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.handle_out_of_range = value
        return self

    def with_handle_out_of_range_status(self, value: Optional[HandleOutOfRangeEnum]) -> "ReceiverComSpecBuilder":
        """Set handle_out_of_range_status attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.handle_out_of_range_status = value
        return self

    def with_max_delta_counter_init(self, value: Optional[PositiveInteger]) -> "ReceiverComSpecBuilder":
        """Set max_delta_counter_init attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_delta_counter_init = value
        return self

    def with_max_no_new_or_repeated_data(self, value: Optional[PositiveInteger]) -> "ReceiverComSpecBuilder":
        """Set max_no_new_or_repeated_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_no_new_or_repeated_data = value
        return self

    def with_network_representation(self, value: Optional[SwDataDefProps]) -> "ReceiverComSpecBuilder":
        """Set network_representation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.network_representation = value
        return self

    def with_reception_props(self, value: Optional[ReceptionComSpecProps]) -> "ReceiverComSpecBuilder":
        """Set reception_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.reception_props = value
        return self

    def with_replace_with(self, value: Optional[VariableAccess]) -> "ReceiverComSpecBuilder":
        """Set replace_with attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.replace_with = value
        return self

    def with_sync_counter_init(self, value: Optional[PositiveInteger]) -> "ReceiverComSpecBuilder":
        """Set sync_counter_init attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sync_counter_init = value
        return self

    def with_transformation_com_spec_propses(self, items: list[TransformationComSpecProps]) -> "ReceiverComSpecBuilder":
        """Set transformation_com_spec_propses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.transformation_com_spec_propses = list(items) if items else []
        return self

    def with_uses_end_to_end_protection(self, value: Optional[Boolean]) -> "ReceiverComSpecBuilder":
        """Set uses_end_to_end_protection attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uses_end_to_end_protection = value
        return self


    def add_composite_network_representation(self, item: CompositeNetworkRepresentation) -> "ReceiverComSpecBuilder":
        """Add a single item to composite_network_representations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.composite_network_representations.append(item)
        return self

    def clear_composite_network_representations(self) -> "ReceiverComSpecBuilder":
        """Clear all items from composite_network_representations list.

        Returns:
            self for method chaining
        """
        self._obj.composite_network_representations = []
        return self

    def add_transformation_com_spec_props(self, item: TransformationComSpecProps) -> "ReceiverComSpecBuilder":
        """Add a single item to transformation_com_spec_propses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.transformation_com_spec_propses.append(item)
        return self

    def clear_transformation_com_spec_propses(self) -> "ReceiverComSpecBuilder":
        """Clear all items from transformation_com_spec_propses list.

        Returns:
            self for method chaining
        """
        self._obj.transformation_com_spec_propses = []
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


    @abstractmethod
    def build(self) -> ReceiverComSpec:
        """Build and return the ReceiverComSpec instance (abstract)."""
        raise NotImplementedError