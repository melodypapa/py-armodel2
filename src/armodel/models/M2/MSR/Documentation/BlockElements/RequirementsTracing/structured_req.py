"""StructuredReq AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 168)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 49)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 313)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 208)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_RequirementsTracing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1 import (
    StandardNameEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    String,
)
from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable import (
    Traceable,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
        DocumentationBlock,
    )



class StructuredReq(Paginateable):
    """AUTOSAR StructuredReq."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    applies_tos: list[StandardNameEnum]
    conflicts: Optional[DocumentationBlock]
    date: DateTime
    dependencies: Optional[DocumentationBlock]
    description: Optional[DocumentationBlock]
    importance: String
    issued_by: String
    rationale: Optional[DocumentationBlock]
    remark: Optional[DocumentationBlock]
    supporting: Optional[DocumentationBlock]
    tested_item_refs: list[ARRef]
    type: String
    use_case: Optional[DocumentationBlock]
    def __init__(self) -> None:
        """Initialize StructuredReq."""
        super().__init__()
        self.applies_tos: list[StandardNameEnum] = []
        self.conflicts: Optional[DocumentationBlock] = None
        self.date: DateTime = None
        self.dependencies: Optional[DocumentationBlock] = None
        self.description: Optional[DocumentationBlock] = None
        self.importance: String = None
        self.issued_by: String = None
        self.rationale: Optional[DocumentationBlock] = None
        self.remark: Optional[DocumentationBlock] = None
        self.supporting: Optional[DocumentationBlock] = None
        self.tested_item_refs: list[ARRef] = []
        self.type: String = None
        self.use_case: Optional[DocumentationBlock] = None

    def serialize(self) -> ET.Element:
        """Serialize StructuredReq to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(StructuredReq, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize applies_tos (list to container "APPLIES-TOS")
        if self.applies_tos:
            wrapper = ET.Element("APPLIES-TOS")
            for item in self.applies_tos:
                serialized = SerializationHelper.serialize_item(item, "StandardNameEnum")
                if serialized is not None:
                    child_elem = ET.Element("APPLIES-TO")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize conflicts
        if self.conflicts is not None:
            serialized = SerializationHelper.serialize_item(self.conflicts, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONFLICTS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize date
        if self.date is not None:
            serialized = SerializationHelper.serialize_item(self.date, "DateTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dependencies
        if self.dependencies is not None:
            serialized = SerializationHelper.serialize_item(self.dependencies, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEPENDENCIES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize description
        if self.description is not None:
            serialized = SerializationHelper.serialize_item(self.description, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DESCRIPTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize importance
        if self.importance is not None:
            serialized = SerializationHelper.serialize_item(self.importance, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IMPORTANCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize issued_by
        if self.issued_by is not None:
            serialized = SerializationHelper.serialize_item(self.issued_by, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ISSUED-BY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rationale
        if self.rationale is not None:
            serialized = SerializationHelper.serialize_item(self.rationale, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RATIONALE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize remark
        if self.remark is not None:
            serialized = SerializationHelper.serialize_item(self.remark, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REMARK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize supporting
        if self.supporting is not None:
            serialized = SerializationHelper.serialize_item(self.supporting, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUPPORTING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tested_item_refs (list to container "TESTED-ITEM-REFS")
        if self.tested_item_refs:
            wrapper = ET.Element("TESTED-ITEM-REFS")
            for item in self.tested_item_refs:
                serialized = SerializationHelper.serialize_item(item, "Traceable")
                if serialized is not None:
                    child_elem = ET.Element("TESTED-ITEM-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize type
        if self.type is not None:
            serialized = SerializationHelper.serialize_item(self.type, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize use_case
        if self.use_case is not None:
            serialized = SerializationHelper.serialize_item(self.use_case, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USE-CASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "StructuredReq":
        """Deserialize XML element to StructuredReq object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized StructuredReq object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(StructuredReq, cls).deserialize(element)

        # Parse applies_tos (list from container "APPLIES-TOS")
        obj.applies_tos = []
        container = SerializationHelper.find_child_element(element, "APPLIES-TOS")
        if container is not None:
            for child in container:
                # Extract enum value (StandardNameEnum)
                child_value = StandardNameEnum.deserialize(child)
                if child_value is not None:
                    obj.applies_tos.append(child_value)

        # Parse conflicts
        child = SerializationHelper.find_child_element(element, "CONFLICTS")
        if child is not None:
            conflicts_value = SerializationHelper.deserialize_by_tag(child, "DocumentationBlock")
            obj.conflicts = conflicts_value

        # Parse date
        child = SerializationHelper.find_child_element(element, "DATE")
        if child is not None:
            date_value = child.text
            obj.date = date_value

        # Parse dependencies
        child = SerializationHelper.find_child_element(element, "DEPENDENCIES")
        if child is not None:
            dependencies_value = SerializationHelper.deserialize_by_tag(child, "DocumentationBlock")
            obj.dependencies = dependencies_value

        # Parse description
        child = SerializationHelper.find_child_element(element, "DESCRIPTION")
        if child is not None:
            description_value = SerializationHelper.deserialize_by_tag(child, "DocumentationBlock")
            obj.description = description_value

        # Parse importance
        child = SerializationHelper.find_child_element(element, "IMPORTANCE")
        if child is not None:
            importance_value = child.text
            obj.importance = importance_value

        # Parse issued_by
        child = SerializationHelper.find_child_element(element, "ISSUED-BY")
        if child is not None:
            issued_by_value = child.text
            obj.issued_by = issued_by_value

        # Parse rationale
        child = SerializationHelper.find_child_element(element, "RATIONALE")
        if child is not None:
            rationale_value = SerializationHelper.deserialize_by_tag(child, "DocumentationBlock")
            obj.rationale = rationale_value

        # Parse remark
        child = SerializationHelper.find_child_element(element, "REMARK")
        if child is not None:
            remark_value = SerializationHelper.deserialize_by_tag(child, "DocumentationBlock")
            obj.remark = remark_value

        # Parse supporting
        child = SerializationHelper.find_child_element(element, "SUPPORTING")
        if child is not None:
            supporting_value = SerializationHelper.deserialize_by_tag(child, "DocumentationBlock")
            obj.supporting = supporting_value

        # Parse tested_item_refs (list from container "TESTED-ITEM-REFS")
        obj.tested_item_refs = []
        container = SerializationHelper.find_child_element(element, "TESTED-ITEM-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tested_item_refs.append(child_value)

        # Parse type
        child = SerializationHelper.find_child_element(element, "TYPE")
        if child is not None:
            type_value = child.text
            obj.type = type_value

        # Parse use_case
        child = SerializationHelper.find_child_element(element, "USE-CASE")
        if child is not None:
            use_case_value = SerializationHelper.deserialize_by_tag(child, "DocumentationBlock")
            obj.use_case = use_case_value

        return obj



class StructuredReqBuilder:
    """Builder for StructuredReq with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: StructuredReq = StructuredReq()


    def with_si(self, value: NameTokens) -> "StructuredReqBuilder":
        """Set si attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.si = value
        return self

    def with_view(self, value: Optional[ViewTokens]) -> "StructuredReqBuilder":
        """Set view attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.view = value
        return self

    def with_break(self, value: Optional[ChapterEnumBreak]) -> "StructuredReqBuilder":
        """Set break attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        setattr(self._obj, 'break', value)
        return self

    def with_keep_with(self, value: Optional[KeepWithPreviousEnum]) -> "StructuredReqBuilder":
        """Set keep_with attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.keep_with = value
        return self

    def with_applies_tos(self, items: list[StandardNameEnum]) -> "StructuredReqBuilder":
        """Set applies_tos list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.applies_tos = list(items) if items else []
        return self

    def with_conflicts(self, value: Optional[DocumentationBlock]) -> "StructuredReqBuilder":
        """Set conflicts attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.conflicts = value
        return self

    def with_date(self, value: DateTime) -> "StructuredReqBuilder":
        """Set date attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.date = value
        return self

    def with_dependencies(self, value: Optional[DocumentationBlock]) -> "StructuredReqBuilder":
        """Set dependencies attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dependencies = value
        return self

    def with_description(self, value: Optional[DocumentationBlock]) -> "StructuredReqBuilder":
        """Set description attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.description = value
        return self

    def with_importance(self, value: String) -> "StructuredReqBuilder":
        """Set importance attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.importance = value
        return self

    def with_issued_by(self, value: String) -> "StructuredReqBuilder":
        """Set issued_by attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.issued_by = value
        return self

    def with_rationale(self, value: Optional[DocumentationBlock]) -> "StructuredReqBuilder":
        """Set rationale attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rationale = value
        return self

    def with_remark(self, value: Optional[DocumentationBlock]) -> "StructuredReqBuilder":
        """Set remark attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.remark = value
        return self

    def with_supporting(self, value: Optional[DocumentationBlock]) -> "StructuredReqBuilder":
        """Set supporting attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.supporting = value
        return self

    def with_tested_items(self, items: list[Traceable]) -> "StructuredReqBuilder":
        """Set tested_items list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.tested_items = list(items) if items else []
        return self

    def with_type(self, value: String) -> "StructuredReqBuilder":
        """Set type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.type = value
        return self

    def with_use_case(self, value: Optional[DocumentationBlock]) -> "StructuredReqBuilder":
        """Set use_case attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.use_case = value
        return self


    def add_applies_to(self, item: StandardNameEnum) -> "StructuredReqBuilder":
        """Add a single item to applies_tos list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.applies_tos.append(item)
        return self

    def clear_applies_tos(self) -> "StructuredReqBuilder":
        """Clear all items from applies_tos list.

        Returns:
            self for method chaining
        """
        self._obj.applies_tos = []
        return self

    def add_tested_item(self, item: Traceable) -> "StructuredReqBuilder":
        """Add a single item to tested_items list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.tested_items.append(item)
        return self

    def clear_tested_items(self) -> "StructuredReqBuilder":
        """Clear all items from tested_items list.

        Returns:
            self for method chaining
        """
        self._obj.tested_items = []
        return self


    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")


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


    def build(self) -> StructuredReq:
        """Build and return the StructuredReq instance with validation."""
        self._validate_instance()
        pass
        return self._obj