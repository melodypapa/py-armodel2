"""ServiceDependency AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 225)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 609)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    ServiceDiagnosticRelevanceEnum,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping.role_based_data_type_assignment import (
    RoleBasedDataTypeAssignment,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.symbolic_name_props import (
    SymbolicNameProps,
)
from abc import ABC, abstractmethod


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
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize assigned_data
        if self.assigned_data is not None:
            serialized = ARObject._serialize_item(self.assigned_data, "RoleBasedDataTypeAssignment")
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
            serialized = ARObject._serialize_item(self.diagnostic, "ServiceDiagnosticRelevanceEnum")
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
            serialized = ARObject._serialize_item(self.symbolic_name_props, "SymbolicNameProps")
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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse assigned_data
        child = ARObject._find_child_element(element, "ASSIGNED-DATA")
        if child is not None:
            assigned_data_value = ARObject._deserialize_by_tag(child, "RoleBasedDataTypeAssignment")
            obj.assigned_data = assigned_data_value

        # Parse diagnostic
        child = ARObject._find_child_element(element, "DIAGNOSTIC")
        if child is not None:
            diagnostic_value = ServiceDiagnosticRelevanceEnum.deserialize(child)
            obj.diagnostic = diagnostic_value

        # Parse symbolic_name_props
        child = ARObject._find_child_element(element, "SYMBOLIC-NAME-PROPS")
        if child is not None:
            symbolic_name_props_value = ARObject._deserialize_by_tag(child, "SymbolicNameProps")
            obj.symbolic_name_props = symbolic_name_props_value

        return obj



class ServiceDependencyBuilder:
    """Builder for ServiceDependency."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ServiceDependency = ServiceDependency()

    def build(self) -> ServiceDependency:
        """Build and return ServiceDependency object.

        Returns:
            ServiceDependency instance
        """
        # TODO: Add validation
        return self._obj
