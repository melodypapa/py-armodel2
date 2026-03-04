"""BswModuleEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 32)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 976)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 216)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 431)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 171)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswInterfaces.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces import (
    BswCallType,
    BswEntryKindEnum,
    BswExecutionContext,
)
from armodel2.models.M2.MSR.DataDictionary.ServiceProcessTask import (
    SwServiceImplPolicyEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
    NameToken,
    PositiveInteger,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.DataDictionary.ServiceProcessTask.sw_service_arg import (
        SwServiceArg,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class BswModuleEntry(ARElement):
    """AUTOSAR BswModuleEntry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BSW-MODULE-ENTRY"


    service_id: Optional[PositiveInteger]
    arguments: list[SwServiceArg]
    bsw_entry_kind: Optional[BswEntryKindEnum]
    is_reentrant: Optional[Boolean]
    is_synchronous: Optional[Boolean]
    call_type: Optional[BswCallType]
    execution_context: Optional[BswExecutionContext]
    function_prototype_emitter: Optional[NameToken]
    return_type: Optional[SwServiceArg]
    role: Optional[Identifier]
    sw_service_impl_policy: Optional[SwServiceImplPolicyEnum]
    _DESERIALIZE_DISPATCH = {
        "SERVICE-ID": lambda obj, elem: setattr(obj, "service_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "ARGUMENTS": lambda obj, elem: obj.arguments.append(SerializationHelper.deserialize_by_tag(elem, "SwServiceArg")),
        "BSW-ENTRY-KIND": lambda obj, elem: setattr(obj, "bsw_entry_kind", BswEntryKindEnum.deserialize(elem)),
        "IS-REENTRANT": lambda obj, elem: setattr(obj, "is_reentrant", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "IS-SYNCHRONOUS": lambda obj, elem: setattr(obj, "is_synchronous", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "CALL-TYPE": lambda obj, elem: setattr(obj, "call_type", BswCallType.deserialize(elem)),
        "EXECUTION-CONTEXT": lambda obj, elem: setattr(obj, "execution_context", BswExecutionContext.deserialize(elem)),
        "FUNCTION-PROTOTYPE-EMITTER": lambda obj, elem: setattr(obj, "function_prototype_emitter", SerializationHelper.deserialize_by_tag(elem, "NameToken")),
        "RETURN-TYPE": lambda obj, elem: setattr(obj, "return_type", SerializationHelper.deserialize_by_tag(elem, "SwServiceArg")),
        "ROLE": lambda obj, elem: setattr(obj, "role", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
        "SW-SERVICE-IMPL-POLICY": lambda obj, elem: setattr(obj, "sw_service_impl_policy", SwServiceImplPolicyEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize BswModuleEntry."""
        super().__init__()
        self.service_id: Optional[PositiveInteger] = None
        self.arguments: list[SwServiceArg] = []
        self.bsw_entry_kind: Optional[BswEntryKindEnum] = None
        self.is_reentrant: Optional[Boolean] = None
        self.is_synchronous: Optional[Boolean] = None
        self.call_type: Optional[BswCallType] = None
        self.execution_context: Optional[BswExecutionContext] = None
        self.function_prototype_emitter: Optional[NameToken] = None
        self.return_type: Optional[SwServiceArg] = None
        self.role: Optional[Identifier] = None
        self.sw_service_impl_policy: Optional[SwServiceImplPolicyEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize BswModuleEntry to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswModuleEntry, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize service_id
        if self.service_id is not None:
            serialized = SerializationHelper.serialize_item(self.service_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize arguments (list to container "ARGUMENTS")
        if self.arguments:
            wrapper = ET.Element("ARGUMENTS")
            for item in self.arguments:
                serialized = SerializationHelper.serialize_item(item, "SwServiceArg")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize bsw_entry_kind
        if self.bsw_entry_kind is not None:
            serialized = SerializationHelper.serialize_item(self.bsw_entry_kind, "BswEntryKindEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BSW-ENTRY-KIND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize is_reentrant
        if self.is_reentrant is not None:
            serialized = SerializationHelper.serialize_item(self.is_reentrant, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-REENTRANT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize is_synchronous
        if self.is_synchronous is not None:
            serialized = SerializationHelper.serialize_item(self.is_synchronous, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-SYNCHRONOUS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize call_type
        if self.call_type is not None:
            serialized = SerializationHelper.serialize_item(self.call_type, "BswCallType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CALL-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize execution_context
        if self.execution_context is not None:
            serialized = SerializationHelper.serialize_item(self.execution_context, "BswExecutionContext")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXECUTION-CONTEXT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize function_prototype_emitter
        if self.function_prototype_emitter is not None:
            serialized = SerializationHelper.serialize_item(self.function_prototype_emitter, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FUNCTION-PROTOTYPE-EMITTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize return_type
        if self.return_type is not None:
            serialized = SerializationHelper.serialize_item(self.return_type, "SwServiceArg")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RETURN-TYPE")
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

        # Serialize sw_service_impl_policy
        if self.sw_service_impl_policy is not None:
            serialized = SerializationHelper.serialize_item(self.sw_service_impl_policy, "SwServiceImplPolicyEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-SERVICE-IMPL-POLICY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModuleEntry":
        """Deserialize XML element to BswModuleEntry object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswModuleEntry object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswModuleEntry, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SERVICE-ID":
                setattr(obj, "service_id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "ARGUMENTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.arguments.append(SerializationHelper.deserialize_by_tag(item_elem, "SwServiceArg"))
            elif tag == "BSW-ENTRY-KIND":
                setattr(obj, "bsw_entry_kind", BswEntryKindEnum.deserialize(child))
            elif tag == "IS-REENTRANT":
                setattr(obj, "is_reentrant", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "IS-SYNCHRONOUS":
                setattr(obj, "is_synchronous", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "CALL-TYPE":
                setattr(obj, "call_type", BswCallType.deserialize(child))
            elif tag == "EXECUTION-CONTEXT":
                setattr(obj, "execution_context", BswExecutionContext.deserialize(child))
            elif tag == "FUNCTION-PROTOTYPE-EMITTER":
                setattr(obj, "function_prototype_emitter", SerializationHelper.deserialize_by_tag(child, "NameToken"))
            elif tag == "RETURN-TYPE":
                setattr(obj, "return_type", SerializationHelper.deserialize_by_tag(child, "SwServiceArg"))
            elif tag == "ROLE":
                setattr(obj, "role", SerializationHelper.deserialize_by_tag(child, "Identifier"))
            elif tag == "SW-SERVICE-IMPL-POLICY":
                setattr(obj, "sw_service_impl_policy", SwServiceImplPolicyEnum.deserialize(child))

        return obj



class BswModuleEntryBuilder(ARElementBuilder):
    """Builder for BswModuleEntry with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BswModuleEntry = BswModuleEntry()


    def with_service_id(self, value: Optional[PositiveInteger]) -> "BswModuleEntryBuilder":
        """Set service_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.service_id = value
        return self

    def with_arguments(self, items: list[SwServiceArg]) -> "BswModuleEntryBuilder":
        """Set arguments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.arguments = list(items) if items else []
        return self

    def with_bsw_entry_kind(self, value: Optional[BswEntryKindEnum]) -> "BswModuleEntryBuilder":
        """Set bsw_entry_kind attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bsw_entry_kind = value
        return self

    def with_is_reentrant(self, value: Optional[Boolean]) -> "BswModuleEntryBuilder":
        """Set is_reentrant attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.is_reentrant = value
        return self

    def with_is_synchronous(self, value: Optional[Boolean]) -> "BswModuleEntryBuilder":
        """Set is_synchronous attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.is_synchronous = value
        return self

    def with_call_type(self, value: Optional[BswCallType]) -> "BswModuleEntryBuilder":
        """Set call_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.call_type = value
        return self

    def with_execution_context(self, value: Optional[BswExecutionContext]) -> "BswModuleEntryBuilder":
        """Set execution_context attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.execution_context = value
        return self

    def with_function_prototype_emitter(self, value: Optional[NameToken]) -> "BswModuleEntryBuilder":
        """Set function_prototype_emitter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.function_prototype_emitter = value
        return self

    def with_return_type(self, value: Optional[SwServiceArg]) -> "BswModuleEntryBuilder":
        """Set return_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.return_type = value
        return self

    def with_role(self, value: Optional[Identifier]) -> "BswModuleEntryBuilder":
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

    def with_sw_service_impl_policy(self, value: Optional[SwServiceImplPolicyEnum]) -> "BswModuleEntryBuilder":
        """Set sw_service_impl_policy attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_service_impl_policy = value
        return self


    def add_argument(self, item: SwServiceArg) -> "BswModuleEntryBuilder":
        """Add a single item to arguments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.arguments.append(item)
        return self

    def clear_arguments(self) -> "BswModuleEntryBuilder":
        """Clear all items from arguments list.

        Returns:
            self for method chaining
        """
        self._obj.arguments = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "argument",
        "bswEntryKind",
        "callType",
        "executionContext",
        "functionPrototypeEmitter",
        "isReentrant",
        "isSynchronous",
        "returnType",
        "role",
        "serviceId",
        "swServiceImplPolicy",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> BswModuleEntry:
        """Build and return the BswModuleEntry instance with validation."""
        self._validate_instance()
        return self._obj