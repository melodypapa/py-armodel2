"""ApplicationInterface AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 28)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AbstractPlatform.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import PortInterfaceBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel2.models.M2.AUTOSARTemplates.AdaptivePlatform.ApplicationDesign.PortInterface.field import (
    Field,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ApplicationInterface(PortInterface):
    """AUTOSAR ApplicationInterface."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "APPLICATION-INTERFACE"


    attributes: list[Field]
    commands: list[ClientServerOperation]
    indication_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "ATTRIBUTES": lambda obj, elem: obj.attributes.append(SerializationHelper.deserialize_by_tag(elem, "Field")),
        "COMMANDS": lambda obj, elem: obj.commands.append(SerializationHelper.deserialize_by_tag(elem, "ClientServerOperation")),
        "INDICATION-REFS": lambda obj, elem: [obj.indication_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize ApplicationInterface."""
        super().__init__()
        self.attributes: list[Field] = []
        self.commands: list[ClientServerOperation] = []
        self.indication_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize ApplicationInterface to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ApplicationInterface, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize attributes (list to container "ATTRIBUTES")
        if self.attributes:
            wrapper = ET.Element("ATTRIBUTES")
            for item in self.attributes:
                serialized = SerializationHelper.serialize_item(item, "Field")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize commands (list to container "COMMANDS")
        if self.commands:
            wrapper = ET.Element("COMMANDS")
            for item in self.commands:
                serialized = SerializationHelper.serialize_item(item, "ClientServerOperation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize indication_refs (list to container "INDICATION-REFS")
        if self.indication_refs:
            wrapper = ET.Element("INDICATION-REFS")
            for item in self.indication_refs:
                serialized = SerializationHelper.serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    child_elem = ET.Element("INDICATION-REF")
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
    def deserialize(cls, element: ET.Element) -> "ApplicationInterface":
        """Deserialize XML element to ApplicationInterface object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationInterface object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ApplicationInterface, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ATTRIBUTES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.attributes.append(SerializationHelper.deserialize_by_tag(item_elem, "Field"))
            elif tag == "COMMANDS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.commands.append(SerializationHelper.deserialize_by_tag(item_elem, "ClientServerOperation"))
            elif tag == "INDICATION-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.indication_refs.append(ARRef.deserialize(item_elem))

        return obj



class ApplicationInterfaceBuilder(PortInterfaceBuilder):
    """Builder for ApplicationInterface with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ApplicationInterface = ApplicationInterface()


    def with_attributes(self, items: list[Field]) -> "ApplicationInterfaceBuilder":
        """Set attributes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.attributes = list(items) if items else []
        return self

    def with_commands(self, items: list[ClientServerOperation]) -> "ApplicationInterfaceBuilder":
        """Set commands list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.commands = list(items) if items else []
        return self

    def with_indications(self, items: list[VariableDataPrototype]) -> "ApplicationInterfaceBuilder":
        """Set indications list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.indications = list(items) if items else []
        return self


    def add_attribute(self, item: Field) -> "ApplicationInterfaceBuilder":
        """Add a single item to attributes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.attributes.append(item)
        return self

    def clear_attributes(self) -> "ApplicationInterfaceBuilder":
        """Clear all items from attributes list.

        Returns:
            self for method chaining
        """
        self._obj.attributes = []
        return self

    def add_command(self, item: ClientServerOperation) -> "ApplicationInterfaceBuilder":
        """Add a single item to commands list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.commands.append(item)
        return self

    def clear_commands(self) -> "ApplicationInterfaceBuilder":
        """Clear all items from commands list.

        Returns:
            self for method chaining
        """
        self._obj.commands = []
        return self

    def add_indication(self, item: VariableDataPrototype) -> "ApplicationInterfaceBuilder":
        """Add a single item to indications list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.indications.append(item)
        return self

    def clear_indications(self) -> "ApplicationInterfaceBuilder":
        """Clear all items from indications list.

        Returns:
            self for method chaining
        """
        self._obj.indications = []
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


    def build(self) -> ApplicationInterface:
        """Build and return the ApplicationInterface instance with validation."""
        self._validate_instance()
        pass
        return self._obj