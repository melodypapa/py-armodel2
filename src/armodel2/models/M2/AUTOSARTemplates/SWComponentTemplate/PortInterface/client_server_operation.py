"""ClientServerOperation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 309)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 306)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 102)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2008)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 218)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 28)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 433)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 174)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

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
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.application_error import (
    ApplicationError,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.argument_data_prototype import (
        ArgumentDataPrototype,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class ClientServerOperation(Identifiable):
    """AUTOSAR ClientServerOperation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CLIENT-SERVER-OPERATION"


    arguments: list[ArgumentDataPrototype]
    diag_arg_integrity: Optional[Boolean]
    possible_error_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "ARGUMENTS": lambda obj, elem: obj.arguments.append(SerializationHelper.deserialize_by_tag(elem, "ArgumentDataPrototype")),
        "DIAG-ARG-INTEGRITY": lambda obj, elem: setattr(obj, "diag_arg_integrity", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "POSSIBLE-ERRORS": lambda obj, elem: obj.possible_error_refs.append(ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ClientServerOperation."""
        super().__init__()
        self.arguments: list[ArgumentDataPrototype] = []
        self.diag_arg_integrity: Optional[Boolean] = None
        self.possible_error_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize ClientServerOperation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ClientServerOperation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize arguments (list to container "ARGUMENTS")
        if self.arguments:
            wrapper = ET.Element("ARGUMENTS")
            for item in self.arguments:
                serialized = SerializationHelper.serialize_item(item, "ArgumentDataPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize diag_arg_integrity
        if self.diag_arg_integrity is not None:
            serialized = SerializationHelper.serialize_item(self.diag_arg_integrity, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAG-ARG-INTEGRITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize possible_error_refs (list to container "POSSIBLE-ERROR-REFS")
        if self.possible_error_refs:
            wrapper = ET.Element("POSSIBLE-ERROR-REFS")
            for item in self.possible_error_refs:
                serialized = SerializationHelper.serialize_item(item, "ApplicationError")
                if serialized is not None:
                    child_elem = ET.Element("POSSIBLE-ERROR-REF")
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
    def deserialize(cls, element: ET.Element) -> "ClientServerOperation":
        """Deserialize XML element to ClientServerOperation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientServerOperation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ClientServerOperation, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "ARGUMENTS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.arguments.append(SerializationHelper.deserialize_by_tag(item_elem, "ArgumentDataPrototype"))
            elif tag == "DIAG-ARG-INTEGRITY":
                setattr(obj, "diag_arg_integrity", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "POSSIBLE-ERRORS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.possible_error_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "ApplicationError"))

        return obj



class ClientServerOperationBuilder(IdentifiableBuilder):
    """Builder for ClientServerOperation with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ClientServerOperation = ClientServerOperation()


    def with_arguments(self, items: list[ArgumentDataPrototype]) -> "ClientServerOperationBuilder":
        """Set arguments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.arguments = list(items) if items else []
        return self

    def with_diag_arg_integrity(self, value: Optional[Boolean]) -> "ClientServerOperationBuilder":
        """Set diag_arg_integrity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.diag_arg_integrity = value
        return self

    def with_possible_errors(self, items: list[ApplicationError]) -> "ClientServerOperationBuilder":
        """Set possible_errors list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.possible_errors = list(items) if items else []
        return self


    def add_argument(self, item: ArgumentDataPrototype) -> "ClientServerOperationBuilder":
        """Add a single item to arguments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.arguments.append(item)
        return self

    def clear_arguments(self) -> "ClientServerOperationBuilder":
        """Clear all items from arguments list.

        Returns:
            self for method chaining
        """
        self._obj.arguments = []
        return self

    def add_possible_error(self, item: ApplicationError) -> "ClientServerOperationBuilder":
        """Add a single item to possible_errors list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.possible_errors.append(item)
        return self

    def clear_possible_errors(self) -> "ClientServerOperationBuilder":
        """Clear all items from possible_errors list.

        Returns:
            self for method chaining
        """
        self._obj.possible_errors = []
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


    def build(self) -> ClientServerOperation:
        """Build and return the ClientServerOperation instance with validation."""
        self._validate_instance()
        pass
        return self._obj