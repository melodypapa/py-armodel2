"""NonqueuedSenderComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 179)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 198)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import polymorphic

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.sender_com_spec import (
    SenderComSpec,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.sender_com_spec import SenderComSpecBuilder
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Filter.data_filter import (
    DataFilter,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class NonqueuedSenderComSpec(SenderComSpec):
    """AUTOSAR NonqueuedSenderComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_filter: Optional[DataFilter]
    _init_value: Optional[ValueSpecification]
    def __init__(self) -> None:
        """Initialize NonqueuedSenderComSpec."""
        super().__init__()
        self.data_filter: Optional[DataFilter] = None
        self._init_value: Optional[ValueSpecification] = None
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
        """Serialize NonqueuedSenderComSpec to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NonqueuedSenderComSpec, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_filter
        if self.data_filter is not None:
            serialized = SerializationHelper.serialize_item(self.data_filter, "DataFilter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-FILTER")
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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NonqueuedSenderComSpec":
        """Deserialize XML element to NonqueuedSenderComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NonqueuedSenderComSpec object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NonqueuedSenderComSpec, cls).deserialize(element)

        # Parse data_filter
        child = SerializationHelper.find_child_element(element, "DATA-FILTER")
        if child is not None:
            data_filter_value = SerializationHelper.deserialize_by_tag(child, "DataFilter")
            obj.data_filter = data_filter_value

        # Parse init_value (polymorphic wrapper "INIT-VALUE")
        wrapper = SerializationHelper.find_child_element(element, "INIT-VALUE")
        if wrapper is not None:
            init_value_value = SerializationHelper.deserialize_polymorphic(wrapper, "ValueSpecification")
            obj.init_value = init_value_value

        return obj



class NonqueuedSenderComSpecBuilder(SenderComSpecBuilder):
    """Builder for NonqueuedSenderComSpec with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: NonqueuedSenderComSpec = NonqueuedSenderComSpec()


    def with_data_filter(self, value: Optional[DataFilter]) -> "NonqueuedSenderComSpecBuilder":
        """Set data_filter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_filter = value
        return self

    def with_init_value(self, value: Optional[ValueSpecification]) -> "NonqueuedSenderComSpecBuilder":
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


    def build(self) -> NonqueuedSenderComSpec:
        """Build and return the NonqueuedSenderComSpec instance with validation."""
        self._validate_instance()
        pass
        return self._obj