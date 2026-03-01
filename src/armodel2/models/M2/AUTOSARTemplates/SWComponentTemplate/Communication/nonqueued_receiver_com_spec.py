"""NonqueuedReceiverComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 172)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2039)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 198)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import polymorphic

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.receiver_com_spec import (
    ReceiverComSpec,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.receiver_com_spec import ReceiverComSpecBuilder
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    HandleTimeoutEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Filter.data_filter import (
    DataFilter,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class NonqueuedReceiverComSpec(ReceiverComSpec):
    """AUTOSAR NonqueuedReceiverComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "NONQUEUED-RECEIVER-COM-SPEC"


    alive_timeout: Optional[TimeValue]
    enable_update: Optional[Boolean]
    filter: Optional[DataFilter]
    handle_data_status: Optional[Boolean]
    handle_never_received: Optional[Boolean]
    handle_timeout_type: Optional[HandleTimeoutEnum]
    _init_value: Optional[ValueSpecification]
    timeout_substitution_value: Optional[ValueSpecification]
    _DESERIALIZE_DISPATCH = {
        "ALIVE-TIMEOUT": lambda obj, elem: setattr(obj, "alive_timeout", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "ENABLE-UPDATE": lambda obj, elem: setattr(obj, "enable_update", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "FILTER": lambda obj, elem: setattr(obj, "filter", SerializationHelper.deserialize_by_tag(elem, "DataFilter")),
        "HANDLE-DATA-STATUS": lambda obj, elem: setattr(obj, "handle_data_status", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "HANDLE-NEVER-RECEIVED": lambda obj, elem: setattr(obj, "handle_never_received", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "HANDLE-TIMEOUT-TYPE": lambda obj, elem: setattr(obj, "handle_timeout_type", HandleTimeoutEnum.deserialize(elem)),
        "INIT-VALUE": ("_POLYMORPHIC", "_init_value", ["AbstractRuleBasedValueSpecification", "ApplicationRuleBasedValueSpecification", "ApplicationValueSpecification", "ArrayValueSpecification", "CompositeRuleBasedValueSpecification", "CompositeValueSpecification", "ConstantReference", "NotAvailableValueSpecification", "NumericalValueSpecification", "RecordValueSpecification", "ReferenceValueSpecification", "TextValueSpecification"]),
        "TIMEOUT-SUBSTITUTION-VALUE": ("_POLYMORPHIC", "timeout_substitution_value", ["AbstractRuleBasedValueSpecification", "ApplicationRuleBasedValueSpecification", "ApplicationValueSpecification", "ArrayValueSpecification", "CompositeRuleBasedValueSpecification", "CompositeValueSpecification", "ConstantReference", "NotAvailableValueSpecification", "NumericalValueSpecification", "RecordValueSpecification", "ReferenceValueSpecification", "TextValueSpecification"]),
    }


    def __init__(self) -> None:
        """Initialize NonqueuedReceiverComSpec."""
        super().__init__()
        self.alive_timeout: Optional[TimeValue] = None
        self.enable_update: Optional[Boolean] = None
        self.filter: Optional[DataFilter] = None
        self.handle_data_status: Optional[Boolean] = None
        self.handle_never_received: Optional[Boolean] = None
        self.handle_timeout_type: Optional[HandleTimeoutEnum] = None
        self._init_value: Optional[ValueSpecification] = None
        self.timeout_substitution_value: Optional[ValueSpecification] = None
    @property
    @polymorphic({"INIT-VALUE": "ValueSpecification"})
    def init_value(self) -> Optional[ValueSpecification]:
        """Get init_value with polymorphic wrapper handling."""
        return self._init_value

    @init_value.setter
    def init_value(self, value: Optional[ValueSpecification]) -> None:
        """Set init_value with polymorphic wrapper handling."""
        self._init_value = value


    def serialize(self) -> ET.Element:
        """Serialize NonqueuedReceiverComSpec to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NonqueuedReceiverComSpec, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize alive_timeout
        if self.alive_timeout is not None:
            serialized = SerializationHelper.serialize_item(self.alive_timeout, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALIVE-TIMEOUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize enable_update
        if self.enable_update is not None:
            serialized = SerializationHelper.serialize_item(self.enable_update, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENABLE-UPDATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize filter
        if self.filter is not None:
            serialized = SerializationHelper.serialize_item(self.filter, "DataFilter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FILTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize handle_data_status
        if self.handle_data_status is not None:
            serialized = SerializationHelper.serialize_item(self.handle_data_status, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HANDLE-DATA-STATUS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize handle_never_received
        if self.handle_never_received is not None:
            serialized = SerializationHelper.serialize_item(self.handle_never_received, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HANDLE-NEVER-RECEIVED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize handle_timeout_type
        if self.handle_timeout_type is not None:
            serialized = SerializationHelper.serialize_item(self.handle_timeout_type, "HandleTimeoutEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HANDLE-TIMEOUT-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize init_value (polymorphic wrapper "INIT-VALUE")
        if self.init_value is not None:
            serialized = SerializationHelper.serialize_item(self.init_value, "ValueSpecification")
            if serialized is not None:
                # For polymorphic types, wrap the serialized element (preserving concrete type)
                wrapped = ET.Element("INIT-VALUE")
                wrapped.append(serialized)
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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NonqueuedReceiverComSpec":
        """Deserialize XML element to NonqueuedReceiverComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NonqueuedReceiverComSpec object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NonqueuedReceiverComSpec, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ALIVE-TIMEOUT":
                setattr(obj, "alive_timeout", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "ENABLE-UPDATE":
                setattr(obj, "enable_update", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "FILTER":
                setattr(obj, "filter", SerializationHelper.deserialize_by_tag(child, "DataFilter"))
            elif tag == "HANDLE-DATA-STATUS":
                setattr(obj, "handle_data_status", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "HANDLE-NEVER-RECEIVED":
                setattr(obj, "handle_never_received", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "HANDLE-TIMEOUT-TYPE":
                setattr(obj, "handle_timeout_type", HandleTimeoutEnum.deserialize(child))
            elif tag == "INIT-VALUE":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ABSTRACT-RULE-BASED-VALUE-SPECIFICATION":
                        setattr(obj, "_init_value", SerializationHelper.deserialize_by_tag(child[0], "AbstractRuleBasedValueSpecification"))
                    elif concrete_tag == "APPLICATION-RULE-BASED-VALUE-SPECIFICATION":
                        setattr(obj, "_init_value", SerializationHelper.deserialize_by_tag(child[0], "ApplicationRuleBasedValueSpecification"))
                    elif concrete_tag == "APPLICATION-VALUE-SPECIFICATION":
                        setattr(obj, "_init_value", SerializationHelper.deserialize_by_tag(child[0], "ApplicationValueSpecification"))
                    elif concrete_tag == "ARRAY-VALUE-SPECIFICATION":
                        setattr(obj, "_init_value", SerializationHelper.deserialize_by_tag(child[0], "ArrayValueSpecification"))
                    elif concrete_tag == "COMPOSITE-RULE-BASED-VALUE-SPECIFICATION":
                        setattr(obj, "_init_value", SerializationHelper.deserialize_by_tag(child[0], "CompositeRuleBasedValueSpecification"))
                    elif concrete_tag == "COMPOSITE-VALUE-SPECIFICATION":
                        setattr(obj, "_init_value", SerializationHelper.deserialize_by_tag(child[0], "CompositeValueSpecification"))
                    elif concrete_tag == "CONSTANT-REFERENCE":
                        setattr(obj, "_init_value", SerializationHelper.deserialize_by_tag(child[0], "ConstantReference"))
                    elif concrete_tag == "NOT-AVAILABLE-VALUE-SPECIFICATION":
                        setattr(obj, "_init_value", SerializationHelper.deserialize_by_tag(child[0], "NotAvailableValueSpecification"))
                    elif concrete_tag == "NUMERICAL-VALUE-SPECIFICATION":
                        setattr(obj, "_init_value", SerializationHelper.deserialize_by_tag(child[0], "NumericalValueSpecification"))
                    elif concrete_tag == "RECORD-VALUE-SPECIFICATION":
                        setattr(obj, "_init_value", SerializationHelper.deserialize_by_tag(child[0], "RecordValueSpecification"))
                    elif concrete_tag == "REFERENCE-VALUE-SPECIFICATION":
                        setattr(obj, "_init_value", SerializationHelper.deserialize_by_tag(child[0], "ReferenceValueSpecification"))
                    elif concrete_tag == "TEXT-VALUE-SPECIFICATION":
                        setattr(obj, "_init_value", SerializationHelper.deserialize_by_tag(child[0], "TextValueSpecification"))
            elif tag == "TIMEOUT-SUBSTITUTION-VALUE":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ABSTRACT-RULE-BASED-VALUE-SPECIFICATION":
                        setattr(obj, "timeout_substitution_value", SerializationHelper.deserialize_by_tag(child[0], "AbstractRuleBasedValueSpecification"))
                    elif concrete_tag == "APPLICATION-RULE-BASED-VALUE-SPECIFICATION":
                        setattr(obj, "timeout_substitution_value", SerializationHelper.deserialize_by_tag(child[0], "ApplicationRuleBasedValueSpecification"))
                    elif concrete_tag == "APPLICATION-VALUE-SPECIFICATION":
                        setattr(obj, "timeout_substitution_value", SerializationHelper.deserialize_by_tag(child[0], "ApplicationValueSpecification"))
                    elif concrete_tag == "ARRAY-VALUE-SPECIFICATION":
                        setattr(obj, "timeout_substitution_value", SerializationHelper.deserialize_by_tag(child[0], "ArrayValueSpecification"))
                    elif concrete_tag == "COMPOSITE-RULE-BASED-VALUE-SPECIFICATION":
                        setattr(obj, "timeout_substitution_value", SerializationHelper.deserialize_by_tag(child[0], "CompositeRuleBasedValueSpecification"))
                    elif concrete_tag == "COMPOSITE-VALUE-SPECIFICATION":
                        setattr(obj, "timeout_substitution_value", SerializationHelper.deserialize_by_tag(child[0], "CompositeValueSpecification"))
                    elif concrete_tag == "CONSTANT-REFERENCE":
                        setattr(obj, "timeout_substitution_value", SerializationHelper.deserialize_by_tag(child[0], "ConstantReference"))
                    elif concrete_tag == "NOT-AVAILABLE-VALUE-SPECIFICATION":
                        setattr(obj, "timeout_substitution_value", SerializationHelper.deserialize_by_tag(child[0], "NotAvailableValueSpecification"))
                    elif concrete_tag == "NUMERICAL-VALUE-SPECIFICATION":
                        setattr(obj, "timeout_substitution_value", SerializationHelper.deserialize_by_tag(child[0], "NumericalValueSpecification"))
                    elif concrete_tag == "RECORD-VALUE-SPECIFICATION":
                        setattr(obj, "timeout_substitution_value", SerializationHelper.deserialize_by_tag(child[0], "RecordValueSpecification"))
                    elif concrete_tag == "REFERENCE-VALUE-SPECIFICATION":
                        setattr(obj, "timeout_substitution_value", SerializationHelper.deserialize_by_tag(child[0], "ReferenceValueSpecification"))
                    elif concrete_tag == "TEXT-VALUE-SPECIFICATION":
                        setattr(obj, "timeout_substitution_value", SerializationHelper.deserialize_by_tag(child[0], "TextValueSpecification"))

        return obj



class NonqueuedReceiverComSpecBuilder(ReceiverComSpecBuilder):
    """Builder for NonqueuedReceiverComSpec with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: NonqueuedReceiverComSpec = NonqueuedReceiverComSpec()


    def with_alive_timeout(self, value: Optional[TimeValue]) -> "NonqueuedReceiverComSpecBuilder":
        """Set alive_timeout attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.alive_timeout = value
        return self

    def with_enable_update(self, value: Optional[Boolean]) -> "NonqueuedReceiverComSpecBuilder":
        """Set enable_update attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.enable_update = value
        return self

    def with_filter(self, value: Optional[DataFilter]) -> "NonqueuedReceiverComSpecBuilder":
        """Set filter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.filter = value
        return self

    def with_handle_data_status(self, value: Optional[Boolean]) -> "NonqueuedReceiverComSpecBuilder":
        """Set handle_data_status attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.handle_data_status = value
        return self

    def with_handle_never_received(self, value: Optional[Boolean]) -> "NonqueuedReceiverComSpecBuilder":
        """Set handle_never_received attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.handle_never_received = value
        return self

    def with_handle_timeout_type(self, value: Optional[HandleTimeoutEnum]) -> "NonqueuedReceiverComSpecBuilder":
        """Set handle_timeout_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.handle_timeout_type = value
        return self

    def with_init_value(self, value: Optional[ValueSpecification]) -> "NonqueuedReceiverComSpecBuilder":
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

    def with_timeout_substitution_value(self, value: Optional[ValueSpecification]) -> "NonqueuedReceiverComSpecBuilder":
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


    def build(self) -> NonqueuedReceiverComSpec:
        """Build and return the NonqueuedReceiverComSpec instance with validation."""
        self._validate_instance()
        pass
        return self._obj