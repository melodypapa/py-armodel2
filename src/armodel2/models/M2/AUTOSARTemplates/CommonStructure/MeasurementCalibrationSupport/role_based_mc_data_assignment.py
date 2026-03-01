"""RoleBasedMcDataAssignment AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 329)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_execution_context import (
    RptExecutionContext,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_data_instance import (
        McDataInstance,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class RoleBasedMcDataAssignment(ARObject):
    """AUTOSAR RoleBasedMcDataAssignment."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ROLE-BASED-MC-DATA-ASSIGNMENT"


    execution_refs: list[ARRef]
    mc_data_instance_refs: list[ARRef]
    role: Optional[Identifier]
    _DESERIALIZE_DISPATCH = {
        "EXECUTIONS": lambda obj, elem: obj.execution_refs.append(ARRef.deserialize(elem)),
        "MC-DATA-INSTANCES": lambda obj, elem: obj.mc_data_instance_refs.append(ARRef.deserialize(elem)),
        "ROLE": lambda obj, elem: setattr(obj, "role", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
    }


    def __init__(self) -> None:
        """Initialize RoleBasedMcDataAssignment."""
        super().__init__()
        self.execution_refs: list[ARRef] = []
        self.mc_data_instance_refs: list[ARRef] = []
        self.role: Optional[Identifier] = None

    def serialize(self) -> ET.Element:
        """Serialize RoleBasedMcDataAssignment to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RoleBasedMcDataAssignment, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize execution_refs (list to container "EXECUTION-REFS")
        if self.execution_refs:
            wrapper = ET.Element("EXECUTION-REFS")
            for item in self.execution_refs:
                serialized = SerializationHelper.serialize_item(item, "RptExecutionContext")
                if serialized is not None:
                    child_elem = ET.Element("EXECUTION-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mc_data_instance_refs (list to container "MC-DATA-INSTANCE-REFS")
        if self.mc_data_instance_refs:
            wrapper = ET.Element("MC-DATA-INSTANCE-REFS")
            for item in self.mc_data_instance_refs:
                serialized = SerializationHelper.serialize_item(item, "McDataInstance")
                if serialized is not None:
                    child_elem = ET.Element("MC-DATA-INSTANCE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RoleBasedMcDataAssignment":
        """Deserialize XML element to RoleBasedMcDataAssignment object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RoleBasedMcDataAssignment object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RoleBasedMcDataAssignment, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "EXECUTIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.execution_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "RptExecutionContext"))
            elif tag == "MC-DATA-INSTANCES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.mc_data_instance_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "McDataInstance"))
            elif tag == "ROLE":
                setattr(obj, "role", SerializationHelper.deserialize_by_tag(child, "Identifier"))

        return obj



class RoleBasedMcDataAssignmentBuilder(BuilderBase):
    """Builder for RoleBasedMcDataAssignment with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RoleBasedMcDataAssignment = RoleBasedMcDataAssignment()


    def with_executions(self, items: list[RptExecutionContext]) -> "RoleBasedMcDataAssignmentBuilder":
        """Set executions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.executions = list(items) if items else []
        return self

    def with_mc_data_instances(self, items: list[McDataInstance]) -> "RoleBasedMcDataAssignmentBuilder":
        """Set mc_data_instances list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mc_data_instances = list(items) if items else []
        return self

    def with_role(self, value: Optional[Identifier]) -> "RoleBasedMcDataAssignmentBuilder":
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


    def add_execution(self, item: RptExecutionContext) -> "RoleBasedMcDataAssignmentBuilder":
        """Add a single item to executions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.executions.append(item)
        return self

    def clear_executions(self) -> "RoleBasedMcDataAssignmentBuilder":
        """Clear all items from executions list.

        Returns:
            self for method chaining
        """
        self._obj.executions = []
        return self

    def add_mc_data_instance(self, item: McDataInstance) -> "RoleBasedMcDataAssignmentBuilder":
        """Add a single item to mc_data_instances list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mc_data_instances.append(item)
        return self

    def clear_mc_data_instances(self) -> "RoleBasedMcDataAssignmentBuilder":
        """Clear all items from mc_data_instances list.

        Returns:
            self for method chaining
        """
        self._obj.mc_data_instances = []
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


    def build(self) -> RoleBasedMcDataAssignment:
        """Build and return the RoleBasedMcDataAssignment instance with validation."""
        self._validate_instance()
        pass
        return self._obj