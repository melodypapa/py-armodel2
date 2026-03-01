"""NvProvideComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 195)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
    PPortComSpec,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import PPortComSpecBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class NvProvideComSpec(PPortComSpec):
    """AUTOSAR NvProvideComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "NV-PROVIDE-COM-SPEC"


    ram_block_init_value: Optional[ValueSpecification]
    rom_block_init_value: Optional[ValueSpecification]
    variable_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "RAM-BLOCK-INIT-VALUE": ("_POLYMORPHIC", "ram_block_init_value", ["AbstractRuleBasedValueSpecification", "ApplicationValueSpecification", "CompositeValueSpecification", "ConstantReference", "NotAvailableValueSpecification", "NumericalValueSpecification", "ReferenceValueSpecification", "TextValueSpecification"]),
        "ROM-BLOCK-INIT-VALUE": ("_POLYMORPHIC", "rom_block_init_value", ["AbstractRuleBasedValueSpecification", "ApplicationValueSpecification", "CompositeValueSpecification", "ConstantReference", "NotAvailableValueSpecification", "NumericalValueSpecification", "ReferenceValueSpecification", "TextValueSpecification"]),
        "VARIABLE-REF": lambda obj, elem: setattr(obj, "variable_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize NvProvideComSpec."""
        super().__init__()
        self.ram_block_init_value: Optional[ValueSpecification] = None
        self.rom_block_init_value: Optional[ValueSpecification] = None
        self.variable_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize NvProvideComSpec to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NvProvideComSpec, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ram_block_init_value
        if self.ram_block_init_value is not None:
            serialized = SerializationHelper.serialize_item(self.ram_block_init_value, "ValueSpecification")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RAM-BLOCK-INIT-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rom_block_init_value
        if self.rom_block_init_value is not None:
            serialized = SerializationHelper.serialize_item(self.rom_block_init_value, "ValueSpecification")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROM-BLOCK-INIT-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize variable_ref
        if self.variable_ref is not None:
            serialized = SerializationHelper.serialize_item(self.variable_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VARIABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NvProvideComSpec":
        """Deserialize XML element to NvProvideComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NvProvideComSpec object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NvProvideComSpec, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "RAM-BLOCK-INIT-VALUE":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ABSTRACT-RULE-BASED-VALUE-SPECIFICATION":
                        setattr(obj, "ram_block_init_value", SerializationHelper.deserialize_by_tag(child[0], "AbstractRuleBasedValueSpecification"))
                    elif concrete_tag == "APPLICATION-VALUE-SPECIFICATION":
                        setattr(obj, "ram_block_init_value", SerializationHelper.deserialize_by_tag(child[0], "ApplicationValueSpecification"))
                    elif concrete_tag == "COMPOSITE-VALUE-SPECIFICATION":
                        setattr(obj, "ram_block_init_value", SerializationHelper.deserialize_by_tag(child[0], "CompositeValueSpecification"))
                    elif concrete_tag == "CONSTANT-REFERENCE":
                        setattr(obj, "ram_block_init_value", SerializationHelper.deserialize_by_tag(child[0], "ConstantReference"))
                    elif concrete_tag == "NOT-AVAILABLE-VALUE-SPECIFICATION":
                        setattr(obj, "ram_block_init_value", SerializationHelper.deserialize_by_tag(child[0], "NotAvailableValueSpecification"))
                    elif concrete_tag == "NUMERICAL-VALUE-SPECIFICATION":
                        setattr(obj, "ram_block_init_value", SerializationHelper.deserialize_by_tag(child[0], "NumericalValueSpecification"))
                    elif concrete_tag == "REFERENCE-VALUE-SPECIFICATION":
                        setattr(obj, "ram_block_init_value", SerializationHelper.deserialize_by_tag(child[0], "ReferenceValueSpecification"))
                    elif concrete_tag == "TEXT-VALUE-SPECIFICATION":
                        setattr(obj, "ram_block_init_value", SerializationHelper.deserialize_by_tag(child[0], "TextValueSpecification"))
            elif tag == "ROM-BLOCK-INIT-VALUE":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ABSTRACT-RULE-BASED-VALUE-SPECIFICATION":
                        setattr(obj, "rom_block_init_value", SerializationHelper.deserialize_by_tag(child[0], "AbstractRuleBasedValueSpecification"))
                    elif concrete_tag == "APPLICATION-VALUE-SPECIFICATION":
                        setattr(obj, "rom_block_init_value", SerializationHelper.deserialize_by_tag(child[0], "ApplicationValueSpecification"))
                    elif concrete_tag == "COMPOSITE-VALUE-SPECIFICATION":
                        setattr(obj, "rom_block_init_value", SerializationHelper.deserialize_by_tag(child[0], "CompositeValueSpecification"))
                    elif concrete_tag == "CONSTANT-REFERENCE":
                        setattr(obj, "rom_block_init_value", SerializationHelper.deserialize_by_tag(child[0], "ConstantReference"))
                    elif concrete_tag == "NOT-AVAILABLE-VALUE-SPECIFICATION":
                        setattr(obj, "rom_block_init_value", SerializationHelper.deserialize_by_tag(child[0], "NotAvailableValueSpecification"))
                    elif concrete_tag == "NUMERICAL-VALUE-SPECIFICATION":
                        setattr(obj, "rom_block_init_value", SerializationHelper.deserialize_by_tag(child[0], "NumericalValueSpecification"))
                    elif concrete_tag == "REFERENCE-VALUE-SPECIFICATION":
                        setattr(obj, "rom_block_init_value", SerializationHelper.deserialize_by_tag(child[0], "ReferenceValueSpecification"))
                    elif concrete_tag == "TEXT-VALUE-SPECIFICATION":
                        setattr(obj, "rom_block_init_value", SerializationHelper.deserialize_by_tag(child[0], "TextValueSpecification"))
            elif tag == "VARIABLE-REF":
                setattr(obj, "variable_ref", ARRef.deserialize(child))

        return obj



class NvProvideComSpecBuilder(PPortComSpecBuilder):
    """Builder for NvProvideComSpec with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: NvProvideComSpec = NvProvideComSpec()


    def with_ram_block_init_value(self, value: Optional[ValueSpecification]) -> "NvProvideComSpecBuilder":
        """Set ram_block_init_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ram_block_init_value = value
        return self

    def with_rom_block_init_value(self, value: Optional[ValueSpecification]) -> "NvProvideComSpecBuilder":
        """Set rom_block_init_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rom_block_init_value = value
        return self

    def with_variable(self, value: Optional[VariableDataPrototype]) -> "NvProvideComSpecBuilder":
        """Set variable attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.variable = value
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


    def build(self) -> NvProvideComSpec:
        """Build and return the NvProvideComSpec instance with validation."""
        self._validate_instance()
        pass
        return self._obj