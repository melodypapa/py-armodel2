"""ServiceDependency AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 225)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 609)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    ServiceDiagnosticRelevanceEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.symbolic_name_props import (
    SymbolicNameProps,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping.role_based_data_type_assignment import (
        RoleBasedDataTypeAssignment,
    )



from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ServiceDependency(Identifiable, ABC):
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
    _DESERIALIZE_DISPATCH = {
        "ASSIGNED-DATA": lambda obj, elem: setattr(obj, "assigned_data", SerializationHelper.deserialize_by_tag(elem, "RoleBasedDataTypeAssignment")),
        "DIAGNOSTIC": lambda obj, elem: setattr(obj, "diagnostic", ServiceDiagnosticRelevanceEnum.deserialize(elem)),
        "SYMBOLIC-NAME-PROPS": lambda obj, elem: setattr(obj, "symbolic_name_props", SerializationHelper.deserialize_by_tag(elem, "SymbolicNameProps")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ASSIGNED-DATA":
                setattr(obj, "assigned_data", SerializationHelper.deserialize_by_tag(child, "RoleBasedDataTypeAssignment"))
            elif tag == "DIAGNOSTIC":
                setattr(obj, "diagnostic", ServiceDiagnosticRelevanceEnum.deserialize(child))
            elif tag == "SYMBOLIC-NAME-PROPS":
                setattr(obj, "symbolic_name_props", SerializationHelper.deserialize_by_tag(child, "SymbolicNameProps"))

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



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "assignedData",
        "diagnostic",
        "symbolicNameProps",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> ServiceDependency:
        """Build and return the ServiceDependency instance (abstract)."""
        raise NotImplementedError