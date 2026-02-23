"""ServiceDependency AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 225)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 609)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from abc import ABC, abstractmethod
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    ServiceDiagnosticRelevanceEnum,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping.role_based_data_type_assignment import (
    RoleBasedDataTypeAssignment,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.symbolic_name_props import (
    SymbolicNameProps,
)


class ServiceDependency(ARObject, ABC):
    """AUTOSAR ServiceDependency."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    assigned_data: Optional[RoleBasedDataTypeAssignment]
    diagnostic: Optional[ServiceDiagnosticRelevanceEnum]
    symbolic_name_props: Optional[SymbolicNameProps]
    def __init__(self) -> None:
        """Initialize ServiceDependency."""
        super().__init__()
        self.assigned_data: Optional[RoleBasedDataTypeAssignment] = None
        self.diagnostic: Optional[ServiceDiagnosticRelevanceEnum] = None
        self.symbolic_name_props: Optional[SymbolicNameProps] = None

    def serialize(self) -> ET.Element:
        """Serialize ServiceDependency to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ServiceDependency, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize assigned_data
        if self.assigned_data is not None:
            serialized = SerializationHelper.serialize_item(self.assigned_data, "RoleBasedDataTypeAssignment")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ASSIGNED-DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize diagnostic
        if self.diagnostic is not None:
            serialized = SerializationHelper.serialize_item(self.diagnostic, "ServiceDiagnosticRelevanceEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAGNOSTIC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize symbolic_name_props
        if self.symbolic_name_props is not None:
            serialized = SerializationHelper.serialize_item(self.symbolic_name_props, "SymbolicNameProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYMBOLIC-NAME-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ServiceDependency":
        """Deserialize XML element to ServiceDependency object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ServiceDependency object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ServiceDependency, cls).deserialize(element)

        # Parse assigned_data
        child = SerializationHelper.find_child_element(element, "ASSIGNED-DATA")
        if child is not None:
            assigned_data_value = SerializationHelper.deserialize_by_tag(child, "RoleBasedDataTypeAssignment")
            obj.assigned_data = assigned_data_value

        # Parse diagnostic
        child = SerializationHelper.find_child_element(element, "DIAGNOSTIC")
        if child is not None:
            diagnostic_value = ServiceDiagnosticRelevanceEnum.deserialize(child)
            obj.diagnostic = diagnostic_value

        # Parse symbolic_name_props
        child = SerializationHelper.find_child_element(element, "SYMBOLIC-NAME-PROPS")
        if child is not None:
            symbolic_name_props_value = SerializationHelper.deserialize_by_tag(child, "SymbolicNameProps")
            obj.symbolic_name_props = symbolic_name_props_value

        return obj



class ServiceDependencyBuilder(BuilderBase, ABC):
    """Builder for ServiceDependency with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ServiceDependency = ServiceDependency()


    def with_assigned_data(self, value: Optional[RoleBasedDataTypeAssignment]) -> "ServiceDependencyBuilder":
        """Set assigned_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.assigned_data = value
        return self

    def with_diagnostic(self, value: Optional[ServiceDiagnosticRelevanceEnum]) -> "ServiceDependencyBuilder":
        """Set diagnostic attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.diagnostic = value
        return self

    def with_symbolic_name_props(self, value: Optional[SymbolicNameProps]) -> "ServiceDependencyBuilder":
        """Set symbolic_name_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.symbolic_name_props = value
        return self




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


    @abstractmethod
    def build(self) -> ServiceDependency:
        """Build and return the ServiceDependency instance (abstract)."""
        raise NotImplementedError