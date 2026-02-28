"""DltArgument AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 983)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 13)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_LogAndTraceExtract.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class DltArgument(Identifiable):
    """AUTOSAR DltArgument."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DLT-ARGUMENT"


    dlt_arguments: list[DltArgument]
    length: Optional[PositiveInteger]
    network: Optional[SwDataDefProps]
    optional: Optional[Boolean]
    predefined_text: Optional[Boolean]
    variable_length: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "DLT-ARGUMENTS": lambda obj, elem: obj.dlt_arguments.append(DltArgument.deserialize(elem)),
        "LENGTH": lambda obj, elem: setattr(obj, "length", elem.text),
        "NETWORK": lambda obj, elem: setattr(obj, "network", SwDataDefProps.deserialize(elem)),
        "OPTIONAL": lambda obj, elem: setattr(obj, "optional", elem.text),
        "PREDEFINED-TEXT": lambda obj, elem: setattr(obj, "predefined_text", elem.text),
        "VARIABLE-LENGTH": lambda obj, elem: setattr(obj, "variable_length", elem.text),
    }


    def __init__(self) -> None:
        """Initialize DltArgument."""
        super().__init__()
        self.dlt_arguments: list[DltArgument] = []
        self.length: Optional[PositiveInteger] = None
        self.network: Optional[SwDataDefProps] = None
        self.optional: Optional[Boolean] = None
        self.predefined_text: Optional[Boolean] = None
        self.variable_length: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize DltArgument to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DltArgument, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dlt_arguments (list to container "DLT-ARGUMENTS")
        if self.dlt_arguments:
            wrapper = ET.Element("DLT-ARGUMENTS")
            for item in self.dlt_arguments:
                serialized = SerializationHelper.serialize_item(item, "DltArgument")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize length
        if self.length is not None:
            serialized = SerializationHelper.serialize_item(self.length, "PositiveInteger")
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

        # Serialize network
        if self.network is not None:
            serialized = SerializationHelper.serialize_item(self.network, "SwDataDefProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NETWORK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize optional
        if self.optional is not None:
            serialized = SerializationHelper.serialize_item(self.optional, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OPTIONAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize predefined_text
        if self.predefined_text is not None:
            serialized = SerializationHelper.serialize_item(self.predefined_text, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PREDEFINED-TEXT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize variable_length
        if self.variable_length is not None:
            serialized = SerializationHelper.serialize_item(self.variable_length, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VARIABLE-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DltArgument":
        """Deserialize XML element to DltArgument object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DltArgument object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DltArgument, cls).deserialize(element)

        # Parse dlt_arguments (list from container "DLT-ARGUMENTS")
        obj.dlt_arguments = []
        container = SerializationHelper.find_child_element(element, "DLT-ARGUMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dlt_arguments.append(child_value)

        # Parse length
        child = SerializationHelper.find_child_element(element, "LENGTH")
        if child is not None:
            length_value = child.text
            obj.length = length_value

        # Parse network
        child = SerializationHelper.find_child_element(element, "NETWORK")
        if child is not None:
            network_value = SerializationHelper.deserialize_by_tag(child, "SwDataDefProps")
            obj.network = network_value

        # Parse optional
        child = SerializationHelper.find_child_element(element, "OPTIONAL")
        if child is not None:
            optional_value = child.text
            obj.optional = optional_value

        # Parse predefined_text
        child = SerializationHelper.find_child_element(element, "PREDEFINED-TEXT")
        if child is not None:
            predefined_text_value = child.text
            obj.predefined_text = predefined_text_value

        # Parse variable_length
        child = SerializationHelper.find_child_element(element, "VARIABLE-LENGTH")
        if child is not None:
            variable_length_value = child.text
            obj.variable_length = variable_length_value

        return obj



class DltArgumentBuilder(IdentifiableBuilder):
    """Builder for DltArgument with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DltArgument = DltArgument()


    def with_dlt_arguments(self, items: list[DltArgument]) -> "DltArgumentBuilder":
        """Set dlt_arguments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.dlt_arguments = list(items) if items else []
        return self

    def with_length(self, value: Optional[PositiveInteger]) -> "DltArgumentBuilder":
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

    def with_network(self, value: Optional[SwDataDefProps]) -> "DltArgumentBuilder":
        """Set network attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.network = value
        return self

    def with_optional(self, value: Optional[Boolean]) -> "DltArgumentBuilder":
        """Set optional attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.optional = value
        return self

    def with_predefined_text(self, value: Optional[Boolean]) -> "DltArgumentBuilder":
        """Set predefined_text attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.predefined_text = value
        return self

    def with_variable_length(self, value: Optional[Boolean]) -> "DltArgumentBuilder":
        """Set variable_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.variable_length = value
        return self


    def add_dlt_argument(self, item: DltArgument) -> "DltArgumentBuilder":
        """Add a single item to dlt_arguments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.dlt_arguments.append(item)
        return self

    def clear_dlt_arguments(self) -> "DltArgumentBuilder":
        """Clear all items from dlt_arguments list.

        Returns:
            self for method chaining
        """
        self._obj.dlt_arguments = []
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


    def build(self) -> DltArgument:
        """Build and return the DltArgument instance with validation."""
        self._validate_instance()
        pass
        return self._obj