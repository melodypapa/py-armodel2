"""ISignal AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 315)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 992)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 320)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 227)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import FibexElementBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
    DataTypePolicyEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ISignalTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    UnlimitedInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_transformation import (
    DataTransformation,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_props import (
    ISignalProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_i_signal_props import (
    TransformationISignalProps,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
class ISignal(FibexElement):
    """AUTOSAR ISignal."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_transformation_ref: Optional[ARRef]
    data_type_policy_enum: Optional[DataTypePolicyEnum]
    init_value: Optional[ValueSpecification]
    i_signal_props: Optional[ISignalProps]
    i_signal_type: Optional[ISignalTypeEnum]
    length: Optional[UnlimitedInteger]
    network_representation_props: Optional[SwDataDefProps]
    system_signal_ref: Optional[ARRef]
    timeout_substitution_value: Optional[ValueSpecification]
    transformation_i_signal_props: list[TransformationISignalProps]
    def __init__(self) -> None:
        """Initialize ISignal."""
        super().__init__()
        self.data_transformation_ref: Optional[ARRef] = None
        self.data_type_policy_enum: Optional[DataTypePolicyEnum] = None
        self.init_value: Optional[ValueSpecification] = None
        self.i_signal_props: Optional[ISignalProps] = None
        self.i_signal_type: Optional[ISignalTypeEnum] = None
        self.length: Optional[UnlimitedInteger] = None
        self.network_representation_props: Optional[SwDataDefProps] = None
        self.system_signal_ref: Optional[ARRef] = None
        self.timeout_substitution_value: Optional[ValueSpecification] = None
        self.transformation_i_signal_props: list[TransformationISignalProps] = []

    def serialize(self) -> ET.Element:
        """Serialize ISignal to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ISignal, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_transformation_ref
        if self.data_transformation_ref is not None:
            serialized = SerializationHelper.serialize_item(self.data_transformation_ref, "DataTransformation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-TRANSFORMATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize data_type_policy_enum
        if self.data_type_policy_enum is not None:
            serialized = SerializationHelper.serialize_item(self.data_type_policy_enum, "DataTypePolicyEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-TYPE-POLICY-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize init_value
        if self.init_value is not None:
            serialized = SerializationHelper.serialize_item(self.init_value, "ValueSpecification")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INIT-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize i_signal_props
        if self.i_signal_props is not None:
            serialized = SerializationHelper.serialize_item(self.i_signal_props, "ISignalProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("I-SIGNAL-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize i_signal_type
        if self.i_signal_type is not None:
            serialized = SerializationHelper.serialize_item(self.i_signal_type, "ISignalTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("I-SIGNAL-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize length
        if self.length is not None:
            serialized = SerializationHelper.serialize_item(self.length, "UnlimitedInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize network_representation_props
        if self.network_representation_props is not None:
            serialized = SerializationHelper.serialize_item(self.network_representation_props, "SwDataDefProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NETWORK-REPRESENTATION-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize system_signal_ref
        if self.system_signal_ref is not None:
            serialized = SerializationHelper.serialize_item(self.system_signal_ref, "SystemSignal")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYSTEM-SIGNAL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timeout_substitution_value
        if self.timeout_substitution_value is not None:
            serialized = SerializationHelper.serialize_item(self.timeout_substitution_value, "ValueSpecification")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT-SUBSTITUTION-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transformation_i_signal_props (list to container "TRANSFORMATION-I-SIGNAL-PROPS")
        if self.transformation_i_signal_props:
            wrapper = ET.Element("TRANSFORMATION-I-SIGNAL-PROPS")
            for item in self.transformation_i_signal_props:
                serialized = SerializationHelper.serialize_item(item, "TransformationISignalProps")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ISignal":
        """Deserialize XML element to ISignal object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ISignal object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ISignal, cls).deserialize(element)

        # Parse data_transformation_ref
        child = SerializationHelper.find_child_element(element, "DATA-TRANSFORMATION-REF")
        if child is not None:
            data_transformation_ref_value = ARRef.deserialize(child)
            obj.data_transformation_ref = data_transformation_ref_value

        # Parse data_type_policy_enum
        child = SerializationHelper.find_child_element(element, "DATA-TYPE-POLICY-ENUM")
        if child is not None:
            data_type_policy_enum_value = DataTypePolicyEnum.deserialize(child)
            obj.data_type_policy_enum = data_type_policy_enum_value

        # Parse init_value
        child = SerializationHelper.find_child_element(element, "INIT-VALUE")
        if child is not None:
            init_value_value = SerializationHelper.deserialize_by_tag(child, "ValueSpecification")
            obj.init_value = init_value_value

        # Parse i_signal_props
        child = SerializationHelper.find_child_element(element, "I-SIGNAL-PROPS")
        if child is not None:
            i_signal_props_value = SerializationHelper.deserialize_by_tag(child, "ISignalProps")
            obj.i_signal_props = i_signal_props_value

        # Parse i_signal_type
        child = SerializationHelper.find_child_element(element, "I-SIGNAL-TYPE")
        if child is not None:
            i_signal_type_value = ISignalTypeEnum.deserialize(child)
            obj.i_signal_type = i_signal_type_value

        # Parse length
        child = SerializationHelper.find_child_element(element, "LENGTH")
        if child is not None:
            length_value = child.text
            obj.length = length_value

        # Parse network_representation_props
        child = SerializationHelper.find_child_element(element, "NETWORK-REPRESENTATION-PROPS")
        if child is not None:
            network_representation_props_value = SerializationHelper.deserialize_by_tag(child, "SwDataDefProps")
            obj.network_representation_props = network_representation_props_value

        # Parse system_signal_ref
        child = SerializationHelper.find_child_element(element, "SYSTEM-SIGNAL-REF")
        if child is not None:
            system_signal_ref_value = ARRef.deserialize(child)
            obj.system_signal_ref = system_signal_ref_value

        # Parse timeout_substitution_value
        child = SerializationHelper.find_child_element(element, "TIMEOUT-SUBSTITUTION-VALUE")
        if child is not None:
            timeout_substitution_value_value = SerializationHelper.deserialize_by_tag(child, "ValueSpecification")
            obj.timeout_substitution_value = timeout_substitution_value_value

        # Parse transformation_i_signal_props (list from container "TRANSFORMATION-I-SIGNAL-PROPS")
        obj.transformation_i_signal_props = []
        container = SerializationHelper.find_child_element(element, "TRANSFORMATION-I-SIGNAL-PROPS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.transformation_i_signal_props.append(child_value)

        return obj



class ISignalBuilder(FibexElementBuilder):
    """Builder for ISignal with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ISignal = ISignal()


    def with_data_transformation(self, value: Optional[DataTransformation]) -> "ISignalBuilder":
        """Set data_transformation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_transformation = value
        return self

    def with_data_type_policy_enum(self, value: Optional[DataTypePolicyEnum]) -> "ISignalBuilder":
        """Set data_type_policy_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_type_policy_enum = value
        return self

    def with_init_value(self, value: Optional[ValueSpecification]) -> "ISignalBuilder":
        """Set init_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.init_value = value
        return self

    def with_i_signal_props(self, value: Optional[ISignalProps]) -> "ISignalBuilder":
        """Set i_signal_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.i_signal_props = value
        return self

    def with_i_signal_type(self, value: Optional[ISignalTypeEnum]) -> "ISignalBuilder":
        """Set i_signal_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.i_signal_type = value
        return self

    def with_length(self, value: Optional[UnlimitedInteger]) -> "ISignalBuilder":
        """Set length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.length = value
        return self

    def with_network_representation_props(self, value: Optional[SwDataDefProps]) -> "ISignalBuilder":
        """Set network_representation_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.network_representation_props = value
        return self

    def with_system_signal(self, value: Optional[SystemSignal]) -> "ISignalBuilder":
        """Set system_signal attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.system_signal = value
        return self

    def with_timeout_substitution_value(self, value: Optional[ValueSpecification]) -> "ISignalBuilder":
        """Set timeout_substitution_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timeout_substitution_value = value
        return self

    def with_transformation_i_signal_props(self, items: list[TransformationISignalProps]) -> "ISignalBuilder":
        """Set transformation_i_signal_props list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.transformation_i_signal_props = list(items) if items else []
        return self


    def add_transformation_i_signal_prop(self, item: TransformationISignalProps) -> "ISignalBuilder":
        """Add a single item to transformation_i_signal_props list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.transformation_i_signal_props.append(item)
        return self

    def clear_transformation_i_signal_props(self) -> "ISignalBuilder":
        """Clear all items from transformation_i_signal_props list.

        Returns:
            self for method chaining
        """
        self._obj.transformation_i_signal_props = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> ISignal:
        """Build and return the ISignal instance with validation."""
        self._validate_instance()
        pass
        return self._obj