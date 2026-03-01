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

from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import PaginateableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1 import (
    StandardNameEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    String,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable import (
    Traceable,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.Documentation.BlockElements.documentation_block import (
        DocumentationBlock,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class StructuredReq(Paginateable):
    """AUTOSAR StructuredReq."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "STRUCTURED-REQ"


    applies_toes: list[StandardNameEnum]
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
    _DESERIALIZE_DISPATCH = {
        "APPLIES-TOES": lambda obj, elem: obj.applies_toes.append(StandardNameEnum.deserialize(elem)),
        "CONFLICTS": lambda obj, elem: setattr(obj, "conflicts", SerializationHelper.deserialize_by_tag(elem, "DocumentationBlock")),
        "DATE": lambda obj, elem: setattr(obj, "date", SerializationHelper.deserialize_by_tag(elem, "DateTime")),
        "DEPENDENCIES": lambda obj, elem: setattr(obj, "dependencies", SerializationHelper.deserialize_by_tag(elem, "DocumentationBlock")),
        "DESCRIPTION": lambda obj, elem: setattr(obj, "description", SerializationHelper.deserialize_by_tag(elem, "DocumentationBlock")),
        "IMPORTANCE": lambda obj, elem: setattr(obj, "importance", SerializationHelper.deserialize_by_tag(elem, "String")),
        "ISSUED-BY": lambda obj, elem: setattr(obj, "issued_by", SerializationHelper.deserialize_by_tag(elem, "String")),
        "RATIONALE": lambda obj, elem: setattr(obj, "rationale", SerializationHelper.deserialize_by_tag(elem, "DocumentationBlock")),
        "REMARK": lambda obj, elem: setattr(obj, "remark", SerializationHelper.deserialize_by_tag(elem, "DocumentationBlock")),
        "SUPPORTING": lambda obj, elem: setattr(obj, "supporting", SerializationHelper.deserialize_by_tag(elem, "DocumentationBlock")),
        "TESTED-ITEM-REFS": ("_POLYMORPHIC_LIST", "tested_item_refs", ["AgeConstraint", "ArbitraryEventTriggering", "BurstPatternEventTriggering", "ConcretePatternEventTriggering", "ExecutionOrderConstraint", "ExecutionTimeConstraint", "LatencyTimingConstraint", "OffsetTimingConstraint", "PeriodicEventTriggering", "SporadicEventTriggering", "StructuredReq", "SynchronizationPointConstraint", "TimingConstraint", "TraceableTable", "TraceableText"]),
        "TYPE": lambda obj, elem: setattr(obj, "type", SerializationHelper.deserialize_by_tag(elem, "String")),
        "USE-CASE": lambda obj, elem: setattr(obj, "use_case", SerializationHelper.deserialize_by_tag(elem, "DocumentationBlock")),
    }


    def __init__(self) -> None:
        """Initialize StructuredReq."""
        super().__init__()
        self.applies_toes: list[StandardNameEnum] = []
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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Serialize applies_toes (list to container "APPLIES-TOES")
        if self.applies_toes:
            wrapper = ET.Element("APPLIES-TOES")
            for item in self.applies_toes:
                serialized = SerializationHelper.serialize_item(item, "StandardNameEnum")
                if serialized is not None:
                    child_elem = ET.Element("APPLIES-TOE")
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "APPLIES-TOES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.applies_toes.append(SerializationHelper.deserialize_by_tag(item_elem, "StandardNameEnum"))
            elif tag == "CONFLICTS":
                setattr(obj, "conflicts", SerializationHelper.deserialize_by_tag(child, "DocumentationBlock"))
            elif tag == "DATE":
                setattr(obj, "date", SerializationHelper.deserialize_by_tag(child, "DateTime"))
            elif tag == "DEPENDENCIES":
                setattr(obj, "dependencies", SerializationHelper.deserialize_by_tag(child, "DocumentationBlock"))
            elif tag == "DESCRIPTION":
                setattr(obj, "description", SerializationHelper.deserialize_by_tag(child, "DocumentationBlock"))
            elif tag == "IMPORTANCE":
                setattr(obj, "importance", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "ISSUED-BY":
                setattr(obj, "issued_by", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "RATIONALE":
                setattr(obj, "rationale", SerializationHelper.deserialize_by_tag(child, "DocumentationBlock"))
            elif tag == "REMARK":
                setattr(obj, "remark", SerializationHelper.deserialize_by_tag(child, "DocumentationBlock"))
            elif tag == "SUPPORTING":
                setattr(obj, "supporting", SerializationHelper.deserialize_by_tag(child, "DocumentationBlock"))
            elif tag == "TESTED-ITEM-REFS":
                for item_elem in child:
                    obj.tested_item_refs.append(ARRef.deserialize(item_elem))
            elif tag == "TYPE":
                setattr(obj, "type", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "USE-CASE":
                setattr(obj, "use_case", SerializationHelper.deserialize_by_tag(child, "DocumentationBlock"))

        return obj



class StructuredReqBuilder(PaginateableBuilder):
    """Builder for StructuredReq with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: StructuredReq = StructuredReq()


    def with_applies_toes(self, items: list[StandardNameEnum]) -> "StructuredReqBuilder":
        """Set applies_toes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.applies_toes = list(items) if items else []
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
        """Add a single item to applies_toes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.applies_toes.append(item)
        return self

    def clear_applies_toes(self) -> "StructuredReqBuilder":
        """Clear all items from applies_toes list.

        Returns:
            self for method chaining
        """
        self._obj.applies_toes = []
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


    def build(self) -> StructuredReq:
        """Build and return the StructuredReq instance with validation."""
        self._validate_instance()
        pass
        return self._obj